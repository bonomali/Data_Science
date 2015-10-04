import scipy as sp 
import numpy as np
import csv
import pandas as pd

'''
data1 = pd.read_csv("./Data/booth_trans2.csv")
data2 = pd.read_csv("./Data/session_trans1.csv")

datafinal = data1.append(data2 , ignore_index = True)

datafinal.to_csv("./Data/Merge.csv")

'''
'''
data = pd.read_csv("./Data/Merge.csv")

cols = list(data.columns)
print len(cols)

for i in range(0,2155) :
	if data["AA_ID"][i] == data["AA_ID"][i+1] :
		for j in range(2,len(cols)) :
			if (data[cols[j]][i] != data[cols[j]][i+1]) :
				if (pd.isnull(data[cols[j]][i]) == 0) & (pd.isnull(data[cols[j]][i+1]) == 0) :
			            	if len(data[cols[j]][i]) < len(data[cols[j]][i+1]) :
					              data[cols[j]][i] = data[cols[j]][i+1]
				else :
				      if pd.isnull(data[cols[j]][i+1]) == 0 :
				      	data[cols[j]][i] = data[cols[j]][i+1]
		data["AA_ID"][i+1] = "abcde"
		i = i + 1

data.to_csv("./Data/Merge1.csv")			
data = pd.read_csv("./Data/Merge1.csv")
data = data[data.AA_ID != "abcde"]
data.to_csv("./Data/Merge2.csv")
'''
'''
data = pd.read_csv("./Data/Merge3.csv")

for i in range(0,1472) :
	if(pd.isnull(data["Total Booths"][i]) != 0) :
		data["Total Booths"][i] = 0 
	if(pd.isnull(data["Total Sessions"][i]) != 0) :
		data["Total Sessions"][i] = 0
	if(pd.isnull(data["Status"][i]) != 0) :
	      if (data["Total Booths"][i] != 0 ) | (data["Total Sessions"][i] != 0) :
	          data["Status"][i] = "Confirmed"	 		

data.to_csv("./Data/Merge4.csv")
'''
'''
dataset = pd.read_csv("./Data/Regi.csv")
cols = list(dataset.columns)
print len(cols)
dataset['AA_ID'] = "a"
dataset['AA_ID'] = dataset['First Name'].map(str) + " " + dataset['Last Name'].map(str) + " " + dataset['Email Address'].map(str)

dataset.to_csv("./Data/Regi1.csv")
'''
'''
data1 = pd.read_csv("./Data/Regi1.csv")
data2 = pd.read_csv("./Data/Merge4.csv")

data = data1.append(data2 , ignore_index = True)

data.to_csv("./Data/Final_Merge.csv")
'''


data = pd.read_csv("./Data/Final_Merge2.csv")
data.to_csv("./Data/Final_Merge3.csv")