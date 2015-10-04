
import scipy as sp 
import csv
import pandas as pd

'''
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



dataset = pd.read_csv("./Data/Booth-Scan-Data/OSI.csv")
dataset['UID'] = dataset['Name'].map(str) + " " + dataset['Email Address'].map(str)

dataset.to_csv("./Data/Booth-Scan-Data/OSI.csv")


'''colHH = data[0]['Event']
print(colHH)
'''

