class Employees:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I'm {self.name} and I'm {self.age} years old")

    def speak(self):
        print("I don't know what to say")

class Csaba(Employees):
    
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def speak(self):
        print(f"Hello, I'm {self.name} , {self.age} years old and {self.color} is the color of my skin.")

class Adri(Employees):

    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def speak(self):
        print(f"Hello, I'm {self.name} , {self.age} years old.")



d = input("Please type Adri or Csaba: ")



if d == "Csaba":
    c = Csaba("Csaba", 25, "white")


else:
    c = Adri("Adri", 24, "white")


c.speak()