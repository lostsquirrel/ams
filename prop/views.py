# -*- coding:utf-8 -*-

"""
Created on 2017年5月23日

@author: lostsquirrel
"""

import tornado
from simpletor import application
from prop import services as prop_service
from model import services as model_service

@application.RequestMapping("/doc/([0-9]+)/model/([0-9]+)/prop")
class PropAddHandler(application.RequestHandler):
    def get(self, doc_id, model_id, *args, **kwargs):
        self.render('prop_add.html', doc_id=doc_id, model_id=model_id)

    def post(self, doc_id, model_id, *args, **kwargs):
        self.params['model_id'] = model_id
        prop_service.save_prop(self.params)
        self.redirect('/doc/model/{0}/prop/manager'.format(model_id))

@application.RequestMapping("/doc/model/([0-9]+)/prop/manager")
class PropManageHandler(application.RequestHandler):
    def get(self, model_id, *args, **kwargs):
        model = model_service.get_model(model_id)
        props = prop_service.get_props_by_model(model_id)
        self.render('prop_manage.html', props=props, model=model)

@application.RequestMapping("/doc/([0-9]+)/model/([0-9]+)/prop/([0-9]+)")
class PropEditHandler(application.RequestHandler):
    def get(self, doc_id, model_id, prop_id, *args, **kwargs):
        prop = prop_service.get_prop(prop_id)
        self.render('prop_edit.html', **prop)

    def post(self, doc_id, model_id, prop_id, *args, **kwargs):
        self.params['id'] = prop_id
        prop_service.update_prop(self.params)
        self.redirect('/doc/model/{0}/prop/manager'.format(model_id))
