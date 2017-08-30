# -*- coding:utf-8 -*-

from simpletor.torndb import transactional
from manager.models import docDAO

def get_doc(doc_id):
    return docDAO.find_one(doc_id)


@transactional
def save_doc(item):
    if item.has_key('id') and item.get('id') is not None and len(item.get('id')) > 0:
        docDAO.update(**item)
    else:
        docDAO.save(**item)


def get_paths_by_doc(doc_id):
    return docDAO.find_paths_by_doc(doc_id)


def get_docs():
    nodes = []
    try:
        nodes = docDAO.all()
    except:
        pass
    return nodes
