from base_serializer import BaseSerializer

class ListSerializer(BaseSerializer):
    @classmethod
    def is_list(cls):
        return True
