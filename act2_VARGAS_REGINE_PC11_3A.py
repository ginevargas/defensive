class Product: 
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
class ShoppingCart:
    def __init__(self, user_balance=0):
        self.user_balance = user_balance
        self.products = []
    
    def add_product(self, product):
        if product.price <= self.user_balance:
            self.products.append(product)
            self.user_balance -= product.price
            print(f"Added {product.name} to the cart: Price: ₱{product.price}")
        else:
            print("\nInsufficient balance to add the product.")

    def list_products(self):
        if self.products:
            print("\nProducts in the cart:")
            for index, product in enumerate(self.products):
                print(f"{index + 1}. {product.name} - ₱{product.price}")
        else:
            print("Your cart is empty.")

    def purchase_product(self, index):
        if 0 <= index < len(self.products):
            product = self.products[index]
            if product.price <= self.user_balance:
                self.user_balance -= product.price
                del self.products[index]
                print(f"\nPurchased {product.name}. Remaining balance: ₱{self.user_balance}")
            else:
                print("\nInsufficient balance to purchase the product.")
        else:
            print("Invalid product index.")
    
if __name__ == "__main__":

    my_cart = ShoppingCart(user_balance=1000000)

    laptop = Product("Laptop", 89000)
    phone = Product("Phone", 10000)
    keyboard = Product("Keyboard", 10000)
    mouse = Product("Mouse", 1000)
    charger = Product("Charger", 1000)
    powerbank = Product("Powerbank", 2000)

    my_cart.add_product(laptop)
    my_cart.add_product(phone)
    my_cart.add_product(keyboard)
    my_cart.add_product(mouse)
    my_cart.add_product(charger)
    my_cart.add_product(powerbank)

    my_cart.list_products()

    print(f"\nAvailable balance:₱{my_cart.user_balance}")
    my_cart.purchase_product(0)
    my_cart.purchase_product(3)
    my_cart.purchase_product(2)





    


        