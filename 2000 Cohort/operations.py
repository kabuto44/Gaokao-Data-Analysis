import numpy as np
import pandas as pd

def indicator_to_series(indicator):
    df = pd.read_csv("Indicators/" + indicator + ".csv", index_col=0, dtype={indicator:float})
    return df[indicator]

def make_df(indicators):
    series = []
    for indicator in indicators:
        series.append(indicator_to_series(indicator))
    return pd.concat(series,axis=1)

def load_df(path):
    df = pd.read_csv("Dataframes/" + path + ".csv", index_col=0,dtype=float)
    return df

def save_series(s, path):
    s.rename(path).to_csv("Indicators/" + path + ".csv")

def save_df(df,path):
    df.to_csv("Dataframes/" + path + ".csv")
