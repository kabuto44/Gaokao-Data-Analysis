import numpy as np
import pandas as pd

def indicator_to_series(indicator,type=float):
    df = pd.read_csv("2000 Cohort/Indicators/" + indicator + ".csv", index_col=0, dtype={indicator:type})
    return df[indicator]

def make_df(indicators,type=float):
    series = []
    for indicator in indicators:
        series.append(indicator_to_series(indicator,type=type))
    return pd.concat(series,axis=1)

def load_df(path):
    df = pd.read_csv("2000 Cohort/Dataframes/" + path + ".csv", index_col=0,dtype=float)
    return df

def save_series(s, path):
    s.rename(path).to_csv("2000 Cohort/Indicators/" + path + ".csv")

def save_df(df,path):
    df.to_csv("2000 Cohort/Dataframes/" + path + ".csv")
