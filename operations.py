import numpy as np
import matplotlib.pyplot as plt
import csv
import consts as const
import yearbookops as ybk

def multiplot(datasets, provinces,title = None, ylabel = None,legend_on=True):
    plt.figure(figsize=(12,8))
    for set in datasets:
        with open("Data/"+set+".csv","r") as csvfile:
            plots = csv.reader(csvfile)
            if provinces == None:
                series = []
                dates = []
                labels = []
                for row in plots:
                    if row[0]=="Region":
                        dates = row[2:]
                        continue
                    else:
                        name = row[0]
                        labels.append(name)
                        prov = []
                        for i in range(2,len(row)):
                            prov.append(float(row[i]))
                        series.append(prov)
                dates.reverse()
                for s in series:
                    s.reverse()
                for i in range(0,len(series)):
                    plt.plot(dates,series[i],label=labels[i] + ", " + set)
            else:
                dates = []
                series = []
                labels = []
                for row in plots:
                    if row[0] == "Region":
                        dates = row[2:]
                        continue
                    elif row[0] in provinces:
                        prov = []
                        for i in range(2,len(row)):
                            prov.append(float(row[i]))
                        series.append(prov)
                        labels.append(row[0])
                        continue
                dates.reverse()
                for prov in series:
                    prov.reverse()
                for i in range(0,len(series)):
                    plt.plot(dates,series[i],label=labels[i]+ ", " + set)
    if(title==None):
        plt.title(datasets)
    else:
        plt.title(title)
    plt.xlabel('Year', fontsize=10)
    plt.ylabel(ylabel, fontsize=10)
    if legend_on:
        plt.legend()
    plt.show()


def extract(path):
    data =[]
    header=[]
    with open("Data/" + path) as csvfile:
        plots = csv.reader(csvfile)
        for row in plots:
            thisrow=[]
            if row[0]=="Region":
                header=row
                continue
            for i in range(2,len(row)):
                thisrow.append(float(row[i]))
            data.append(thisrow)
    return np.array(data),header

def save(data, title,firstyear=2022):
    data = data.astype(str)
    length = len(data[0])
    data = np.insert(data,0,"",axis=1)
    data = np.insert(data,0,const.PROVINCES,axis=1)
    header = ["Region",""]
    for i in range(length):
        header.append(firstyear-i)
    all_data = np.insert(data,0,header,axis=0)
    np.savetxt("Data/" + title+".csv",all_data,delimiter=",",fmt='%s')


        


def clean_from_yearbook(indicator):
    metadata,data=ybk.extract_ybk(indicator)
    metadata,data=ybk.sort_provinces(metadata,data)
    metadata,data=ybk.fix_date_range(metadata,data)
    metadata_lines = []
    for key in metadata:
        metadata_lines.append(key + ": " + str(metadata[key]))
    np.savetxt("Cleaned Data/" + indicator + ".csv",data,delimiter=",",fmt='%s')
    np.savetxt("Cleaned Data/" + indicator + ".txt", metadata_lines, fmt='%s')
    # with open("Yearbook Imported Data/"+indicator + ".csv") as imported:
    #     is_partial=False
    #     data=[]
    #     dates=[]
    #     rawdata=[]
    #     region_dict = {}
    #     final_data=[]
        
    #     print(indicator_name)
    #     print(dates)
    #     print(data)
    #     print(region_dict)