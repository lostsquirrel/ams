# -*- coding:utf-8 -*-

from simpletor import torndb

class PropDAO:
    def __init__(self):
        pass

    @torndb.insert
    def save_prop(self, **item):
        sql = '''
        INSERT INTO response_model_prop (
        `name`,
        type,
        format,
        description,
        model_id
        ) VALUES (
        %(name)s,
        %(type)s,
        %(format)s,
        %(description)s,
        %(model_id)s
        )
        '''
        return sql

    @torndb.get
    def find_prop(self, prop_id):
        sql = '''
        SELECT 
        id,
        `name`,
        type,
        format,
        description,
        model_id
        FROM response_model_prop
        WHERE id = %s
        '''
        return sql

    @torndb.update
    def update_prop(self, **item):
        sql = '''
        UPDATE response_model_prop SET
        `name` = %(name)s,
        type = %(type)s,
        format = %(format)s,
        description = %(description)s
        WHERE id = %(id)s
        '''
        return sql

    @torndb.select
    def find_props_by_model(self, model_id):
        sql = '''
        SELECT id,
        `name`,
        type,
        format,
        description,
        prop_model_id,
        model_id
        FROM response_model_prop
        WHERE model_id = %s
        '''
        return sql

    @torndb.update
    def bind_model(self, **item):
        sql = '''
        UPDATE response_model_prop SET prop_model_id = %(model_id)s WHERE id = %(prop_id)s
        '''
        return sql
prop_dao = PropDAO()