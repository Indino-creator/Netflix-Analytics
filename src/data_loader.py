import pandas as pd 


def data_loader():
    Data = pd.read_csv("Datasets/netflix_titles.csv")
    return Data

data_loader()
