#1.Create a variable called age and store your age. Print it.
#age = 25
#print(age)

#2. Create two variables a and b with values 10 and 5. Print their sum
#a = 10
#b = 5
#print(a+b)

#3. Multiply two numbers and print the result.
#a,b = 10,5
#print(a * b)

#4. Divide 20 by 4 and print the result.
print(20 // 4)
print(20 / 4)

#5. Write a program that prints “Python is fun”
#program = "Python is fun"
#print(program)

#Exercise 1
# Create a class called Student.
class Student:
    pass

# Exercise 2
# Add an __init__ method that takes name and age.

class Student:
    def __init__(self, name, age):
        pass

# Exercise 3
# Inside the __init__ method, store name and age using self. 
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Exercise 4
# Create a Student object and print the name.
student1 = Student("Diana", 15)
print(student1.name)

# Exercise 5
# Create a method called introduction that prints the student's name and age.

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduction(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

student2 = Student("Vicky", 16)
student2.introduction()

# Exercise 6
# Add a grade attribute to the Student class.
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

# Exercise 7
# Create a Student object with grade and print the grade.

student3 = Student("Diana", 15, 80)
print(student3.grade)

# Exercise 8
# Update the student's grade and print the new grade.

student3.grade = 87
print(student3.grade)

# Exercise 9
# Add a method age_group that prints "Adult" if age >= 18 else "Minor".

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def age_group(self):
        if self.age >= 18:
            print("Adult")
        else:
            print("Minor")

student4 = Student("Mary", 10, 67)
student4.age_group()

# Exercise 10
# Create three Student objects, store them in a list and print their names.
 
students = [
    Student("Dan", 14, 90),
    Student("Grace", 18, 78),
    Student("Harry", 19, 69)
]
 
for student in students:
    print(student.name)