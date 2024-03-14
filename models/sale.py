from pydantic import BaseModel
from typing import List
from models.cart import CartItem

class Sale(BaseModel):
    cart_items: List[CartItem]
    total_amount: float
    payment_option: str