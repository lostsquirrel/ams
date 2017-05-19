# -*- coding:utf-8 -*-

from simpletor import torndb


class Doc(torndb.Row):
    '''
    一个文档
    '''
    def __init__(self):
        self.id = None
        self.schemes = None
        self.host = None
        self.base_path = None
        self.title = None
        self.description = None
        self.version = None
        self.produces = None

class DocDAO:


    @torndb.insert
    def save(self, **item):
        sql = '''
        INSERT INTO apis (
            schemes,
            host,
            base_path,
            title,
            description,
            version,
            produces
            )
        VALUES
        (
            %(schemes)s,
            %(host)s,
            %(base_path)s,
            %(title)s,
            %(description)s,
            %(version)s,
            %(produces)s
        ) 
        '''
        return sql

    @torndb.select
    def all(self):
        sql = '''
             SELECT id,
                schemes,
                host,
                base_path,
                title,
                description,
                version,
                produces
                FROM apis 
             '''
        return sql

    @torndb.delete
    def delete(self, aid):
        sql = '''
        DELETE FROM apis WHERE id = %s;
        '''
        return sql

    @torndb.get
    def find_one(self, aid):
        sql = '''
        SELECT 
                id,
                schemes,
                host,
                base_path,
                title,
                description,
                version,
                produces
        FROM apis WHERE id = %s
        '''
        return sql

    @torndb.update
    def update(self, **item):
        sql = '''
        UPDATE apis 
        SET schemes = %(schemes)s,
            host = %(host)s,
            base_path = %(base_path)s,
            title = %(title)s,
            description = %(description)s,
            version = %(version)s,
            produces = %(produces)s
        WHERE id = %(id)s
        '''
        return  sql

docDAO = DocDAO()