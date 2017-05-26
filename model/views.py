# -*- coding:utf-8 -*-

"""
Created on 2017年5月23日

@author: lostsquirrel
"""

from simpletor import application
from model import services as model_service
from resp import services as resp_service

@application.RequestMapping("/model")
class ModelAddHandler(application.RequestHandler):
    def get(self, *args, **kwargs):
        self.render('model_add.html', model=None, **self.params)

    def post(self, *args, **kwargs):
        model_service.save_model(self.params)
        self.redirect('/doc/{0}/model/manager'.format(self.params.get('doc_id')))

@application.RequestMapping("/model/([0-9]+)")
class ModelEditHandler(application.RequestHandler):
    def get(self, model_id, *args, **kwargs):
        model = model_service.get_model(model_id)
        self.render('model_add.html', model=model)

# 带来源进入模型列表
@application.RequestMapping("/doc/([0-9]+)/model/manager")
class ModelManagerHandler(application.RequestHandler):
    def get(self, doc_id, *args, **kwargs):
        params = self.params
        if not params.has_key('resp_id'):
            params['resp_id'] = None
        if not params.has_key('is_wrapper'):
            params['is_wrapper'] = None
        if not params.has_key('current_model_id'):
            params['current_model_id'] = -1
        models = model_service.get_models(doc_id)
        self.render('model_manger.html', models=models, doc_id=doc_id, **params)

    def post(self, doc_id, *args, **kwargs):
        params = self.params
        resp_service.bind_model_resp(params)
        np = '/doc/{0}/model/manager'.format(doc_id)

        self.redirect(np)
