import json
import pandas as pd
from model.result import Result
import os

results_dir = 'campaign-results'

def main():
    for results_file in reversed(os.listdir(results_dir)):
        results_file_path = os.path.join(results_dir, results_file)
        with open(results_file_path) as rd:
            datapoint = json.loads(rd.read())
            result = Result.from_dict(datapoint)
            print(result)


if __name__ == "__main__":
    main()
