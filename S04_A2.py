products = []

def read_file():
    f = open("database.txt", "r")
    for line in f:
        result = line.split(",")
        my_dic = {"id" : result[0], "name" : result[1], "price" : result[2], "count" : result[3]}
        products.append(my_dic)
        print(result)
# print(products)        
        
def show_menu():
    print("1- Add")
    print("2- Remove")
    print("3- Search")
    print("4- Edit")
    print("5- Show list")
    print("6- Buy")
    print("7- Exit")
    
    
def name():
    key_name = input("Enter the product name: ")
    New_name = input("Insert new name of the product: ")
    for product in products:
        if product["name"] == key_name:
            product["name"] = New_name
            print(product)
            print("The operation was successful")
            show_list()
            break
            
def price():
    key_price = input("Enter the product price: ")
    New_price = input("Insert new price of the product: ")
    for product in products:
        if product["price"] == key_price:
            product["price"] = key_price
            price(product)
            print("The operation was successful")
            show_list()
            break
    
def count():
    key_count = input("Enter the number of product: ")
    New_count = input("Insert new count of product: ")
    for product in products:
        if product["count"] == key_count:
            product["count"] = New_count
            price(product)
            print("The operation was successful") 
            show_list()
            break

def add():
    id = input("Enter product id: ")
    name = input("Enter product name: ")
    price = input("Enter product price: ")
    count = input("Enter product count: ")
    new_dic = {"id" : id, "name" : name, "price" : price, "count" : count}
    products.append(new_dic)
    # price(products)
    show_list()
def remove():
    key = input("Enter the product key or name: ")
    for product in products:
        if product["id"] == key or product["name"] == key:
            products.remove(product)
            print(products)
            print("The operation was successful")
            show_list()
            break
    else:
        print("Product not found")
def search():
    key = input("Enter your search key: ")
    for product in products:
        if product["id"] == key or product["name"] == key:
            print(product)
            break                                            #agar else ra payin if benevisim 3 bar chap mikonad
    else:
        print("Not found")
        
def edit():
    a = input("what do you want to edit: ")
    print("1- name",
          "2- price: ",
          "3- count: ")
    if a == "1":
        name()
    elif a == "2":
        price()
    if a == "3":
        count()
        
def show_list():
    print("id\tname\tprice\tcount")
    for product in products:
        print(product["id"], product["name"], product["price"], product["count"])
def buy():
    read_file()
    basket = []
    key = input("Enter the id key of name key of the product: ")
    for product in products:
        if product["id"] == key or product["name"] == key:
            print(product)
            number = int(input("How many do wanna purchase? : "))
            count = int(product["count"])
            price = int(product["price"])
            print(price)
            print(count)
            if count == 0:
                price("Unavailable")
                break
            if number > count:
                print("The number of products requested is more than the stock")
                break
            else:
                print("available")
                
                b = input("Do you wanna purchase or not yes or no: ")
                if b == "yes"or "y":
                    Total_price = number * price
                    print("The operation was successful", "\nTotal price is: ", Total_price)
                    basket.append(product["name"])
                    basket.append(count)
                    basket.append(Total_price)
                    print(basket)
                    show_list()
                    break
            
def save_to_database():
    c = input("Do wanna save the file yes or no:")
    if c == "yes":
        f = open("database.txt", "a")
        for product in products:
            f.write(str(product))
            f.write("")
        print(product)
    else:
        print("Not saved")
read_file() 
while True:
    show_menu()


    user_choice = input("Enter your choice: ")

    if user_choice == "1":
        add()
    elif user_choice == "2":
        remove()
    elif user_choice == "3":
        search()
    elif user_choice == "4":
        edit()
    elif user_choice == "5":
        show_list()
    elif user_choice == "6":
        buy()
    elif user_choice == "7":
        save_to_database()
        exit(0)
    else:
        print("Please enter another choice: ")
