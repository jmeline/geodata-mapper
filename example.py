__author__ = 'jmeline'

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

# # Example
flickr = flickrapi.FlickrAPI(apikey, secret)
request = flickr.places.getChildrenWithPhotosPublic(woe_id=sampleId)
list = request[0].getchildren()
print("length: %s" % len(list))
for i in list:
    if i.attrib['place_type_id'] == '22':
        print("latitude: %s, longitude: %s \n\t-> %s" % (colored(i.attrib['latitude'], "green"),
                                                         colored(i.attrib['longitude'], "green"),
                                                         colored(i.text, "blue")))

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
