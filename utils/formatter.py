from datetime import datetime

#altenative to print ticket
def friendly_print_ticket(ticket):
    print(f"[{ticket['id']}] {ticket['title']} - {ticket['status']} @ {ticket['created_at']}")
    
    
def current_timestamp():
    return datetime.now().replace(microsecond=0).isoformat()