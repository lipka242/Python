# setup data
tplData = ('Item' + ',' + 'Value'), #last comma makes it a tuple
strSaveToFIle = 'n'

# get user input data
strItem = input('Enter an item: ')
strValue = input('Enter Estimated Value: ')
tplData += (strItem + ',' + strValue),

# ASk if they want to save data
strSaveToFIle = input('Save to file? (y/n)')
if(strSaveToFIle.lower() == 'y'):
    #process the data into a file
    objFile = open('HomeInventory2.txt', 'w')
    for row in tplData:
        objFile.write(str(row) + "\n")

# Display a message to the user
print('Data saved to file!')


# to add more data strMoreData = ("4"),
# for Row in tplDataTableA