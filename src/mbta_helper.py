import urllib.request   # urlencode function
import json

# Useful URLs (you need to add the appropriate parameters for your requests)
GMAPS_BASE_URL = "https://maps.googleapis.com/maps/api/geocode/json" #the key
MBTA_BASE_URL = "http://realtime.mbta.com/developer/api/v2/stopsbylocation"
MBTA_DEMO_API_KEY = "wX9NwuHnZU2ToO7GmGR9uw" #public key for MBTA


# A little bit of scaffolding if you want to use it

def get_json(url):
    # """
    # Given a properly formatted URL for a JSON web API request, return
    # a Python JSON object containing the response to that request.
    # """
    f = urllib.request.urlopen(url)
    response_text = f.read().decode('utf-8')
    response_data = json.loads(response_text)
    # print(response_data
    return response_data
####
#
# url_testing = "https://maps.googleapis.com/maps/api/geocode/json?address=Harvard%20University"
#     json = get_json(url)

#
def get_lat_long(place_name):

    """
    Given a place name or address, return a (latitude, longitude) tuple
    with the coordinates of the given place.
    See https://developers.google.com/maps/documentation/geocoding/
    for Google Maps Geocode API URL formatting requirements.
    """
    url = GMAPS_BASE_URL + '?address='+ place_name.replace(' ','%20')
    mydata = get_json(url)
    # from pprint import pprint
    # pprint(mydata)
    latt = mydata['results'][0]['geometry']['location']['lat']
    lgtt = mydata['results'][0]['geometry']['location']['lng']
    return latt, lgtt
    # Given a place name or address, return the nearest MBTA stop and the
    # distance from the given place to that stop.
    # """
#
#
#
# print(mylat, mylng)


def get_nearest_station(mylat, mylng):
    """
    Given latitude and longitude strings, return a (station_name, distance)
    tuple for the nearest MBTA station to the given coordinates.
    See http://realtime.mbta.com/Portal/Home/Documents for URL
    formatting requirements for the 'stopsbylocation' API.
    """
    # print(mylat, mylng)
    mbtaurl = MBTA_BASE_URL+'?api_key='+MBTA_DEMO_API_KEY+'&lat='+str(mylat)+'&lon='+str(mylng)+'&format=json'
    # print(mbtaurl)
    mymbtadata = get_json(mbtaurl)
    #
    # from pprint import pprint
    # pprint(mymbtadata)
    sname = mymbtadata['stop'][0]['stop_name']
    sdist = mymbtadata['stop'][0]['distance']
    return sname, sdist
#
#
def find_stop_near(place_name):
#     """
    mylat=0
    mylng=0
    mylat, mylng = get_lat_long(place_name)
    return get_nearest_station(mylat, mylng)


# stn=0
# dis=0
# place_test='Harvard University'
# stn, dis = find_stop_near(place_test)
# print(stn, dis)
