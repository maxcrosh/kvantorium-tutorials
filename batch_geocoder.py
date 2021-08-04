import requests
from bs4 import BeautifulSoup
import io
import zipfile

SERVICE_URL = "https://batch.geocoder.ls.hereapi.com/6.2/jobs"
API_KEY = "YOUT_API_KEY"
job_id = None

with open('data2geocode.txt', 'rb') as file:
  print(file.read())
 
def start():
  """
  Run batch geocoder.
  Save ID of job for checking status.
  """
  file = open('data2geocode.txt', 'rb')

  params = {
      "action": "run",
      "apiKey": API_KEY,
      "politicalview": "RUS",
      "gen": 9,
      "maxresults": "1",
      "header": "true",
      "indelim": "|",
      "outdelim": ";",
      "outcols": "displayLatitude,displayLongitude,locationLabel,houseNumber,street,district,city,postalCode,county,state,country",
      "outputcombined": "true",
  }

  response = requests.post(SERVICE_URL, params=params, data=file)

  parsedXMLResponse = BeautifulSoup(response.text, "lxml")
  job_id = parsedXMLResponse.find('requestid').get_text()
  print(job_id)
  
  file.close()
  

  
def status(jobId):
  """
  Check job status.
  """
  statusURL = SERVICE_URL + "/" + jobId

  params = {
      "action": "status",
      "apiKey": API_KEY
  }

  response = requests.get(statusURL, params=params)
  print(response.text)
 

def result(job_id):
  """
  Download geocoding results.
  """
  resultURL = f'{SERVICE_URL}/{job_id}/result'

  params = {
      "apiKey": API_KEY
  }

  response = requests.get(resultURL, params=params)

  zipResult = zipfile.ZipFile(io.BytesIO(response.content))
  zipResult.extractall()
  print(response.url)
