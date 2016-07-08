from list_serializer import ListSerializer

class QuerySetSerializer(ListSerializer):
    def serializer_document(self):
        return [ele for ele in self.document]
