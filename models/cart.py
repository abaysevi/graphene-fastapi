from pydantic import BaseModel

class CartItem(BaseModel):
    product_name: str
    product_price: float
    unique_code: str
    tax: float
    quantity: int