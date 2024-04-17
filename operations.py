from importlib import metadata
import numpy as np
import matplotlib.pyplot as plt
import csv
import consts as const
import yearbookops as ybk
import ast

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