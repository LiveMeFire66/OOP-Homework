lecturers_list = []

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course_name, grade):
        if isinstance(lecturer, Lecturer) and course_name in self.courses_in_progress and course_name in lecturer.courses_attached and 1 <= grade <= 10:
            if course_name in lecturer.grades:
                lecturer.grades[course_name] += [grade]
            else:
                lecturer.grades[course_name] = [grade]
        else:
            return 'Ошибка'

    def avg_grade(self):
        overall_grade = 0
        grades_count = 0
        if not self.grades:
            return 0
        for grades in self.grades.values():
            overall_grade += sum(grades)
            grades_count += len(grades)
        return overall_grade / grades_count if grades_count else 0

    def __str__(self):
        return f"Имя: {self.name}\n" \
               f"Фамилия: {self.surname}\n" \
               f"Средняя оценка за домашние задания: {round(self.avg_grade(), 2)}\n" \
               f"Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\n" \
               f"Завершенные курсы: {', '.join(self.finished_courses)}"

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)


    def __lt__(self, other):
        if isinstance(other, Student):
            return self.avg_grade() < other.avg_grade()
        else:
            return "Ошибка"

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        lecturers_list.append(self)

    def avg_grade(self):
        overall_grade = 0
        grades_count = 0
        for grades in self.grades.values():
            overall_grade += sum(grades)
            grades_count += len(grades)
        return overall_grade / grades_count if grades_count else 0

    def __str__(self):
        return f"Имя: {self.name}\n" \
               f"Фамилия: {self.surname}\n" \
               f"Средняя оценка за лекции: {round(self.avg_grade(), 2)}"

    def __lt__(self, other):
        if isinstance(other, Lecturer):
            return self.avg_grade() < other.avg_grade()
        else:
            return "Ошибка"

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def __str__(self):
        return f"Имя: {self.name}\n" \
               f"Фамилия: {self.surname}"

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

        def average_student_grade(students, course):
            total_grade = 0
            total_count = 0
            for student in students:
                if course in student.grades:
                    total_grade += sum(student.grades[course])
                    total_count += len(student.grades[course])
            return total_grade / total_count if total_count else 0

        def average_lecturer_grade(lecturers, course):
            total_grade = 0
            total_count = 0
            for lecturer in lecturers:
                if course in lecturer.grades:
                    total_grade += sum(lecturer.grades[course])
                    total_count += len(lecturer.grades[course])
            return total_grade / total_count if total_count else 0


def average_student_grade(students, course):
    total_grade = 0
    total_count = 0
    for student in students:
        if course in student.grades:
            total_grade += sum(student.grades[course])
            total_count += len(student.grades[course])
    return total_grade / total_count if total_count else 0


def average_lecturer_grade(lecturers, course):
    total_grade = 0
    total_count = 0
    for lecturer in lecturers:
        if course in lecturer.grades:
            total_grade += sum(lecturer.grades[course])
            total_count += len(lecturer.grades[course])
    return total_grade / total_count if total_count else 0


# Создаем экземпляры
lecturer1 = Lecturer('Иван', 'Иванов')
lecturer2 = Lecturer('Сергей', 'Сергеев')
reviewer1 = Reviewer('Пётр', 'Петров')
reviewer2 = Reviewer('Дмитрий', 'Дмитриев')
student1 = Student('Алёхина', 'Ольга', 'Ж')
student2 = Student('Ruoy', 'Eman', 'М')

# Задаем курсы
student1.courses_in_progress += ['Python', 'Java']
student1.finished_courses += ['Основы программирования']

student2.courses_in_progress += ['Python', 'Git']
student2.finished_courses += ['Введение в программирование']

lecturer1.courses_attached += ['Python', 'Java']
lecturer2.courses_attached += ['Python', 'C++']

reviewer1.courses_attached += ['Python']
reviewer2.courses_attached += ['Java']

# Оцениваем лекторов и добавляем оценки студентам
student1.rate_lecturer(lecturer1, 'Python', 9)
student1.rate_lecturer(lecturer1, 'Python', 10)
student2.rate_lecturer(lecturer1, 'Python', 8)
student2.rate_lecturer(lecturer2, 'Python', 7)

# Вывод информации о студентах, лекторах и рецензентах
print(student1)
print()
print(student2)
print()
print(lecturer1)
print()
print(lecturer2)
print()
print(reviewer1)
print()
print(reviewer2)

# Вывод средних оценок
print("Средняя оценка за домашние задания (Python):", average_student_grade([student1, student2], 'Python'))
print("Средняя оценка за лекции (Python):", average_lecturer_grade([lecturer1, lecturer2], 'Python'))