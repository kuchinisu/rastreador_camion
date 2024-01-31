from geopy.geocoders import Nominatim
from geopy.point import Point

geolocator = Nominatim(user_agent="my_app")
location = geolocator.geocode("me")

location


def detect_coor():
    coor = [0,0]
    return coor
###################

from geopy.geocoders import Nominatim


def get_gps_coordinates(address):
    geolocator = Nominatim(user_agent="uniqueName")
    location = geolocator.geocode(address)
    
    if location:
        latitude = location.latitude
        longitude = location.longitude
        return latitude, longitude
    else:
        return None


if __name__ == "__main__":
    
    address = "me"
    
    coordinates = get_gps_coordinates(address)
    
    if coordinates:
        latitude, longitude = coordinates
        print(f"Latitude: {latitude}, Longitude: {longitude}")
    else:
        print("Location not found.")