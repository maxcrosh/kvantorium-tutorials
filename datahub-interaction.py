"""
This file contains basic examples of how to interact with HERE Data Hub API - https://www.here.xyz/api/

Complete list of REST API methods could be found here:
 - ReDoc: https://xyz.api.here.com/hub/static/redoc/index.html
 - SwaggerUI: https://xyz.api.here.com/hub/static/swagger/index.html
 
Documentation of Data Hub on official developer portal: 
  https://developer.here.com/documentation/data-hub/dev_guide/index.html
"""

import requests
import json
import folium

DATA_HUB_SERVICE = "https://xyz.api.here.com/hub"
ACCESS_TOKEN = "DATA_HUB_ACCESS_TOKEN"

def get_spaces(access_token=None):
  """
  Get list of spaces in account.
  """
  params = {
      "access_token": access_token
  }

  response = requests.get(f'{DATA_HUB_SERVICE}/spaces', params=params)

  return response.json()


def get_space(access_token=None, space_id=None):
  """
  Get information about space by SPACE_ID.
  """
  params = {
      "access_token": access_token
  }

  response = requests.get(f'{DATA_HUB_SERVICE}/spaces/{space_id}', params=params)

  return response.json()


def iterate_space(access_token=None, space_id=None):
  """
  Get all features from space.
  """
  params = {
      "access_token": access_token
  }

  response = requests.get(f'{DATA_HUB_SERVICE}/spaces/{space_id}/iterate', params=params)

  return response.json()


def put_feature(_id, lat, lng, access_token=None, space_id=None):
  """
  Add new feature to space.
  """
  params = {
      "access_token": access_token
  }

  headers = {
      "Content-Type": "application/geo+json"
  }
  
  data = {
    "type": "FeatureCollection",
    "features": [
      {
        "type": "Feature",
        "geometry": {
          "type": "Point",
          "coordinates": [
            lng,
            lat
          ]
        },
        "properties": {
          "name": "Anfield",
          "@ns:com:here:xyz": {
            "createdAt": 1517504700726,
            "updatedAt": 1517504700726,
            "tags": [
              "football",
              "stadium"
            ]
          },
          "amenity": "Football Stadium",
          "capacity": 54074,
          "description": "Home of Liverpool Football Club"
        }
      }
    ]
  }
  
  response = requests.put(f'{DATA_HUB_SERVICE}/spaces/{space_id}/features/{_id}', headers=headers, params=params, data=json.dumps(data))

  return response.json()
