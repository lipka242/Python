objFile = open("todo.txt","r")
print(objFile.readline())
print(objFile.readline())

dicRow0 = {"Task": "Clean house", "Priority":"low"}
dicRow1 = {"Task": "Pay bills", "Priority":"high"}
lstTable = [dicRow0,dicRow1]
print(lstTable)

print ("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
print()

Todo = ("clean house",
        "pay bills:")
if(strChoice == '1'):
    print("Your todo:")
    for item in Todo:
        print(item)

if(strChoice == '2'):
    strT = input("Enter a new task: ")
    strP = input("Enter priority: ")
    dicNewRow = {"Task": strT, "Priority": strP}
    lstTable.append(dicNewRow)
    print(lstTable)

if(strChoice == '3'):
    strR = str(input("Choose task to delete [1 or 2] - "))
    if str(input == '1'):
        lstTable.remove(dicRow0)
        print(lstTable)
    elif str(input == '2'):
        lstTable.remove(dicRow1)
        print(lstTable)

if(strChoice == '4'):
    strSaveToFIle = input('Save to file? (y)')
    if (strSaveToFIle.lower() == 'y'):
        objFile = open('Todo.txt', 'w')
        for row in lstTable:
            objFile.write(str(row))
        print("Data saved!")

if(strChoice == '5'):
    print(input("Press enter to exit"))