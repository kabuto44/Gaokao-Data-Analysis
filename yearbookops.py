import numpy as np
import csv
import consts as const

def extract_ybk(indicator):
    with open("Yearbook Imported Data/" + indicator + ".csv") as imported:
        indicator_name = ""
        data = []
        dates = []
        raw_data = []
        region_dict = {}
        current_index=0
        rows = csv.reader(imported)
        #put data into list to work with
        for row in rows:
            raw_data.append(row)

        #determine date range
        for row in raw_data:
            if row[0]=="Region":
                dates = row[1:]

        #copy numerical data into data, copy province information into region_dict
        for row in raw_data:
            if row[0][:4]=="Data":
                continue
            if str(row[0][:10])=="Indicators":
                indicator_name+=row[0][12:]
            if str(row[0][:4])=="Year":
                continue
            if str(row[0]) in const.PROVINCES:
                region_dict[row[0]]=current_index
                data.append(row[1:])
                current_index+=1
        
        metadata = {"indicator": indicator_name, "dates": dates,"regions": region_dict}
        return metadata,data

def sort_provinces(metadata,data):
    sorted_data=[]
    for i in range(len(const.PROVINCES)):
            this_row=data[metadata["regions"][const.PROVINCES[i]]]
            sorted_data.append(this_row)
    return metadata,data

def fix_date_range(metadata,data):
    fixed_data = []
    for i in range(len(const.PROVINCES)):
        prov = const.PROVINCES[i]
        row = metadata["regions"][prov]
        row_data = []
        for j in range(const.LASTYEAR-const.FIRSTYEAR+1):
            datum = None
            try:
                column = metadata["dates"].index(str(j+const.FIRSTYEAR))
                try:
                    datum = data[row][column]
                except IndexError:
                    datum = None
            except ValueError:
                datum = None
            row_data.append(datum)
        fixed_data.append(row_data)
    data = fixed_data
    new_dates = [const.FIRSTYEAR+k for k in range(0,const.LASTYEAR-const.FIRSTYEAR+1)]
    metadata["dates"]=new_dates
    metadata["regions"]=const.PROV_DICT
    return metadata,data