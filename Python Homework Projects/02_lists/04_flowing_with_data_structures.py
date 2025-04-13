def add_three_copies(my_list, data):
   
    for i in range(3):
        my_list.append(data)  # List is mutable, so this change stays

def main():
    message = input("Enter a message to copy: ")  
    my_list = [] 

    print("List before:", my_list)  # Show list before calling the function
    add_three_copies(my_list, message)  # Function modifies the list in-place
    print("List after:", my_list)  # Show list after, to see the effect


if __name__ == '__main__':
    main()
