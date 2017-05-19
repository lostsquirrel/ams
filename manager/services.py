# -*- coding:utf-8 -*-
from simpletor.torndb import transactional
from manager.models import docDAO

def get_doc(doc_id):
    return docDAO.find_one(doc_id)
#
# def get_default_item():
#     return itemDAO.get_default_item()

@transactional
def save_doc(item):
    docDAO.save(**item)

# @transactional
# def set_default(item_id):
#     itemDAO.reset_default()
#     itemDAO.set_default(item_id)

# @transactional
# def remove_item(item_id):
#     itemDAO.delete_item(item_id)

def get_docs():
    nodes = []
    try:
        nodes = docDAO.all()
    except:
        pass
    return nodes

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