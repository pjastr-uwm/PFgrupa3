class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print("Hello, my name is", self.name)

    def __str__(self):
        return "Person: " + self.name + ", " + str(self.age)


class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def greet(self):
        print("Hi, I'm", self.name, "and my student id is", self.student_id)

    def study(self, subject):
        print(self.name, "is studying", subject)


class Teacher(Person):
    def __init__(self, name, age, subject):
        Person.__init__(self, name, age)
        self.subject = subject

    def greet(self):
        print("Good day, I am Professor", self.name)

    def teach(self):
        print(self.name, "is teaching", self.subject)


def main():
    student1 = Student("Anna", 20, "S1234")
    teacher1 = Teacher("Dr. Smith", 45, "Mathematics")
    people = [student1, teacher1]
    for person in people:
        person.greet()
        if isinstance(person, Student):
            person.study("Physics")
        elif isinstance(person, Teacher):
            person.teach()

    print("Representation of student:", student1)
    print("Representation of teacher:", teacher1)

    print(
        "This is a very long line of code that is intentionally written to exceed the recommended maximum line length as per PEP8 standards and should be flagged by flake8."
    )


if __name__ == "__main__":
    main()
