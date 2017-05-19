# -*- coding:utf-8 -*-

from simpletor import torndb

class param(torndb.Row):
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

def param_dao(object):
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
            default,
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
    def save_operation_parameter(self, **item):
        sql = '''
        INSERT INTO operation_parameter  (operation_id, parameter_id) VALUES (%(operation_id)s, %(parameter_id)s)
        '''
        return sql

    @torndb.select
    def find_operation_parameters(self, op_id):
        sql = '''
            SELECT 
                source,
                name,
                type,
                required,
                description,
                default,
                minimum,
                maximum
            FROM operation_parameter op 
            JOIN path_operation o on op.operation_id = o.id AND o.id = %s        
        '''
        return sql