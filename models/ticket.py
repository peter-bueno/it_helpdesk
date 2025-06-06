from uuid import uuid4
from utils.formatter import current_timestamp
from utils import DEFAULT_TICKET_STATUS,TICKET_STATUS_RESOLVED


class Ticket:
    def __init__(self, title, description):
        self.__ticket_id = str(uuid4())
        self.__title = title
        self.__description = description
        self.__status = DEFAULT_TICKET_STATUS
        self.__created_at = current_timestamp()
          

    def get_id(self):
        return self.__ticket_id
    
    def resolve(self):
        self.__status = TICKET_STATUS_RESOLVED
        
    @property
    def get_title(self):
        return self.__title
    @property
    def get_description(self):
        return self.__description
    @property
    def get_status(self):
        return self.__status
    @property
    def get_created_at(self):
        return self.__created_at

     
    def to_dict(self):
            return {
                "id": self.__ticket_id,
                "title": self.__title,
                "description": self.__description,
                "status": self.__status,
                "created_at": self.__created_at
            }
        
    @classmethod     
    def from_dict(cls, data: dict):
        ticket = cls(data["title"], data["description"])
        ticket.__ticket_id = data["id"]
        ticket.__status = data["status"]
        ticket.__created_at = data["created_at"]
        return ticket