import hashlib

class Profile:
    def init(self,username,agent):
        self._username = username
        self._hashed = hashlib.sha256(username.encode()).hexdigest()
        self._agent = agent

    @property
    def getUsername(self):
        return self._username
    @property
    def hashed(self):
        return self._hashed

profile = Profile("YOUR_USERNAME",self.agent)
