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
        self.api_id= None
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
        INSERT INTO paths (path_url, api_id)
        VALUES (%(path_url)s, %(api_id)s)
        '''
        return sql

    @torndb.insert
    def save_tag(self, **item):
        sql = '''
        INSERT INTO operation_tag (tag, operation_id)
        VALUES (%(tag)s, %(operation_id)s)
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
    #
    # @torndb.get
    # def find(self, item_id):
    #     sql = '''
    #     SELECT id, name, status FROM item a WHERE a.id = %s;
    #     '''
    #     return sql
    #
    # @torndb.get
    # def get_default_item(self,):
    #     sql = '''
    #     SELECT id, name, status FROM item a WHERE a.status = 1;
    #     '''
    #     return sql
    #
    # @torndb.update
    # def update_name(self, **item):
    #     sql = '''
    #         UPDATE item a SET
    #         name = %(name)s
    #         WHERE a.id = %(id)s
    #         '''
    #     return sql
    #
    # @torndb.delete
    # def delete_item(self, item_id):
    #     sql = '''
    #     DELETE FROM item WHERE id = %s
    #     '''
    #     return sql
    #
    # @torndb.update
    # def set_default(self, item_id):
    #     sql = '''
    #         UPDATE item a SET
    #         status = 1
    #         WHERE a.id = %s
    #         '''
    #     return sql
    #
    # @torndb.update
    # def reset_default(self):
    #     sql = '''
    #     UPDATE item a SET
    #         status = NULL
    #         WHERE a.status = 1
    #     '''
    #     return sql
    #
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
            p.api_id, 
            (SELECT tag FROM operation_tag WHERE operation_id = o.id) as tags 
            FROM path_operation o 
            JOIN paths p ON o.path_id = p.id AND p.api_id = %s
            ORDER BY p.path_url
            '''
        return sql

    @torndb.get
    def find_op(self, op_id):
        sql = '''
        SELECT po.id, operation, path_id, summary, description, p.api_id AS doc_id
        FROM path_operation po
        JOIN paths p ON po.path_id = p.id AND po.id = %s
        '''
        return sql

op_dao = OperationDAO()

# class NodeDAO:
#
#
#     @torndb.insert
#     def save(self, **node):
#         sql = '''
#         INSERT INTO node (
#             open,
#             close,
#             lowest,
#             highest,
#             item_id,
#             date
#             )
#         VALUES
#         (
#         %(open)s,
#         %(close)s,
#         %(lowest)s,
#         %(highest)s,
#         %(item_id)s,
#         %(date)s
#         );
#         '''
#         return sql
#
#     @torndb.select
#     def all(self):
#         sql = '''
#              SELECT id,
#                 open,
#                 close,
#                 lowest,
#                 highest,
#                 item_id,
#                 date
#                 FROM node WHERE item_id =  (SELECT id FROM item WHERE status = 1) ORDER BY date ASC;
#              '''
#         return sql
#
#     @torndb.delete
#     def delete(self, node_id):
#         sql = '''
#         DELETE FROM node WHERE id = %s;
#         '''
#         return sql
#
#     @torndb.select
#     def find_node(self, **node):
#         sql = '''
#         SELECT
#                 id,
#                 open,
#                 close,
#                 lowest,
#                 highest,
#                 item_id,
#                 date
#         FROM node a WHERE a.item_id = %(item_id)s AND a.date = %(date)s;
#         '''
#         return sql
#
#     @torndb.update
#     def update_node(self, **node):
#         sql = '''
#         UPDATE node
#         SET open = %(open)s,
#         close = %(close)s,
#         lowest = %(lowest)s,
#         highest = %(highest)s
#         WHERE item_id = %(item_id)s AND date = %(date)s
#         '''
#         return  sql
#
# nodeDAO = NodeDAO()