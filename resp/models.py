# -*- coding:utf-8 -*-

from simpletor import torndb


class RespDAO(object):
    def __init__(self):
        pass

    @torndb.select
    def find_resp_by_operation_with_model_prop(self, op_id):
        sql = '''
            SELECT 
                p.id,
                p.name,
                p.type,
                p.description,
                p.format,
                p.model_id,
                r.id as resp_id,
                r.code,
                r.type,
                r.description as resp_description
            FROM responses r
            JOIN response_model m ON r.response_model_id = m.id AND r.operation_id = %s
            JOIN response_model_prop p ON m.id = p.model_id
        '''
        return sql

    @torndb.select
    def find_resp_by_operation(self, op_id):
        sql = '''
        SELECT 
            r.id,
            r.code,
            r.type,
            r.description,
            r.response_model_id,
            r.wrapper_id
            FROM responses r
            WHERE r.operation_id = %s
        '''

        return sql

    @torndb.get
    def find_resp_model(self, model_id):
        sql = '''
        SELECT id, name, type FROM response_model WHERE id = %s
        '''
        return sql

    @torndb.get
    def find_resp(self, resp_id):
        sql = '''
        SELECT 
            r.id,
            r.code,
            r.type,
            r.description,
            r.response_model_id,
            r.wrapper_id
            FROM responses r
            WHERE r.id = %s
        '''

        return sql



    @torndb.insert
    def save_resp(self, **item):
        sql = '''
        INSERT INTO responses (
        `code`,
        description,
        type,
        operation_id
        ) VALUES 
        (
        %(code)s,
        %(description)s,
        %(type)s,
        %(operation_id)s
        )
        '''
        return sql

    @torndb.update
    def update_resp(self, **item):
        sql = '''
        UPDATE responses SET
        code = %(code)s,
        description = %(description)s,
        type = %(type)s
        WHERE id = %(id)s
        '''
        return sql

    @torndb.insert
    def save_resp_prop_relation(self, response_model_id, resp_id):
        sql = '''
        UPDATE responses SET response_model_id = %s WHERE id %s
        '''
        return sql

    @torndb.insert
    def save_resp_prop(self, **item):
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

    @torndb.update
    def update_resp_prop(self, **item):
        sql = '''
        UPDATE response_model_prop SET
        `name` = %(name)s,
        type = %(type)s,
        format = %(format)s,
        description = %(description)s,
        WHERE id = %(id)s
        '''
        return sql

    @torndb.update
    def bind_model(self, **item):
        sql = '''
        UPDATE responses SET response_model_id =  %(model_id)s WHERE id = %(resp_id)s
        '''
        return sql

    @torndb.update
    def bind_wrapper(self, **item):
        sql = '''
        UPDATE responses SET wrapper_id = %(model_id)s WHERE id = %(resp_id)s
        '''
        return sql

resp_dao = RespDAO()