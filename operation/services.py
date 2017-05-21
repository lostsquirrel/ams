# -*- coding:utf-8 -*-

from simpletor.torndb import transactional
from  simpletor.utils import dict_slice
from operation.models import op_dao


def get_op(op_id):
    return op_dao.find_op(op_id)


def get_ops_by_doc(doc_id):
    return op_dao.find_ops_by_doc(doc_id)


@transactional
def save_op(item):
    u =  dict_slice(item, 'path_url', 'api_id')
    ep_id = op_dao.save_url(**u)

    o = dict_slice(item, 'operation', 'summary', 'description')
    o['path_id'] = ep_id
    op_id = op_dao.save_operation(**o)

    item['operation_id'] = op_id
    tags = item.get('tags')
    if tags is not None and len(tags) > 0:
        for tag in tags.split(','):
            t = dict(operation_id=op_id, tag=tag)
            op_dao.save_tag(**t)

# @transactional
# def set_default(item_id):
#     itemDAO.reset_default()
#     itemDAO.set_default(item_id)
#
# @transactional
# def remove_item(item_id):
#     itemDAO.delete_item(item_id)
#
# def get_nodes():
#     nodes = []
#     try:
#         nodes = nodeDAO.all()
#     except:
#         pass
#     return nodes
#
# @transactional
# def save_node(node):
#     n = None
#     try:
#         n = nodeDAO.find_node(**node)
#     except:
#         pass
#     if n is None or len(n) == 0:
#         nodeDAO.save(**node)
#     else:
#         nodeDAO.update_node(**node)
#
# @transactional
# def remove_node(node_id):
#     nodeDAO.delete(node_id)