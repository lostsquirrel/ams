# -*- coding:utf-8 -*-

from simpletor import torndb


class Operation(torndb.Row):
    '''
    Operation
    '''
    def __init__(self):
        self.id = None
        self.operation = None
        self.summary = None
        self.description = None
        self.path_url = None
        self.path_id = None
        self.doc_id= None
        self.tags = None


# class Item(torndb.Row):
#     '''
#     Node
#     '''
#     def __init__(self):
#         self.id = None
#         self.name = None
#         self.status = None  # NULL 初始， 1, 默认 9，删除

class OperationDAO:
    '''
    ItemDAO DAO
    '''

    @torndb.insert
    def save_url(self, **item):
        sql = '''
        INSERT INTO paths (path_url, doc_id)
        VALUES (%(path_url)s, %(doc_id)s)
        '''
        return sql

    @torndb.insert
    def bind_tag(self, **item):
        sql = '''
        INSERT INTO operation_tag (tag_id, operation_id)
        VALUES (%(tag_id)s, %(operation_id)s)
        '''
        return sql

    @torndb.insert
    def save_tag(self, **item):
        sql = '''
        INSERT INTO tags (tag, description, doc_id) VALUES (%(tag)s, %(description)s, %(doc_id)s)
        '''
        return sql

    @torndb.delete
    def unbind_operation_tag(self, op_id):
        sql = '''
        DELETE FROM operation_tag WHERE operation_id = %s
        '''
        return sql
    @torndb.get
    def find_tag_by_operation(self, doc_id, operation_id):
        sql = '''
        SELECT id, tag, description, doc_id 
        FROM tags t JOIN operation_tag ot ON t.id = ot.tag_id 
        AND t.doc_id = %s 
        AND ot.operation_id = %s
        '''
        return sql

    @torndb.get
    def find_tag_by_doc(self, doc_id, tag):
        sql = '''
        SELECT id, tag, description, doc_id FROM tags WHERE doc_id = %s AND tag = %s
        '''
        return sql

    @torndb.insert
    def save_operation(self, **item):
        sql = '''
        INSERT INTO path_operation (
            operation,
            path_id,
            summary,
            description
        ) VALUE (
            %(operation)s,
            %(path_id)s,
            %(summary)s,
            %(description)s
        )
        '''
        return sql

    @torndb.select
    def find_ops_by_doc(self, doc_id):
        sql = '''
            SELECT 
            o.operation, 
            o.summary, 
            o.description, 
            o.id, 
            o.path_id, 
            p.path_url, 
            p.doc_id,
            (SELECT group_concat(tag) FROM tags t JOIN operation_tag ot ON t.id = ot.tag_id WHERE ot.operation_id = o.id) AS tags
            FROM path_operation o 
            JOIN paths p ON o.path_id = p.id AND p.doc_id = %s
            ORDER BY p.path_url
            '''
        return sql

    @torndb.select
    def find_tags_by_operation(self, op_id):
        sql = '''
        SELECT tag FROM tags t JOIN operation_tag ot ON t.id = ot.tag_id WHERE ot.operation_id = %s
        '''
        return sql

    @torndb.select
    def find_ops_by_path(self, path_id):
        sql = '''
        SELECT 
            o.operation, 
            o.summary, 
            o.description, 
            o.id, 
            (SELECT group_concat(tag) FROM tags t JOIN operation_tag ot ON t.id = ot.tag_id WHERE ot.operation_id = o.id) as tags 
            FROM path_operation o 
            JOIN paths p ON o.path_id = p.id AND p.id = %s
        '''
        return sql

    @torndb.get
    def find_op(self, op_id):
        sql = '''
        SELECT po.id, operation, path_id, p.path_url, summary, description, p.doc_id,
        (SELECT group_concat(tag) FROM tags t JOIN operation_tag ot ON t.id = ot.tag_id WHERE ot.operation_id = po.id) AS tags
        FROM path_operation po
        JOIN paths p ON po.path_id = p.id AND po.id = %s
        '''
        return sql

    @torndb.get
    def find_url(self, url):
        sql = '''
        SELECT id, path_url, doc_id from paths WHERE path_url = %s
        '''
        return sql

    @torndb.update
    def update_operation(self, **item):
        sql = '''
        UPDATE path_operation SET
        operation = %(operation)s,
        path_id = %(path_id)s,
        summary = %(summary)s,
        description = %(description)s
        WHERE id = %(id)s
        '''
        return sql

op_dao = OperationDAO()
