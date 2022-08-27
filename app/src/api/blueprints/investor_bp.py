# this file will contain all the endpoints that relate to the investor resource
# expected endpoints: create/update/remove/get
from http import HTTPStatus
import json
from unicodedata import name
from flask import Blueprint, make_response, request
import app.src.db.investor_dao as investordao
from app.src.domain.Investor import Investor

investor_bp = Blueprint('investor', __name__, url_prefix='/investor') 
# url_prefix means that any endpoint declared as part of this blueprint will need to have /investor appended to it

@investor_bp.route('/', methods=['GET'])
def default():
    res = make_response()
    res.response=  'OK'
    return res

@investor_bp.route('/get-all', methods=['GET'])
def get_all():
    try:
        investors = investordao.get_all_investors()
        res = make_response()
        res.response = json.dumps([investor.__dict__ for investor in investors])
        res.headers['Content-Type'] = 'application/json'
        res.status = HTTPStatus.OK
        return res
    except Exception as e:
        error_res = make_response()
        error_res.status = HTTPStatus.INTERNAL_SERVER_ERROR # status 500
        error_res.headers['Content-Type'] = 'plain/text'
        error_res.response = f'Error while getting all investors: {str(e)}'
        return error_res

@investor_bp.route('/get-investor-by-id/<id>', methods=['GET'])
def get_investor_by_id(id: int):
    try:
        investor = investordao.get_investor_by_id(id)
        res = make_response()
        res.headers['Content-Type'] = 'application/json'
        res.status = HTTPStatus.OK
        res.response = json.dumps(investor.__dict__)
        return res
    except Exception as e:
        error_res = make_response()
        error_res.status = HTTPStatus.INTERNAL_SERVER_ERROR # status 500
        error_res.headers['Content-Type'] = 'plain/text'
        error_res.response = f'Error while getting investor with id {id}: {str(e)}'
        return error_res

@investor_bp.route('/get-investors-by-name/<name>', methods=['GET'])
def get_investors_by_name(name): # expects query parameter name, if not available it will get all investors
    try:
        investor = investordao.get_investor_with_name(name)
        res = make_response()
        res.response = json.dumps([investor.__dict__])
        res.headers['Content-Type'] = 'application/json'
        res.status = HTTPStatus.OK
        return res
    except Exception as e:
        error_res = make_response()
        error_res.status = HTTPStatus.INTERNAL_SERVER_ERROR # status 500
        error_res.headers['Content-Type'] = 'plain/text'
        error_res.response = f'Error while getting investor with name {name}: {str(e)}'
        return error_res
        
@investor_bp.route('/create', methods=['POST'])
def create_investor():
    try:
        content_type = request.headers.get('Content-Type')
        if content_type is None or content_type != 'application/json':
            return ('Expected application/json content-type', HTTPStatus.METHOD_NOT_ALLOWED)
        else:
            data = request.json
            investor = Investor.from_dict(data)
            investordao.create_investor(investor)
            res = make_response()
            res.status = HTTPStatus.OK
            return res
    except Exception as e:
        error_res = make_response()
        error_res.status = HTTPStatus.INTERNAL_SERVER_ERROR # status 500
        error_res.headers['Content-Type'] = 'plain/text'
        error_res.response = f'Error while creating a new investor: {str(e)}'
        return error_res

@investor_bp.route('/update-address/<id>/<new_addr>', methods=['PUT'])
def update_investor_status(id, new_addr):
    try:
        investordao.update_investor_address(id, new_addr)
        res = make_response()
        res.status = HTTPStatus.OK
        return res
    except Exception as e:
        error_res = make_response()
        error_res.status = HTTPStatus.INTERNAL_SERVER_ERROR # status 500
        error_res.headers['Content-Type'] = 'plain/text'
        error_res.response = f'Error while updating investor (ID: {id}) address: {str(e)}'
        return error_res

@investor_bp.route('/update-name/<id>/<new_name>', methods=['PUT'])
def update_investors_name(id, new_name):
    try:
        investordao.update_investor_name(id, new_name)
        res = make_response()
        res.status = HTTPStatus.OK
        return res
    except Exception as e:
        error_res = make_response()
        error_res.status = HTTPStatus.INTERNAL_SERVER_ERROR # status 500
        error_res.headers['Content-Type'] = 'plain/text'
        error_res.response = f'Error while updating investor (ID: {id}) name: {str(e)}'
        return error_res

@investor_bp.route('/delete-investor/<id>', methods = ['DELETE'])
def delete_investor(id):
    try:
        investordao.delete_investor_by_id(id)
        res = make_response()
        res.status = HTTPStatus.OK
        return res
    except Exception as e:
        error_res = make_response()
        error_res.status = HTTPStatus.INTERNAL_SERVER_ERROR # status 500
        error_res.headers['Content-Type'] = 'plain/text'
        error_res.response = f'Error while deleteing investor (ID: {id}) address: {str(e)}'
        return error_res