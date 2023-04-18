from contents import pantry, recipes


# dictionary comprehension
# display_dict = {str(index + 1): meal for index, meal in enumerate(recipes)}

def add_shopping_item(data: list, item: str, amount: int) -> None:
    """Add tuple containing `item` and `amount` to the `data` list."""
    data.append((item, amount))


shopping_list = []
display_dict = {}
for index, key in enumerate(recipes):
    display_dict[str(index + 1)] = key
print(display_dict)


while True:
    print("Please choose your recipe")
    print("-"*8)
    for key, value in display_dict.items():
        print(f"{key} - {value}")

    choice = input("Please enter you recipe: ")
    if choice == "0":
        break
    elif choice in display_dict:
        selected_item = display_dict[choice]
        print(f"You have selected {selected_item}")
        print("Checking ingredients ...")
        ingredients = recipes[selected_item]
        print(ingredients)
        for food_item, required_quantity in ingredients.items():
            quantity_in_pantry = pantry.get(food_item, 0)
            if required_quantity <= quantity_in_pantry:
                print(f"{food_item} OK")
            else:
                quantity_to_buy = required_quantity - quantity_in_pantry
                print(f"You need to buy {quantity_to_buy} of the {food_item}")
                add_shopping_item(shopping_list, food_item, required_quantity)

for things in shopping_list:
    print(things)
