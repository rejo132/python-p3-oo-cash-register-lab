#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.last_transaction = None
    
    def add_item(self, title, price, quantity=1):
        self.total += price * quantity
        self.items.extend([title] * quantity)
        self.last_transaction = (title, price, quantity)
    
    def apply_discount(self):
        if self.discount == 0:
            print("There is no discount to apply.")
        else:
            discount_amount = self.total * (self.discount / 100)
            self.total = int(self.total - discount_amount)
            print(f"After the discount, the total comes to ${self.total}.")
    
    def void_last_transaction(self):
        if self.last_transaction is None:
            return
        title, price, quantity = self.last_transaction
        self.total -= price * quantity
        for _ in range(quantity):
            self.items.pop(self.items.index(title))
        self.last_transaction = None