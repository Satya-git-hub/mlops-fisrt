#read params 
#process data from source
#return the dataframe 

import pandas as pd
import argparse
import yaml

def read_config(file_path):
    with open(file_path) as yaml_file:
        config = yaml.safe_load(yaml_file)
    return config 

def read_data(file_path):
    config = read_config(file_path)
    data_path = config["data_source"]["s3_source"]
    data = pd.read_csv(data_path)
    return data

if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config", default="params.yaml")
    parsed_args = args.parse_args()
    data = read_data(parsed_args.config)
    
