import hashlib
import instaloader

#set your own username
username = "YOUR_USERNAME"
agent = hashlib.sha256(username.encode()).hexdigest()

loader = instaloader.Instaloader(
	user_agent=agent,
	dirname_pattern="data/" + username,
	download_pictures=False,
	download_videos=False,
	download_video_thumbnails=False,
	download_comments=False,
	compress_json=False
	)

loader.download_profile(profile_name=username)
