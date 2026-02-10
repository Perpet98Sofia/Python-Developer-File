#6. add a grade attribute to student class
#7. create a student object with grade and print the grade
#8. update the student's grade and print the new grade
#9.add method called introduce that prints "Hello, my name is {name} and I am {age} years old."
#10. call the introduce method for one student
#11. add a method age_group that prints "Adult" if age >= 18 else "Minor"
#12. create three student object and store them in a list. 
#13. use loop to print the names of all students in the list
#14. use loop to call the introduce method for all students in the list

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
        if self.grade >= 90:
            self.grade_letter = 'A'
        elif self.grade >= 80:
            self.grade_letter = 'B'
        elif self.grade >= 70:
            self.grade_letter = 'C'
        elif self.grade >= 60:
            self.grade_letter = 'D'
        else:
            self.grade_letter = 'F'
    
    def introduction(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")
    def age_group(self):
        if self.age >= 18:
            print("adult")
        else:
            print("minor")

students = [
    Student("Conny", 23, 90),
    Student("Perpetua", 21, 88),
    Student("Eucabeth", 17, 60)
    ]
for student in students:
    print(student.name)
    student.age_group()

for student in students:
    student.introduction()

#student1 = Student("Diane", 17, 85)
#student2 = Student("Lovelyn", 20, 92)
#print(student1.name)
#student2.introduction()
#print(student1.grade_letter)
#print(student2.grade_letter)

