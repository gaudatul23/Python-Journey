# ploymorphism 

# create a polymorphism example where two different classes have the same method name and we call that method using a common interface
class car:
  def start(self):
    print("car started")

class bike:
  def start(self):
    print("bike started")

def start_any_vehicle(vehicle):
  vehicle.start() # THIS FUNCTION TAKES ANY VEHICLE AND CALLS ITS START METHOD


c = car()
b = bike()

start_any_vehicle(c)
start_any_vehicle(b)


#Create a list of object and cell the sam emethod on each 
class dog:
  def sound(self):
    print("Woof")

class cat:
  def sound(self):
    print("Meow")

animals = [dog(), cat()] # alternting method to create objects 
for animal in animals:
  #all animals have sound method
  animal.sound()


# Method Overriding ( Inheritance + Polymers)
# Parent and child class with overriden greet() method 

class Person:
  def greet(self):
    print("hello i am a person ")

class student(Person):
  def greet(self):
    print("hi i am student ")

p= Person()
s= student()
p.greet()
s.greet()


# call Overriden method using super()

class Animals:
  def sound(self):
    print("make the sound ")


class dog(Animals):
  def sound(self):
    super().sound() # call the parents method 
    print("Dog barks")

d = dog()
d.sound()

