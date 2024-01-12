class Menu:
    def __init__(self, name):
        self.name = name


chicken_alfredo = Menu("Chicken Alfredo")
spaghetti_meatballs = Menu("Spaghetti with Meatballs")
baked_ziti = Menu("Baked Ziti")
chicken_carbonara = Menu("Chicken Carbonara")


print("Welcome to the Italian Restaurant!")
print("Menu:")
print(f"1. {chicken_alfredo.name}")
print(f"2. {spaghetti_meatballs.name}")
print(f"3. {baked_ziti.name}")
print(f"4. {chicken_carbonara.name}")