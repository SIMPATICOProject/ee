import numpy as np
import matplotlib.pyplot as plt
import urllib2
response = urllib2.urlopen("http://192.168.26.187:8080/simpatico/api/logs/find")
html = response.read()
logs=eval(html)["results"]
logslist=map(lambda x: x["data"], logs)

drlist0=[];drlist1=[];drlist2=[];drlist3=[];drlist4=[]
for logdict in logslist:
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
dravlist = map(lambda x: np.mean(x),drlist)
drhistlist = map(lambda x: plt.hist(x),drlist)

#plt.title("Histgram")
#plt.xlabel("x")
#plt.ylabel("frequency")
#plt.show()

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
