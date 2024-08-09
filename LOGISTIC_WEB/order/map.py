import googlemaps
from datetime import datetime
from datetime import datetime

gmaps = googlemaps.Client(key='AIzaSyCylRnlEZdmLKjm1NzXZ5nO4RzvyNifhpk')

# Find place
def find_location_place(location):
    find_place = gmaps.find_place(input=location,input_type='textquery')['candidates'][0]['place_id']
    place_info = geocode_result = gmaps.geocode(place_id=find_place)
    place_location = place_info[0]['geometry']['location']
    
    lat = place_location['lat']
    lng = place_location['lng']

    return lat,lng

# Calcualte Distance

def distance_calculate(receiving_location,destination_location):
    distance_json = gmaps.distance_matrix(origins=receiving_location,
                                    destinations=destination_location,
                                    mode='driving',
                                    departure_time=datetime.now(),
                                    traffic_model='best_guess',
                                    region='tr'
                                    )
    distance = distance_json['rows'][0]['elements'][0]['distance'] # meter
    duration = distance_json['rows'][0]['elements'][0]['duration'] # second

    print(distance)
    print(duration)

"""

# Geocoding an address
geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')
#print(geocode_result[0]['address_components'][0]['long_name'])

# Look up an address with reverse geocoding
reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))
#print(reverse_geocode_result)

# Request directions via public transit
now = datetime.now()
directions_result = gmaps.directions("Sydney Town Hall",
                                     "Parramatta, NSW",
                                     mode="transit",
                                     departure_time=now)


# Validate an address with address validation
addressvalidation_result =  gmaps.addressvalidation(['1600 Amphitheatre Pk'], 
                                                    regionCode='US',
                                                    locality='Mountain View', 
                                                    enableUspsCass=True)

"""