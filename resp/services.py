# -*- coding:utf-8 -*-

from simpletor.torndb import transactional
from simpletor.utils import dict_slice
from resp.models import resp_dao


def get_resp(resp_id):
    return resp_dao.find_resp(resp_id)


def get_resp_by_operation(op_id):
    return resp_dao.find_resp_by_operation(op_id)


def get_resp_model(model_id):
    return resp_dao.find_resp_model(model_id)


def get_model_props(model_id):
    return resp_dao.find_props_by_model(model_id)


def get_resp_by_operation_with_model_prop(op_id):
    rps = resp_dao.find_resp_by_operation(op_id)
    resp = list()
    temp_resp = dict()
    for rp in rps:
        # 假设一个响应只有一个模型
        resp_id = rp.resp_id
        resp = temp_resp.get(resp_id)
        if resp is None:
            resp = dict_slice(resp, 'resp_id', 'code', 'type', 'resp_description')
            resp['properties'] = list()
            temp_resp[resp_id] = resp

        resp['properties'].add(dict_slice(resp, 'id', 'name', 'type', 'description', 'format'))

    return resp


@transactional
def save_resp(item):
    resp_dao.save_resp(**item)


@transactional
def update_resp(item):
    resp_dao.update_resp(**item)
