# -*- coding:utf-8 -*-

"""
Created on 2017年5月23日

@author: lostsquirrel
"""

from simpletor import application
from model import services as model_service

@application.RequestMapping("/model")
class ModelAddHandler(application.RequestHandler):
    def post(self, *args, **kwargs):
        model_service.save_model(self.params)
        self.redirect('/doc/{doc_id}/operation/{op_id}/resp/{resp_id}/manager'.format(**self.params))


