'''
Create an Account class that mimics the account table
'''
import typing as t

class Account():
    def __init__(self, investor_id: int, balance: float, account_type: str, id: int=-1):
        self.id = id
        self.investor_id = investor_id
        self.balance = balance
        self.account_type = account_type
    
    def __str__(self) -> str:
        return f'[id: {self.id}, investor_id: {self.investor_id}, balance: {self.balance}, account_type: {self.account_type}]'

    @staticmethod
    def from_dict(dict):
        if dict.get('investor_id') is None or dict.get('balance') is None or dict.get('account_type') is None or dict.get('id') is None: # all attributes are required
            raise Exception(f'Cannot create Account object from dict {dict}: missing required attributes')
        else:
            return Account(dict.get('investor_id'), dict.get('balance'), dict.get('account_type'))
    