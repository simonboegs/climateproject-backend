import json
import requests
with open('data/cityIndex.json','r') as f:
    cityIndex = json.load(f)

def getResults(coords):
    #in the frontend we will check if certain elements exist (eg check if hurricanes are supposed to show up on the west coast)
    #this method will return a dict with keys as elements that are to be shown
    
    #revision: some states have some hurricanes but none in the past 100 years. Because our numbers won't return anything
    #for a state like that, we should decide later whether to display it or not based on the future results.
    
    results = {}
    results['temperature'] = getTemperatureResults(coords)
    return results


def getTemperatureResults(coords):
    with open('data/heat.json','r') as f:
        heat = json.load(f)
    exLat = '37.760655'
    exLon = '-122.244884'
    radius = '200'
    s = 'http://api.geonames.org/findNearbyPlaceNameJSON?lat=' + coords['latitude'] + '&lng=' + coords['longitude'] + '&radius=' + radius + '&cities=cities15000&maxRows=30&username=simonboegs' 
    res = requests.get(s)
    data = res.json()
    for place in data['geonames']:
        city = place['toponymName']
        print(city)
        if city in heat:
            break
    ans = {
            'historical': heat[city]['historical'],
            'future': heat[city]['future']
            }
    return ans

def getFloodStats(coords):
    s = 'http://api.geonames.org/findNearbyPlaceNameJSON?lat=' + coords['latitude'] + '&lng=' + coords['longitude'] + '&radius=' + radius + '&cities=cities15000&maxRows=30&username=simonboegs'
    res = requests.get(s)
    data = res.json()
    for place in data['geonames']:
        city = place['toponymName']
        if city in cityIndex:
            county = cityIndex[city]['county']
    
