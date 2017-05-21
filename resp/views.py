# -*- coding:utf-8 -*-

"""
Created on 2017年5月19日

@author: lostsquirrel
"""
import tornado
from simpletor import application
from simpletor.utils import get_request_param
import param.services as param_service
from operation import services as ep_service

@application.RequestMapping("/doc/([0-9]+)/param/manager")
class ParamMangerHandler(application.RequestHandler):
    def get(self, doc_id):
        self.render('param_manager.html', items=param_service.get_params(doc_id))


@application.RequestMapping("/doc/([0-9]+)/param")
class ParamAddHandler(application.RequestHandler):
    def get(self, doc_id):
        self.render('param_add.html', doc_id=doc_id)

    def post(self, doc_id):
        param = get_request_param(self)
        param_service.save_param(param)
        self.redirect('/doc/%s/param/manager'.format(doc_id))

@application.RequestMapping("/doc/([0-9]+)/param/([0-9]+)")
class ParamAddBindHandler(application.RequestHandler):
    def get(self, doc_id, op_id):
        self.render('param_add_bind.html', doc_id=doc_id, op_id=op_id)

    def post(self, doc_id, op_id):
        param = get_request_param(self)
        param_service.save_bind_param(param)
        self.redirect('/doc/%s/param/manager'.format(doc_id))