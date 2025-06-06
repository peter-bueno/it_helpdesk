from models import Ticket
from utils import save_json, load_json 
import os
from utils.formatter import friendly_print_ticket#utilizar para mostrar ticket 

class TicketManager:
    def __init__(self):
        self.__tickets = {}
        self.__file_path = os.path.join("data", "tickets.json")
        self.load_tickets()
    
    #cria ticket
    def create_ticket(self,title,description):
        new_ticket = Ticket(title,description)
        self.__tickets[new_ticket.get_id()] = new_ticket
        self.save_tickets()
        return new_ticket.get_id()
    
    #lista tickets
    def list_all_tickets(self):
        return [ticket.to_dict() for ticket in self.__tickets.values()]
    
    #resolve tickets
    def resolve_ticket(self,ticket_id):
        ticket = self.__tickets.get(ticket_id)
        if ticket:
            ticket.resolve()
            self.save_tickets()
            return True
        return False
    
    #salva tickets em json
    def save_tickets(self):
        raw_data = {ticket_id: ticket_value.to_dict() for ticket_id, ticket_value in self.__tickets.items()} 
        save_json(self.__file_path, raw_data)
    
    #carrega tickets do json salvo  
    def load_tickets(self):
        data = load_json(self.__file_path)
        for ticket_id, ticket_data in data.items():
            ticket = Ticket.from_dict(ticket_data)
            self.__tickets[ticket_id] = ticket         



    
    
    
