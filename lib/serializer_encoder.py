import json
from app.serializers import BaseSerializer

class SerializerEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, BaseSerializer):
            return obj.to_mongo().to_dict()
        return json.JSONEncoder.default(self, obj)

    @classmethod
    def dumps(cls, obj):
        return json.dumps(obj, cls=cls)
