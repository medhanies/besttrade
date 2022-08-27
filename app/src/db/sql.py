
# Investor SQL statements
get_all_investors_sql = 'SELECT id, name, address, brokerage, status FROM investor'
get_investor_count = 'SELECT COUNT(*) AS cnt FROM investor'
get_active_investor_count = "SELECT COUNT(*) AS cnt FROM investor WHERE status = 'ACTIVE'"
investor_by_id = 'SELECT name, address, brokerage, status, id FROM investor WHERE id = %s'
get_investors_by_name_sql = 'SELECT name, address, brokerage, status, id FROM investor WHERE name = %s'
create_investor = 'INSERT INTO investor (name, address, brokerage, status) VALUES (%s, %s, %s, %s)'
update_investor_name = 'UPDATE investor SET name = %s WHERE id = %s'
update_investor_address = 'UPDATE investor SET address = %s WHERE id = %s'
delete_investor_broke = 'DELETE FROM investor WHERE brokerage = %s'
delete_investor_by_id = 'delete from investor where id = %s'

# Account SQL statements
get_all_accounts = 'SELECT investor_id, balance, account_type, id FROM account'
account_by_id = 'SELECT investor_id, balance, account_type, id FROM account WHERE id = %s'
get_accounts_by_balance_sql = 'SELECT investor_id, balance, account_type, id FROM account WHERE balance = %s'
create_account = 'INSERT INTO account (investor_id, balance, account_type) VALUES (%s, %s, %s)'
update_account_balance = 'UPDATE account SET balance = %s WHERE id = %s'
delete_account_id = 'DELETE FROM account WHERE id = %s'

# Portfolio SQL statements
get_all_portfolios = 'SELECT account_id, ticker, brokerage, quantity, id FROM portfolio'
get_account_balance_by_id = 'SELECT balance from account WHERE account_id = %s'
portfolio_by_id = 'SELECT account_id, ticker, brokerage, quantity, id FROM portfolio WHERE id = %s'
get_portfolio_by_ticker_sql = 'SELECT account_id, ticker, brokerage, quantity, id FROM portfolio WHERE ticker = %s'
create_portfolio = 'INSERT INTO portfolio (account_id, ticker, brokerage, quantity) VALUES (%s, %s, %s, %s)'
update_portfolio_quantity = 'UPDATE portfolio SET quantity = %s WHERE id = %s'
update_portfolio_ticker = 'UPDATE portfolio SET ticker = %s WHERE id = %s'
update_portfolio_brokerage = 'UPDATE portfolio SET brokerage = %s WHERE id = %s'
delete_portfolio_id = 'DELETE FROM portfolio WHERE id = %s'
delete_portfolio_ticker = 'DELETE FROM portfolio WHERE ticker = %s'
delete_portfolio_broke = 'DELETE FROM portfolio WHERE brokerage = %s'
get_stock_quantity = 'SELECT quantity from portfolio WHERE account_id = %s AND ticker = %s'
update_portfolio = 'UPDATE portfolio SET quantity = current_qty - quantity WHERE account_id = %s'
