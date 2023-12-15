import pyinputplus as pyip

class SandwichOrderSystem:
    def __init__(self):
        #prices as is, don't change it
        self.prices_dict = {
            'breads': {
                'wheat': 10.00,
                'white': 10.25,
                'sourdough': 20.00,
            },
            'proteins': {
                'chicken': 10.50,
                'turkey': 10.25,
                'ham': 10.75,
                'tofu': 20.00,
            },
            'cheeses': {
                'cheddar': 10.75,
                'Swiss': 10.25,
                'mozzarella': 11.25,
            },
            'add_ons': {
                'mayo': 5.5,
                'mustard': 5.25,
                'lettuce': 5.50,
                'tomat': 5.50,
            }
        }
        self.discountcode_list = [43312, 67433, 67886, 55534, 89074]  # you can add more
        self.total_price = 0

    # you can add more functions if you wish
    def order_sandwiches(self):
        # your code here
        print("Welcome to the Sandwich Order System!")
        while True:
            breads = pyip.inputMenu(['wheat', 'white', 'sourdough'], numbered=True, prompt='Please select bread type: \n')
            proteins = pyip.inputMenu(['chicken', 'turkey', 'ham', 'tofu'], numbered=True, prompt='Please select protein type: \n')
            
            want_cheeses = pyip.inputYesNo(prompt='Do you want cheese? (y/n): ')
            if want_cheeses.lower().startswith('y'):
                cheeses = pyip.inputMenu(['cheddar', 'Swiss', 'mozzarella'], numbered=True, prompt='Please select cheese type: \n')
            else:
                cheeses = 'No Cheese'

            mayo = pyip.inputYesNo(prompt='Do you want mayo? (yes/no): ')
            mustard = pyip.inputYesNo(prompt='Do you want mustard? (yes/no): ')
            lettuce = pyip.inputYesNo(prompt='Do you want lettuce? (yes/no): ')
            tomato = pyip.inputYesNo(prompt='Do you want tomato? (yes/no): ')
            
            quantity = pyip.inputInt(prompt='How many sandwiches do you want?: ', min=1)
            
            add_ons = ', '.join([addon for addon, choice in [('mayo', mayo), ('mustard', mustard), ('Lettuce', lettuce), ('Tomato', tomato)] if choice.lower().startswith('y')])
            
            sandwich_price = (self.prices_dict['breads'][breads] +
                            self.prices_dict['proteins'][proteins] +
                            self.prices_dict['cheeses'][cheeses] +
                            sum([self.prices_dict['add_ons'][add.strip()] for add in add_ons.split(', ')])) * quantity
            
            print(f"The price will be: P{sandwich_price:.2f}")
            
            self.order.append((breads, proteins, cheeses, add_ons, quantity, sandwich_price))
            
            another_sandwich = pyip.inputYesNo(prompt='Add another sandwich? (yes/no): ')
            if not another_sandwich.lower().startswith('y'):
                break


    def apply_discount_code(self):
        # your code here
        discount_code = pyip.inputStr(prompt='Have a Discount code? ')
        if discount_code in self.discountcode_list:
            self.total_price *= 0.25
            print("Discount applied! Your new total price is: P{:.2f}".format(self.total_price))
        else:
            print("Invalid discount code. No discount applied.")

    def print_total_price(self):
        # your code here
        self.total_price = sum([item[5] for item in self.order])
        print("\nOrder Summary:")
        for item in self.order:
            print(f"{item[4]} {item[0]} sandwich with {item[1]} and {item[2]} cheeses, add_ons: {item[3]}, P{:.2}".format(item[5]))
            print("\nTotal Price: P{:.2f}".format(self.total_price))

if __name__ == "__main__":
    order_system = SandwichOrderSystem()
    order_system.order_sandwiches()
    order_system.apply_discount_code()
    order_system.print_total_price()

