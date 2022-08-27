'''
Create CRUD functions for the account data table. Example: get_account_by_id
'''
import typing as t
from mysql.connector import MySQLConnection
from .dbutils import get_db_cnx
from app.src.domain.Account import Account
from app.src.domain.Portfolio import Portfolio
import app.src.db.sql as sql

def get_all_accounts() -> t.List[Account]:
    try:
        db_cnx: MySQLConnection = get_db_cnx()
        cursor = db_cnx.cursor(dictionary=True) # results will return as a dict
        cursor.execute(sql.get_all_accounts)
        rs = cursor.fetchall()
        if len(rs) == 0:
            return []
        else:
            accounts = []
            for row in rs:
                accounts.append(Account(row.get('investor_id'), row.get('balance'), row.get('account_type'), row.get('id')))
            return accounts
    except Exception as e:
        print(f'An exception occurred while trying to get a list of all accounts: {str(e)}')
    finally:
        cursor.close()
        db_cnx.close() # to prevent any memory leaks

def get_balance(account_id: int) -> float:
    try:
        db_cnx: MySQLConnection = get_db_cnx()
        cursor = db_cnx.cursor(dictionary=True)
        cursor.execute(sql.get_account_balance_by_id, (account_id,))
        rs = cursor.fetchone()
        if rs is None:
            return None
        return Account(rs['balance'])
    except Exception as e:
        print(f'Unable to retrieve account by Id {id}: {str(e)}')
    finally:
        cursor.close()
        db_cnx.close()

def get_account_by_id(id: int) -> t.Optional[Account]:
    try:
        db_cnx: MySQLConnection = get_db_cnx()
        cursor = db_cnx.cursor(dictionary=True)
        cursor.execute(sql.account_by_id, (id,))
        rs = cursor.fetchone()
        if rs is None:
            return None
        return Account(rs['investor_id'], rs['balance'], rs['account_type'], rs['id'])
    except Exception as e:
        print(f'Unable to retrieve account by Id {id}: {str(e)}')
    finally:
        cursor.close()
        db_cnx.close()

def get_accounts_by_balance(balance: float) -> t.Optional[Account]:
    try:
        db_cnx: MySQLConnection = get_db_cnx()
        cursor = db_cnx.cursor(dictionary=True)
        cursor.execute(sql.get_accounts_by_balance_sql, (balance, ))
        rs = cursor.fetchone()
        if rs is None:
            return None
        return Account(rs['investor_id'], rs['balance'], rs['account_type'], rs['id'])
    except Exception as e:
        print(f'Unable to retrieve account by balance {balance}: {str(e)}')
    finally:
        cursor.close()
        db_cnx.close()

def create_account(account: Account) -> None:
    try:
        db_cnx: MySQLConnection = get_db_cnx()
        cursor = db_cnx.cursor()
        cursor.execute(sql.create_account, (account.investor_id, account.balance, account.account_type))
        db_cnx.commit()
    except Exception as e:
        print(f'Unable to create a new account: {str(e)}')
    finally:
        cursor.close()
        db_cnx.close()


def update_account_balance(id: int, balance: float) -> None:
    try:
        db_cnx: MySQLConnection = get_db_cnx()
        cursor = db_cnx.cursor()
        cursor.execute(sql.update_account_balance, (balance, id))
        db_cnx.commit()
    except Exception as e:
        print(f'Unable to update account balance: {str(e)}')
    finally: 
        cursor.close()
        db_cnx.close()

def delete_account_id(id: int) -> None:
    try:
        db_cnx: MySQLConnection = get_db_cnx()
        cursor = db_cnx.cursor()
        cursor.execute(sql.delete_account_id, (id,))
        db_cnx.commit()
    except Exception as e:
        print(f'Unable to delete account: {str(e)}')
    finally: 
        cursor.close()
        db_cnx.close()