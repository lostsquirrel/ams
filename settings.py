# -*- coding:utf-8 -*-
"""
Created on 2013-3-26

@author: zhuhua
"""
import os

installed_apps = ['manager', 'api', 'operation', 'param', 'resp', 'model', 'prop']

template_dir = os.path.join(os.path.dirname(__file__), "templates")
static_dir = os.path.join(os.path.dirname(__file__), "static")
db_user = 'ams'
db_password = 'ams_pass'
db_name = 'ams'
db_host = 'mariadb_10_1_main'
pass_code = 'a'
port = 9000
