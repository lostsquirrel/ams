# -*- coding:utf-8 -*-

"""
Created on 2017年5月23日

@author: lostsquirrel
"""

from simpletor import application
from model import services as model_service


@application.RequestMapping("/model")
class ModelAddHandler(application.RequestHandler):
    def get(self, *args, **kwargs):
        self.render('model_add.html', model=None, **self.params)

    def post(self, *args, **kwargs):
        model_service.save_model(self.params)
        self.redirect('/model/manager')

@application.RequestMapping("/model/([0-9]+)")
class ModelEditHandler(application.RequestHandler):
    def get(self, model_id, *args, **kwargs):
        model = model_service.get_model(model_id)
        self.render('model_add.html', model=model)

# 带来源进入模型列表
@application.RequestMapping("/model/manager")
class ModelManagerHandler(application.RequestHandler):
    def get(self, *args, **kwargs):
        params = self.params
        if not params.has_key('resp_id'):
            params['resp_id'] = None
        if not params.has_key('is_wrapper'):
            params['is_wrapper'] = None
        models = model_service.get_models()
        self.render('model_manger.html', models=models, **params)

