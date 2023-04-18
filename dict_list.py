available_parts = {
    "1": "computer",
    "2": "monitor",
    "3": "keyboard",
    "4": "mouse",
    "5": "hdmi",
    "6": "dvd drive",
}


current_choice = None
while current_choice != "0":
    if current_choice in available_parts:
        chosen_part = available_parts[current_choice]
        print(f"Adding {chosen_part}")
    else:
        print("Please add options from the list below")
        for key, value in available_parts.items():
            print(key, value, sep=": ")
        print("0: to finish")
    current_choice = input("> ")

