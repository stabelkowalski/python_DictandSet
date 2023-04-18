d = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    "iv": "four",
}

pantry_items = ['chicken', 'spam', 'egg', 'bread', 'lemon']

d2 = {
    7: "lucky seven",
    10: "ten",
    3: "this is the new three",
}

v = d.values()
print(v)

d[10] = "ten"
print(v)

print("four" in v)
print("eleven" in v)

keys = list(d.keys())
values = list(d.values())

if "four" in values:
    index = values.index("four")
    key = keys[index]
    print(f"{d[key]} was found with the key {key}")

print()

for key, value in d.items():
    if value == "four":
        print(f"{d[key]} was found with the key {key}")


# Code for "The dict `update` method" lecture.
# d.update(d2)
# for key, value in d.items():
#     print(key, value)
#
# print()
# d.update(enumerate(pantry_items))
# for key, value in d.items():
#     print(key, value)

#  code for the remaining dict methods lecture
# # new_dict = dict.fromkeys(pantry_items, 0)
# # print(new_dict)
#
# keys = d.keys()
# print(keys)
#
# # .keys dodaje się po to żeby w dużych projektach było wiadomo że mamy do czynienia z dictionary
# for item in d.keys():
#     print(item)
