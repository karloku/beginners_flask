from base_serializer import BaseSerializer

class ObjectIdSerializer(BaseSerializer):
    def serializer_document(self):
        return str(self.document)
