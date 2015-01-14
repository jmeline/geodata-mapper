__author__ = 'jmeline'

from matplotlib.mlab import griddata
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


try:
    import flickrapi
except ImportError as e:
    print(e)

from geodata.JsonConfigHandler import JsonConfigHandler
from common.termcolor import colored

apikey = None
secret = None

json = JsonConfigHandler()

try:
    apikey = json.extractedObject.apikey
    secret = json.extractedObject.secret
except:
    print("Error! You need to have a valid apikey and secret key to use Flickr")
    import sys

    sys.exit(1)

sampleId = 753692
camasId = 2373510

# # Example
flickr = flickrapi.FlickrAPI(apikey, secret)
request = flickr.places.getChildrenWithPhotosPublic(woe_id=sampleId)
list = request[0].getchildren()
print("length: %s" % len(list))

x = []
y = []
z = []

for item in list:
    if item.attrib['place_type_id'] == '22':
        print("latitude: %s, longitude: %s \n\t-> %s" % (colored(item.attrib['latitude'], "green"), colored(item.attrib['longitude'], "green"), colored(item.text, "blue")))
        x.append(float(item.attrib['latitude']))
        y.append(float(item.attrib['longitude']))
        z.append(int(item.attrib['photo_count']))

#df = pd.DataFrame({'latitude':x, 'longitude':y, 'photo_count':z})

#xmin = df['latitude'].min()
#xmax = df['latitude'].max()
#ymin = df['longitude'].min()
#ymax = df['longitude'].max()

xmin = min(x)
xmax = max(x)
ymin = min(y)
ymax = max(y)



#xmin = min(x)
#xmax = max(x)
#ymin = min(y)
#ymax = max(y)

x += xmin, xmin, xmax, xmax
y += ymin, ymax, ymin, ymax
z += 0, 0, 0, 0,
yrange = ymax - ymin
xrange = xmax - xmin

maxrange = max(xrange, yrange)
stepsize = maxrange/500

# create empty grid
xi = np.linspace(xmin, xmax, int(xrange/stepsize))
yi = np.linspace(ymin, ymax, int(yrange/stepsize))

#grid the data
zi = griddata(x,y,z,xi,yi, interp='linear')
#CS = plt.contour(xi, yi, zi, 15, linewidths=.5, colors='k')
#CS = plt.contour(xi, yi, zi, 15, cmap=plt.cm.jet)
#plt.colorbar()
#plt.scatter(x,y,marker='o', c='b', s=5)
#plt.xlim(xmin, xmax)
#plt.ylim(ymin, ymax)
#plt.title('Barcelona')
#plt.show()


'''
41.380 2.176
Ciutat Vella, Barcelona, Catalonia, ES, Spain
41.393 2.161
L'example, Barcelona, Catalonia, ES, Spain
41.386 2.177
Ribera, Barcelona, Catalonia, ES, Spain
41.383 2.183
Barceloneta, Barcelona, Catalonia, ES, Spain
41.379 2.167
El Raval, Barcelona, Catalonia, ES, Spain
41.406 2.179
La Dreta De L'eixample, Barcelona, Catalonia, ES, Spain
41.414 2.158
El Carmel, Barcelona, Catalonia, ES, Spain
41.365 2.149
Anella Olimpica, Barcelona, Catalonia, ES, Spain
41.363 2.157
Montjuic, Barcelona, Catalonia, ES, Spain
...
'''
