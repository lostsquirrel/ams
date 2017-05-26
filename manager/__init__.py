# -*- coding:utf-8 -*-

from simpletor.utils import dict_slice, dict_copy, has_contents
from manager.models import DocVO, VO
from model import services as model_service
from prop import services as prop_service
from operation import services as op_service
from manager import services as mgr_service
from param import services as param_service
from resp import services as resp_service

def get_doc_swagger_json(doc_id):
    res = DocVO()
    doc = mgr_service.get_doc(doc_id)
    res.host = doc.host
    res.basePath = doc.base_path
    res.schemes = [x.strip() for x in doc.schemes.split(',')]
    res.info = dict_slice(doc, 'title', 'version', 'description')
    res.produces = [doc.produces]
    # definitions
    definitions = VO()
    res.definitions = definitions
    models = model_service.get_models(doc_id)
    for model in models:
        m = VO()
        if 'array' == model.type:
            child_model_id = model.get('child_model_id')
            if child_model_id is not None:
                child_model = model_service.get_model(child_model_id)
                definitions[model.name] = m
                m.type = model.type
                m.schema = VO()
                m.schema['$ref'] = '#/definitions/{0}'.format(child_model.name)
        else:
            definitions[model.name] = m
            m.type = model.type
            props = prop_service.get_props_by_model(model.id)
            m.properties = VO()
            for prop in props:
                property = VO()
                m.properties[prop.name] = property
                dict_copy(prop, property, 'type', 'format', 'description')

    # paths
    paths = VO()
    res.paths = paths

    ps = mgr_service.get_paths_by_doc(doc_id)
    for p in ps:
        path = VO()
        paths[p.path_url] = path
        ops = op_service.get_ops_by_path(p.id)
        for o in ops:
            operation = VO()
            path[o.operation] = operation

            dict_copy(o, operation, 'tags', 'summary', 'description')
            if type(operation.tags) != type(list):
                operation.tags = operation.tags
            #         parameters
            params = param_service.get_params_by_operation(o.id)
            for param in params:
                param.pop('id')
                param['in'] = param.pop('source')
                param['required'] = int(param.pop('required')) == 1
                if not has_contents(param.format):
                    param.pop('format')
                if not has_contents(param.default):
                    param.pop('default')
                if not has_contents(param.minimum):
                    param.pop('minimum')
                if not has_contents(param.maximum):
                    param.pop('maximum')

            operation.parameters = params

            # response
            resps = resp_service.get_resp_by_operation(o.id)
            for rp in resps:
                response = VO()
                operation[rp.code] = response
                response.description = rp.description
                response.schema = VO()
                child_model = model_service.get_model(rp.response_model_id)
                child_model_name = '#/definitions/{0}'.format(child_model.name)
                if rp.has_key('wrapper_id') and rp.wrapper_id is not None:
                    wrapper_model = model_service.get_model(rp.wrapper_id)
                    wrapper_name = '{0}{1}'.format(child_model.name, wrapper_model.name)
                    response.schema['$ref'] = '#/definitions/{0}'.format(wrapper_name)
                    wrapper = res.definitions[wrapper_model.name].copy()
                    res.definitions[wrapper_name] = wrapper
                    wrapper['data'] = VO()
                    wrapper['data']['type'] = rp.type
                    wrapper['data']['schema'] = VO()
                    if 'array' == rp.type:
                        wrapper['data']['schema'].items = VO()
                        wrapper['data']['schema'].items['$ref'] = child_model_name
                    else:
                        wrapper['data']['schema']['$ref'] = child_model_name
                else:
                    response.schema.type = rp.type

                    if 'array' == rp.type:
                        response.schema.items = VO()
                        response.schema.items['$ref'] = child_model_name
                    else:
                        response.schema['$ref'] = child_model_name


    return res