

def add_to_list():
    item = input("What do you want to add to the list? ")
    f = open('shopping_list', 'a')
    f.write(item + ",")
    f.close()




def show_items():
    f = open("shopping_list", 'r')
    data = f.read()
    items = data.split(",")
    count = 1
    print(items)

    for item in items:
        if item != "":
            print(f"{count}, {item}")
            count += 1
        
    f.close



def main():

    while True:


        print("""
        Type A to add item to the list
        Tyte B to view the content of the list 
        Type C to exit the program
        """)


        option = input("Type option A, B or C: " )


        if option.lower() == "a":
            add_to_list()


        if option.lower() == "b":
            show_items()


        if option.lower() == "c":
            break


main()