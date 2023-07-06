import pandas as pd


class DocToXlsx:

    def __init__(self, keys: list):
        self.df = pd.DataFrame({k:[] for k in keys})

    def add(self, row):
        self.df = self.df._append(row, ignore_index=True)

    def save(self, path):
        if ".xlsx" not in path:
            path = path + ".xlsx"

        self.df.to_excel(path, index=False)
