import numpy as np
import matplotlib.pyplot as plt
import csv
import provinces as const

def multiplot(datasets, provinces,title = None, ylabel = None):
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
                plt.legend()
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
                plt.legend()
    if(title==None):
        plt.title(datasets)
    else:
        plt.title(title)
    plt.xlabel('Year', fontsize=10)
    plt.ylabel(ylabel, fontsize=10)
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
