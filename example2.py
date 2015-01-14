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

## Example 2
out = open("bath.csv", "w")
woeid = 12056
geolist = []
flickr = flickrapi.FlickrAPI(apikey, secret)
#request = flickr.interestingness_getList(extras='geo', per_page=500)
request = flickr.photos_search(woe_id=woeid, per_page=250)
foo = request.getchildren()
pages = int(foo[0].items()[3][1])
print (pages)
for i in range(1, pages + 1):
    try:
        request = flickr.photos_search(woe_id=woeid, extras='geo', per_page=250, page=i)
        foo = request.getchildren()
        bar = foo[0].getchildren()

        ## Bar is now a list of photo elements
        print ("attempt" + str(i))

        for pic in bar:
            if(int(pic.attrib['accuracy']))>14:
                lat=(float(pic.attrib['latitude']))
                lon = (float(pic.attrib['longitude']))
                if (lat,lon) != (0.0, 0.0):
                    out.writelines(str(lat)+','+str(lon)+'\n')
    except Exception as e:
        print('skipped' + str(i) + str(e))
out.close