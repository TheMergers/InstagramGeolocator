import hashlib

class Profile:
	def __init__(self, username):
		self.username = username

	def get_username(self):
		return self.username

	def get_agent(self):
		return hashlib.sha256(self.username.encode()).hexdigest()