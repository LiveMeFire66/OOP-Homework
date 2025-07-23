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


lecturer = Lecturer('Иван', 'Иванов')
reviewer = Reviewer('Пётр', 'Петров')
student = Student('Алёхина', 'Ольга', 'Ж')

student.courses_in_progress += ['Python', 'Java']
lecturer.courses_attached += ['Python', 'C++']
reviewer.courses_attached += ['Python', 'C++']

print(student.rate_lecturer(lecturer, 'Python', 7))  # None
print(student.rate_lecturer(lecturer, 'Java', 8))  # Ошибка
print(student.rate_lecturer(lecturer, 'С++', 8))  # Ошибка
print(student.rate_lecturer(reviewer, 'Python', 6))  # Ошибка

print(lecturer.grades)  # {'Python': [7]}
