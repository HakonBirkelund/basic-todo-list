def add_todo():
    lst, Done = [], False
    while Done == False:
        entry = input("What would you like to add to the todo list?")
        lst.append(entry)
        completed = input("Are you done adding new entries?\nY/N -> ")
        if completed == "Y":
            Done = True
    with open("todo.txt", "a") as f:
        for x in lst:
            f.write(x + '\n')

#def delete_todo(lst:list):
    #with open("todo.txt", "w") as f:
    #    for x in lst:
    #        f.write(x)
    # TODO Add option to delete an item from the list.

def show_todo():
    print("Your todo list:")
    with open("todo.txt", "r") as f:
        output = f.read().splitlines()
        for i in output:
            print("-" + i)


def main():
    Done = False
    while Done == False:
        print("What would you like to do?\
            \nSee todo list -> A\
            \nAdd items to the todo list -> B\
            \nRemove an item from the todo list -> C\
            \nClose todo list -> D")
        choice = input("-> ")
        if choice not in "ABCD":
            print("Invalid option. Please select another.\
                \n-------------------------------------")
        else:
            if choice == "A":
                show_todo()
            elif choice == "B":
                add_todo()
            #elif choice == "C":
            # TODO   delete_todo()
            elif choice == "D":
                print("Thank you for using todo list.\
                    \nI'm proud of your accomplishments!")
                
                Done = True
                return Done
main()    