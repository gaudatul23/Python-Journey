class Animal: # Base class (Parent Class)
  def speak(self): # Self is Constructor used to activate function
    print("Animal speaks")
  
class Dog(Animal): # Derived class (Child Class) Inheritance
  pass # no additional properties or methods

d=Dog() # create a object for dog class 
d. speak() # call the speak method from the parent class

# function are always used using the in built function called def (define)


# method Overriding
class Animal:
  def speak(self):
    print("Animal speaks") # base method 

class Dog(Animal):
  def speak(self):
    print("Dog barks")  # overridden method

d=Dog()
d.speak()  # calls the overridden method in Dog class


# add new method in child class

class Animal: # Perent class
  def moves(self): # self is Constructor used to activate function
    print("Animal moves") # Method of Parent class

class Fish(Animal):
  def swim(self): # New method in Child class
    print("Fish swims")

f= Fish() # create object for Fish class
f.moves() # call method from Parent class
f.swim() # call method from Child class
    


class Warehouse:
  def Cars(self):
    print("name the car brand")


class Showroom(Warehouse):
  def display(self):
    print("Displaying cars in showroom")

s = Showroom()
s.Cars()  # inherited method from Warehouse class
s.display()  # method from Showroom class


# Inheriting and __init__ method
class Person: # Parent class
  def __init__ (self, name):
    self.name = name # call parent class attribute

class student(Person):
  def __init__(self, name, grade):
    super().__init__(name) # call the parent class __init__ method
    self.grade = grade  # child class attribute

s= student("John", "A")
print(s.name, s.grade)  # inherited attribute from Person class


# Multi level Inheritance

class Grandparent: # Base class
  def house(self):
    print("Owns House ")

class Parent(Grandparent): # Derived class from Grandparent
  def car(self):
    print("Owns Car")

class Child(Parent): # Derived class from Parent
  def bike(self):
    print("Owns Bicycle")

c = Child()
c.house()  # inherited from Grandparent class
c.car()    # inherited from Parent class
c.bike()   # method from Child class

# multiple Inheritance 

class Father: 
  def skills(self):
    print("Programming")

class Mother:
  def skills(self):
    print("Cooking")

class Child(Father, Mother): # Child class inherits from Father and Mother    # first come first serve
  pass

c = Child()
c.skills()  # calls the skills method from Father class due to method resolution order MRO : first come first serve


# Basic Multiple Inheritance 
class Father:
  def height(self):
    print("tall")

class Mother:
  def skin(self):
    print("fair")

class Child(Father, Mother):
  pass

c = Child()
c.height()  # calls the skills method from Father class due to method resolution order MRO : first come first serve
c.skin()  # calls the skills method from Mother class due to method resolution order MRO : first come first serve
#MRO : Method Resolution Order
    


# overriding  across levels 
class A:
  def show(self):
    print("Class A method")

class B(A):
  def show(self):
    print("Class B method")

class C(B):
  def show(self):
    print("Class C method")

c = C()
c.show()  # calls the overridden method in Class C

