import abc

# class ConverterType(type):
#     def __new__(mcs, name, bases, attrs):
#         new = super(ConverterType, mcs).__new__
#         if not attrs.get('type'):
#             raise NotImplementedError('Class {} does not implement type'.format(mcs.__name__))
#
#         converter_type = attrs['type']
#         register(new(mcs, name, bases, attrs))
#
#         return plugins[converter_type].__class__


class Converter(metaclass=abc.ABCMeta):
    def __init__(self):
        pass
    # self.FLAGS = flags

    @property
    @abc.abstractmethod
    def type(self):
        raise NotImplementedError('Class {} does not implement type'.format(self.__class__.__name__))

    @abc.abstractmethod
    def get_dataset_names(self):
        raise NotImplementedError('Class {} does not implement get_dataset_names()'.format(self.__class__.__name__))

    @abc.abstractmethod
    def get_dataset(self, name):
        raise NotImplementedError('Class {} does not implement get_dataset()'.format(self.__class__.__name__))

    @abc.abstractmethod
    def get_dataset_columns(self, name):
        raise NotImplementedError('Class {} does not implement get_dataset_columns()'.format(self.__class__.__name__))

    def store_dataset(self, name):
        pass
