import csv
import numpy as np
import os

def clean_data(indicator, name = None):
    if name is None:
        name = indicator
    with open("2000 Cohort/Yearbook Data/" + indicator + ".csv") as csvfile:
        data=[[indicator]]
        raw_data = []
        rows = csv.reader(csvfile)
        for row in rows:
            raw_data.append(row)
        for row in raw_data:
            if row[0][:4]=="Data":
                continue
            if str(row[0][:10])=="Indicators":
                continue
            if str(row[0][:4])=="Year":
                continue
            if str(row[0][:6])=="Region":
                continue
            data.append([row[1]])
        np.savetxt("2000 Cohort/Indicators/" + name + ".csv",data,delimiter=",",fmt='%s')

def clean_data_alt(indicator, name = None):
    if name is None:
        name = indicator
    with open("2000 Cohort/Yearbook Data/" + indicator + ".csv") as csvfile:
        data=[]
        raw_data = []
        rows = csv.reader(csvfile)
        for row in rows:
            raw_data.append(row)
        for row in raw_data:
            if row[0][:4]=="Data":
                continue
            if str(row[0][:10])=="Indicators":
                continue
            if str(row[0][:4])=="Year":
                continue
            if str(row[0][:6])=="Region":
                row[1]=indicator
            data.append(row)
        np.savetxt("2000 Cohort/Indicators/" + name + ".csv",data,delimiter=",",fmt='%s')

def clean_all():
    for path in os.listdir("2000 Cohort/Yearbook Data"):
        indicator = path[:-4]
        clean_data_alt(indicator)

clean_all()