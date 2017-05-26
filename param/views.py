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
        param['doc_id'] = doc_id
        param['op_id'] = op_id
        if len(param.get('maximum')) == 0:
            param['maximum'] = None
        if len(param.get('minimum')) == 0:
            param['minimum'] = None

        param_service.save_bind_param(param)
        manager__format = '/operation/{0}/manager'.format(op_id)
        self.redirect(manager__format)


@application.RequestMapping("/operation/([0-9]+)/param/([0-9]+)")
class ParamEditHandler(application.RequestHandler):
    def get(self, op_id, param_id, *args, **kwargs):
        param = param_service.get_param(param_id)
        self.render('param_edit.html', op_id=op_id, param=param)

    def post(self, op_id, param_id, *args, **kwargs):
        param = get_request_param(self)
        param['id'] = param_id
        param['operation_id'] = op_id
        param_type = param['type']
        isNum = 'integer' == param_type or 'number' == param_type
        maximum = param.get('maximum')
        if isNum or len(maximum) == 0 or 'None' == maximum:
            param['maximum'] = None
        minimum = param.get('minimum')
        if isNum or len(minimum) == 0 or 'None' == minimum:
            param['minimum'] = None

        param_service.update_param(param)
        manager__format = '/operation/{0}/manager'.format(op_id)
        self.redirect(manager__format)