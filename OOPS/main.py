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
        self.name = name
        self.price = price
        self.quantity = quantity
        
        
        # Actions to execute
        Item.all.append(self)
    
    def calculate_total_price(self):
        return self.price * self.quantity  #x * y
    
    def apply_discount(self):
        self.price = self.price * self.pay_rate
    
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

# Inheritance
# here we are inheriting from Item class(Parent Class) to Phone class(Child class)
class Phone(Item):
    # all = []
    def __init__(self, name: str, price: float, quantity = 0, broken_phones = 0):
        #print(f'an instance created: {name}')
        
        # Call to super function to have access to all attributes / methods
        super().__init__(
            name,price,quantity
        )
        
        # Run validations to the recieved arguments
        assert broken_phones >= 0, f"Broken phones {broken_phones} is not greater than or equal to zero!"
        
        # Assign to self object
        self.broken_phones = broken_phones
        
        
        # Actions to execute
        # Phone.all.append(self)


phone1 = Phone("jscPhonev10", 500, 5, 1)

print(Item.all)
print(Phone.all)


# phone1 = Phone("jscPhonev10", 500, 5, 1)
# print(phone1.calculate_total_price())
# # phone1.broken_phones = 1
# phone2 = Phone("jscPhonev20", 700, 5, 1)
# # phone2.broken_phones = 1




        
# Item.instantiate_from_csv()
# print(Item.all)

# print(Item.is_integer(7.0))



# item1 = Item("Phone", 100, 1)
# item2 = Item("Laptop", 1000, 3)
# item3 = Item("Cable", 10, 5)
# item4 = Item("Mouse", 50, 5)
# item5 = Item("Keyboard", 75, 5)

# print(Item.all)

# for instance in Item.all:
#     print(instance.name)


# item1 = Item("Phone",100,1)
# item1.name = "Phone"
# item1.price = 100
# item1.quantity = 5
# print(item1.name, item1.price, item1.quantity)
# print(item1.calculate_total_price())


# item2 = Item("Laptop",1000,3)
# item2.name = "Laptop"
# item2.price = 1000
# item2.quantity = 3
# print(item2.name, item2.price, item2.quantity)
# print(item2.calculate_total_price())


# print(Item.__dict__) # All the attributes for class level
# print(item1.__dict__) # All the attributes for instance level


# item1.apply_discount()
# print(item1.price)


# item2.pay_rate = 0.7
# item2.apply_discount()
# print(item2.price)


# print(type(item1))
# print(type(item1.name))
# print(type(item1.price))
# print(type(item1.quantity))
# print(item1.name.upper())
