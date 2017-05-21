# -*- coding:utf-8 -*-

from simpletor.torndb import transactional
from param.models import param_dao



def get_api_params(doc_id):
    return param_dao.find_api_parameters(doc_id)

def get_params_by_operation(op_id):
    return param_dao.find_operation_parameters(op_id)

@transactional
def save_bind_param(item):
    pid = param_dao.save_param(**item)
    relation = dict(parameter_id=pid, operation_id=item.get('op_id'))
    param_dao.save_operation_parameter_relation(**relation)