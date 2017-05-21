# -*- coding:utf-8 -*-

from simpletor import torndb


class RespDAO(object):
    def __init__(self):
        pass

    @torndb.select
    def find_resp_by_operation(self, op_id):
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
            JOIN response_model m ON r.id = m.response_id AND r.operation_id = %s
            JOIN response_model_prop p ON m.id = p.model_id
        '''
        return sql


resp_dao = RespDAO()