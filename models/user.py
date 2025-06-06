class User:
    def __init__(self,user_name,user_password):
        self.user_name = user_name
        self.__user_password = self._hash_password(user_password)
        
    def _hash_password(self,plain_pw):
        #coloca um hash simples  pra estudo
        import hashlib
        return hashlib.sha256(plain_pw.encode()).hexdigest()
    
    def check_password(self,plain_pw):
        return self._hash_password(plain_pw) == self.__user_password
        
    
    def to_dict(self):
        return {
            "user_name": self.user_name,
            "user_password": self.__user_password
        }
    
    @classmethod     
    def from_dict(cls, data: dict):
        user = cls(data["user_name"], data["user_password"])
        return user
        