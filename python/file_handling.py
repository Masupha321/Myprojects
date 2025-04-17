def add_entry():
    date = input("Enter the date (YYYY-MM-DD): ")
    title = input("Enter the title: ")
    body = input("Enter the diary entry: ")

    entry = f"\n========== {date} ==========\n\n"
    entry += f"Title: {title}\n\n"
    entry += f"{body}\n"
    entry += f"-----------\n"

    with open("diary.txt", "a") as file:
        file.write(entry)

    print("Entry added successfully")

def view_entries():
    with open("diary.txt", "r") as file:
        content = file.read()
        print(content)

def search_entries():
    keyword = input("Enter a keyword to search for: ").lower()

    with open("diary.txt", "r") as file:
        entries = file.read().split("----------\n")
    
    for entry in entries:
        if keyword in entry.lower():
            print(entry + "------------")



#add_entry()
#view_entries()
search_entries()