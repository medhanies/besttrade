'''
Create CRUD functions for the portfolio data table. Example: get_portfolio_by_id
'''
import typing as t
from mysql.connector import MySQLConnection

from .dbutils import get_db_cnx
from app.src.domain.Portfolio import Portfolio
import app.src.db.sql as sql

def get_all_portfolios() -> t.List[Portfolio]: # empty list if no investors are created in the db
    try:
        db_cnx: MySQLConnection = get_db_cnx()
        cursor = db_cnx.cursor(dictionary=True) # results will return as a dict
        cursor.execute(sql.get_all_portfolios)
        rs = cursor.fetchall()
        if len(rs) == 0:
            return []
        else:
            investors = []
            for row in rs:
                investors.append(Portfolio(row.get('account_id'), row.get('ticker'), row.get('brokerage'), row.get('quantity'), row.get('id')))
            return investors
    except Exception as e:
        print(f'An exception occurred while trying to get a list of all portfolios: {str(e)}')
    finally:
        cursor.close()
        db_cnx.close() # to prevent any memory leaks

def get_portfolio_by_id(id: int) -> t.Optional[Portfolio]:
    try:
        db_cnx: MySQLConnection = get_db_cnx()
        cursor = db_cnx.cursor(dictionary=True)
        cursor.execute(sql.portfolio_by_id, (id,))
        rs = cursor.fetchone()
        if rs is None:
            return None
        return Portfolio(rs['account_id'], rs['ticker'], rs['brokerage'], rs['quantity'], rs['id'])
    except Exception as e:
        print(f'Unable to retrieve portfolio by Id {id}: {str(e)}')
    finally:
        cursor.close()
        db_cnx.close()

def get_portfolio_by_ticker(ticker: str) -> t.Optional[Portfolio]:
    try:
        db_cnx: MySQLConnection = get_db_cnx()
        cursor = db_cnx.cursor(dictionary=True)
        cursor.execute(sql.get_portfolio_by_ticker_sql, (ticker, ))
        rs = cursor.fetchone()
        if rs is None:
            return None
        return Portfolio(rs['account_id'], rs['ticker'], rs['brokerage'], rs['quantity'], rs['id'])
    except Exception as e:
        print(f'Unable to retrieve portfolio by ticker {ticker}: {str(e)}')
    finally:
        cursor.close()
        db_cnx.close()

def create_portfolio(portfolio: Portfolio) -> None:
    try:
        db_cnx: MySQLConnection = get_db_cnx()
        cursor = db_cnx.cursor()
        cursor.execute(sql.create_portfolio, (portfolio.account_id, portfolio.ticker, portfolio.brokerage, portfolio.quantity))
        db_cnx.commit()
    except Exception as e:
        print(f'Unable to create a new portfolio: {str(e)}')
    finally:
        cursor.close()
        db_cnx.close()

def update_portfolio_quantity(id: int, quantity: int) -> None:
    try:
        db_cnx: MySQLConnection = get_db_cnx()
        cursor = db_cnx.cursor()
        cursor.execute(sql.update_portfolio_quantity, (quantity, id))
        db_cnx.commit()
    except Exception as e:
        print(f'Unable to update portfolio quantity: {str(e)}')
    finally: 
        cursor.close()
        db_cnx.close()

def update_portfolio_ticker(id: int, ticker: str) -> t.Optional[Portfolio]:
    try:
        db_cnx: MySQLConnection = get_db_cnx()
        cursor = db_cnx.cursor()
        cursor.execute(sql.update_portfolio_ticker, (ticker, id))
        db_cnx.commit()
    except Exception as e:
        print(f'Unable to update portfolio ticker: {str(e)}')
    finally: 
        cursor.close()
        db_cnx.close()

def update_portfolio_broke(id: int, brokerage: str) -> t.Optional[Portfolio]:
    try:
        db_cnx: MySQLConnection = get_db_cnx()
        cursor = db_cnx.cursor()
        cursor.execute(sql.update_portfolio_brokerage, (brokerage, id))
        db_cnx.commit()
    except Exception as e:
        print(f'Unable to update portfolio brokerage: {str(e)}')
    finally: 
        cursor.close()
        db_cnx.close()

def delete_portfolio_id(id: int) -> None:
    try:
        db_cnx: MySQLConnection = get_db_cnx()
        cursor = db_cnx.cursor()
        cursor.execute(sql.delete_portfolio_id, (id,))
        db_cnx.commit()
    except Exception as e:
        print(f'Unable to delete portfolio id: {str(e)}')
    finally: 
        cursor.close()
        db_cnx.close()

def delete_portfolio_broke(brokerage: str) -> None:
    try:
        db_cnx: MySQLConnection = get_db_cnx()
        cursor = db_cnx.cursor()
        cursor.execute(sql.delete_portfolio_broke, (brokerage,))
        db_cnx.commit()
    except Exception as e:
        print(f'Unable to delete portfolio id: {str(e)}')
    finally: 
        cursor.close()
        db_cnx.close()

def get_stock_quantity(account_id: int, ticker: str):
    try:
        db_cnx: MySQLConnection = get_db_cnx()
        cursor = db_cnx.cursor(dictionary=True)
        cursor.executesql(sql.get_stock_quantity, (ticker, account_id))
        rs = cursor.fetchone()
        if rs is None:
            return None
        return Portfolio(rs['account_id'], rs['ticker'], rs['brokerage'], rs['quantity'], rs['id'])
    except Exception as e:
        print(f'Unable to retrieve portfolio by account id {account_id} and ticker {ticker}: {str(e)}')
    finally:
        cursor.close()
        db_cnx.close()
#returns the quantity: select quantity from portfolio where account_id = account_id and ticker = ticker

def sell_stock(account_id: int, ticker: int, quantity: int, profit: int):
    current_qty = get_stock_quantity(account_id, ticker)
    if current_qty == quantity:
        try: 
            db_cnx: MySQLConnection = get_db_cnx()
            cursor = db_cnx.cursor()
            cursor.execute(sql.delete_portfolio_ticker, (ticker, ))
            db_cnx.commit()
        except Exception as e:
            print(f'Unable to delete ticker {ticker}: {str(e)}')            
        finally: 
            cursor.close()
            db_cnx.close()
    elif current_qty > quantity:
        try: 
            db_cnx: MySQLConnection = get_db_cnx()
            cursor = db_cnx.cursor()
            cursor.execute(sql.update_portfolio, (ticker, ))
            db_cnx.commit()
        except Exception as e:
            print(f'Unable to update ticker {ticker}: {str(e)}')            
        finally: 
            cursor.close()
            db_cnx.close()
    
