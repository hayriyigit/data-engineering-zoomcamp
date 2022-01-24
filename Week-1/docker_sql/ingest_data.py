#!/usr/bin/env python
# coding: utf-8

import os
from time import time
import pandas as pd
import argparse
from sqlalchemy import create_engine


def main(params):
    user = params.user
    password = params.password
    host = params.host
    port = params.port
    db = params.db
    table_name = params.table_name
    url = params.url
    csv_name = 'output.csv'

    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db}')

    os.system(f'wget {url} -O {csv_name}')

    data = pd.read_csv(csv_name, iterator=True, chunksize=100000)

    df = next(data)

    #df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
    #df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)

    df.head(n = 0).to_sql(name = table_name, con = engine, if_exists = 'replace')

    df.to_sql(name = table_name, con = engine, if_exists = 'append')

    while True:
        tic = time()

        try:
            df = next(data)
        except StopIteration:
            print("Finished ingestion...")
            break

        #df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
        #df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)

        df.to_sql(name = table_name, con = engine, if_exists = 'append')

        toc = time()

        print('inserted another chunk and took %.3f secods' % (toc-tic))



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Ingest CSV data to Postgres')

    parser.add_argument('--user', help='user name for postgres')
    parser.add_argument('--password', help='password for postgres')
    parser.add_argument('--host', help='host for postgres')
    parser.add_argument('--port', help='port for postgres')
    parser.add_argument('--db', help='database name for postgres')
    parser.add_argument('--table_name', help='name of the table where we will write the results to')
    parser.add_argument('--url', help='url of the csv file')


    args = parser.parse_args()

    main(args)
