"""The code below makes use of an items dictionary to simulate 
    vendor machine item and prices;
    It first prints welcome messages, iterates through the dictionary
    to produce a list of items and prices then prompts user for an input.
    verifies if the input is valid before stepping in and executing payment
    prompt.
    Here it checks if the amount deposited by user cover expense for product.
    and display messages according to satisfied condition
    Error handling to handle user input
"""

items = {
    1: {'name':'Candy', 'price': 1.95},
    2: {'name':'Chips', 'price': 2.95},
    3: {'name':'Soda', 'price': 3.95},
    4: {'name': 'water', 'price':4.99}
}


class machine():
    
    print("**********\n Welocom to the vending manchine \n **************")
    print("Please Select an Item")
    
    def __init__(self):
        for key, item in items.items():
            print(f"{key}. {item['name']}: {item['price']}")
            
        self.option = int(input("Make a selection: "))
        
        self.cart()
    
    def cart(self):
        if self.option in items:
            cart = items[self.option]
            print(f"You have selected {cart['name']}!")
            print(f"Amount to be paid {cart['price']}")
    
            try:
                payment = float(input(f"Please insert ${cart['price']:.2f}: "))
                if payment > cart['price']:
                    balance = payment - cart['price']
                    print(f"Thank you for purchase!, Balance is ${balance:.2f}.")
                else:
                    print("Insufficient Funds, Pay higher deposit")
                    balance_due = payment - cart['price']
                    print(f"Remains ${balance_due:.2f}")
            except ValueError:
                print("Please enter a valid input (numeric origins)")
        else:
            print("Invalid selection, Please try again!!!")
                    


if __name__ == "__main__":
    machine()