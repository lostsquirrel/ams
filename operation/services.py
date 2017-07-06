# -*- coding:utf-8 -*-

from simpletor.torndb import transactional
from  simpletor.utils import dict_slice
from operation.models import op_dao


def get_op(op_id):
    return op_dao.find_op(op_id)


def get_ops_by_doc(doc_id):
    ops = op_dao.find_ops_by_doc(doc_id)
    split_tags(ops)
    return ops

def get_ops_by_path(path_id):
    ops = op_dao.find_ops_by_path(path_id)
    split_tags(ops)
    return ops

def split_tags(ops):
    for op in ops:
        tags = op.tags
        tag_list = list()
        if tags is not None and len(tags) > 0:
            tag_list = tags.split(',')

        op.tags = tag_list

@transactional
def save_op(item):
    doc_id = item.get('doc_id')
    u =  dict_slice(item, 'path_url', 'doc_id')
    exists_op = op_dao.find_url(u['path_url'])
    ep_id = None
    if exists_op is None:
        ep_id = op_dao.save_url(**u)
    else:
        ep_id = exists_op.id

    o = dict_slice(item, 'id', 'operation', 'summary', 'description', 'secure')
    o['path_id'] = ep_id
    op_id = None
    if o.has_key('id') and o.get('id') is not None:
        op_dao.update_operation(**o)
        op_id = o.get('id')
    else:
        op_id = op_dao.save_operation(**o)

    item['operation_id'] = op_id
    tags = item.get('tags')
    op_dao.unbind_operation_tag(op_id)
    if tags is not None and len(tags) > 0:
        for tag_name in tags.split(','):
            tag = op_dao.find_tag_by_doc(doc_id, tag_name)
            tag_id = None
            if tag is None:
                new_tag = dict(tag=tag_name,doc_id=doc_id, description=None)
                tag_id = op_dao.save_tag(**new_tag)
            else:
                tag_id = tag.id

            op_dao.bind_tag(**dict(tag_id=tag_id, operation_id=op_id))


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