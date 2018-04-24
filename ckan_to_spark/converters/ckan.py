from converters import Converter
import conf
import prequest


class Ckan(Converter):
    API_GET_PACKAGES = '/api/3/action/package_list'

    @property
    def type(self):
        return 'ckan'

    def __init__(self):
        super().__init__()

    def get_dataset_names(self):
        res = prequest.get(conf.FLAGS.url + self.API_GET_PACKAGES)
        if res.status_code == 200:
            return res.json()['result']

    def get_dataset(self, name):
        pass

    def get_dataset_columns(self, name):
        pass
