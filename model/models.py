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

model_dao = ModelDAO()