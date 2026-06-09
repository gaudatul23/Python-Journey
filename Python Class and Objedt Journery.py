#Create an empty class

class Student: # Define a class named Student
    pass # Empty class body

s1 = Student()
s2 = Student() # Create an object 
print(s1)
print(s2)

# Whenever there is a empty class 
# Then only we write pass


# Q2 : create an object from a class 
class Car: # Define a class named Car
    pass # Empty class body]

my_car = Car() # Create an object of the class Car
c2 = Car()
print(my_car)
print(c2)

# on executing the empty class we get the address of the object created


#Q3: Class with attributes
class Animal: # Define a class named Animal
    name="dog"
    color="Brown" # Attributes of the class

a = Animal() # Create an object of the class Animal
print(a.name,a.color) # Accessing attribute name

# Q4: Using __init__ method to initialize values

class Book: # Define a class named Book
    def __init__(self, title, author): # Constructor with parameters
        self.title = title # Initialize title attribute
        self.author = author # Initialize author attribute
    
b1 = Book("1984", "George Orwell") # Create an object of the class Book
print(b1.title, b1.author) 

#Q5: Multiple objects with different values
class Mobile:
    def __init__(self, price):
        self.price = price

m1 = Mobile(50000)
m2 = Mobile(30000)

print(m1.price)
print(m2.price)


# Q6: Adding methods to a class
class Person:
    def greet(self):
        print("Hello!")

p = Person()
p.greet() # Calling the greet method


# Q7: Class with method using attributes
class Employee:
    def __init__(self, name,salary):
        self.name = name
        self.salary = salary
    
    def details(self):
       print(self.name, self.salary)

e = Employee("Alice", 70000)
e.details() # Calling the details method

# Q8: Modifying object attributes
class laptop:
    def __init__(self,ram):
        self.ram = ram

lap = laptop("8GB")
lap.ram = "16GB" # Modifying the ram attribute
lap.ram = "32GB"
print(lap.ram)


#Q9: Adding a new attribute to an object creation 
class shoes:
    def __init__(self,size):
        self.size = size

s= shoes(9)
s.brand = "Nike" # Adding a new attribute brand
print(s.size, s.brand)


#Q10: Changing class variable for all objects
class Country:
    name = "India" # Class variable

c1 = Country()
c2 = Country()
Country.name = "Bharat" # Changing class variable
print(c1.name, c2.name)

#Q12: Method that returns a value ( Expression maths , stats)
class Maths:
    def add(self,a,b):
        return a + b

m = Maths()
print(m.add(5, 10)) # Calling the add method and printing the result