class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def grade_item_student(self):
        ocenka = map(sum, list(self.grades.values()))
        ocenka = list(ocenka)
        count_ocenka = map(len, list(self.grades.values()))
        count_ocenka = list(count_ocenka)
        result_ocenka = sum(ocenka) / sum(count_ocenka)
        return result_ocenka

    def __str__(self):
        return 'Имя: ' + self.name + '\nФамилия: ' + self.surname + '\nСредняя оценка за домашние задания: ' + str(self.grade_item_student()) + '\nКурсы в процессе изучения: '+str(", ".join(self.courses_in_progress))+'\nЗавершенные курсы: '+str(", ".join(self.finished_courses))

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Not a Student!')
            return
        return self.grade_item_student() < other.grade_item_student()

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

    def grade_item_lecturer(self):
        ocenka = map(sum, list(self.grades_for_lectures.values()))
        ocenka = list(ocenka)
        count_ocenka = map(len, list(self.grades_for_lectures.values()))
        count_ocenka = list(count_ocenka)
        result_ocenka = sum(ocenka) / sum(count_ocenka)
        return result_ocenka

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Not a Lecturer!')
            return
        return self.grade_item_lecturer() < other.grade_item_lecturer()

    def __str__(self):
        return 'Имя: ' + self.name + '\nФамилия: ' + self.surname + '\nСредняя оценка за лекции: ' + str(self.grade_item_lecturer())

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


student1 = Student('Ruoy', 'Eman', 'your_gender')
student1.courses_in_progress += ['Python']
student1.courses_in_progress += ['C++']

student2 = Student('Ruoy2', 'Eman2', 'your_gender2')
student2.courses_in_progress += ['Python']
student2.courses_in_progress += ['C++']

mentor = Mentor('Some', 'Buddy')
mentor.courses_attached += ['Python']


# Reviewer ставит оценки студентам

reviewer = Reviewer('Ivan', 'Popov')
reviewer.courses_attached += ['Python']
reviewer.courses_attached += ['C++']

reviewer.rate_hw(student1, 'Python', 8)
reviewer.rate_hw(student1, 'Python', 8)
reviewer.rate_hw(student1, 'Python', 8)

reviewer.rate_hw(student1, 'C++', 6)
reviewer.rate_hw(student1, 'C++', 6)
reviewer.rate_hw(student1, 'C++', 6)

reviewer.rate_hw(student2, 'C++', 6)
reviewer.rate_hw(student2, 'C++', 6)
reviewer.rate_hw(student2, 'C++', 6)


#print(student1.grades)
print('###')

# Lecturer получают оценки от студентов

lecturer1 = Lecturer('Elena', 'Nikolaeva')
lecturer1.courses_attached += ['Python']
lecturer1.courses_attached += ['C++']

student1.rate_hw_lecturer('Python', lecturer1, 8)
student1.rate_hw_lecturer('Python', lecturer1, 8)

student1.rate_hw_lecturer('C++', lecturer1, 7)
student1.rate_hw_lecturer('C++', lecturer1, 6)

lecturer2 = Lecturer('Viktor', 'Evdeev')
lecturer2.courses_attached += ['Python']
lecturer2.courses_attached += ['C++']

student1.rate_hw_lecturer('C++', lecturer2, 10)
student1.rate_hw_lecturer('C++', lecturer2, 10)




#print(lecturer.grades_for_lectures)

print()

# Проверяем перезагрузку __str__
# print('Проверяем перезагрузку __str__:')
# print(reviewer)
# print()
# print(lecturer)
# print()
# print(student1)
# print(best_student < best_student2)
print(lecturer1.grade_item_lecturer())
print(lecturer2.grade_item_lecturer())

print(lecturer1)
