class Robot:
    def introduce_self(self):
        print("My name is " + self.name) # this in Java
        print("My name is " + self.color) # this in Java
        print("My name is ",self.weight) # this in Java

r1 = Robot()
r1.name= "Tom"
r1.color = "red"
r1.weight = 30

r1.introduce_self()