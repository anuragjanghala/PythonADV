import csv

class Item:
    pay_rate = 0.8 # The pay rate after 20% discount
    all = []
    def __init__(self, name: str, price: float, quantity = 0):
        #print(f'an instance created: {name}')
        
        # Run validations to the recieved arguments
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero!"
        
        # Assign to self object
        self.__name = name
        self.__price = price
        self.quantity = quantity
        
        
        # Actions to execute
        Item.all.append(self)
    
    @property
    def price(self):
        return self.__price
    
    
    def apply_discount(self):
        self.__price = self.__price * self.pay_rate
    
    
    def apply_increment(self, increment_value):
        self.__price = self.price + self.__price * increment_value
    
    
    @property
    # Property Decorator = Read-only Attribute
    def name(self):
        #print('you are trying to get an attribute')
        return self.__name  # this double underscore will create private readonly attribute
    
    @name.setter # this decorator can be used to set new value to private read-only attribute attribute
    def name(self, value):
        #print('you are trying to set an attribute')
        if len(value) > 10:
            raise Exception('The name is too long')
        self.__name = value  # here we can set new values
    
    def calculate_total_price(self):
        return self.__price * self.quantity  #x * y
    
    
    
    @classmethod    
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        
        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity')),
            )
    
    
    @staticmethod
    def is_integer(num):
        # we will count out the floats that are oint zero
        # For i.e: 5.0, 10.0
        if isinstance(num, float):
            # Count out the floats that are point zero
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False
        
        
    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}, {self.price}, {self.quantity}')"
    
    # @property
    # def read_only_name(self):
    #     return "AAA"