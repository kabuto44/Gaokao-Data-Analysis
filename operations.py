from importlib import metadata
import numpy as np
import matplotlib.pyplot as plt
import csv
import consts as const
import yearbookops as ybk
import ast
from random import randint

def singleplot(variable, provinces = const.PROVINCES, title = None,xlabel = "Year", ylabel = None, legend_on = True):
    plt.figure(figsize=(12,8))
    data,metadata = extract(variable,provinces)
    if title==None:
        plt.title(metadata["indicator"][0])
    else:
        plt.title(title)
    plt.xlabel(xlabel)
    if ylabel == None:
        plt.ylabel(metadata["indicator"][0])
    else:
        plt.ylabel(ylabel)
    for prov in metadata["regions"]:
        plt.plot(metadata["dates"],data[metadata["regions"][prov]],label=prov)
    if legend_on:
        plt.legend()
    plt.show()


def saveplot(name,variable, provinces = const.PROVINCES, title = None, xlabel = "Year", ylabel = None, legend_on = True):
    plt.figure(figsize=(12,8))
    data,metadata = extract(variable,provinces)
    if title==None:
        plt.title(metadata["indicator"][0])
    else:
        plt.title(title)
    plt.xlabel(xlabel)
    if ylabel == None:
        plt.ylabel(metadata["indicator"][0])
    else:
        plt.ylabel(ylabel)
    for prov in metadata["regions"]:
        plt.plot(metadata["dates"],data[metadata["regions"][prov]],label=prov)
    if legend_on:
        plt.legend()
    plt.savefig("Plots/"+name+".pdf",bbox_inches="tight")

def scatterplot(xvar, yvar, year_range=[i for i in range(const.FIRSTYEAR,const.LASTYEAR+1)], provinces = const.PROVINCES, title = None, xlabel = None, ylabel = None):
    plt.figure(figsize=(12,8))
    xdata,xmetadata = extract(xvar, provinces)
    ydata, ymetadata = extract(yvar, provinces)
    if title == None:
        plt.title(ymetadata["indicator"][0]+" against \n"+xmetadata["indicator"][0])
    else:
        plt.title(title)
    if xlabel == None:
        plt.xlabel(xmetadata["indicator"][0])
    else:
        plt.xlabel(xlabel)
    if ylabel == None:
        plt.ylabel(ymetadata["indicator"][0])
    else:
        plt.ylabel(ylabel)
    for prov in provinces:
        color='#%06X' % randint(0, 0xFFFFFF)
        for year in year_range:
            x = xdata[xmetadata["regions"][prov]][xmetadata["dates"].index(year)]
            y = ydata[ymetadata["regions"][prov]][ymetadata["dates"].index(year)]
            if x==np.nan or y == np.nan:
                continue
            plt.scatter(x,y,color=color)
    plt.show()


def savescatter(name, xvar, yvar, year_range=[i for i in range(const.FIRSTYEAR,const.LASTYEAR+1)], provinces = const.PROVINCES, title = None, xlabel = None, ylabel = None):
    plt.figure(figsize=(12,8))
    xdata,xmetadata = extract(xvar, provinces)
    ydata, ymetadata = extract(yvar, provinces)
    if title == None:
        plt.title(ymetadata["indicator"][0]+" against \n"+xmetadata["indicator"][0])
    else:
        plt.title(title)
    if xlabel == None:
        plt.xlabel(xmetadata["indicator"][0])
    else:
        plt.xlabel(xlabel)
    if ylabel == None:
        plt.ylabel(ymetadata["indicator"][0])
    else:
        plt.ylabel(ylabel)
    for prov in provinces:
        color='#%06X' % randint(0, 0xFFFFFF)
        for year in year_range:
            x = xdata[xmetadata["regions"][prov]][xmetadata["dates"].index(year)]
            y = ydata[ymetadata["regions"][prov]][ymetadata["dates"].index(year)]
            if x==np.nan or y == np.nan:
                continue
            plt.scatter(x,y,color=color)
    plt.savefig("Plots/"+name+".pdf",bbox_inches="tight")
    
   
    


def extract(path,select=const.PROVINCES):
    metadata={}
    with open("Indicators/" + path + ".txt") as txtfile:
        lines = txtfile.readlines()
        for line in lines:
            metadata[line[:line.index(":")]]=ast.literal_eval(line[line.index(":")+2:])
    data=[]
    all_data=[]
    new_regions = {}
    i=0
    with open("Indicators/" + path+ ".csv") as csvfile:
        plots = csv.reader(csvfile)
        for row in plots:
            all_data.append(row)
        for prov in select:
            index = metadata["regions"][prov]
            this_row = all_data[index]
            row_data=[]
            for item in this_row:
                if item == "":
                    row_data.append(np.NaN)
                else:
                    row_data.append(float(item))
            data.append(row_data)
            new_regions[prov]=i
            i+=1
    metadata["regions"]=new_regions
    return data,metadata

def save(data,metadata, path):
    # data = data.astype(str)
    np.savetxt("Indicators/" + path+".csv",data,delimiter=",",fmt='%s')
    metadata_lines = []
    for key in metadata:
        metadata_lines.append(key + ": " + str(metadata[key]))
    np.savetxt("Indicators/" + path + ".txt", metadata_lines, fmt='%s')



        


def clean_from_yearbook(indicator):
    metadata,data=ybk.extract_ybk(indicator)
    metadata,data=ybk.sort_provinces(metadata,data)
    metadata,data=ybk.fix_date_range(metadata,data)
    metadata_lines = []
    for key in metadata:
        metadata_lines.append(key + ": " + str(metadata[key]))
    np.savetxt("Indicators/" + indicator + ".csv",data,delimiter=",",fmt='%s')
    np.savetxt("Indicators/" + indicator + ".txt", metadata_lines, fmt='%s')