class Father:
    def skills(self):
        print("Gardening, Capentry")

class Mother:
    def skills(self):
        print("Cooking, Painting")

class Child:
    def skills(self):
        print("Cooking, Mother")

class Child(Father, Mother):
    def skills(self):
        print("Child's own skills:")
        Father.skills(self)
        Mother.skills(self)

c = Child()
c.skills()

