'''1. Write a program that calculates and prints the value according to the given formula:
Q= Square root of [(2*C*D)/H]
Following are the fixed values of C and H:
C is 50.
H is 30.
D is a variable whose values should be input to your program in a comma-separated sequence.
#solution:

import math

D=input("Enter the value of D to perform the operation:")
D=D.split(",")
C=50
H=30

for i in D:
    sq=math.sqrt((2*C*int(i))/H)
    print(sq)
'''

'''2. Define a class named Shape and its subclass Square. The Square class has an init function which
takes length as argument. Both classes have an area function which can print the area of the shape
where Shape’s area is 0 by default.     

#solution:


from turtle import shape
class Shape(object):
    def __init__(self):
        print("area for shape")
        pass
    def area(self):
        return 0

class Square(Shape):
    def __init__(self,length):
        shape.__init__(self,length)
        self.length=length

    def area(self):
        return self.length*self.length

a=Square(3)
print(a.area())

'''

        
'''
'''


'''4. Create a Time class and initialize it with hours and minutes.
Create a method addTime which should take two Time objects and add them.
E.g.- (2 hour and 50 min)+(1 hr and 20 min) is (4 hr and 10 min)
Create another method displayTime which should print the time.
Also create a method displayMinute which should display the total minutes in the Time.
E.g.- (1 hr 2 min) should display 62 minute'''
'''
class Time():
    def __init__(self,hours,minutes):
        self.hours=hours
        self.minutes=minutes
        
    def addTime(t1,t2):
        t3=Time(0,0)
        t3.hours =t1.hours+t2.hours
        t3.minutes=t1.minutes+ t2.minutes
        while t3.minutes >=60:
            t3.hours+=1
            t3.minutes-=60
        return t3

    def displayTime(self):
        print("Time is %d hours and %d minutes" %(self.hours,self.minutes))

    def displayMinutes(self):
        print((self.hours*60)+self.minutes, "minutes")

a=Time(2,90)
b=Time(1,90)
c=Time.addTime(a,b)

c.displayTime()
c.displayMinutes()
'''

'''5. Write a Person class with an instance variable “age” and a constructor that takes an integer as a
parameter. The constructor must assign the integer value to the age variable after confirming the
argument passed is not negative; if a negative argument is passed then the constructor should set
age to 0 and print “Age is not valid, setting age to 0”. In addition, you must write the following instance
methods:'''

'''
class Person:
    age = 0
    def __init__(self,initialAge):
        if initialAge < 0:
            self.age =0
            print("Age is not valid, setting age to 0")
        else:
            self.age = initialAge
    def amIOld(self):
        if self.age < 13:
            print("You are young.")
        elif self.age >= 13 and self.age < 18:
            print("You are a teenager.")
        else:
            print("You are old.")

    def yearPasses(self):
        self.age += 1

obj=Person(5)
obj=Person(-1)


'''