# -*- coding:utf-8 -*-
import tornado
from simpletor import application


from manager import get_doc_swagger_json
from api import Api

SUCCESS_ = {"status": "success"}



@application.RequestMapping("/doc/swagger/([0-9]+)")
class DocHandler(application.RequestHandler):
    '''获取标签列表'''
    def get(self, doc_id):

        res = get_doc_swagger_json(doc_id)

        self.render_json(res)
#
#     @Api(auth=True)
#     def post(self, *args, **kwargs):
#         params = tornado.escape.json_decode(self.request.body)
#         item = Item()
#         item.name = params['name']
#         services.save_item(item)
#         self.render_json(SUCCESS_)
#
#     @Api(auth=True)
#     def put(self):
#         params = tornado.escape.json_decode(self.request.body)
#         item_id = params['id']
#         services.set_default(item_id)
#         self.render_json(SUCCESS_)
#
#     @Api(auth=True)
#     def delete(self, *args, **kwargs):
#         params = tornado.escape.json_decode(self.request.body)
#         item_id = params['id']
#         services.remove_item(item_id)
#         self.render_json(SUCCESS_)
#
# @application.RequestMapping("/api/item/default")
# class DefaultItemHandler(application.RequestHandler):
#     def get(self, *args, **kwargs):
#         item = services.get_default_item()
#         self.render_json(item)
#
# @application.RequestMapping("/api/node")
# class NodeHandler(application.RequestHandler):
#     def get(self, *args, **kwargs):
#         nodes = services.get_nodes()
#         self.render_json(nodes)
#
#     @Api(auth=True)
#     def post(self, *args, **kwargs):
#         params = tornado.escape.json_decode(self.request.body)
#         node = Node()
#         node.open = params['open']
#         node.close = params['close']
#         node.highest = params['highest']
#         node.lowest = params['lowest']
#         node.date = params['ndate']
#         node.item_id = params['item']
#         services.save_node(node)
#         self.render_json(SUCCESS_)
#
#     @Api(auth=True)
#     def delete(self, *args, **kwargs):
#         params = tornado.escape.json_decode(self.request.body)
#         node_id = params['id']
#         services.remove_node(node_id)
#         self.render_json(SUCCESS_)
#
# @application.RequestMapping("/api/evaluation/data")
# class EvaluationDataHandler(application.RequestHandler):
#     def get(self, *args, **kwargs):
#         dataList = evaluationService.get_all_data()
#         self.render_json(dataList)
#
#     def post(self, *args, **kwargs):
#         params = tornado.escape.json_decode(self.request.body)
#         # print type(params)
#         # print params['evaluation_score']
#         data = EvaluationData()
#         data.trade_date = params['trade_date']
#         # data.position_time = params.get('position_time')
#         # data.position_time_str = params['position_time_str']
#         data.profit = params['profit']
#         data.commission = params['commission']
#         data.evaluation_score = params['evaluation_score']
#         data.volume = params['volume']
#         evaluationService.save_data(data)
#         self.render_json(SUCCESS_)
#
#     def delete(self, *args, **kwargs):
#         params = tornado.escape.json_decode(self.request.body)
#         data_id = params['id']
#         evaluationService.remove_data(data_id)
#         self.render_json(SUCCESS_)
#
# @application.RequestMapping("/api/evaluation/stats/general")
# class EvaluationStatsGeneralHandler(application.RequestHandler):
#     def get(self, *args, **kwargs):
#         data = evaluationService.get_stats_general()
#         # print(data)
#         self.render_json(data)
#
# @application.RequestMapping("/api/evaluation/stats/unit")
# class EvaluationStatsUnitHandler(application.RequestHandler):
#     def get(self, *args, **kwargs):
#         data = evaluationService.get_stats_unit()
#         # print(data)
#         self.render_json(data)