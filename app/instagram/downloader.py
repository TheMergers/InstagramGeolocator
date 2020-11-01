import hashlib
import instaloader

def get_user_data(ig_user):
	username = ig_user
	agent = hashlib.sha256(username.encode()).hexdigest()

	loader = instaloader.Instaloader(
		user_agent=agent,
		dirname_pattern="data/" + username,
		download_pictures=False,
		download_videos=False,
		download_video_thumbnails=False,
		download_comments=False,
		compress_json=False,
    		request_timeout=2
	)

	loader.download_profile(profile_name=username)
