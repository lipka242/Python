#Creata an application that uses a two dimensional tuple to hold the following data

tplHeader = "ID", "Name", "Email"
tplRow1 = 1, "Bob Smith", "Bsmith@Hotamil.com"
tplRow2 = 2, "Sue Jones", "SueJ@Yahoo.com"
tplRow3 = 3, "Joe James", "JoeJames@gmail.com"

tplTable = (tplRow1, tplRow2, tplRow3)
print(tplTable)

# Create a for loop that prints out each row of the data as follows
print(tplHeader) # change to (str(tplHeader).strip("(").strip(")"))
for row in tplTable:
    print(row)
    for item in row: # Now add a nested for loop to extract the individual elements (colums) data and display as follows.
        print(item)
