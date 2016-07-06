from mongoengine import Document, StringField

class User(Document):
    name = StringField(max_length=200, required=True)

    @classmethod
    def get_by_id(cls, id):
        return cls.objects.get(id=id)
