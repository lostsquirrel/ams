# -*- coding:utf-8 -*-

import copy
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
    secure = VO()
    secureToken = VO()
    secureToken.type = "apiKey"
    secureToken.name = "Authorization"
    secureToken['in'] = "header"
    secure.Bearer = secureToken
    res.securityDefinitions = secure
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
                if prop.prop_model_id is not None:
                    prop_model = model_service.get_model(prop.prop_model_id)
                if prop.type == 'object':
                    property_schema = VO()
                    property.schema = property_schema
                    property_schema['$ref'] = '#/definitions/{0}'.format(prop_model.name)
                elif prop.type == 'array':
                    property_item = VO()
                    property.items = property_item
                    property_item['$ref'] = '#/definitions/{0}'.format(prop_model.name)
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
            security = list()
            security.append(dict(Bearer=list()))
            operation.security = security
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
            responses = VO()
            operation['responses'] = responses
            for rp in resps:
                response = VO()
                responses[rp.code] = response
                response.description = rp.description
                response_schema = VO()
                response.schema = response_schema
                if has_contents(rp.response_model_id):
                    child_model = model_service.get_model(rp.response_model_id)
                    child_model_name = '#/definitions/{0}'.format(child_model.name)
                    if has_contents(rp.wrapper_id):
                        wrapper_model = model_service.get_model(rp.wrapper_id)
                        wrapper_name = '{0}{1}'.format(child_model.name, wrapper_model.name)
                        response_schema.type = 'object'
                        wrapper = copy.deepcopy(res.definitions[wrapper_model.name])
                        res.definitions[wrapper_name] = wrapper
                        wrapper_properties = wrapper['properties']
                        wrapper_data = VO()
                        wrapper_properties['data'] = wrapper_data

                        wrapper_schema = VO()
                        wrapper_data['schema'] = wrapper_schema
                        wrapper_schema.type = rp.type
                        response_ref = '#/definitions/{0}'.format(wrapper_name)
                        response_schema['$ref'] = response_ref
                        if 'array' == rp.type:
                            wrapper_items = VO()
                            wrapper_schema['items'] = wrapper_items
                            wrapper_items['$ref'] = child_model_name
                        else:
                            wrapper_schema['$ref'] = child_model_name
                    else:
                        response_schema.type = rp.type

                        if 'array' == rp.type:
                            schema_items = VO()
                            response_schema.items = schema_items
                            schema_items['$ref'] = child_model_name
                        else:
                            response_schema['$ref'] = child_model_name
    return res