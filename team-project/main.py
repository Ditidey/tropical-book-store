
# data for foods, drinks and best selling books - Enna
data = {
    "books":{
        "name": "book1"
    },
    "food":{
        "name": "food"
    },
    "drinks":{
        "name": "drink"
    }

}
# global variable: for using customer information in others functions - Diti
customerOrderDetails = []

# showing menu and books list - Diti
def showing_details(details):

    for item, values in details.items():
        if( item == "books"):
            print(f"Our best selling {item} here: ")
            print(f" {item.title()} Name: {values['name']}")
        elif(item == "drinks"):
            print(f"Let’s raise a glass to the beginning of Happy Hour and choose your {item}: ")
            print(f" {item.title()} Name: {values['name']}")
        else:
           print(f"Food is the ultimate comfort. All of your favorite {item} here: ")
           print(f" {item.title()} Name: {values['name']}")
   
# showing_details(data)

# these are for user 
           
# taking order from customer: Ana
def get_order():
    choices = input("insert item: ")
    customerOrderDetails.append(choices)
    return choices

# taking customer details: Ana
def get_customer():
    name = input("type your name: ")
    address = input("type your address: ")
    phone = input("type your phone: ")
    customerDetails = {name, address, phone}
    customerOrderDetails.append(customerDetails)
    return customerDetails

# showing completed order to customer: Ana or Richard
def finish_order(items, details="unknown" ):
    print(f"-"*10)
    print(f"{details} Order is completed")
    print(f"Order items: {items}")
    print("Thank you for staying with us")
    # orderDetails = {name, items}
    # return orderDetails
 
#  adding special requirements according to customers - Diti
def add_order():
    addedItems = input("Add items: \n")
    orderDetails = customerOrderDetails.append(addedItems)
    print(f"Order added! You added: {addedItems}")

# starting order from customers and taking data for preferable service - Diti
def start_order():
    print("Do you want to seat here or take away? ")
    service = input("Type your preferable service: here or home\n")

    if(service == 'here'):
        showing_details(data)
        items = get_order()
        print(f"You order - {items}. Thanks!")   
    else:
        showing_details(data)
        items = get_order()
        customerDetails = get_customer()
        # print(customerDetails)
        finish_order(items, customerDetails)

 
# these are for owner 

# updating items: owner can update their menu, books
def update_items():
     item = input("type the new item: ")
     price = input("type the price: ")
     updatedItems = {item: price}
     print(f"Your updated item is {item} and price is {price}")
     data.update(updatedItems)   
     
# showing customer details
def show_customer_details():
    print(customerOrderDetails)
 
