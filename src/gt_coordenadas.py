from geopy.geocoders import Nominatim
from geopy.point import Point
import requests
import json


def detect_coor():
    with open('data/secreto/secretos.json') as f:
        dk = json.load(f)
    rec = requests.post(f"https://www.googleapis.com/geolocation/v1/geolocate?key={dk['Api']}")
    print(rec)
    coor = [rec.json()['location']['lat'] , rec.json()['location']['lng']]
    return coor
###################

