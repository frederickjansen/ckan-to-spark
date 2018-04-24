from converters import Converter
import conf
import prequest


class Ckan(Converter):
    API_GET_PACKAGES = '/api/3/action/package_list'
    API_GET_METADATA = '/api/3/action/package_show?id={}'
    API_GET_COLUMNS = '/api/3/action/datastore_search?resource_id={}&limit=5'

    @property
    def type(self):
        return 'ckan'

    def __init__(self):
        super().__init__()

    def get_dataset_names(self):
        res = prequest.get(conf.FLAGS.url + self.API_GET_PACKAGES)
        if res.status_code == 200:
            return res.json()['result']

    def get_dataset(self, resource_id):
        pass

    def get_dataset_columns(self, name):
        res = prequest.get(conf.FLAGS.url + self.API_GET_METADATA.format(name))
        if res.status_code == 200:
            resource_id = res.json()['result']['resources'][0]['id']

            res = prequest.get(conf.FLAGS.url + self.API_GET_COLUMNS.format(resource_id))

            fields = []
            for field in res.json()['result']['fields']:
                fields.append((field['type'], field['id']))
            return fields
