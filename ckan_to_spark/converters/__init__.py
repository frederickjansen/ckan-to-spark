from .converter import Converter
from .ckan import Ckan

types = {'ckan': Ckan()}

__all__ = ['Converter', 'types']
