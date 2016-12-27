import json
import urllib2
import numpy as np

base_url = 'http://192.168.26.187:8080/simpatico/api/analytics/'

########################
def toGoogleChartTimePerTab(list):
	jsondata = {}
	jsondata['type'] = 'time_per_tab'
	jsondata['payload'] = list
	data = json.dumps(jsondata)
	req = urllib2.Request(base_url + 'insert', data, {'Content-Type': 'application/json'})
	f = urllib2.urlopen(req)
	response = f.read()
	f.close()
	print 'Response toGoogleChartTimePerTab: ' + response
########################	
def toGoogleChartDurationFrequency(listArrays):
	# We recibe multiple matrix. The 2 first arrays are from tab 0. for example. array(28, 0), array (7,5) = 28 users spend 7 seconds in tab 0 and 0 users spend 5 second in tab 0
	w, h = 5, 5
	matrix = [[0 for x in range(w)] for y in range(h)] 

	numDoubleArray = len(listArrays)
	numElems = len(listArrays[0][0]) 

	tab = 4

	for i in range(numDoubleArray):
		for j in range(numElems):
			value = listArrays[i][1][j]
			users = listArrays[i][0][j]
			if (value >= 0 and value <= 30):
				matrix[tab][0] += users 
			elif (value > 30 and value <= 60):
				matrix[tab][1] += users 
			elif (value > 60 and value <= 90):
				matrix[tab][2] += users 
			elif (value > 90 and value <= 120):
				matrix[tab][3] += users 
			else:	
				matrix[tab][4] += users	
		tab -= 1		

	# Create array data and convert to python native data type
	arrayJson = []
	arrayJson.append([np.uint32(matrix[4][0]).item(), np.uint32(matrix[4][1]).item(), np.uint32(matrix[4][2]).item(), np.uint32(matrix[4][3]).item(), np.uint32(matrix[4][4]).item()])
	arrayJson.append([np.uint32(matrix[3][0]).item(), np.uint32(matrix[3][1]).item(), np.uint32(matrix[3][2]).item(), np.uint32(matrix[3][3]).item(), np.uint32(matrix[3][4]).item()])
	arrayJson.append([np.uint32(matrix[2][0]).item(), np.uint32(matrix[2][1]).item(), np.uint32(matrix[2][2]).item(), np.uint32(matrix[2][3]).item(), np.uint32(matrix[2][4]).item()])
	arrayJson.append([np.uint32(matrix[1][0]).item(), np.uint32(matrix[1][1]).item(), np.uint32(matrix[1][2]).item(), np.uint32(matrix[1][3]).item(), np.uint32(matrix[1][4]).item()])
	arrayJson.append([np.uint32(matrix[0][0]).item(), np.uint32(matrix[0][1]).item(), np.uint32(matrix[0][2]).item(), np.uint32(matrix[0][3]).item(), np.uint32(matrix[0][4]).item()])

	jsondata = {}
	jsondata['type'] = 'duration_frecuency'
	jsondata['payload'] = arrayJson
	data = json.dumps(jsondata)
	req = urllib2.Request(base_url + 'insert', data, {'Content-Type': 'application/json'})
	f = urllib2.urlopen(req)
	response = f.read()
	f.close()
	print 'Response toGoogleChartDurationFrequency: ' + response
########################	