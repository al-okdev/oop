class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __str__(self):
        ocenka = ''
        for name, ocenka_item in self.grades.items():
            ocenka += ' '+name+': '
            ocenka += str(+sum(ocenka_item) / len(ocenka_item))

        return 'Имя: ' + self.name + '\nФамилия: ' + self.surname + '\nСредняя оценка за домашние задания: ' + str(ocenka) + '\nКурсы в процессе изучения: '+str(", ".join(self.courses_in_progress))+'\nЗавершенные курсы: '+str(", ".join(self.finished_courses))

    def rate_hw_lecturer(self, course, lecturer, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached:
            if course in lecturer.grades_for_lectures:
                lecturer.grades_for_lectures[course] += [grade]
            else:
                lecturer.grades_for_lectures[course] = [grade]
        else:
            return 'Ошибка'

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, power):
        super().__init__(name, power)
        self.grades_for_lectures = {}

    def __str__(self):
        ocenka = ''
        for name, ocenka_item in self.grades_for_lectures.items():
            ocenka += ' ' + name + ': '
            ocenka += str(+sum(ocenka_item) / len(ocenka_item))
        return 'Имя: ' + self.name + '\nФамилия: ' + self.surname + '\nСредняя оценка за лекции: ' + str(ocenka)

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return 'Имя: ' + self.name + '\nФамилия: ' + self.surname

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['C++']

cool_mentor = Mentor('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']


# Reviewer ставит оценки студентам

cool_reviewer = Reviewer('Ivan', 'Popov')
cool_reviewer.courses_attached += ['Python']
cool_reviewer.courses_attached += ['C++']

cool_reviewer.rate_hw(best_student, 'Python', 8)
cool_reviewer.rate_hw(best_student, 'Python', 7)
cool_reviewer.rate_hw(best_student, 'Python', 9)

cool_reviewer.rate_hw(best_student, 'C++', 7)
cool_reviewer.rate_hw(best_student, 'C++', 6)
cool_reviewer.rate_hw(best_student, 'C++', 5)


print(best_student.grades)
print('###')

# Lecturer получают оценки от студентов

cool_lecturer = Lecturer('Elena', 'Nikolaeva')
cool_lecturer.courses_attached += ['Python']
cool_lecturer.courses_attached += ['C++']

best_student.rate_hw_lecturer('Python', cool_lecturer, 8)
best_student.rate_hw_lecturer('Python', cool_lecturer, 8)

best_student.rate_hw_lecturer('C++', cool_lecturer, 7)
best_student.rate_hw_lecturer('C++', cool_lecturer, 6)


print(cool_lecturer.grades_for_lectures)

print()

# Проверяем перезагрузку __str__
print('Проверяем перезагрузку __str__:')
print(cool_reviewer)
print()
print(cool_lecturer)
print()
print(best_student)

