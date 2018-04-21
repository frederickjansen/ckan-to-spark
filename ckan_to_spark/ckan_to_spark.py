import argparse

FLAGS = None


def main(_):
    print(FLAGS)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--url',
        type=str,
        required=True,
        help='URL of CKAN data portal'
    )
    parser.add_argument(
        '--output-dir',
        type=str,
        required=True,
        help='Directory to store Spark Parquet files'
    )
    parser.add_argument(
        '--temp-dir',
        type=str,
        default='/tmp',
        help='Directory to store temporary files'
    )
    parser.add_argument(
        '--datasets',
        type=str,
        nargs='+',
        default=['ALL'],
        help='List of datasets to download, space separated. Defaults to ALL to download the entire collection'
    )
    parser.add_argument(
        '--auth',
        type=str,
        nargs='*',
        help='Optional space separated authentication details'
    )
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Output list of datasets to download, but don\'t store them in Spark'
    )

    FLAGS, unparsed = parser.parse_known_args()

    if FLAGS.auth and len(FLAGS.auth) == 1:
        parser.error('You have to provide both a username and password')

    main(FLAGS)