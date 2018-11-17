# Create an script that uses a two-dimensional tuple to hold the following data
# Add code that searches for customers by name and returns a customer Id.

tplHeader = "ID", "Name", "Email"
tplRow1 = 1, "Bob Smith", "Bsmith@Hotamil.com"
tplRow2 = 2, "Sue Jones", "SueJ@Yahoo.com"
tplRow3 = 3, "Joe James", "JoeJames@gmail.com"

tplTable = (tplRow1, tplRow2, tplRow3)
#print(tplTable)

# Add code that searches for customers by name and returns a customer id
strCustomerName = input("Enter a Customer Name: ")
for row in tplTable:
    if(strCustomerName in row):
        print(row[0])