import googlemaps
from datetime import datetime

gmaps = googlemaps.Client(key='AIzaSyBmOFFysOy7w_51eFwMGA0sKVRiprDnoVo')

# Geocoding an address
geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')
geocode_result
# Look up an address with reverse geocoding
reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))
reverse_geocode_result
# Request directions via public transit
now = datetime.now()
now

directions_result = gmaps.directions("Sydney Town Hall",
                                     "Parramatta, NSW",
                                     mode="transit",
                                     departure_time=now)

directions_result

# Validate an address with address validation
addressvalidation_result =  gmaps.addressvalidation(['1600 Amphitheatre Pk'], 
                                                    regionCode='US',
                                                    locality='Mountain View', 
                                                    enableUspsCass=True)

addressvalidation_result


import geocoder

g = geocoder.ip('me')
print(g.latlng)
