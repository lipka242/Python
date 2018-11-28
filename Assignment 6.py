#load the any data you have in a text file called ToDo.txt
objFile = open("ToDo.txt","r")
print(objFile.readline())
print(objFile.readline())
objFile.close()

dicRow0 = {"Task": "Clean house", "Priority":"low"}
dicRow1 = {"Task": "Pay bills", "Priority":"high"}
lstTable = [dicRow0,dicRow1]

#Display a menu of choices to the user
while(True):
    def menuoptions():
        print("""
        Menu of Options
        1) Show current data
        2) Add a new item.
        3) Remove an existing item.
        4) Save Data to File
        5) Exit Program
        """)

# Display all todo items to user
    def ToDo(lstTable):
        print("Here's your ToDo list: " "clean house, " "pay bills ")

# Add a new item to the list/table
    def add():
        input("What to add:? ")

# Remove an item from the list/table
    def remove():
       input("Choose task to delete [1 or 2] - ")

# Save tasks to the todo.txt file
    def question():
        input('Save to file? (y)')

# Exit program
    def exit():
        print(input("Press enter to exit"))

    #main
    menuoptions()
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))

    if (strChoice == '1'):
        ToDo(lstTable)
        continue

    if (strChoice == '2'):
        #add()
        strT = input("Enter a new task: ")
        strP = input("Enter priority: ")
        dicNewRow = {"Task": strT, "Priority": strP}
        lstTable.append(dicNewRow)
        print(lstTable)
        continue

    if (strChoice == '3'):
        remove()
        if str(input == '1'):
            lstTable.remove(dicRow0)
            print(lstTable)
        #elif str(input == '2'):
        #    lstTable.remove(dicRow1)
        #    print(lstTable)
        continue

    if (strChoice == '4'):
        question()
        objFile = open('Todo.txt', 'w')
        for row in lstTable:
            objFile.write(str(row))
        print("Data saved!")
        continue

    if (strChoice == '5'):
        exit()
        break