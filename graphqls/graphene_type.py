import graphene

class ProductType(graphene.ObjectType):
    product_name = graphene.String()
    product_price = graphene.Float()
    unique_code = graphene.String()
    tax = graphene.Float()

class CartItemType(graphene.ObjectType):
    product_name = graphene.String()
    product_price = graphene.Float()
    unique_code = graphene.String()
    tax = graphene.Float()
    quantity = graphene.Int()

class SaleType(graphene.ObjectType):
    cart_items = graphene.List(CartItemType)
    total_amount = graphene.Float()
    payment_option = graphene.String()