from main import*

# running the app and defining actions
def run():
    action = input("Type:  1 to update 'inventory'\n  2 to start an order \n 3 to add special requirements or order \n 4 to show customer details \n ")
    if action == '2':       
        start_order()      
    elif action == '1':        
        update_items()       
    elif action == '4':   
            #  only employee will be able to see customer details
        show_customer_details()       
    elif action == '3':
        showing_details(data)
        print("What items do you want to add: ")
        add_order()
    else:
        print(f"Invalid option")

run()
