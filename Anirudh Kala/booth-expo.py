
import scipy as sp 
import csv
import pandas as pd
import numpy as np

path = {}

path[1]  = "AF (OSIsoft)"
path[2]  = "Analytics (OSIsoft)"
path[3] = "BI (OSIsoft)"
path[4]  = "Cloud Connect (OSIsoft)"
path[5]  = "Data Archive (OSIsoft)"
path[6]  = "ESRI (OSIsoft)"
path[7]  = "Interfaces (OSIsoft)"
path[8]  = "Managed PI"
path[9]  = "Odata & SQL (OSIsoft)"
path[10] = "Online Services (OSIsoft)"
path[11] = "OSI soft Event Frames"
path[12] = "OSIsoft PI Coresight"
path[13] = "OSIsoft PI DataLink"
path[14] = "OSIsoft PI Manual Logger"
path[15] = "OSIsoft PI Notifications"
path[16] = "OSIsoft PI ProcessBook"
path[17] = "OSIsoft Product Expo (OSIsoft)"
path[18] = "Search (OSIsoft)"
path[19] = "WebAPI (OSIsoft)"
path[20] = "WebParts (OSIsoft)"
path[21]  = "ADMSE"
path[22]  = "BARCO"
path[23] =  "Casne"
path[24]  = "Data South System"
path[25]  = "Datawatch Corporation"
path[26]  = "Doble"
path[27]  = "Ekhosoft"
path[28]  = "Emerson"
path[29]  = "Eng. Consultants Group"
path[30] = "ESRI"
path[31] = "Exele Information Sys."
path[32] = "Industrial Evolution"
path[33] = "Infotechnics Limited"
path[34] = "Metrix Vib"
path[35] = "O-Sys"
path[36] = "Owl Computing Tech."
path[37] = "Pattern Discovery Tech."
path[38] = "Pimsoft"
path[39] = "Process Plugins"
path[40] = "Rockwell"
path[41] = "RoviSys"
path[42] = "SAS"
path[43] = "Special Partner Booth"
path[44] = "Tatsoft"
path[45] = "TIBCO Software"
path[46] = "Trinity Consultants"
path[47] = "Waterfall Security"
'''


# data = sp.genfromtxt("./Data/Registration-Data/UC2014AllFields.csv",delimiter = "\t")
#data = csv.reader("./Data/Booth-Scan-Data/ExpoScansOSI/AF (OSIsoft).csv.clean.csv", delimiter= " ")

data = {}
data1 = {}

for i in range(0,20) :
	data[i] = pd.read_csv("./Data/Booth-Scan-Data/ExpoScansOSI/" + path[i+1] + ".csv.clean.csv" , sep = ',' )
	data[i]['Event'] = path[i+1]



for i in range(0,20) :
      data[i].to_csv("./Data/Booth-Scan-Data/ExpoScansOSI/process/" + path[i+1]  + ".csv" , sep = ',' )

## to contanicate

for i in range(0,20) :
	data1[i] = pd.read_csv("./Data/Booth-Scan-Data/ExpoScansOSI/process/" + path[i+1] + ".csv" , sep = ',' )


	#result = data1[0].append(data1[1] )
	result = data1[0]
for i in range(1,20) :
       result = result.append(data1[i] , ignore_index = True)  

result.to_csv("./Data/Booth-Scan-Data/ExpoScansOSI/process/FINAL.csv" , sep = ',' )

final = pd.read_csv("./Data/Booth-Scan-Data/ExpoScansOSI/process/FINAL.csv" , sep = ',' )
final["Address Line"] = final["Address Line 1"].map(str) + final["Address Line 2"].map(str)
final["Name"] = final["Name Badge First Name"].map(str) + " " + final["Name Badge Last Name"].map(str)
final.pop('Address Line 2')
final.pop('Address Line 1')
final.to_csv("./Data/Booth-Scan-Data/ExpoScansOSI/process/FINAL2.csv" , sep = ',' )

'''
## ***************************** Till here I got the FINAL2.csv file ***************************************************
'''
#mix two csv in Booth-Scan-Data

data1 = pd.read_csv("./Data/Booth-Scan-Data/OSI.csv")
data2 = pd.read_csv("./Data/Booth-Scan-Data/Partner.csv")

result = data1.append(data2 , ignore_index = True )
result.to_csv("./Data/booth.csv")
'''
'''
words = []
data = pd.read_csv("./Data/booth.csv")
data['First Name'] = "nan"
data['Second Name'] = "nan"
for i in range (0,2428) :
	words = data['Name'][i].split(" ");
	data['First Name'][i] = words[0]
	data['Second Name'][i] = words[1]

data.to_csv("./Data/booth.csv")

'''
# to get the learning using the levels 
#data = pd.read_csv("./Data/booth_trans.csv")
'''
for i in range(1,47) :
	data[path[i]] = 0

for i in range(0,2428) :
	for j in range(i , 2428) :
		if(data["AA_ID"][i] == data["AA_ID"][j]) :
			str = data["Booth"][j]
			for k in range(1,47) :
				if(str == path[k]) :
					data[str][i] = 1
					break
		else :
		     i = j-1 
		     break
		if(i != j) :
		       data["AA_ID"][j] = "abcdef" 

data = data[data.AA_ID != "abcdef"]
data.to_csv("./Data/booth_trans1.csv")
data = pd.read_csv("./Data/booth_trans1.csv")
data.to_csv("./Data/booth_trans1.csv")
'''        			
data = pd.read_csv("./Data/booth_trans1.csv")
for i in range(0,764) :
	if (pd.isnull(data['Business Phone'][i])!=0) :
		data['Business Phone'][i] = data['Mobile Phone'][i]
data.to_csv("./Data/booth_trans2.csv")
'''
City = data["City"].unique()

print data["Booth"].value_counts()
'''
'''colHH = data[0]['Event']
print(colHH)
'''

