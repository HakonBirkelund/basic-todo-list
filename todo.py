import json


def separator() -> str:
    """Prints a string of '-' to separate parts of the terminal.

    Returns:
        str: a line made of '-'s
    """
    print("------------------------------------------")


def read_json() -> list:
    """Reads todo.json

    Returns:
        list: A list of all to do tasks.
    """
    with open("todo.json", 'r') as json_file:
        try:
            return json.load(json_file)
        except:
            print("There was an error reading the file.")
# General functions to improve readability of the code.


def add_todo():
    """Adds a task to the to do list.
    """
    entry = input("What would you like to add to the to do list?\n-> ")
    data = read_json()  # Access the file and save as data   |
    data.append(entry)  # Append the new entry to the list   |
    with open("todo.json", "w") as jsonFile:  # Open the JSON|
        json.dump(data, jsonFile)             # Add new task.|
        print("Successfully added new task!")  # Print out. |
    separator()


def delete_todo():
    """Deletes a task from the todo list.

    Returns:
        bool: Returns a False value if the deletion was unsuccessful.
    """
    del_line, data = ".", read_json()       # default del_line, get data \\\
    if data != []:                          # If list isn't empty, print  \\\
        for counter, i in enumerate(data):  # the tasks in it. E.g:        \|
            print(f'{counter} - {i}')       # 0 - Water the plants upstairs |
        while not del_line.isnumeric():     # 1 - Study Python Programming  |
            del_line = input("Which entry do you want to delete?\
                \n(enter a positive, non-existant number to cancel)\n-> ")

        del_line = int(del_line)     # cast the input, meaning no try/except|
        if del_line >= 0 and del_line <= len(data)-1:   # If input is valid |
            data.pop(del_line)        # remove the task the user specified  |
            with open('todo.json', 'w') as json_write:        # Update JSON |
                json.dump(data, json_write)                   # Also, super |
                separator()                                   # cool prints |
                print("Successfully deleted the todo item!")
                separator()
        else:                    # If the input is outside list index range |
            separator()          # Run this block instead and return False  |
            print("There is no such entry, deletion cancelled.")
            separator()
            return False                                  # If all of the   |
    else:                                                 # fails, the todo |
        print("There are no entries in the todo list!")   # list is empty.. |
        return False                                      # Return False    |


def show_todo():
    data = read_json()         # Access the file and save as data \
    if data:                   # If the to do has at least one task\
        print("Your to do list:")  # the whole list will be printed/ 
        for i in data:         # & formatted like this for users: /
            print(f'- {i}')    # - Water the plants upstairs    /
    else:                      # - Study Python programming    /
        print("No tasks on the to do list!")  # <- Print this /
    separator()                # if there weren't any tasks. /


def todo():
    """Starts the to do list program.
    """
    Done = False     # The program will run until |
    while not Done:  # the user ends the program. |
        print("What would you like to do?\
            \nSee to do list -> A\
            \nAdd items to the to do list -> B\
            \nRemove a task from the to do list -> C\
            \nClose to do list -> D")  # D/d will quit it\
        choice = input("-> ")         # Input the choice.|
        if choice not in "AaBbCcDd":  # Check validity. /
            print("Invalid option. Please select another.")
            separator()
        else:
            separator()
            if choice in "Aa":    # This program does not need returns from \
                show_todo()       # the auxiliary functions in order to work.|
            elif choice in "Bb":  # Functions show_todo() & add_todo() don't |
                add_todo()        # have those, but you could implement it if|
            elif choice in "Cc":  # desired. Unlike those two, delete_todo() |
                delete_todo()     # can return False, which can be useful for|
            elif choice in "Dd":  # cases where you may have to find a bug. /
                print("Thank you for using the to do list.\
                    \nI'm proud of your accomplishments!")
                Done = True       # Program is done, change Done to True.
todo()
