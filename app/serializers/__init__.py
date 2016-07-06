import sys
from base_serializer import BaseSerializer
from object_id_serializer import ObjectIdSerializer
from user_serializer import UserSerializer

serializers = sys.modules[__name__]

def get_by_name(name):
    return getattr(serializers, name)

def get_by_model_name(name):
    return getattr(serializers, "{0}Serializer".format(name))

def get_by_model(model):
    return get_by_model_name(model.__name__)

def get_by_document(document):
    return get_by_model(document.__class__)

def init_by_document(document):
    return get_by_document(document)(document)

def serialize(serializer):
    pass
