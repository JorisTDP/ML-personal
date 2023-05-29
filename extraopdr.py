import numpy as np

# Specify the file path of the CSV file

# Load the data from the CSV file using numpy's genfromtxt function
data = np.genfromtxt('test.csv', delimiter=';', skip_header=1, usecols=(0, 1, 2, 3, 4, 5, 6))
y = np.genfromtxt('test.csv', delimiter=';', skip_header=1, usecols=(7))

dataT = np.transpose(data)

# Extract the columns you need and convert the strings to float
for d in data:
    #d = d.astype(float)
    print(d)

length = data[1]
mass = data[2].astype(float)
exercise = data[3].astype(float)
smoking = data[4].astype(float)
alcohol = data[5].astype(float)
sugar = data[6].astype(float)
lifespan = data[7].astype(float)

print(length)
print("------")

print(data)
print("------")
print(y)

mult = np.dot(dataT, data)
inverse = np.linalg.inv(mult)
mult1 = np.dot(inverse, dataT)
final = np.dot(mult1, y) 
print(final)