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




def sum_grade_student (student_list, name_kurs):
    # Cредняя оценка за домашние задания по всем студентам
    result_list = []
    for student_item in student_list:
        if name_kurs in student_item.grades:
            result_list.append(sum(student_item.grades[name_kurs])/len(student_item.grades[name_kurs]))

    if result_list:
        result = sum(result_list)/len(student_list)
    else:
        result = 'Указанного курса нет в программе'

    return result

def sum_grade_lecturer (lecturer_list, name_kurs):
    # Средняя оценка за лекции всех лекторов
    result_list = []
    for lecturer_item in lecturer_list:
        if name_kurs in lecturer_item.grades_for_lectures:
            result_list.append(sum(lecturer_item.grades_for_lectures[name_kurs])/len(lecturer_item.grades_for_lectures[name_kurs]))

    if result_list:
        result = sum(result_list)/len(student_list)
    else:
        result = 'Указанного курса нет в программе'

    return result



student1 = Student('Ruoy', 'Eman', 'your_gender')
student1.courses_in_progress += ['Python']
student1.courses_in_progress += ['C++']
student1.finished_courses += ['HTML']

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

reviewer.rate_hw(student1, 'C++', 10)
reviewer.rate_hw(student1, 'C++', 10)
reviewer.rate_hw(student1, 'C++', 10)

reviewer.rate_hw(student2, 'C++', 6)
reviewer.rate_hw(student2, 'C++', 6)
reviewer.rate_hw(student2, 'C++', 6)


lecturer1 = Lecturer('Elena', 'Nikolaeva')
lecturer1.courses_attached += ['Python']
lecturer1.courses_attached += ['C++']

student1.rate_hw_lecturer('Python', lecturer1, 8)
student1.rate_hw_lecturer('Python', lecturer1, 8)

student1.rate_hw_lecturer('C++', lecturer1, 8)
student1.rate_hw_lecturer('C++', lecturer1, 8)

lecturer2 = Lecturer('Viktor', 'Evdeev')
lecturer2.courses_attached += ['Python']
lecturer2.courses_attached += ['C++']

student1.rate_hw_lecturer('C++', lecturer2, 10)
student1.rate_hw_lecturer('C++', lecturer2, 10)

# №3

print(student1)
print()
print(student2)
print()
print(student1 > student2)

print('\n')

print(lecturer1)
print()
print(lecturer2)
print()
print(lecturer1 > lecturer2)




# №4
print('\n')

student_list = [student1, student2]
print(f"Cредняя оценка за домашние задания по всем студентам: {sum_grade_student(student_list, 'C++')}")


lecturer_list = [lecturer1, lecturer2]
print(f"Средняя оценка за лекции всех лекторов: {sum_grade_lecturer(lecturer_list, 'C++')}")