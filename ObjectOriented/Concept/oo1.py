class Computer:
    graphic="yes"                         #class variable / static variable
    def __init__(self,cpu,ram):
        self.cpu=cpu                      #instance variable / object variable / attriutes
        self.ram=ram

    def config(self):
        print("CPU and RAM = ",self.cpu,self.ram)

c1=Computer('i5',8)
c2=Computer('i8',16)

c1.cpu='i7'
c1.config()
# Computer.config(c1)
print(type(c1))
print(c1.graphic)
Computer.graphic="NO"
c1.graphic="YES"
print(c2.graphic)
print(Computer.graphic)

#  Accessors - Mutators        //   Setters and Getters        in oo2.py
