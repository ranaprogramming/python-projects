import json
class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self._price = price
        self._stock = stock

    def __str__(self):
        return f"Product: {self.name} | Price: {self._price} | Stock: {self._stock}"
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            print("price cannot be negative")
        else:
            self._price = value

    @property
    def stock(self):
        return self._stock

    @stock.setter
    def stock(self, value):
        if value < 0:
            print("Stock cannot be negative")
        else:
            self._stock = value

    @classmethod
    def create_product(cls, name, price, stock):
        return cls(name, price, stock)



products = []
cart = []

def add_product():
        name = input("Enter product name: ")
        price = int(input("Enter product price: "))
        stock = int(input("Enter product Stock: "))
        product = Product(name, price, stock)
        products.append(product)
        save_product()

def view_products():
    if len(products) == 0:
            print("No product found")
    else:
        for product in products:
            print(product)

def search_product():
    product_name = input("Enter product name to search: ")
    for product in products:
        if product.name == product_name:
            print(product)
            break
    else:
        print("Product not found")
def add_to_cart():
    product_name = input("Enter Product Name: ")
    for product in products:
        if product.name == product_name:
            if product.stock <= 0:
                print("Out of Stock") 
            else:               
                cart.append(product)
                product.stock -= 1
                print(f"{product.name} is add to cart successfully")
            break
    else:
        print("product not found")
def view_cart():
    if len(cart) == 0:
        print("Cart is empty")
    else:
        for product in cart:
            print(f"{product.name} | {product.price}")
def place_order():
    total = 0
    if len(cart) == 0:
            print("Cart is empty")
    else:
        for product in cart:
            total += product.price
        print(f"Total Amount: {total}")
        cart.clear()
        print("Order Placed Successfully")

def update_stock():
    product_name = (input("Enter product name to search: "))
    for product in products:
        if product.name == product_name:
            update = int(input("How many units to add? "))
            product.stock += update
            print(f"Stock is Updated. New Stock of {product.name} is {product.stock}")
            break
    else:
        print("No product found")

def save_product():
    data = []

    for product in products:
        data.append({
            "product_name": product.name,
            "price": product.price,
            "stock": product.stock
        })
    with open("product.json", "w") as file:
        json.dump(data, file, indent = 4)
    print("Product Added Successfully")
while True:
    print("1. Add Product")
    print("2: View Product")
    print("3: Search Product")
    print("4: Add to Cart")
    print("5: View Cart")
    print("6: Place Order")
    print("7: Update Stock")
    print("8: Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_product()

    elif choice == "2":
        view_products()

    elif choice == "3":
        search_product()
    elif choice == "4":
        add_to_cart()
    elif choice == "5":
        view_cart()
    elif choice == "6":
        place_order()
    elif choice == "7":
        update_stock()
    elif choice == "8":
            break