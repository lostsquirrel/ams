# -*- coding:utf-8 -*-
'''
Created on 2015年5月14日

@author: zhuhua
'''

from simpletor import application
from simpletor.utils import get_request_param
from operation import services as op_service
from param import services as param_service
from resp import services as resp_service


@application.RequestMapping("/doc/([0-9]+)/operation")
class OperationHandler(application.RequestHandler):
    def get(self, doc_id):
        self.render('operation_add.html', doc_id=doc_id)

    def post(self, doc_id, *args, **kwargs):
        param = get_request_param(self)
        op_service.save_op(param)
        self.redirect('/doc/{0}'.format(doc_id))

@application.RequestMapping("/operation/([0-9]+)")
class OperationDetailHandler(application.RequestHandler):
    def get(self, op_id):
        op = op_service.get_op(op_id)
        params = param_service.get_params_by_operation(op_id)
        resp = resp_service.get_resp_by_operation(op_id)
        self.render('operation_detail.html', params=params, resp=resp, operation=op)

# @application.RequestMapping("/chart")
# class ChartHandler(application.RequestHandler):
#     def get(self):
#         self.render('k_line_chart.html')
#
# @application.RequestMapping("/")
# class IndexHandler(application.RequestHandler):
#     def get(self):
#         self.render('index.html')
