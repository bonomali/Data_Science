import os
from os.path import join, getsize

import scipy as sp 
import numpy as np
import csv
import pandas as pd


path = {}
data1 = {}

'''
# to get the files of the directory 
for root, dirs, files in os.walk("./Data/Session Activity Data/"):
	print len(files)
	
    
for i in range(0 , 60) :
	path[i] = files[i]
	print(path[i])

for i in range(0,60) :
	print i 
	if i!=22 :
	    data[i] = pd.read_csv("./Data/Session Activity Data/" + path[i] , sep = ',' )
	    path[i] =  path[i][:-4]   # to remove last 4 char : .csv
	    data[i]['Event'] = path[i]


for i in range(0,60) :
	if i!=22 :
          data[i].to_csv("./Data/process/" + path[i]  + ".csv" , sep = ',' )	    


for i in range(0,60) :
	if i!=22 :
	    data1[i] = pd.read_csv("./Data/process/" + path[i] + ".csv" , sep = ',' )


	#result = data1[0].append(data1[1] )
	result = data1[0]
for i in range(1,60) :
	if i != 22 :
          result = result.append(data1[i] , ignore_index = True)  


result.to_csv("./Data/process/FINAL.csv" , sep = ',' )

final = pd.read_csv("./Data/process/FINAL.csv" , sep = ',' )
final = final[pd.notnull(final['Badge ID'])]

final["Address Line"] = final["Address Line 1"].map(str) + " " + final["Address Line 2"].map(str)
final["Badge Name"] = final["Name Badge First Name"].map(str) + " " + final["Name Badge Last Name"].map(str)
final["Name"] = final["First Name"].map(str) + " " + final["Last Name"].map(str)
final.to_csv("./Data/xxx_old.csv" , sep = ',' )

'''
## processing done till here 
'''
1. Explain the understannding from deleted columns
2. Algo to verify email 
3. Algo to remove Others from Field ... use of @ depicting others
'''

# dataset = pd.read_csv("./Data/session.csv")

'''
for i in range(0,6969) :
	if(pd.isnull(dataset['Verify Email Address'][i])==0) & (pd.isnull(dataset['Email Address'][i])==0):
         if(dataset['Email Address'][i] != dataset['Verify Email Address'][i]) :
         	if(dataset['Email Address'][i] == dataset['CC Email'][i]) :
         		dataset['Verify Email Address'][i] , dataset['CC Email'][i] = dataset['CC Email'][i] , dataset['Verify Email Address'][i]
         	else :
         		print(i)
'''

'''
for i in range(0,6969) :
	if(pd.isnull(dataset['What is your role? Conditional'][i])==0) :
		 dataset['What is your role?'][i] = "@ " + dataset['What is your role? Conditional'][i]
	if(pd.isnull(dataset['Which department do you work for? Conditional'][i])==0) :
		 dataset['Which department do you work for?'][i] = "@ " + dataset['Which department do you work for? Conditional'][i]		 
	if(pd.isnull(dataset['Which industry do you work in? Conditional'][i])==0) :
		 dataset['Which industry do you work in?'][i] = "@ " + dataset['Which industry do you work in? Conditional'][i]
'''

'''dataset['UID'] = dataset['Badge Name'].map(str) + " " + dataset['Email Address'].map(str)'''

'''
words = []
 		data = pd.read_csv("./Data/session.csv")
 		data['First Name'] = "nan"
 		data['Second Name'] = "nan"
 		for i in range (0,6969) :
 			words = data['Name'][i].split(" ");
 			data['First Name'][i] = words[0]
 			data['Second Name'][i] = words[1]
 		
 		
 		data.to_csv("./Data/session.csv")        
''' 		
'''
for i in range(0,6969) :
	if (pd.isnull(data['How often do you use the OSIsoft PI System products?'][i])!=0) :
         data['How often do you use the OSIsoft PI System products?'][i] = data['How often do you use the OSIsoft PI System products?.1'][i]
   	if (pd.isnull(data['Business Phone'][i])!=0) :
		data['Business Phone'][i] = data['Mobile Phone'][i]	
	if (pd.isnull(data['Email Address'][i])!=0) :
		data['Email Address'][i] = data['CC Email'][i]	
	if (pd.isnull(data['Are you attending the Multi Themed Parties on Wednesday, March 26?'][i])!=0) :
		data['Are you attending the Multi Themed Parties on Wednesday, March 26?'][i] = data['Are you attending the Multi Themed Parties on Wednesday, March 26?*'][i]	
	if (pd.isnull(data['Are you attending the Partner Meeting on Thursday, March 27?'][i])!=0) :
          data['Are you attending the Partner Meeting on Thursday, March 27?'][i] = data['Are you attending the Partner Meeting on Thursday, March 27?.1'][i]			 
    
    '''
'''   
for root, dirs, files in os.walk("./Data/Session Activity Data/"):
	print len(files)
	
    
for i in range(0 , 60) :
	path[i] = files[i][:-4]
	print(path[i])

data = pd.read_csv("./Data/session1.csv")
for i in range(0,60) :
	if(i != 22) :
		data[path[i]] = 0

for i in range(0,6969) :
	for j in range(i , 6969) :
		if(data["AAA_ID"][i] == data["AAA_ID"][j]) :
			str = data["Session"][j]
			for k in range(0,60) :
				if(k!=22) :
				      if(str == path[k]) :
				        	data[str][i] = 1
				         	break
		else :
		     i = j-1 
		     break
		if(i != j) :
		       data["AAA_ID"][j] = "abcdef" 

data = data[data.AAA_ID != "abcdef"]

data.to_csv("./Data/session_trans.csv")
'''
data = pd.read_csv("./Data/session_trans.csv")
data.to_csv("./Data/session_trans1.csv")