__author__ = 'jmeline'


try:
    import flickrapi
except ImportError as e:
    print(e)

apikey="< api key here >"
secret="< secret key here >"

sampleId=753692

## Example

flickr = flickrapi.FlickrAPI(apikey, secret)
request = flickr.places.getChildrenWithPhotosPublic(woe_id=sampleId)

'''
In [18]: for i in list:
   ....:     if i.attrib['place_type_id']== '22':
   ....:         print(i.attrib['latitude'], i.attrib['longitude'])
   ....:         print(i.text)
   ....:
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
