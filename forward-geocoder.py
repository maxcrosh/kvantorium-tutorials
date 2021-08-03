import requests

# Get API_KEY on https://developer.here.com
API_KEY = "YOUR_API_KEY"

def geocode(text, apiKey=None):

  if apiKey is None:
    raise Exception("Argument apiKey is required!!!")

  # Geocoding endpoint
  base_url = 'https://geocode.search.hereapi.com/v1/geocode'
  
  # Request parameters
  params = {
      "q": text,
      "apiKey": apiKey
  }
  
  # Request to geocoding service
  data = requests.get(base_url, params=params).json()

  return data

result = geocode('Москва', apiKey=API_KEY)
print(result)
