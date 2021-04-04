import json
import os

import numerapi
import pandas as pd


example_public_id = os.getenv("NMR_PUBLIC_ID")
example_secret_key = os.getenv("NMR_SECRET_KEY")
NAPI = numerapi.NumerAPI(example_public_id, example_secret_key)

                         
def download_current_data(directory: str):
    """
        Downloads the data for the current round
        :param directory: The path to the directory where the data needs to be saved
        """
    current_round = NAPI.get_current_round()
    if os.path.isdir(f"{directory}/numerai_dataset_{current_round}/"):
        print(f"You already have the newest data! Current round is: {current_round}")
    else:
        print(f"Downloading new data for round: {current_round}!")
        NAPI.download_current_dataset(dest_path=directory)

                         
def read_current(directory: str):
    with open(os.path.dirname(__file__) + "/dtypes.json") as f:
        dtypes = json.load(f)
    
    full_path = f"{directory}/numerai_dataset_{NAPI.get_current_round()}/"
    train_path = full_path + "numerai_training_data.csv"
    test_path = full_path + "numerai_tournament_data.csv"
    train = pd.read_csv(train_path, dtype=dtypes)
    test = pd.read_csv(test_path, dtype=dtypes)
    
    return train, test