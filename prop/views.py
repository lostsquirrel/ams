# -*- coding:utf-8 -*-

"""
Created on 2017年5月23日

@author: lostsquirrel
"""

import tornado
from simpletor import application
from prop import services as prop_service

@application.RequestMapping("/doc/([0-9]+)/operation/([0-9]+)/resp/([0-9]+)/model/([0-9]+)/prop")
class PropAddHandler(application.RequestHandler):
    def get(self, doc_id, op_id, resp_id, model_id, *args, **kwargs):
        self.render('prop_add.html')

    def post(self, doc_id, op_id, resp_id, model_id, *args, **kwargs):
        self.params['model_id'] = model_id
        prop_service.save_prop(self.params)
        self.redirect('/doc/{0}/operation/{1}/resp/{2}/manager'.format(doc_id, op_id, resp_id))

@application.RequestMapping("/doc/([0-9]+)/operation/([0-9]+)/resp/([0-9]+)/model/([0-9]+)/prop/([0-9]+)")
class PropEditHandler(application.RequestHandler):
    def get(self, doc_id, op_id, resp_id, model_id, prop_id, *args, **kwargs):
        prop = prop_service.get_prop(prop_id)
        self.render('prop_edit.html', **prop)

    def post(self, doc_id, op_id, resp_id, model_id, prop_id, *args, **kwargs):
        self.params['id'] = prop_id
        prop_service.update_prop(self.params)
        self.redirect('/doc/{0}/operation/{1}/resp/{2}/manager'.format(doc_id, op_id, resp_id))
