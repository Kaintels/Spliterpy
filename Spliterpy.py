import pandas as pd
import os
import traceback
import math
from tqdm import tqdm
import sys

try:
    delimiter = '-'
    file_version = str('0.1.0')
    print('**************************************************')
    print("* Spliterpy *")
    print("Version : ", file_version)
    print("Author : Kaintels (https://github.com/Kaintels)")
    print('**************************************************')
    print('\n')
    print('**************************************************')
    print('* Notice *')
    print("Header name must be only [Data]")
    print("csv file must be in the same path as an exe file.")
    print('**************************************************')
    print('\n')
    data_load = input("Please input your csv file name. : ")
    data = pd.read_csv(""+str(data_load)+".csv")
    numdata = list(data['[Data]'].values)
    sublist = []
    slice_data = []
    for i in tqdm(range(len(numdata)),desc='running...', mininterval=1, file=sys.stdout):
        if numdata[i] == '-':
            slice_data.append(sublist)
            sublist = []
        else:
            sublist.append(numdata[i])
except:
    traceback.print_exc()
input("Finished, Press Enter to close.")
slice_data = [x for x in slice_data if x]
slice_data.append(sublist)
for i in range(len(slice_data)):
    Total = pd.DataFrame(slice_data[i])
    Total.to_csv("datasplit" + str(i+1) + ".csv", header=False, index=False)
print("Done.")