from fastapi import APIRouter,HTTPException, status

from schemas import TicketCreate,TicketOut

api_router=APIRouter(prefix='/api/Tickets')


tickets=[]
current_ticket_id=1


@api_router.post("/",response_model=TicketOut)
def create_ticket(ticket_in: TicketCreate): 
    global current_ticket_id
    
    for sold_ticket in tickets:
        if (sold_ticket["seat_number"] == ticket_in.seat_number and 
            sold_ticket["movie_name"] == ticket_in.movie_name):
            return HTTPException(status_code=404 ,detail="bu bilet allaqchon sotilgan") 
        
    price =80000 if ticket_in.is_vip else 40000
        
    new_ticket={
        "ticket_id":current_ticket_id,
        "customer_name": ticket_in.customer_name,
        "seat_number": ticket_in.seat_number,
        "movie_name":ticket_in.movie_name,
        "is_vip":ticket_in.is_vip,
        "price": price }

    tickets.append(new_ticket)
    current_ticket_id +=1
    return   new_ticket      

@api_router.get("/",response_model=list[TicketOut])
def get_all_tickets():
    
    return tickets
        
    