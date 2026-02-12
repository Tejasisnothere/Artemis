import pandas as pd
from intent_extractor.constants.application import REVIEW_DATA_PATH
import requests
import os


class TextIngestor:
    def __init__(self, json_arr, filename):
        self.filename = filename
        self.json_arr = json_arr
        self.save_file()
        
    def save_file(self):
        file_path = os.path.join(REVIEW_DATA_PATH, f"{self.filename}.csv")
        df = pd.DataFrame(self.json_arr)
        df.to_csv(file_path)
    