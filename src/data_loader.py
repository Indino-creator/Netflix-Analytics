import pandas as pd 
# Here we will load data fo further cleanin process 

def data_loader():
    Data = pd.read_csv("../Datasets/netflix_titles.csv")
    return Data
