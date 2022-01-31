#!/usr/bin/env python
# coding: utf-8

import os
from time import time
import pandas as pd
from sqlalchemy import create_engine


def ingest_callable(user, password, host, port, db, table_name, csv_file):

    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db}')
    engine.connect()

    data = pd.read_csv(csv_file, iterator=True, chunksize=100000)

    df = next(data)

    df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
    df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)

    df.head(n = 0).to_sql(name = table_name, con = engine, if_exists = 'replace')

    df.to_sql(name = table_name, con = engine, if_exists = 'append')

    while True:
        tic = time()

        try:
            df = next(data)
        except StopIteration:
            print("Finished ingestion...")
            break

        df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
        df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)

        df.to_sql(name = table_name, con = engine, if_exists = 'append')

        toc = time()

        print('inserted another chunk and took %.3f secods' % (toc-tic))

