# lets calculate the Speed Distance and time 

class formula:
  def __init__(self, speed, distance, time):
    self.speed = speed
    self.distance = distance
    self.time = time
  
  def calculate_speed(self, distance, time):
    return distance / time
  
  def calculate_distance(self, speed, time):
    return speed * time
  
  def calculate_time(self, distance, speed):
    return distance / speed
  
Cal = formula(10, 100, 30)

print("Speed is: ", Cal.calculate_speed(100, 30))
print("Distance is: ", Cal.calculate_distance(10, 30))
print("Time is: ", Cal.calculate_time(100, 10))








# Now lets create some Arthermetic operations 

class Calculator:
  def add(self, a, b):
    return a + b
  
  def substract(self, a, b):
    return a - b
  
  def multiply(self, a, b):
    return a * b
  
  def divide(self, a, b):
    return a // b
  
cal = Calculator()
print("Addition: ", cal.add(10, 5))
print("Substraction: ", cal.substract(10, 20))
print("Multiplication: ", cal.multiply(7, 5))
print("Division: ", cal.divide(40, 20))




