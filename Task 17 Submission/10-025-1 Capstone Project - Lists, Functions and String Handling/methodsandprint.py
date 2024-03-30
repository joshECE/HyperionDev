class Print_class:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.options = {
            "name" : self.printName,
            "age" : self.printAge
        }

    def printSelect(self):
        user_input = input("Select Option:")
        self.options[user_input]()

    def printName(self):
        print(f"Name is {self.name}")

    def printAge(self):
        print(f"Name is {self.age}")


new_print_class = Print_class("Gregg",55)

new_print_class.printSelect()


    
