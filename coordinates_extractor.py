from geopy.geocoders import Nominatim
import instaloader
import json
import os

#set your own public_profile
public_profile = "YOUR_PUBLIC_PROFILE_HERE"
geolocator = Nominatim(user_agent="personal_user_agent_or_leave_this")

if os.path.exists("coords.txt"):
	os.remove("coords.txt")

coords = open("coords.txt", "a")
path = os.chdir(public_profile)

for filename in os.listdir(os.getcwd()):
	data = []
	if filename.endswith(".json"):
		with open(filename, "r") as file:
			data = json.load(file)
		try:
			location_name = data["node"]["location"]["name"];
			location = geolocator.geocode(location_name)
			coords.write("{} {} {}\n".format(location.latitude, location.longitude, location_name))
		except:
			pass
			
coords.close()