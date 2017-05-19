# -*- coding:utf-8 -*-
'''
Created on 2015年5月14日

@author: zhuhua
'''

from simpletor import application
from endpoint import services as ep_service

@application.RequestMapping("/doc/([0-9]+)/endpoint")
class EndPointHandler(application.RequestHandler):
    def get(self, doc_id):
        self.render('ep_add.html', doc_id=doc_id)

    def post(self, doc_id, *args, **kwargs):
        param = {k: self.get_argument(k) for k in self.request.arguments}
        ep_service.save_ep(param)
        self.redirect('/doc/'+doc_id)

@application.RequestMapping("/item")
class ItemHandler(application.RequestHandler):
    def get(self):
        self.render('k_line_edit.html')

@application.RequestMapping("/chart")
class ChartHandler(application.RequestHandler):
    def get(self):
        self.render('k_line_chart.html')

@application.RequestMapping("/")
class IndexHandler(application.RequestHandler):
    def get(self):
        self.render('index.html')
