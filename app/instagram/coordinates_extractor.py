import hashlib
import json
from geopy.geocoders import Nominatim
import os

#set your own username
username = "YOUR_USERNAME"
agent = hashlib.sha256(username.encode()).hexdigest()
geolocator = Nominatim(user_agent=agent)
coords_path = "data/coords.txt"

if os.path.exists(coords_path):
	os.remove(coords_path)

coords = open(coords_path, "a")
path = os.chdir("data/" + username)

for filename in os.listdir(os.getcwd()):
	data = []
	if filename.endswith(".json"):
		with open(filename, "r") as file:
			data = json.load(file)
		try:
			location_name = data["node"]["location"]["name"]
			location = geolocator.geocode(location_name)
			coords.write("{} {} {}\n".format(location.latitude, location.longitude, location_name))
		except:
			pass
			
coords.close()
