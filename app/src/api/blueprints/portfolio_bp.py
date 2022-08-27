# create portfolio blueprint
# minimum endpoints:
# Create/Update/Delete/GET
# /buy-stock: adds a new stock to an investor portfolio
# /sell-stock: removes a stock from the investor portfolio

# this file will contain all the endpoints that relate to the investor resource
# expected endpoints: create/update/remove/get
from http import HTTPStatus
import json
from flask import Blueprint, make_response, request
from app.src.db.portfolio_dao import get_stock_quantity, sell_stock
from app.src.domain.Portfolio import Portfolio
import app.src.db.portfolio_dao as portfoliodao
from app.src.db.account_dao import update_account_balance, get_balance

portfolio_bp = Blueprint('portfolio', __name__, url_prefix='/portfolio')


@portfolio_bp.route('/', methods=['GET'])
def default():
    res = make_response()
    res.response=  'OK'
    return res

@portfolio_bp.route('/get-all', methods=['GET'])
def get_all():
    try:
        portfolios = portfoliodao.get_all_portfolios()
        res = make_response()
        res.response = json.dumps([portfolio.__dict__ for portfolio in portfolios])
        res.headers['Content-Type'] = 'application/json'
        res.status = HTTPStatus.OK
        return res
    except Exception as e:
        error_res = make_response()
        error_res.status = HTTPStatus.INTERNAL_SERVER_ERROR # status 500
        error_res.headers['Content-Type'] = 'plain/text'
        error_res.response = f'Error while getting all portfolios: {str(e)}'
        return error_res

@portfolio_bp.route('/get-portfolio-by-id/<id>', methods=['GET'])
def get_portfolio_by_id(id: int):
    try:
        portfolio = portfoliodao.get_portfolio_by_id(id)
        res = make_response()
        res.headers['Content-Type'] = 'application/json'
        res.status = HTTPStatus.OK
        res.response = json.dumps(portfolio.__dict__)
        return res
    except Exception as e:
        error_res = make_response()
        error_res.status = HTTPStatus.INTERNAL_SERVER_ERROR # status 500
        error_res.headers['Content-Type'] = 'plain/text'
        error_res.response = f'Error while getting portfolio with id {id}: {str(e)}'
        return error_res

@portfolio_bp.route('/get-portfolios-by-ticker/<ticker>', methods=['GET'])
def get_portfolios_by_ticker(ticker): # expects query parameter name, if not available it will get all investors
    try:
        portfolio = portfoliodao.get_portfolio_by_ticker(ticker)
        res = make_response()
        res.response = json.dumps([portfolio.__dict__])
        res.headers['Content-Type'] = 'application/json'
        res.status = HTTPStatus.OK
        return res
    except Exception as e:
        error_res = make_response()
        error_res.status = HTTPStatus.INTERNAL_SERVER_ERROR # status 500
        error_res.headers['Content-Type'] = 'plain/text'
        error_res.response = f'Error while getting portfolio with ticker {ticker}: {str(e)}'
        return error_res

@portfolio_bp.route('/create', methods=['POST'])
def create_portfolio():
    try:
        content_type = request.headers.get('Content-Type')
        if content_type is None or content_type != 'application/json':
            return ('Expected application/json content-type', HTTPStatus.METHOD_NOT_ALLOWED)
        else:
            data = request.json
            portfolio = Portfolio.from_dict(data)
            portfoliodao.create_portfolio(portfolio)
            res = make_response()
            res.status = HTTPStatus.OK
            return res
    except Exception as e:
        error_res = make_response()
        error_res.status = HTTPStatus.INTERNAL_SERVER_ERROR # status 500
        error_res.headers['Content-Type'] = 'plain/text'
        error_res.response = f'Error while creating a new portfolio: {str(e)}'
        return error_res

@portfolio_bp.route('/update-quantity/<id>/<new_quantity>', methods=['PUT'])
def update_portfolio_quantity(id, new_quantity):
    try:
        portfoliodao.update_portfolio_quantity(id, new_quantity)
        res = make_response()
        res.status = HTTPStatus.OK
        return res
    except Exception as e:
        error_res = make_response()
        error_res.status = HTTPStatus.INTERNAL_SERVER_ERROR # status 500
        error_res.headers['Content-Type'] = 'plain/text'
        error_res.response = f'Error while updating portfolio (ID: {id}) quantity: {str(e)}'
        return error_res

@portfolio_bp.route('/update-brokerage/<id>/<new_broke>', methods=['PUT'])
def update_portfolio_brokerage(id, new_broke):
    try:
        portfoliodao.update_portfolio_broke(id, new_broke)
        res = make_response()
        res.status = HTTPStatus.OK
        return res
    except Exception as e:
        error_res = make_response()
        error_res.status = HTTPStatus.INTERNAL_SERVER_ERROR # status 500
        error_res.headers['Content-Type'] = 'plain/text'
        error_res.response = f'Error while updating investor (ID: {id}) brokerage: {str(e)}'
        return error_res

@portfolio_bp.route('/delete-portfolio/<id>', methods = ['DELETE'])
def delete_portfolio(id):
    try:
        portfoliodao.delete_portfolio_id(id)
        res = make_response()
        res.status = HTTPStatus.OK
        return res
    except Exception as e:
        error_res = make_response()
        error_res.status = HTTPStatus.INTERNAL_SERVER_ERROR # status 500
        error_res.headers['Content-Type'] = 'plain/text'
        error_res.response = f'Error while deleteing portfolio (ID: {id}) address: {str(e)}'
        return error_res

@portfolio_bp.route('/sell-stock/<account_id>/<ticker>/<quantity>/<profit>', methods=['PUT'])
def sell_stock(account_id, ticker, quantity, profit):
    current_qty = get_stock_quantity(account_id, ticker)
    # if quantity > current_qty return error message 
    if current_qty > quantity:
        err_res = make_response()
        err_res.status = HTTPStatus.INTERNAL_SERVER_ERROR
        err_res.headers['Content-Type'] = 'plain/text'
        err_res.response = 'Cannot sell more stocks than already owned'
        return err_res
    else:
        try:
            sell_stock(account_id, ticker, quantity)
            current_bal = get_balance(account_id)
            update_account_balance(account_id, current_bal + profit)
            res = make_response()
            res.status = HTTPStatus.OK
            return res
        except Exception as e:
            error_res = make_response()
            error_res.status = HTTPStatus.INTERNAL_SERVER_ERROR # status 500
            error_res.headers['Content-Type'] = 'plain/text'
            error_res.response = f'Error while trying to sell stock: {str(e)}'
            return error_res

@portfolio_bp.route('/buy-stock', methods=['POST'])
def buy_stock():
    pass




