from fastapi import FastAPI
from shapely.geometry import Polygon, Point
import flexpolyline
import requests

from config import API_KEY, PLACES_ENDPOINT, ISOLINE_ENDPOINT

app = FastAPI()

def filter_places (places, isoline):
  for place in places:
    marker = Point(place['lat'], place['lng'])
    isInsidePolygon = isoline.contains(marker)

    if isInsidePolygon:
      yield place

@app.get("/")
async def root(lat: float, lng: float, time: int):
    places_params = {
        'apiKey': API_KEY, 
        'at': f'{lat},{lng}',
        'limit': 100
    }
    
    response_places = requests.get(PLACES_ENDPOINT, params=places_params).json()
    places = [{'title': place['title'], 'lat': place['position']['lat'], 'lng': place['position']['lng']} for place in response_places['items']]

    isoline_params = {
        'apiKey': API_KEY, 
        'origin': f'{lat},{lng}',
        'transportMode': 'pedestrian',
        'range[type]': 'time',
        'range[values]': time
    }

    response_isoline = requests.get(ISOLINE_ENDPOINT, params=isoline_params).json()
    isoline = Polygon(flexpolyline.decode(response_isoline['isolines'][0]['polygons'][0]['outer']))

    filtered_places = list(filter_places(places, isoline))

    return {
        "initial_length": len(places),
        "filtered_length": len(filtered_places),
        "filtered_places": filtered_places
    }
