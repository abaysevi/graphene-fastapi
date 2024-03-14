from pydantic import BaseModel

class Product(BaseModel):
    product_name: str
    product_price: float
    unique_code: str
    tax: float