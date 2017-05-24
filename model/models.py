# -*- coding:utf-8 -*-

from simpletor import torndb

class ModelDAO:
    def __init__(self):
        pass

    @torndb.insert
    def save_model(self, **item):
        sql = '''
        INSERT INTO response_model (name, type) VALUES (%(name)s, %(type)s)
        '''
        return sql


    @torndb.update
    def bind_model(self, tid, mid):
        sql='''
        UPDATE response_model SET model_id = %s WHERE id = %s
        '''
        return sql

    @torndb.update
    def update_model(self, **item):
        sql = '''
        UPDATE response_model SET
        type = %(type)s,
        `name` = %(name)s
        WHERE id = %(id)s
        '''
        return sql

    @torndb.select
    def find_models(self):
        sql = '''
        SELECT id, `name`, type FROM response_model
        '''
        return sql

    @torndb.get
    def find_model(self, model_id):
        sql = '''
        SELECT id, `name`, type FROM response_model WHERE id = %s
        '''
        return sql

model_dao = ModelDAO()