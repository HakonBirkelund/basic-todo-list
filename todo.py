import json

def add_todo():
    entry = input("What would you like to add to the todo list?\n-> ")
    with open("todo.json", 'r') as json_file:
        try:
            data = json.load(json_file)
            todo_name = len(data)
        except:
            todo_name = 0
    data[f'{todo_name+1}'] = entry
    with open("todo.json", "w") as jsonFile:
        json.dump(data, jsonFile)
        print("Successfully added todo item!")
        
def delete_todo():
    del_line = "."
    with open("todo.json", 'r') as json_file:
        data = json.load(json_file)
    if data != {}:
        print("Todo list items:")
        for i in data:
            print(f'{data[i]} - {i}')
        while del_line.isnumeric() == False:
            del_line = input("Which entry do you want to delete ?\n-> ")
            try:
                if del_line in data[del_line]:
                    del data[del_line]
            except:
                print("There is no such entry!")
        with open('todo.json', 'w') as json_file:
            json.dump(data, json_file)
            print("Successfully deleted the todo item!")
    else:
        print("No items to delete!")
    
def show_todo():
    with open("todo.json") as f:
        items = json.load(f)
        if items:
            print("Your todo list:")
            for i in items:
                print(f'{items[i]}')
        else:
            print("No items on the todo list!")
        
def todo():
    Done = False
    while Done == False:
        print("What would you like to do?\nSee todo list -> A\nAdd items to the todo list -> B\
            \nRemove an item from the todo list -> C\nClose todo list -> D")
        choice = input("-> ")
        if choice not in "AaBbCcDd":
            print("Invalid option. Please select another.\
                \n-------------------------------------")
        else:
            if choice in "Aa":
                show_todo()
            elif choice in "Bb":
                add_todo()
            elif choice in "Cc":
                delete_todo()
            elif choice in "Dd":
                print("Thank you for using todo list.\
                    \nI'm proud of your accomplishments!")
                Done = True
todo()    