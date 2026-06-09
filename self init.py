class Person: 
    pass 

s1 = Person()
s2 = Person() 
print(s1)
print(s2)








































# Normal creating a class using __init__ method and displaying attributes
class Cars:
  def __init__(self, brand, color):
    self.brand = brand
    self.color = color

  def display(self):
    print(self.brand , self.color)

c1 = Cars("Toyota", "White")
c2 = Cars("Nissan", "Black")

c1.display()
c2.display()







# now lets modify the above code 

class Cars:
  def __init__(self, brand, color):
    self.brand = brand
    self.color = color

C = Cars
C. carname ="Supra"
C.brand = "Toyota"
C.color = "White"

print(C.carname, C.brand, C.color)

