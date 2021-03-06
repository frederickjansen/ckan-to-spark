from pyspark.sql import SparkSession
from pyspark.sql.utils import AnalysisException
import conf
import os


def csv_to_parquet(file):
    spark = SparkSession.builder.appName('csv-to-parquet').getOrCreate()
    try:
        df = spark.read.option('header', 'true').option('inferschema', 'true').csv(file)
        df.write.mode('overwrite').parquet(os.path.join(conf.FLAGS.output_dir, os.path.splitext(file)[0]) + '.parquet')
    except TypeError:
        print('Spark Error: ' + file)
    except AnalysisException as e:
        print('Spark Analysis Error for {}'.format(file) + e.desc)
