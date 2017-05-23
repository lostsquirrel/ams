# -*- coding:utf-8 -*-

"""
Created on 2017年5月19日

@author: lostsquirrel
"""
import tornado
from simpletor import application
from simpletor.utils import get_request_param
import param.services as param_service
from operation import services as op_service
from resp import services as resp_service

# 添加响应
@application.RequestMapping("/doc/([0-9]+)/operation/([0-9]+)/resp")
class RespAddHandler(application.RequestHandler):
    def get(self, doc_id, op_id):
        op = op_service.get_op(op_id)
        self.render('resp_add.html', doc_id=doc_id, operation=op)

    def post(self, doc_id, op_id, *args, **kwargs):
        param = get_request_param(self)
        param['operation_id'] = op_id
        resp_service.save_resp(param)
        self.redirect("/operation/{0}".format(op_id))

# 修改响应
@application.RequestMapping("/doc/([0-9]+)/operation/([0-9]+)/resp/([0-9]+)")
class RespEditHandler(application.RequestHandler):
    def get(self, doc_id, op_id, resp_id, *args, **kwargs):
        resp = resp_service.get_resp(resp_id)
        self.render('resp_edit.html', resp=resp, doc_id=doc_id, op_id=op_id)

    def post(self, doc_id, op_id, resp_id, *args, **kwargs):
        param = get_request_param(self)
        param['id'] = resp_id
        resp_service.update_resp(param)
        self.redirect('/operation/{0}'.format(op_id))

# 响应详情
@application.RequestMapping("/doc/([0-9]+)/operation/([0-9]+)/resp/([0-9]+)/manager")
class RespDetailHandler(application.RequestHandler):
    def get(self, doc_id, op_id, resp_id, *args, **kwargs):
        resp = resp_service.get_resp(resp_id)
        model_id = resp.response_model_id
        model = None
        model_props = []
        if model_id is not None:
            model = resp_service.get_resp_model(model_id)
            model_props = resp_service.get_model_props(model.model_id)

        wrapper = None
        wrapper_props = []
        wrapper_id = resp.wrapper_id
        if wrapper_id is not None:
            wrapper = resp_service.get_resp_model(wrapper_id)
            wrapper_props = resp_service.get_model_props(wrapper.model_id)

        self.render('resp_manager.html', doc_id=doc_id,
                    op_id=op_id,
                    resp=resp, model=model, wrapper=wrapper, model_props=model_props, wrapper_props=wrapper_props)


# 添加响应模型属性
@application.RequestMapping("/doc/([0-9]+)/operation/([0-9]+)/resp/([0-9]+)/prop")
class RespPropHandler(application.RequestHandler):
    def get(self, doc_id):
        self.render('param_add.html', doc_id=doc_id)

    def post(self, doc_id):
        param = get_request_param(self)
        param_service.save_param(param)
        self.redirect('/doc/%s/param/manager'.format(doc_id))

# @application.RequestMapping("/doc/([0-9]+)/param/([0-9]+)")
# class ParamAddBindHandler(application.RequestHandler):
#     def get(self, doc_id, op_id):
#         self.render('param_add_bind.html', doc_id=doc_id, op_id=op_id)
#
#     def post(self, doc_id, op_id):
#         param = get_request_param(self)
#         param_service.save_bind_param(param)
#         self.redirect('/doc/%s/param/manager'.format(doc_id))