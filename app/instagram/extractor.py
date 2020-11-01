import hashlib
import json
from geopy.geocoders import Nominatim
import os
from profile import Profile

def dump_coordinates(ig_user, coords_path="data/coords.txt"):
	profile = Profile(ig_user)
	username = profile.get_username()
	agent = profile.get_agent()

	geolocator = Nominatim(user_agent=agent)

	coords_path = coords_path

	if os.path.exists(coords_path):
		os.remove(coords_path)

	coords = open(coords_path, "a")
	os.chdir("data/" + username)

	for filename in os.listdir(os.getcwd()):
		data = []
		if filename.endswith(".json"):
			with open(filename, "r") as file:
				data = json.load(file)
			try:
				location_name = data["node"]["location"]["name"]
				location = geolocator.geocode(location_name)
				coords.write("{}\t{}\t\"{}\"\n".format(location.latitude, location.longitude, location_name))
			except:
				pass
				
	coords.close()
