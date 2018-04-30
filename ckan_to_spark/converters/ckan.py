from converters import Converter
import conf
import prequest
import os
from helpers import spark
from multiprocessing.dummy import Pool


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

    def store_datasets(self, names):
        pool = Pool()
        results = pool.map(self._store_dataset, names)
        return results

    def _store_dataset(self, name):
        res = prequest.get(conf.FLAGS.url + self.API_GET_METADATA.format(name))
        if res.status_code == 200:
            resources = res.json()['result']['resources']
            url, path = None, None
            for resource in resources:
                if resource['format'] == 'CSV':
                    url = resource['url']
                    break
            if url:
                res = prequest.get(url)
                path = os.path.join(conf.FLAGS.temp_dir, name) + '.csv'
                with open(path, 'w', encoding='utf8') as f:
                    f.write(res.text)
                spark.csv_to_parquet(path)

            return path

    def get_dataset_columns(self, name):
        pass

    def get_dataset(self, name):
        pass
