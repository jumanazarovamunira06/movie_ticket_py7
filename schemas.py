from pydantic import BaseModel,Field


class TicketCreate(BaseModel):
    movie_name: str=Field(max_length=200)
    seat_number: int=Field(ge=1,le=50)
    customer_name: str =Field(max_length=100)
    is_vip: bool=False
    
class TicketOut(BaseModel):
    ticket_id: int =Field(le=1)
    movie_name: str=Field(max_length=200)
    seat_number: int=Field(ge=1,le=50)
    customer_name: str =Field(max_length=100)
    is_vip: bool=False
    price: float=Field(decimal_places=2, max_digits=10,default=0)