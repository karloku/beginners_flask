import sys
import json
from base_serializer import BaseSerializer
from list_serializer import ListSerializer
from object_id_serializer import ObjectIdSerializer
from query_set_serializer import QuerySetSerializer
from user_serializer import UserSerializer

serializers = sys.modules[__name__]

def get_by_name(name):
    if hasattr(serializers, name):
        return getattr(serializers, name)

    return BaseSerializer

def get_by_model_name(name):
    name = __capitalize_model_name__(name)
    return get_by_name("{0}Serializer".format(name))

def __capitalize_model_name__(name):
    if len(name) <= 0:
        return name

    return name[0].upper() + name[1:]

def get_by_model(model):
    return get_by_model_name(model.__name__)

def get_by_document(document):
    return get_by_model(document.__class__)

def init_by_document(document):
    return get_by_document(document)(document)

def dumps(document, serializer=None, list_serializer=None):
    return json.dumps(serialize(document, serializer, list_serializer))

def serialize(document, serializer=None, list_serializer=None):
    doc_serializer = get_by_document(document)
    if doc_serializer.is_list():
        list_serializer = list_serializer if list_serializer else doc_serializer
    else:
        serializer = serializer if serializer else doc_serializer

    if list_serializer:
        return __serialize_list__(document, serializer, list_serializer)
    else:
        return __serialize_object__(document, serializer)

def __serialize_object__(obj, serializer):
    s_instance = serializer(obj)
    doc = s_instance.serializer_document()

    if not serializer.is_object():
        return doc

    serialized = {}

    for attr in serializer.attr_names():
        config = serializer.attr_configs()[attr]
        serialized[attr] = serialize(doc[attr], serializer=config['serializer'], list_serializer=config['list_serializer'])

    return serialized

def __serialize_list__(obj_list, serializer, list_serializer):
    ls_instance = list_serializer(obj_list)
    doc = ls_instance.serializer_document()

    return [serialize(ele, serializer=serializer) for ele in doc]


