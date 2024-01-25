from main import*

# running the app and defining actions - Ana & Diti
def run():
    action = input("Type...\n 1 to update 'inventory'\n 2 to start an order \n 3 to add special requirements or order \n 4 to show customer details \n ")
    if action == '2':       
        start_order()      
    elif action == '1':
        yesType = isEmp()
        if(yesType):
            update_items()    
        else:
            print("You do not have access to update menu")   
    elif action == '4':   
            #  only employee will be able to see customer details
        yesType = isEmp()
        if(yesType):
           show_customer_details() 
        else:
            print("You cannot see our customer. You are a user")      
    elif action == '3':
        showing_details(data)
        print("What items do you want to add: ")
        add_order()
    else:
        print(f"Invalid option")

run()
