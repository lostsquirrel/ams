# -*- coding:utf-8 -*-

from simpletor.torndb import transactional
from model.models import model_dao
from resp.models import resp_dao

@transactional
def save_model(item):
    is_wrapper = item.has_key('is_wrapper')
    inner_id = None

    if item['type'] == 'array' or is_wrapper:
        n = dict(type='object',name=item.pop('name'))
        inner_id = model_dao.save_model(**n)
        model_dao.bind_model(inner_id, inner_id)
        item['name'] = None

    outer_id = model_dao.save_model(**item)

    if item['type'] != 'array' and not is_wrapper:
        inner_id = outer_id

    item['model_id'] = outer_id
    model_dao.bind_model(inner_id, outer_id)
    if is_wrapper:
        resp_dao.bind_wrapper(**item)
    else:
        resp_dao.bind_model(**item)

