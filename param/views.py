# -*- coding:utf-8 -*-

"""
Created on 2017年5月19日

@author: lostsquirrel
"""
import tornado
from simpletor import application
import param.services as param_service
from endpoint import services as ep_service

@application.RequestMapping("/param/manager")
class DocMangerHandler(application.RequestHandler):
    def get(self):
        self.render('param_manager.html', items=param_service.get_params())