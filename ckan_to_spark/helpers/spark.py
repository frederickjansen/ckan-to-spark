from pyspark.sql import SparkSession
import conf
import os


def csv_to_parquet(file):
    spark = SparkSession.builder.appName('csv-to-parquet').getOrCreate()
    df = spark.read.csv(file)
    df.write.parquet(os.path.join(conf.FLAGS.output_dir, os.path.splitext(file)[0]) + '.parquet')
