# split the raw data 
# save it in data/processed folder

from operator import index
import pandas as pd 
from get_data import read_config
from sklearn.model_selection import train_test_split
import argparse

def split_and_save(path):
    config = read_config(path)
    raw__path = config["load_data"]["raw_dataset_csv"]
    train_path = config["split_data"]["train_path"]
    test_path = config["split_data"]["test_path"]
    test_size = config["split_data"]["test_size"]
    random_state = config["base"]["random_state"]

    data = pd.read_csv(raw__path)
    train, test = train_test_split(data, test_size=test_size, random_state=random_state)
    train.to_csv(train_path, index=False)
    test.to_csv(test_path, index=False)

if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config", default="params.yaml")
    parsed_args = args.parse_args()
    split_and_save(parsed_args.config)