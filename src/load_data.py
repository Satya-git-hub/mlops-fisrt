#load the data from data source 
#store the data to data/raw

from operator import index
import os
import pandas as pd
import argparse
from get_data import read_config, read_data

def store_data(path):
    config = read_config(path)
    dataframe = read_data(path)
    columns = [cols.replace(" ", "_") for cols in dataframe.columns]
    dataframe.to_csv(config["load_data"]["raw_dataset_csv"], header=columns, index=False)

if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config", default="params.yaml")
    parsed_args = args.parse_args()
    store_data(parsed_args.config)