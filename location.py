from geopy.geocoders import Nominatim

def get_location():
    array = []
    geolocator = Nominatim()
    location = geolocator.geocode('Sri City, India')
    print(location.latitude, location.longitude)
    array.append(location.latitude)
    array.append(location.longitude)
    return array
