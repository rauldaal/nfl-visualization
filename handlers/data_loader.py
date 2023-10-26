import pandas as pd


class Dataset:
    def __init__(self, path="data/dataset.csv"):
        self.data = None
        self.path = path

    def load_data(self):
        self.data = pd.read_csv(self.path)

    def filter(self, column_name, value):
        pass
