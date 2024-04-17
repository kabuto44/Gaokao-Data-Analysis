from importlib import metadata
import numpy as np
import matplotlib.pyplot as plt
import csv
import consts as const
import yearbookops as ybk
import ast

def singleplot(variable, provinces = const.PROVINCES, xlabel = "Year", ylabel = None, legend_on = True):
    plt.figure(figsize=(12,8))
    data,metadata = extract(variable,provinces)
    plt.title(metadata["indicator"][0])
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


# def multiplot(indicators, provinces=const.PROVINCES,dates = None,title = None, ylabel = None,legend_on=True):
#     plt.figure(figsize=(12,8))
#     for variable in indicators:
#         data, metadata = extract(variable,provinces)
#         if dates == None:
#             dates = metadata["dates"]
#         for prov in metadata["regions"]:
#             index = metadata["regions"][prov]
#             prov_data = data[index]
#             row_dates = dates.copy()
#             new_data = []
#             for yr in row_dates:
#                 try:
#                     i = metadata["dates"].index(yr)
#                     datum = prov_data[i]
#                     if datum == "nan":
#                         row_dates.remove(yr)
#                         continue
#                     new_data.append(float(datum))
#                 except IndexError:
#                     row_dates.remove(yr)

            
#     for set in datasets:
#         with open("Data/"+set+".csv","r") as csvfile:
#             plots = csv.reader(csvfile)
#             if provinces == None:
#                 series = []
#                 dates = []
#                 labels = []
#                 for row in plots:
#                     if row[0]=="Region":
#                         dates = row[2:]
#                         continue
#                     else:
#                         name = row[0]
#                         labels.append(name)
#                         prov = []
#                         for i in range(2,len(row)):
#                             prov.append(float(row[i]))
#                         series.append(prov)
#                 dates.reverse()
#                 for s in series:
#                     s.reverse()
#                 for i in range(0,len(series)):
#                     plt.plot(dates,series[i],label=labels[i] + ", " + set)
#             else:
#                 dates = []
#                 series = []
#                 labels = []
#                 for row in plots:
#                     if row[0] == "Region":
#                         dates = row[2:]
#                         continue
#                     elif row[0] in provinces:
#                         prov = []
#                         for i in range(2,len(row)):
#                             prov.append(float(row[i]))
#                         series.append(prov)
#                         labels.append(row[0])
#                         continue
#                 dates.reverse()
#                 for prov in series:
#                     prov.reverse()
#                 for i in range(0,len(series)):
#                     plt.plot(dates,series[i],label=labels[i]+ ", " + set)
#     if(title==None):
#         plt.title(datasets)
#     else:
#         plt.title(title)
#     plt.xlabel('Year', fontsize=10)
#     plt.ylabel(ylabel, fontsize=10)
#     if legend_on:
#         plt.legend()
#     plt.show()


def extract(path,select=const.PROVINCES):
    metadata={}
    with open("Data/" + path + ".txt") as txtfile:
        lines = txtfile.readlines()
        for line in lines:
            metadata[line[:line.index(":")]]=ast.literal_eval(line[line.index(":")+2:])
    data=[]
    all_data=[]
    new_regions = {}
    i=0
    with open("Data/" + path+ ".csv") as csvfile:
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
    data = data.astype(str)
    np.savetxt("Data/" + path+".csv",data,delimiter=",",fmt='%s')
    metadata_lines = []
    for key in metadata:
        metadata_lines.append(key + ": " + str(metadata[key]))
    np.savetxt("Data/" + path + ".txt", metadata_lines, fmt='%s')



        


def clean_from_yearbook(indicator):
    metadata,data=ybk.extract_ybk(indicator)
    metadata,data=ybk.sort_provinces(metadata,data)
    metadata,data=ybk.fix_date_range(metadata,data)
    metadata_lines = []
    for key in metadata:
        metadata_lines.append(key + ": " + str(metadata[key]))
    np.savetxt("Data/" + indicator + ".csv",data,delimiter=",",fmt='%s')
    np.savetxt("Data/" + indicator + ".txt", metadata_lines, fmt='%s')