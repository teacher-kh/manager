from datetime import datetime
from typing import Union

class PositiveValue:    
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError(f'{self.name.capitalize()} must be a positive value!')
        instance.__dict__[self.name] = value

class Transaction:    
    amount = PositiveValue()

    def __init__(self, amount: float, category: str, date: Union[str, datetime] = None, description: str = None):
        self.amount = amount
        self.category = category
        self.description = description
        self.date = (datetime.strptime(date, '%Y-%m-%d') if isinstance(date, str) else 
                     (date or datetime.now()))

    def __repr__(self):
        return f'<Transaction {self.amount}: {self.category} - {self.date.strftime("%Y-%m-%d")}>'

    def to_dict(self):
        return {
            'amount': self.amount,
            'category': self.category,
            'date': self.date.strftime("%Y-%m-%d %H:%M:%S"),
            'description': self.description
        }

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            amount=data['amount'],
            category=data['category'],
            date=datetime.strptime(data['date'], '%Y-%m-%d %H:%M:%S'),
            description=data.get('description')
        )
