import hashlib
import instaloader
from instagram.profile import Profile

def get_user_data(ig_user):
	profile = Profile(ig_user)
	username = profile.get_username()
	agent = profile.get_agent()

	loader = instaloader.Instaloader(
		user_agent=agent,
		dirname_pattern="app/data/" + username,
		download_pictures=False,
		download_videos=False,
		download_video_thumbnails=False,
		download_comments=False,
		compress_json=False,
    	request_timeout=2
	)

	loader.download_profile(profile_name=username)
