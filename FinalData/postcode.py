import csv
import pandas as pd
import numpy as np

ogdata = pd.read_csv("RealFinalData2009.csv")
postsource = pd.read_csv("sbk_postcode_buurtcombinatie.csv")
lijst = []
def is_lower(a, b):
    if ord(a[0]) < ord(b[0]):
        return True
    elif ord(a[0]) == ord(b[0]):
        if ord(a[1]) > ord(b[1]):
            return False
        if ord(a[1]) < ord(b[1]):
            return True
        else:
            return False
    else:
        return False


for i in ogdata["POSTCODE_VAN"]:
    for j in postsource["postcode_min"]:
        if i[:4] == j[:4]:
            if is_lower(ogdata[ogdata.POSTCODE_VAN == i]["POSTCODE_VAN"].iloc[0][4:], postsource[postsource.postcode_min == j]["postcode_max"].iloc[0][4:]) and not is_lower(ogdata[ogdata.POSTCODE_VAN == i]["POSTCODE_VAN"].iloc[0][4:], postsource[postsource.postcode_min == j]["postcode_min"].iloc[0][4:]):
                lijst.append(postsource[postsource.postcode_min == j]["buurtcombinatie"].iloc[0])
            elif ogdata[ogdata.POSTCODE_VAN == i]["POSTCODE_VAN"].iloc[0][4:] == postsource[postsource.postcode_min == j]["postcode_max"].iloc[0][4:] or ogdata[ogdata.POSTCODE_VAN == i]["POSTCODE_VAN"].iloc[0][4:] == postsource[postsource.postcode_min == j]["postcode_min"].iloc[0][4:]:
                lijst.append(postsource[postsource.postcode_min == j]["buurtcombinatie"].iloc[0])
print(lijst)
                
            
