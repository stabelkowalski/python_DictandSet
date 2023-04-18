vehicles = {
    'dream': 'Honda 250T',
    'er5': 'Kawasaki ER5',
    'can-am': 'Bombardier Can-Am 250',
    'virago': 'Yamaha XV250',
    'tenere': 'Yamaha XT650',
    'jimny': 'Suzuki Jimny 1.5',
    'fiesta': 'Ford Fiesta Ghia 1.4',
    'roadster': 'Triumph Street Triple'
}

# my_car = vehicles['fiesta']
# print(my_car)
# commuter = vehicles['virago']
# print(commuter)
# learner = vehicles.get("er5")
# print(learner)

# add to dictionary
vehicles["starfighter"] = "Lockheed F-104"
vehicles["learjet"] = "Bombardier Learjet 75"
vehicles["toy"] = "glider"

# upgrade the Virago
vehicles["virago"] = "Yamaha XV535"

# remove
del vehicles["starfighter"]
# del vehicles["f1"]
result = vehicles.pop("f1", None)
print(result)
plane = vehicles.pop("learjet")
print(plane)
bike = vehicles.pop("tenere", "Not present")
print(bike)
print()





# for key in vehicles:
#     print(key, vehicles[key], sep=", ")


for key, value in vehicles.items():
    print(key, value, sep=", ")
