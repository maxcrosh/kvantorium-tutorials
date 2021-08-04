import requests
import geojson

# Base URL for data extraction
URL ="https://avoska.ru/api/get_shops.php?map=1"

# Data extraction function
def get_data (url=None):
    if url is None:
        return False
    
    response = requests.get(URL)

    if response.status_code is 200:
        print("Data successfully extracted")
        return response.json()
    else:
        print("Error while extracting data")
        return False


def save_data (data=None):
    if data is None:
        return False

    with open('avoska.geojson', 'w', encoding='utf-8') as file:
        geojson.dump(data, file, ensure_ascii=False, indent=4)
        return True
    
if __name__ == "__main__":
    data = get_data(url=URL)

    if data:
        result = save_data(data)
        if result:
            print("Data successfully saved")
        else:
