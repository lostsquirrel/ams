# -*- coding:utf-8 -*-
'''
Created on 2015年5月14日

@author: zhuhua
'''
import tornado
from simpletor import application
from simpletor.utils import get_request_param
import manager.services as doc_service
from operation import services as op_service

@application.RequestMapping("/doc/manager")
class DocMangerHandler(application.RequestHandler):
    def get(self):
        self.render('doc_manager.html', items=doc_service.get_docs())

@application.RequestMapping("/doc/add")
class DocAddHandler(application.RequestHandler):
    def get(self):
        self.render('doc_add.html')

    def post(self, *args, **kwargs):
        param = get_request_param(self)
        doc_service.save_doc(param)
        self.redirect('/doc/manager')

@application.RequestMapping("/doc/([0-9]+)")
class DocEditHandler(application.RequestHandler):
    def get(self, doc_id):
        doc = doc_service.get_doc(doc_id)
        self.render('doc_add.html', doc=doc)

    def post(self, doc_id, *args, **kwargs):
        param = get_request_param(self)
        doc_service.save_doc(param)
        self.redirect('/doc/manager')

@application.RequestMapping("/doc/([0-9]+)/path/manager")
class DocDetailHandler(application.RequestHandler):
    def get(self, doc_id):
        doc = doc_service.get_doc(doc_id)
        ops = op_service.get_ops_by_doc(doc_id)
        self.render('doc_detail.html', item=doc, ops=ops)


@application.RequestMapping("/")
class IndexHandler(application.RequestHandler):
    def get(self):
        self.redirect('/doc/manager')

@application.RequestMapping("/about_us")
class AboutUsHandler(application.RequestHandler):
    def get(self):
        self.render('about_us.html')