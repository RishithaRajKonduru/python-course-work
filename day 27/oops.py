'''class Book:
    def __init__(self, title, author, price):
        
        self.title = title
        self.author = author
        self.price = price
    def display_info(self):
        print(f"Title: {self.title}, Author: {self.author},Price: ${self.price}")
book1=Book("Clean Code","Robert Martin",450)
book1.display_info()'''


'''class Employee:
    def __init__(self,name,base_salary):
        self.name=name
        self.base_salary=base_salary
    def calculate_annual_salary(self):
        return self.base_salary*12
emp=Employee("John",35000)
print("Annual Salary:",emp.calculate_annual_salary())'''




'''class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def is_passed(self):
        avg = sum(self.marks) / len(self.marks)
        return avg >= 40
# Object and method call
s1 = Student("Priya", [45, 56, 60])
print("Passed:", s1.is_passed())'''



'''class BankAccount:
    def __init__(self, owner):
        self.owner = owner
        self.balance = 0
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
         if amount <= self.balance:
             self.balance -= amount
         else:
            print("Insufficient balance")

    def show_balance(self):
         print(f"Balance: {self.balance}")

# Use case
acc = BankAccount("Arjun")
acc.deposit(1000)
acc.withdraw(500)
acc.show_balance()'''



'''class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
        self.odometer = 0
    def drive(self, km):
        self.odometer += km
    def show_odometer(self):
        print(f"Odometer: {self.odometer} km")
car1 = Car("Toyota", "Innova")
car1.drive(120)
car1.drive(30)
car1.show_odometer()'''


'''class Movie:
    def __init__(self, title, genre, rating):
        self.title = title
        self.genre = genre
        self.rating = rating
    def is_family_friendly(self):
        return self.rating < 13
m1 = Movie("Finding Nemo", "Animation", 8)
print("Family Friendly:", m1.is_family_friendly())'''


'''class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def apply_discount(self, percent):
        self.price -= self.price * (percent / 100)
    def show_price(self):
        print(f"Discounted price: {self.price}")
p = Product("Laptop", 50000)
p.apply_discount(10)
p.show_price()'''


'''class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius
    def to_fahrenheit(self):
        return (self.celsius * 9/5) + 32
    def to_celsius(self, fahrenheit):
        return (fahrenheit - 32) * 5/9
temp = Temperature(25)
print("Fahrenheit:", temp.to_fahrenheit())
print("Celsius from 98F:", temp.to_celsius(98))'''



