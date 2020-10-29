from geopy.geocoders import Nominatim
import instaloader

#set your own public_profile
public_profile = "YOUR_PUBLIC_PROFILE_HERE"
loader = instaloader.Instaloader(
	download_pictures=False,
	download_videos=False,
	download_video_thumbnails=False,
	download_comments=False,
	compress_json=False
	)

loader.download_profile(profile_name=public_profile)
