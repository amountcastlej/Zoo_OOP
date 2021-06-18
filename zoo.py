class Zoo:
    def __init__(self, zoo_name):
        self.animals = []        
        self.name = zoo_name
    def add_giraffe(self, name, age=0, happiness=1, health=0, color="orange"):
        self.animals.append(Giraffe(name, age, happiness, health, color))

    def add_monkey(self, name, age=0, happiness=1, health=0, color="brown"):
        self.animals.append(Monkey(name, age, happiness, health, color))

    def add_gorilla(self, name, age=0, happiness=1, health=0, color="black"):
        self.animals.append(Gorilla(name, age, happiness, health, color))

    def add_lion(self, name, age=0, happiness=1, health=0, color="yellow"):
        self.animals.append(Lion(name, age, happiness, health, color))

    def add_elephant(self, name, age=0, happiness=1, health=0, color="gray"):
        self.animals.append(Elephant(name, age, happiness, health, color))

    def add_tiger(self, name, age=0, happiness=1, health=0, color="orange"):
        self.animals.append(Tiger(name, age, happiness, health, color))

    def feed(self):
        for animal in self.animals:            
            animal.eat()
            
    def print_all_info(self):
        print("-"*30, self.name, "-"*30)
        for animal in self.animals:
            animal.display_info()

class Animal:
    def __init__(self, name, age, happiness, health):
        self.animals = []
        self.name = name        
        self.age = age        
        self.happiness = happiness        
        self.health = health
    def eat (self):        
        self.heath = self.health + 10        
        self.happiness = self.happiness + 10
    def display_info(self):        
        print("Name: ", self.name, "Age: ", self.age, "Health: ", self.health, "Happiness: ", self.happiness)
        for animal in self.animals:            
            animal.display_info()

class Giraffe(Animal):    
    def __init__(self, name, age, happiness, health, color):        
        super().__init__(name, age, happiness, health)        
        self.color = color
    def eat(self):        
        self.health = self.health + 20        
        self.happiness = self.happiness + 20
    def run(self):        
        self.health = self.health -20        
        self.happiness = self.happiness + 10
    def display_info(self):        
        print("Name: ", self.name, "Age: ", self.age, "Health: ", self.health, "Happiness: ", self.happiness, "Color: ", self.color)
        for animal in self.animals:            
            animal.display_info()

class Gorilla(Animal):    
    def __init__(self, name, age, happiness, health, color):        
        super().__init__(name, age, happiness, health)        
    self.color = color
    def eat(self):        
        self.health = self.health + 20        
        self.happiness = self.happiness + 20    
    def groom(self):        
        self.health = self.health + 50        
        self.happiness = self.happiness + 20    
    def display_info(self):        
        print("Name: ", self.name, "Age: ", self.age, "Health: ", self.health, "Happiness: ", self.happiness, "Color: ", self.color)        
        for animal in self.animals:            
            animal.display_info()

class Tiger(Animal):    
    def __init__(self, name, age, happiness, health, size):        
        super().__init__(name, age, happiness, health)        
        self.size = size    
    def eat(self):        
        self.health = self.health + 50        
        self.happiness =self.happiness + 50      
    def groom(self):        
        self.health = self.health + 50        
        self.happiness = self.happiness + 20    
    def display_info(self):        
        print("Name: ", self.name, "Age: ", self.age,"Health: ", self.health, "Happiness: ", self.happiness, "Size: ", self.size)        
        for animal in self.animals:            
            animal.display_info()

class Lion(Animal):    
    def __init__(self, name, age, happiness, health, size):       
        super().__init__(name, age, happiness, health)        
        self.size = size    
    def eat(self):        
        self.health = self.health + 50        
        self.happiness =self.happiness + 50      
    def play(self):        
        self.health = self.health + 10        
        self.happiness = self.happiness + 40    
    def display_info(self):        
        print("Name: ", self.name, "Age: ", self.age,"Health: ", self.health, "Happiness: ", self.happiness, "Size: ", self.size)
        for animal in self.animals:            
            animal.display_info()

class Monkey(Animal):    
    def __init__(self, name, age, happiness, health, size):        
        super().__init__(name, age, happiness, health)        
        self.size = size   
             def eat(self):        
        self.health = self.health + 50        
        self.happiness =self.happiness + 50      
    def play(self):        
        self.health = self.health + 10        
        self.happiness = self.happiness + 40    
    def display_info(self):        
        print("Name: ", self.name, "Age: ", self.age,"Health: ", self.health, "Happiness: ", self.happiness, "Size: ", self.size)        
        for animal in self.animals:            
            animal.display_info()

class Elephant(Animal):    
    def __init__(self, name, age, happiness, health, sex):        
        super().__init__(name, age, happiness, health)        
        self.sex = sex    
    def eat(self):        
        self.health = self.health + 30        
        self.happiness =self.happiness + 30      
    def run(self):        
        self.health = self.health -20        
        self.happiness = self.happiness + 10    
    def display_info(self):        
        print("Name: ", self.name, "Age: ", self.age,"Health: ", self.health, "Happiness: ", self.happiness, "sex: ", self.sex)        
        for animal in self.animals:            
            animal.display_info()

zoo1 = Zoo("Zoomania")
zoo1.add_giraffe("Spot", 5, 100, 100, "orange") 
zoo1.add_lion("Simba", 2, 100, 100, "250 cm")
zoo1.add_gorilla("Koko", 10, 100, 100, "brown" )
zoo1.add_tiger("Tony", 1, 100, 100, "250 cm")
zoo1.add_monkey("Diddy Kong", 3, 100, 100, "50 cm")
zoo1.add_elephant("Horton", 4, 100, 100, "male")
zoo1.print_all_info()

zoo1.feed()
zoo1.print_all_info()

print(zoo1.animals)

zoo1.animals[0].run()
zoo1.animals[1].play()
zoo1.animals[2].groom()
zoo1.animals[3].groom()
zoo1.animals[4].play()
zoo1.animals[5].run()
zoo1.print_all_info()