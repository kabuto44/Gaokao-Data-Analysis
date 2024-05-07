import operations as ops
import os

def prep_all():
    indicators = []
    for path in os.listdir("2000 Cohort/Indicators"):
        indicator = path[:-4]
        indicators.append(indicator)
    df = ops.make_df(indicators,type=str)
    ops.save_df(df,path="All Data")

prep_all()