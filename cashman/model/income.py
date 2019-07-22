from marshmallow import post_load

from .transaction import Transaction, TransactionSchema
from .transaction_type import TransactionType

class Income(Transaction):
    def __init__(self, description, amount):
        super(Income, self).__init__(description, amount, TransactionType.INCOME)

    def __repr__(self):
        return '<Income(name={self.description!r})>'.format(self=self)

class IncomeSchema(TransactionSchema):
    @post_load
    # Register make_income method to invoke after deserializing income object and returns processed income data
    def make_income(self, data):
        return Income(**data)