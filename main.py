from managers import UserManager,TicketManager

user_manager = UserManager()
ticket_manager = TicketManager()

def ticket_menu():
        while True:
            print("--- Menu de Tickets ---\n")
            print("\n1. Criar novo Ticket\n2. Visualizar Tickets\n3. Resolver Ticket\n4. Sair\n")
            
            ticket_menu_choice = input("Escolha uma opção: ")
            
            if ticket_menu_choice == "1":
                try: 
                    new_ticket_title =  input("\nTitulo do Ticket: ")
                    new_ticket_description =  input("\nDescrição do Ticket: ")
                    created_id = ticket_manager.create_ticket(new_ticket_title,new_ticket_description)
                    print(f"Ticket criado com sucesso. ID: {created_id}")

                          
                except ValueError:
                    print("Dados invalidos.")
            
            elif ticket_menu_choice == "2":
                tickets = ticket_manager.list_all_tickets()
                for ticket in tickets:
                    print(ticket) 
            
            elif ticket_menu_choice == "3":
                try:
                    ticket_manager.list_all_tickets()
                    ticket_id = input("\nDigite o ID do Ticket que seja Resolver: ")
                    resolved_ticked = ticket_manager.resolve_ticket(ticket_id)
                    
                    if resolved_ticked == True:
                        print("\nTicket Resolvido com sucesso.")
                    elif resolved_ticked == False:
                        print("\nID incorreto.")
                    else:
                        print("Não foi possivel resolver esse Ticket.")
                except ValueError:
                         print("Digite um ID valido.\n")
            elif ticket_menu_choice == "4":
                print("Saindo do menu de Tickets...")
                break
        
def user_menu():
    while True:
        
        print("\n1. Acessar\n2. Criar novo usuario\n0. Sair\n\n")
        user_menu_choice = input("Escolha sua opção: ")
        
        if user_menu_choice == "1":
            try: 
                registred_user_name =  input("Digite seu nome de usuario: ")
                registred_user_pass =  input("\nDigite sua senha: ")
                verification = user_manager.authenticate(registred_user_name,registred_user_pass)
                if verification == True:
                    ticket_menu()
                elif verification == False:
                    print("\nDados incorretos.")
                    continue
                else:
                    print("\nDados informados não cadastrados.")
                    continue
            except ValueError:
                print("Senha ou Usuario incorreto.")
        
        elif user_menu_choice == "2":
            try:    
                name = input("\nDigite seu novo nome: ")
                senha = input("\nDigite sua nova senha: ")
                user = user_manager.create_user(name,senha)
                if user:
                    print("Usuario cadastrado com sucesso.")
                    continue
            except ValueError:
                print("\nDigite um valor valido.")
               
        elif user_menu_choice == "0":
            print("Saindo...")
            break 
        
        else:
            print("Digite uma opção valida")

        
if __name__ == "__main__":
                 #Presentation menu
    print("--- Controle Interno de Tickets HELPDESK ---\n")
    user_menu()