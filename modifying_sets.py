# numbers = set()
numbers = {*""}

print(numbers, type(numbers))

# numbers.add(1)
# print(numbers)

# while len(numbers) < 4:
#     next_value = int(input("please enter your next value: "))
#     numbers.add(next_value)
# print(numbers)

data = ['blue', 'red', 'blue', 'green', 'red', 'blue', 'white']
# create a set from the list to remove duplicates
# unique_data = set(data)
unique_data = sorted(set(data))
print(unique_data, type(unique_data))

# Create a list of unique colors, keeping the order they appeared
unique_data = list(dict.fromkeys(data))
print(unique_data)

print()
print(dict.fromkeys(data))

