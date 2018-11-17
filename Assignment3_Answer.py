# get user input data

strItem = input('Enter an item: ')
strValue = input('Enter an Estimated Value: ')

# Process the data into a file

objFile = open('HomeInventory.txt', 'w')
objFile.write(strItem + ',' + strValue)

# Display a message to the user

print('Data saved to file!')
