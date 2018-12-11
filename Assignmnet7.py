#--------------------
# JLipka
# December 10, 2018
# IT FDN 100B
# Assignment 7
#--------------------
# Create a simple example of how you would use Python Pickling.
import pickle

# lists to pickle
type = ["sedan", "suv", "truck"]
brand = ["bmw", "honda", "toyota"]
color = ["red", "blue", "green"]

# open new file to store the data
f = open("cars.dat","wb")

# pickle the data
pickle.dump(type,f)
pickle.dump(brand,f)
pickle.dump(color,f)
f.close()

# unpickle
f = open("cars.dat","rb")
type = pickle.load(f)
brand = pickle.load(f)
color = pickle.load(f)

# print list
print(type)
print(brand)
print(color)
f.close()


# Create a simple example of how you would use Python Exception Handling.
try:
    number = float(input("Enter a number: "))
except:
    print("Something went wrong")