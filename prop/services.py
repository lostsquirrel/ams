# -*- coding:utf-8 -*-

from simpletor.torndb import transactional
from prop.models import prop_dao


@transactional
def save_prop(item):
    prop_dao.save_prop(**item)


def get_prop(prop_id):
    return prop_dao.find_prop(prop_id)

def get_props_by_model(model_id):
    return prop_dao.find_props_by_model(model_id)

@transactional
def update_prop(item):
    prop_dao.update_prop(**item)

@transactional
def bind_model(item):
    prop_dao.bind_model(**item)