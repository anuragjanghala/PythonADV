from item import Item

class Keyboard(Item):
    # all = []
    def __init__(self, name: str, price: float, quantity = 0):
        #print(f'an instance created: {name}')
        
        # Call to super function to have access to all attributes / methods
        super().__init__(
            name,price,quantity
        )
        
        