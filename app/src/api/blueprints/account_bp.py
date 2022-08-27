# create account blueprint
# minimum endpoints:
# Create/Update/Delete/GET

from http import HTTPStatus
import json
from flask import Blueprint, make_response, request
import app.src.db.account_dao as accountdao
from app.src.domain.Account import Account

account_bp = Blueprint('account', __name__, url_prefix='/account') 

@account_bp.route('/', methods=['GET'])
def default():
    res = make_response()
    res.response=  'OK'
    return res

@account_bp.route('/get-all', methods=['GET'])
def get_all():
    try:
        accounts = accountdao.get_all_accounts()
        res = make_response()
        res.response = json.dumps([account.__dict__ for account in accounts])
        res.headers['Content-Type'] = 'application/json'
        res.status = HTTPStatus.OK
        return res
    except Exception as e:
        error_res = make_response()
        error_res.status = HTTPStatus.INTERNAL_SERVER_ERROR # status 500
        error_res.headers['Content-Type'] = 'plain/text'
        error_res.response = f'Error while getting all accounts: {str(e)}'
        return error_res

@account_bp.route('/get-account-by-id/<id>', methods=['GET'])
def get_account_by_id(id: int):
    try:
        account = accountdao.get_account_by_id(id)
        res = make_response()
        res.headers['Content-Type'] = 'application/json'
        res.status = HTTPStatus.OK
        res.response = json.dumps(account.__dict__)
        return res
    except Exception as e:
        error_res = make_response()
        error_res.status = HTTPStatus.INTERNAL_SERVER_ERROR # status 500
        error_res.headers['Content-Type'] = 'plain/text'
        error_res.response = f'Error while getting account with id {id}: {str(e)}'
        return error_res

 
@account_bp.route('/create', methods=['POST'])
def create_account():
    try:
        content_type = request.headers.get('Content-Type')
        if content_type is None or content_type != 'application/json':
            return ('Expected application/json content-type', HTTPStatus.METHOD_NOT_ALLOWED)
        else:
            data = request.json
            account = Account.from_dict(data)
            accountdao.create_account(account)
            res = make_response()
            res.status = HTTPStatus.OK
            return res
    except Exception as e:
        error_res = make_response()
        error_res.status = HTTPStatus.INTERNAL_SERVER_ERROR # status 500
        error_res.headers['Content-Type'] = 'plain/text'
        error_res.response = f'Error while creating a new account: {str(e)}'
        return error_res

@account_bp.route('/update-account-balance/<id>/<new_acc_bal>', methods=['PUT'])
def update_account_balance(id: int, new_acc_bal: int):
    try:
        accountdao.update_account_balance(id, new_acc_bal)
        res = make_response()
        res.status = HTTPStatus.OK
        return res
    except Exception as e:
        error_res = make_response()
        error_res.status = HTTPStatus.INTERNAL_SERVER_ERROR # status 500
        error_res.headers['Content-Type'] = 'plain/text'
        error_res.response = f'Error while updating account (ID: {id}) balance: {str(e)}'
        return error_res


@account_bp.route('/delete-account/<id>', methods = ['DELETE'])
def delete_account(id):
    try:
        accountdao.delete_account_id(id)
        res = make_response()
        res.status = HTTPStatus.OK
        return res
    except Exception as e:
        error_res = make_response()
        error_res.status = HTTPStatus.INTERNAL_SERVER_ERROR # status 500
        error_res.headers['Content-Type'] = 'plain/text'
        error_res.response = f'Error while deleteing account (ID: {id}): {str(e)}'
        return error_res