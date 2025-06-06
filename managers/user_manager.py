from utils.storage import save_json, load_json
from models import User
import json
import os


class UserManager:
    def __init__(self):
        self.__users = {}
        self.__file_path = os.path.join("data", "users.json")
        self.load_users()
        
    def create_user(self,user_name, user_password):
        if user_name in self.__users:
            raise ValueError("User already exists.")
        self.__users[user_name] = User(user_name,user_password)
        
    
    def authenticate(self,user_name, user_password):
            user = self.__users.get(user_name)#busca nome do usuario do dicionario
            if user and user.check_password(user_password):#verifica se o usuario e a senha sao verdadeiras
                return True
            return False
        
    #salva users em json
    def save_users(self):
        raw_user_data = {
            user_name: user_value.to_dict()
            for user_name, user_value in self.__users.items()
        } 
        save_json(self.__file_path, raw_user_data)
    
    #carrega users de json salvo  
    def load_users(self):
        data = load_json(self.__file_path)
        for user_name, user_data in data.items():
            user = User.from_dict(user_data)
            self.__users[user_name] = user