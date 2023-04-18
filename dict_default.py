from contents import pantry

chicken_quantity = pantry.setdefault("chicken", 0)
print(f"chicken: {chicken_quantity}")

# setdefault dodaje key do dict, co nie robi get
beans_quantity = pantry.setdefault("beans", 0)
print(f"beans: {beans_quantity}")

ketchup_quantity = pantry.get("ketchup", 0)
print(f"ketchup: {ketchup_quantity}")

z_quantity = pantry.setdefault("zucchini", "eight")
print(f"zucchini: {z_quantity}")
print()
print("Pantry now contains...")

for key, value in pantry.items():
    print(key, value)



