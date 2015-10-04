
import scipy as sp 
import numpy as np
import csv
import pandas as pd


path = {}

path[1]  = "ADMSE"
path[2]  = "BARCO"
path[3] =  "Casne"
path[4]  = "Data South System"
path[5]  = "Datawatch Corporation"
path[6]  = "Doble"
path[7]  = "Ekhosoft"
path[8]  = "Emerson"
path[9]  = "Eng. Consultants Group"
path[10] = "ESRI"
path[11] = "Exele Information Sys."
path[12] = "Industrial Evolution"
path[13] = "Infotechnics Limited"
path[14] = "Metrix Vib"
path[15] = "O-Sys"
path[16] = "Owl Computing Tech."
path[17] = "Pattern Discovery Tech."
path[18] = "Pimsoft"
path[19] = "Process Plugins"
path[20] = "Rockwell"
path[21] = "RoviSys"
path[22] = "SAS"
path[23] = "Special Partner Booth"
path[24] = "Tatsoft"
path[25] = "TIBCO Software"
path[26] = "Trinity Consultants"
path[27] = "Waterfall Security"


# data = sp.genfromtxt("./Data/Registration-Data/UC2014AllFields.csv",delimiter = "\t")
#data = csv.reader("./Data/Booth-Scan-Data/ExpoScansOSI/AF (OSIsoft).csv.clean.csv", delimiter= " ")

data = {}
data1 = {}
'''
for i in range(0,27) :
	data[i] = pd.read_csv("./Data/Booth-Scan-Data/ExpoScansPartner/" + path[i+1] + ".csv" , sep = ',' )
	data[i]['Event'] = path[i+1]
    



for i in range(0,27) :
      data[i].to_csv("./Data/Booth-Scan-Data/ExpoScansPartner/process/" + path[i+1]  + ".csv" , sep = ',' )


## to contanicate

for i in range(0,27) :
	data1[i] = pd.read_csv("./Data/Booth-Scan-Data/ExpoScansPartner/process/" + path[i+1] + ".csv" , sep = ',' )


	#result = data1[0].append(data1[1] )
	result = data1[0]
for i in range(1,27) :
       result = result.append(data1[i] , ignore_index = True)  

result.to_csv("./Data/Booth-Scan-Data/ExpoScansPartner/process/FINAL.csv" , sep = ',' )


final = pd.read_csv("./Data/Booth-Scan-Data/ExpoScansPartner/process/FINAL.csv" , sep = ',' )
final["Address Line"] = final["Address Line 1"].map(str) + " " + final["Address Line 2"].map(str)
final["Name"] = final["Name Badge First Name"].map(str) + " " + final["Name Badge Last Name"].map(str)
final.to_csv("./Data/Booth-Scan-Data/ExpoScansPartner/process/FINAL1.csv" , sep = ',' )

final = pd.read_csv("./Data/Booth-Scan-Data/ExpoScansPartner/process/FINAL1.csv" , sep = ',' )

final = final[pd.notnull(final['Badge ID'])]
final.to_csv("./Data/Booth-Scan-Data/ExpoScansPartner/process/FINAL2.csv" , sep = ',' )

final = pd.read_csv("./Data/Booth-Scan-Data/ExpoScansPartner/process/FINAL2.csv" , sep = ',' ) 
final.to_csv("./Data/Booth-Scan-Data/ExpoScansPartner/process/FINAL3.csv" , sep = ',' )
'''
## ***************************** Till here I got the FINAL1.csv file ***************************************************

dataset = pd.read_csv("./Data/Booth-Scan-Data/Partner.csv")
dataset['UID'] = dataset['Name'].map(str) + " " + dataset['Email Address'].map(str)

dataset.to_csv("./Data/Booth-Scan-Data/Partner.csv")
'''colHH = data[0]['Event']
print(colHH)
'''

