from app.src.db.account_dao import create_account, delete_account_id, get_account_by_id, get_accounts_by_balance, update_account_balance
from app.src.db.investor_dao import get_all_investors, create_investor, delete_investor_broke, get_investor_by_id, get_investors_by_name, update_investor_address, update_investor_name
from app.src.db.portfolio_dao import create_portfolio, delete_portfolio_broke, delete_portfolio_id, get_portfolio_by_id, get_portfolio_by_ticker, update_portfolio_quantity, update_portfolio_ticker
from app.src.domain.Account import Account
from app.src.domain.Investor import Investor
from app.src.domain.Portfolio import Portfolio
from app.src.db.investor_dao import create_investor

def main():

    '''Investor'''

    investors = get_all_investors()
    for investor in investors:
        print(investor)

    investor_id = get_investor_by_id(10)
    print(investor_id)

    new_address = update_investor_address(10, '800 W St')
    print(new_address)

    get_investor = get_investors_by_name('jimmy walker')
    print(get_investor)

    create_i = create_investor(Investor('mike tyson', '3983 Knockout Way', 'M1 Finance', 'ACTIVE'))
    print(create_i)

    update_i = update_investor_name(3, 'jon snow')
    print(update_i)

    update_a = update_investor_address(6, '4923 Montgomerey Rd')
    print(update_a)

    delete_investor = delete_investor_broke('M1 Finance')
    print(delete_investor)

    '''Account'''

    account_id = get_account_by_id(4)
    print(account_id)
    
    account_balance = get_accounts_by_balance(5000000.00)
    print(account_balance)

    account_create = create_account(Account(11, 45000, 'Retirement'))
    print(account_create)

    update_account = update_account_balance(4, 75000)
    print(update_account)

    delete_account = delete_account_id(11)
    print(delete_account)

    '''Portfolio'''

    get_portfolio = get_portfolio_by_id(1)
    print(get_portfolio)

    get_ticker = get_portfolio_by_ticker("AAPL")
    print(get_ticker)

    portfolio_create = create_portfolio(Portfolio(10, 'AAPL', 'M1 Finance', 70))
    print(portfolio_create)

    port_update_id = update_portfolio_quantity(2, 5000)
    print(port_update_id)

    port_update_ticker = update_portfolio_ticker(2, 'JIMM')
    print(port_update_ticker)

    delete_portfolio = delete_portfolio_id(16)
    print(delete_portfolio)

    delete_port_broke = delete_portfolio_broke('M1 Finance')
    print(delete_port_broke)

if __name__ == '__main__':
    main()
