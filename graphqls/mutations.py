import graphene
from db.database import products_collection,sales_collection,cart_collection  # Import your products collection
from graphqls.graphene_type import ProductType,CartItemType,SaleType
# Define the mutation class
class CreateProduct(graphene.Mutation):
    # Define the arguments for the mutation
    class Arguments:
        product_name = graphene.String(required=True)
        product_price = graphene.Float(required=True)
        unique_code = graphene.String(required=True)
        tax = graphene.Float(required=True)

    # Define the output fields of the mutation
    product = graphene.Field(ProductType)

    # Define the logic to mutate/create the product
    async def mutate(root, info, product_name, product_price, unique_code, tax):
        print("Received product data:")
        print("Product Name:", product_name)
        print("Product Price:", product_price)
        print("Unique Code:", unique_code)
        print("Tax:", tax)

        result = products_collection.insert_one({
            "product_name": product_name,
            "product_price": product_price,
            "unique_code": unique_code,
            "tax": tax
        })

        # Retrieve the inserted product from the collection using the inserted_id
        inserted_product = products_collection.find_one({"_id": result.inserted_id})

        # Construct a ProductType object using the retrieved data
        product_instance = ProductType(
            product_name=inserted_product["product_name"],
            product_price=inserted_product["product_price"],
            unique_code=inserted_product["unique_code"],
            tax=inserted_product["tax"]
        )

        # Return the product instance as the mutation response
        return CreateProduct(product=product_instance)


class CreateSale(graphene.Mutation):
    class Arguments:
        cart_items = graphene.List(graphene.JSONString, required=True)
        total_amount = graphene.Float(required=True)
        payment_option = graphene.String(required=True)

    sale = graphene.Field(SaleType)

    async def mutate(root, info, cart_items, total_amount, payment_option):
        print("Received sale data:")
        print("Cart Items:", cart_items)
        print("Total Amount:", total_amount)
        print("Payment Option:", payment_option)

        # Insert the sale data into the sales collection
        result = sales_collection.insert_one({
            "cart_items": cart_items,
            "total_amount": total_amount,
            "payment_option": payment_option
        })

        # Retrieve the inserted sale from the collection
        inserted_sale = sales_collection.find_one({"_id": result.inserted_id})

        # Construct a SaleType instance
        sale_instance = SaleType(
            cart_items=inserted_sale['cart_items'],
            total_amount=inserted_sale["total_amount"],
            payment_option=inserted_sale["payment_option"]
        )

        return CreateSale(sale=sale_instance)


class CreateCartItem(graphene.Mutation):
    class Arguments:
        product_name = graphene.String(required=True)
        product_price = graphene.Float(required=True)
        unique_code = graphene.String(required=True)
        tax = graphene.Float(required=True)
        quantity = graphene.Int(required=True)

    cart_item = graphene.Field(CartItemType)

    async def mutate(root, info, product_name, product_price, unique_code, tax, quantity):
        print("Received cart item data:")
        print("Product Name:", product_name)
        print("Product Price:", product_price)
        print("Unique Code:", unique_code)
        print("Tax:", tax)
        print("Quantity:", quantity)

        result = cart_collection.insert_one({
            "product_name": product_name,
            "product_price": product_price,
            "unique_code": unique_code,
            "tax": tax,
            "quantity": quantity
        })

        inserted_cart_item = cart_collection.find_one({"_id": result.inserted_id})

        cart_item_instance = CartItemType(
            product_name=inserted_cart_item["product_name"],
            product_price=inserted_cart_item["product_price"],
            unique_code=inserted_cart_item["unique_code"],
            tax=inserted_cart_item["tax"],
            quantity=inserted_cart_item["quantity"]
        )

        return CreateCartItem(cart_item=cart_item_instance)



# Define the mutation class
class Mutation(graphene.ObjectType):
    create_product = CreateProduct.Field()
    create_cart_item = CreateCartItem.Field()
    create_sale = CreateSale.Field()
