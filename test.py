"""
Este módulo define la clase Student para gestionar estudiantes y sus calificaciones 
con sus metodos asociados.
"""

class Student:
    """
    Representa a un estudiante con un ID, nombre y lista de calificaciones.
    """

    def __init__(self, student_id, name):
        """
        Inicializa un estudiante con ID, nombre y atributos predeterminados.
        """
        self.student_id = student_id
        self.name = name
        self.grades = []
        self.is_passed = "NO"
        self.honor = "?"

    def add_grade(self, grade):
        """
        Agrega una calificación a la lista de calificaciones si es válida.
        """
        if isinstance(grade, (int, float)) and 0 <= grade <= 100:
            self.grades.append(grade)
        else:
            print(f"Error: '{grade}' no es una calificación válida.")

    def calculate_average(self):
        """
        Calcula y retorna el promedio de las calificaciones.
        """
        if not self.grades:
            print("Error: No hay calificaciones para calcular el promedio.")
            return 0
        return sum(self.grades) / len(self.grades)

    def check_honor(self):
        """
        Verifica si el estudiante merece un reconocimiento de honor.
        """
        average = self.calculate_average()
        if average > 90:
            self.honor = "YES"
        else:
            self.honor = "NO"

    def delete_grade(self, index):
        """
        Elimina una calificación por índice si el índice es válido.
        """
        if 0 <= index < len(self.grades):
            del self.grades[index]
        else:
            print(f"Error: Índice {index} fuera de rango.")

    def report(self):
        """
        Genera un reporte con la información del estudiante.
        """
        print(f"ID: {self.student_id}")
        print(f"Nombre: {self.name}")
        print(f"Cantidad de calificaciones: {len(self.grades)}")
        print(f"Promedio final: {self.calculate_average():.2f}")
        print(f"Honor: {self.honor}")


def main():
    """
    Función principal para probar la clase Student.
    """
    student = Student("001", "Juan Perez")
    student.add_grade(100)
    student.add_grade(85)
    student.add_grade("Fifty")  # Error: no es una calificación válida
    student.calculate_average()
    student.check_honor()
    student.delete_grade(5)  # Error: índice fuera de rango
    student.report()

main()
