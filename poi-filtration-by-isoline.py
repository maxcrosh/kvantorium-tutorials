import requests
from shapely.geometry import Polygon, Point
import flexpolyline

API_KEY = "YOUR_API_KEY"
PLACES_ENDPOINT = "https://browse.search.hereapi.com/v1/browse"
ISOLINE_ENDPOINT = "https://isoline.router.hereapi.com/v8/isolines"

def get_place():
  params = {
    'apiKey': API_KEY, 
    'at': '52.5308,13.3856',
    'limit': 100
  }

  response_places = requests.get(ENDPOINT, params=params)
  return response_places.json()


def get_isoline():
  isoline_params = {
      'apiKey': API_KEY, 
      'origin': '52.5308,13.3856',
      'range[type]': 'time',
      'range[values]': 120,
      'transportMode': 'pedestrian'
  }

  response_isoline = requests.get(ISOLINE_ENDPOINT, params=isoline_params).json()
  isoline = Polygon(flexpolyline.decode(response_isoline['isolines'][0]['polygons'][0]['outer']))
  return isoline

def filter_places ():
  for place in places:
    marker = Point(place['lat'], place['lng'])
    isInsidePolygon = isoline.contains(marker)

    if isInsidePolygon:
      yield place
      
if "__name__" == "__main__":
  isoline = get_isoline()
  places = [{'title': place['title'], 'lat': place['position']['lat'], 'lng': place['position']['lng']} for place in get_place()['items']]
  print(list(filter_places()))
