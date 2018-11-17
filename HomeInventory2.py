#---------------------------------
# Title: Home Inventory Script
# Dev: JLipka
# Date: Nov 11, 2018
#---------------------------------

#Get User Input data
strData1 = input("Enter an item: ") # TV
strData2 = input("Enter an estimated value: ") # 299
strData3 = input("Enter an item: ") # Stove
strData4 = input("Enter an estimated value: ") #999

tplHeader =("Household Item", "Estimated Value")
tplDataRow1 = (strData1, strData2)
tplDataRow2 = (strData3, strData4)
tplDataTableA = (tplDataRow1, tplDataRow2)
#print(tplDataTableA)

# you will store them in the 2-dimensional Tuple.
print(tplHeader)
for item in tplDataTableA:
    print(item)

# ask if they would like to save the data to a text file
print("Save Data?: " + "Y/N")

#Yes = "Y"
#No = "N"
# if Y == Yes
# Then run this
text_file = open("HomeInventory2.txt","w")
text_file.write(str(tplDataTableA))
text_file.close()
#print ("Data saved!")

#else:
    #print ("Not saved")
