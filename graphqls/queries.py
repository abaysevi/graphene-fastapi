from graphene import ObjectType, List
from models.product import Product
from models.cart import CartItem
from models.sale import Sale
from db.database import products_collection, cart_collection, sales_collection
import json
from graphqls.graphene_type import ProductType, CartItemType, SaleType


class Query(ObjectType):
    products = List(ProductType)
    cart_items = List(CartItemType)
    sales = List(SaleType)
    
    async def resolve_products(self, info):
        products = []
        async for product in products_collection.find():
            product["_id"] = str(product["_id"])
            products.append(Product(**product))
        return products

    async def resolve_cart_items(self, info):
        cart_items = []
        async for cart_item in cart_collection.find():
            cart_item["_id"] = str(cart_item["_id"])
            cart_items.append(CartItem(**cart_item))
        return cart_items

    async def resolve_sales(self, info):
        sales = []
        async for sale in sales_collection.find():
            sale["_id"] = str(sale["_id"])
            sale["cart_items"] = json.loads(sale["cart_items"])
            sales.append(Sale(**sale))
        return sales
