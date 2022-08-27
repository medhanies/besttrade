'''
Create a Portfolio class that mimics the portfolio object
'''
import typing as t

class Portfolio():
    def __init__(self, account_id: int, ticker: str, brokerage: str, quantity: int, id: int = -1):
        self.id = id
        self.account_id = account_id
        self.ticker = ticker
        self.brokerage = brokerage
        self.quantity = quantity

    def __str__(self): 
        return f'[id: {self.id}, account_id: {self.account_id}, ticker: {self.ticker}, brokerage: {self.brokerage}, quantity: {self.quantity}]'

    @staticmethod
    def from_dict(dict):
        if dict.get('account_id') is None or dict.get('ticker') is None or dict.get('brokerage') is None or dict.get('quantity') is None: # all attributes are required
            raise Exception(f'Cannot create Portfolio object from dict {dict}: missing required attributes')
        else:
            return Portfolio(dict.get('account_id'), dict.get('ticker'), dict.get('brokerage'), dict.get('quantity'))
    