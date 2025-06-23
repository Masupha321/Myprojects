fruits = {
    "apple": 3.5,
    "banana": 2.0,
    "cherry": 5.0,
    "mango": 3.5,
    "orange": 4.0,
  }

fruit_names = list(fruits.keys())
print("List of fruit names:", fruit_names)

unique_prices = set(fruits.values())
print("Unique prices:", unique_prices)

fruit_items = list(fruits.items())
print("List of (fruit, price) tuples:", fruit_items)