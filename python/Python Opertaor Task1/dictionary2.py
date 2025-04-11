fruits = {
    "apple": 3.5,
    "banana": 1.2,
    "orange": 2.0,
    "mango": 4.0,
 
}

fruit_name = input(str("Enter the name of the fruit to get its price:")).lower()
if fruit_name in fruits:
    print(f"The price of {fruit_name} is ${fruits[fruit_name]} per kg.")

new_fruit = input("Enter name of new fruit to add:").lower()
new_price = float(input(f"Enter the price per kg for {new_fruit}:"))
fruits[new_fruit] = new_price
print(f"{new_fruit} has been added with a price of ${new_price} per kg.")

update_fruit = input("Enter the name of the fruit to update its price:").lower()
if update_fruit in fruits:
    updated_price = float(input(f"Enter the new price for {update_fruit}:"))
    fruits[update_fruit] = updated_price
    print(f"The price of {update_fruit} has been updated ${updated_price} per kg.")

print("\nAll fruits and their prices:")
for fruit, price in fruits.items():
    print(f"{fruit.capitalize()}: ${price} per kg")
