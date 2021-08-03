import requests
import folium

API_KEY = "YOUR_API_KEY"
basemap = "https://1.base.maps.ls.hereapi.com/maptile/2.1/maptile/newest/normal.day/{z}/{x}/{y}/256/png8"

m = folium.Map(
      location=[55.7477, 37.62189], 
      zoom_start=10,
      tiles= f"{basemap}?apiKey={API_KEY}",
      attr='HERE'
    )

def getWeather(lat, lon, apiKey):
  """
  Get weather conditions by coordinates.
  
  Documentation of Weather API: 
  https://developer.here.com/documentation/examples/rest/auto_weather/weather-observation-lat-long
  """

  weather_url = "https://weather.ls.hereapi.com/weather/1.0/report.json"

  params = {
      "product": "observation",
      "latitude": lat,
      "longitude": lon,
      "oneobservation": "true",
      "apiKey": apiKey,
  }

  response = requests.get(weather_url, params=params).json()
  temperature = response['observations']['location'][0]['observation'][0]['temperature']
  
  return { "lat": lat, "lon": lon, "temp": temperature }

markerData = getWeather(55.7477, 37.62189, API_KEY)

marker = folium.Marker(
           location=[markerData['lat'], markerData['lon']],
           popup=f"{markerData['temp']}"
         )

marker.add_to(m)

m.save("weather-map.html")
