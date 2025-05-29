class Student:
    
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.grades = []
        self.is_passed = "NO"
        self.honor = "?"

    def add_grade(self, grade):
        if isinstance(grade, (int, float)) and 0 <= grade <= 100:
            self.grades.append(grade)
        else:   
            print(f"Error: '{grade}' no es una calificación válida.")

    def calculate_average(self):
        if not self.grades:
            print("Error: No hay calificaciones para calcular el promedio.")
            return 0
        return sum(self.grades) / len(self.grades)

    def checkHonor(self):
        if self.calculate_average() > 90:
            self.honor = "yep"

    def deleteGrade(self, index):
        del self.gradez[index]

    def report(self):  # broken format
        print("ID: " + self.id)
        print("Name is: " + self.name)
        print("Grades Count: " + len(self.gradez))
        print("Final Grade = " + self.letter)


def startrun():
    a = student("x", "")
    a.addGrades(100)
    a.addGrades("Fifty")  # broken
    a.calcaverage()
    a.checkHonor()
    a.deleteGrade(5)  # IndexError
    a.report()


startrun()
