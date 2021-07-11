# To Do List - Using Dictionaries
def intro_message():
    print("\nHello! This app is for creating a to-do list.\nPlease pay attention to the options below:\n\nPress 1 to Add Task\nPress 2 to Delete Task\nPress 3 to View Tasks\nPress q to quit\n")

def exit_message():
    print("\nYou are now exiting the app.\nThank you for using this tool!")

def add_tasks(title,priority):
    to_do_dic["Title"] = title
    to_do_dic["Priority"] = priority
    to_do_list.append(to_do_dic)


def view_tasks(to_do_list):
    print("\nBelow are your current tasks:\n")
    for index in range(0, len(to_do_list)):
        print(f"{index + 1} - {to_do_list[index]['Title']} - {to_do_list[index]['Priority']}")
    print("\n")

def delete_tasks(to_do_list):
    print("\nTo delete a task, review task list below:\n")
    view_tasks(to_do_list)
    remove_index = (int(input("\nPlease enter the task number that you would like deleted: ")))
    del to_do_list[remove_index - 1]
    print(f"\nBelow is the updated to do list:\n")
    view_tasks(to_do_list)

to_do_list = []
intro_message()


while True:
    user_input = input("Enter your choice: ")
    
    if user_input == "1":
        print("\nTo add a task, provide a brief description, and label its priority.\n")
        to_do_dic = {}
        title = input("Enter your task: ")
        priority = input("Enter the priority: ")
        print("\n")
        add_tasks(title, priority)        
    elif user_input == "2":
        delete_tasks(to_do_list)
    elif user_input == "3":
        view_tasks(to_do_list)
    elif user_input == "q":
        break
    else:
        print("Please enter in one of these values: 1, 2, 3, or q.\n")

exit_message()