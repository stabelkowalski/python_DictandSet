farm_animals = {'cow', 'sheep', 'hen', 'goat', 'horse'}
print(farm_animals)
for animal in farm_animals:
    print(animal)

print()
print("Indexing a sequence")
animals_list = ['cow', 'sheep', 'hen', 'goat', 'horse']
goat = animals_list[3]
print(goat)
print("Indexing a set is not possible")

more_animals = {'sheep', 'goat', 'cow', 'horse', 'hen'}

if more_animals == farm_animals:
    print("the sets are equal")
else:
    print("the sets are different")


