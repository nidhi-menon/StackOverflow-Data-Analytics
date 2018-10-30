# Get ids from csv

# #iterate over 

# API call
# "https://api.stackexchange.com/2.2/posts/"+i+"?order=desc&sort=activity&site=stackoverflow&filter=!9YdnSG37y"

# parse JSON response
# extract body

import requests
import numpy as np
# api-endpoint
import csv
question=[]
#************** +++++++++ ************** 
#************** read from answers.csv only unique occurrences of QID store it to uniqueQid.csv ************** 
# with open('answers.csv') as csvDataFile:
# 	csvReader = csv.reader(csvDataFile)
# 	for row in csvReader:
# 		question.append(row[0])
# question=np.array(question)
# unique_items= np.unique(question[:]) #for a given feature column, finds occurences of string
# final_val=unique_items.tolist()

# writer = csv.writer(open("uniqueQid.csv", 'wb'),delimiter=',', lineterminator='\n')
# writer.writerow(final_val)


#************** +++++++++ ************** 
# read from uniqueQid.csv and get body using request
final_val=[]
with open('uniqueQid.csv') as csvDataFile:
	csvReader = csv.reader(csvDataFile)
	for row in csvReader:
		for col in row:
			final_val.append(col)

# print final_val
# i=563366
start=0
end=2000
writer1 = csv.writer(open("output"+str(start)+"_"+str(end)+".csv", 'wb'),delimiter=',', lineterminator='\n')
writer2 = csv.writer(open("empty.csv", 'wb'),delimiter=',', lineterminator='\n')
# text=[]
# emptyQ=[]
for i in range(start,end):
	print final_val[i]
	textInner=[]
	key1="CeulhyxEeq*DnWwdaOj6NQ(("
	key2="*sBegB5YQ6Q813Wjnmv)ow(("
	URL = "https://api.stackexchange.com/2.2/posts/"+final_val[i]+"?order=desc&sort=activity&site=stackoverflow&filter=!9YdnSG37y&key="+key2

# # sending get request and saving the response as response object
	r = requests.get(url = URL)

# # extracting data in json format
	data = r.json()
	# print final_val[i]
	try:
		textItem = data['items'][0]['body']
	except Exception as e:
		print 'error',data
		# break
		# exit()
		# emptyQ.append(final_val[i])
		writer2.writerow(final_val[i])
		continue
	
	# print textItem

	textInner.append(final_val[i])
	textInner.append(textItem)
	writer1.writerow([textInner[0].encode("utf-8"), textInner[1].encode("utf-8")])
	# text.append(textInner)

#configure writer to write standard csv file

# writer.writerow(['number', 'text', 'number'])
# for item in text:
        #Write item to outcsv
        # writer.writerow([item[0].encode("utf-8"), item[1].encode("utf-8")])
# writer.writerow(text)

# writer.writerow(emptyQ)
# # extracting latitude, longitude and formatted address 
# # of the first matching location
# # latitude = data['results'][0]['geometry']['location']['lat']
# # longitude = data['results'][0]['geometry']['location']['lng']
# # formatted_address = data['results'][0]['formatted_address']

# # printing the output
# print(data)