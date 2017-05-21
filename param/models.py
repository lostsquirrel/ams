# -*- coding:utf-8 -*-

from simpletor import torndb

class Param(torndb.Row):
    def __init__(self):
        self.id = None
        self.source = None
        self.name = None
        self.type = None
        self.required = None
        self.description = None
        self.default = None
        self.minimum = None
        self.maximum = None

class ParamDAO(object):
    def __init__(self):
        pass

    @torndb.insert
    def save_param(self, **item):
        sql = '''
        INSERT INTO parameters (
            source,
            name,
            type,
            required,
            description,
            `default`,
            minimum,
            maximum
        ) VALUES (
            %(source)s,
            %(name)s,
            %(type)s,
            %(required)s,
            %(description)s,
            %(default)s,
            %(minimum)s,
            %(maximum)s
        )
        '''
        return sql

    @torndb.insert
    def save_operation_parameter_relation(self, **item):
        sql = '''
        INSERT INTO operation_parameter  (operation_id, parameter_id) VALUES (%(operation_id)s, %(parameter_id)s)
        '''
        return sql

    @torndb.select
    def find_operation_parameters(self, op_id):
        sql = '''
            SELECT 
                p.source,
                p.name,
                p.type,
                p.required,
                p.description,
                p.default,
                p.minimum,
                p.maximum
            FROM parameters p 
            JOIN operation_parameter op  ON p.id = op.parameter_id
            JOIN path_operation o ON op.operation_id = o.id AND o.id = %s        
        '''
        return sql

    @torndb.select
    def find_api_parameters(self, doc_id):
        sql = '''
        SELECT 
            op.source,
            op.name,
            op.type,
            op.required,
            op.description,
            op.default,
            op.minimum,
            op.maximum
            FROM operation_parameter op 
            JOIN path_operation o on op.operation_id = o.id
            JOIN paths p on p.path_id = o.path_id AND p.api_id = %s            
        '''
        return sql
param_dao = ParamDAO()