import requests
import geocoder

API_BASE_URL = "https://api.darksky.net/forecast/c73c375afbedccd447f98b4e275bb84c/"

destinations = [
  "The Space Needle",
  "Crater Lake",
  "The Golden Gate Bridge",
  "Yosemite National Park",
  "Las Vegas, Nevada",
  "Grand Canyon National Park",
  "Aspen, Colorado",
  "Mount Rushmore",
  "Yellowstone National Park",
  "Sandpoint, Idaho",
  "Banff National Park",
  "Capilano Suspension Bridge"
]

for point in destinations:
  # Get the latitude and longitude from `geocoder`.
  loc = geocoder.arcgis(point)
  full_api_url = API_BASE_URL + {loc.lat} + "," + {loc.lng}
  result = requests.request('GET', full_api_url).json()
  # Print out `geopy`'s results.
  print("{0} is located at ({1:.4f}, {2: .4f})".format(point, loc.latlng[0], loc.latlng[1]))
  print(f'At {point} right now, it is {result["currently"]["summary"]} with a temperature of {result["currently"]["temperature"]:.1f}')


# g = geocoder.arcgis("The Space Needle")
# print(g.latlng) # latlng is a tuple with a length of 2.

# g = geocoder.arcgis('Mountain View, CA', maxRows=1)
# print(g.geojson)
# for result in g:
#   print(result.address, result.latlng, result.currently)