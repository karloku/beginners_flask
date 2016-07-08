import json
from mongoengine import Document
from mongoengine.queryset.queryset import QuerySet
from bson.objectid import ObjectId

class ModelJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Document):
            return obj.to_mongo().to_dict()
        if isinstance(obj, ObjectId):
            return unicode(obj)
        if isinstance(obj, QuerySet):
            return [ele for ele in obj]
        return json.JSONEncoder.default(self, obj)

    @classmethod
    def dumps(cls, obj):
        return json.dumps(obj, cls=cls)
