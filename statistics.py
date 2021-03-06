import numpy as np
import matplotlib as mpl
mpl.use('Agg')              # Workaround to generating matplotlib graphs without a running X server
import matplotlib.pyplot as plt
import urllib2
import pandas as pd
from transform import toGoogleChartTimePerTab, toGoogleChartDurationFrequency

### VARIABLES ####
ip_simpatico = 'http://localhost:8080'
###


####################
def standardize(x):
    x_copy = np.copy(x)
    z = (x_copy - x_copy.mean()) / x_copy.std()
    return z
####################

#get data from DB
durationdata = urllib2.urlopen(ip_simpatico + "/simpatico/api/logs/find?words=duration")
durationdata = durationdata.read()
drlogs=eval(durationdata)["results"]
drlogslist=map(lambda x: x["data"], drlogs)

#duration per each tab
drlist0=[];drlist1=[];drlist2=[];drlist3=[];drlist4=[]
for logdict in drlogslist:
    if logdict["type"]==0:
        drlist0.append(logdict["duration"])
    elif logdict["type"]==1:
        drlist1.append(logdict["duration"])
    elif logdict["type"]==2:
        drlist2.append(logdict["duration"])
    elif logdict["type"]==3:
        drlist3.append(logdict["duration"])
    elif logdict["type"]==4:
        drlist4.append(logdict["duration"])

drlist = [drlist0,drlist1,drlist2,drlist3,drlist4]
#duration mean
dravlist = map(lambda x: np.mean(x),drlist)  #--> output
#duration histgram
drhistlist = map(lambda x: plt.hist(x),drlist)  #--> output

# insert to elastic search
toGoogleChartTimePerTab(dravlist, ip_simpatico)
toGoogleChartDurationFrequency(drhistlist, ip_simpatico)

#plt.title("Histgram") 
#plt.xlabel("x")
#plt.ylabel("frequency")
#plt.show()

'''
#kmean using duration time and number of click
tmpdict={}
for logdict in drlogslist:
    if logdict["serial"] in tmpdict.keys():
        tmpdict[logdict["serial"]]["duration"] += logdict["duration"]
        tmpdict[logdict["serial"]]["clicknum"] += 1
    else:   
        tmpdict[logdict["serial"]]={"duration":logdict["duration"], "clicknum":1}

durlist = []; clnlist = []
for key in tmpdict.keys():
    tmpdict[key]["duration"] = tmpdict[key]["duration"]/tmpdict[key]["clicknum"]
    durlist.append(tmpdict[key]["duration"])
    clnlist.append(tmpdict[key]["clicknum"])

durlist_z = standardize(durlist)
clnlist_z = standardize(clnlist)

data_for_kmean = np.array([durlist_z, clnlist_z],np.int32)
data_for_kmean = data_for_kmean.T
pred = KMeans(n_clusters=3).fit_predict(data_for_kmean)
kmlist=list(pred)

for i in range(0,len(tmpdict.keys())):
    key = tmpdict.keys()[i]
    tmpdict[key]["kmclass"]=kmlist[i]

kmdict = tmpdict #--> output

#
#import json
#
#data = {
#}
#
#req = urllib2.Request('http://example.com/api/posts/create')
#req.add_header('Content-Type', 'application/json')
#
#response = urllib2.urlopen(req, json.dumps(data))
'''
