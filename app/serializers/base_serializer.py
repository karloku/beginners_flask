from collections import OrderedDict

class BaseSerializer:
    __attr_configs__ = OrderedDict()

    @classmethod
    def set_attr(cls, name, serializer=None, list_serializer=None, **kargs):
        # Init attr_config if the subclass does not have its own attr_config dict initialized
        if not '__attr_configs__' in cls.__dict__:
            cls.__attr_configs__ = cls.__attr_configs__.copy()

        cls.__attr_configs__[name] = {
            'serializer': serializer,           # serializer responsible to serialize a field or elements in a list field
            'list_serializer': list_serializer, # serializer responsible to serialize the list it self
            'arguments': kargs                  # arguments passed to the field
        }

    @classmethod
    def attr_configs(cls):
        return cls.__attr_configs__

    @classmethod
    def attr_names(cls):
        return cls.__attr_configs__.keys()

    # returns whether the output document of the serializer is a list
    # - True if be
    # - False if not
    @classmethod
    def is_list(cls):
        return False    

    # returns whether the output document of the serializer is an object
    # objects require further serialization of fields
    # - True if it has attrs
    # - False if not
    @classmethod
    def is_object(cls):
        return bool(cls.attr_configs())

    # init with document inside
    def __init__(self, document):
        self.document = document

    # returns the output document ready to be serialized
    def serializer_document(self):
        if not self.__class__.is_object():
            return self.document

        attrs = []
        for attr in self.__class__.attr_names():
            attr_arguments = self.__class__.attr_configs()[attr]['arguments']
            attrs.append((
                    attr,
                    getattr(self, attr)(**attr_arguments)
                ))

        return OrderedDict(attrs)

    # methods defined in the serializer prefered
    # fallbacks to the document itself if not defined. always return lambdas
    def __getattr__(self, name):
        return lambda: getattr(self.document, name)
