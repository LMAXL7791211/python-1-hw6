# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать
# в неограниченном кол-ве классов свой определенный предмет.
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе


# Класс Ученик (Родители (мама, папа)) Учитель(предмет)

class Klass:
    def __init__(self, cl_num_lett):
        self.cl_num_lett = cl_num_lett
        self.teachers = set()
        self.pupils = list()

    def add_pupil(self, pupil):
        self.pupils.append(pupil)

    def add_teacher(self, teacher):
        self.teachers.add(teacher)

    def display_num_lett(self):
        print(self.cl_num_lett, end=', ')

    def display_pupils_name_list(self):
        print(f"Список учеников класса {self.cl_num_lett}:\n")
        for i, pupil_klass in enumerate(self.pupils):
            print(f'{i+1}. {pupil_klass.name}')
        print(f"ИТОГО {len(self.pupils)} ученик (а, ов).")

    def display_teachers(self):
        print(f"Список учителей и предметов класса {self.cl_num_lett}:\n")
        for i, teacher_klass in enumerate(self.teachers):
            print(f'{i+1}. {teacher_klass.name} - {teacher_klass.lesson}')
        print(f"ИТОГО {len(self.teachers)} учителей (я, ь) и предметов (а).")


class Pupil:
    def __init__(self, name, klass, parents):
        self.name = name
        self.klass = klass
        self.parents = parents

    def participate(self, klass):
        """присоединится к лекции."""
        klass.add_pupil(self)

    def display_information(self):
        """Печатает информацию о студенте"""
        print('Pupil: ', self.name)
        print('Class:', self.klass)
        print('Parents: ', self.parents)


class Teacher:
    def __init__(self, name, lesson):
        self.name = name
        self.lesson = lesson


    def display_information(self):
        print('Teacher: ', self.name)
        print('lesson: ', self.lesson)


klasses = [
           Klass('1 А'),  # 0
           Klass('1 Б'),  # 1
           Klass('1 В'),  # 2
           Klass('2 А'),  # 3
           Klass('2 Б'),  # 4
           Klass('2 В'),  # 5
           Klass('3 А'),  # 6
           Klass('3 Б'),  # 7
           Klass('3 В'),  # 8
]

pupils = [
          Pupil('Жуков И.А.', klasses[0].cl_num_lett, 'Жукова Елена, Жуков Андрей'),
          Pupil('Ефремов О.Г.', klasses[4].cl_num_lett, 'Ефремова Оксана, Ефремов Григорий'),
          Pupil('Павлов Н.С.', klasses[0].cl_num_lett, 'Павлова Мария, Павлов Сергей'),
          Pupil('Ватутина А.К.', klasses[6].cl_num_lett, 'Ватутина Наталия, Ватутин Константин'),
          Pupil('Говоров Л.А.', klasses[8].cl_num_lett, 'Говорова Екатерина, Говоров Андрей'),
          Pupil('Голиков Ф.И.', klasses[8].cl_num_lett, 'Голикова Ольга, Голиков Илья'),
          Pupil('Голубев К.Д.', klasses[1].cl_num_lett, 'Голубева Ирина, Голубев Дмитрий'),
          Pupil('Горбатов А.В.', klasses[3].cl_num_lett, 'Горбатова Екатерина, Горбатов Василий'),
          Pupil('Гореленко Ф.Д.', klasses[7].cl_num_lett, 'Гореленко Анна, Гореленко Данила'),
          Pupil('Ерёменко А.И.', klasses[2].cl_num_lett, 'Ерёменко Марина, Ерёменко Иван'),
          Pupil('Жадов А.С', klasses[1].cl_num_lett, 'Жадова Людмила, Жадов Семён'),
          Pupil('Журавлёв Е.П.', klasses[3].cl_num_lett, 'Журавлёва Наталья, Журавлёв Пётр'),
          Pupil('Зайцев В.А.', klasses[2].cl_num_lett, 'Зайцева Василиса, Зайцев Александр'),
          Pupil('Иванов Ф.С.', klasses[6].cl_num_lett, 'Иванова Евгения, Иванов Сергей'),
          Pupil('Ионов К.Т.', klasses[5].cl_num_lett, 'Ионова Арина, Ионов Тимофей')
]

teachers = [
            Teacher('Владимир Петрович', 'русский язык'),
            Teacher('Ольга Игоревна', 'окружающий мир'),
            Teacher('Вера Павловна', 'литература'),
            Teacher('Елена Прокофьевна', 'математика'),
            Teacher('Ирина Васильевна', 'музыка'),
            Teacher('Игорь Маркович', 'физкультура'),
            Teacher('Ольга Андреевна', 'английский язык')
]

total_subjects = 0
for i, teacher in enumerate(teachers):  # заполнение классов учителями
    for j in range(7):
        total_subjects += 1
        klasses[total_subjects % 9].add_teacher(teacher)


# 1. Получить полный список всех классов школы
print('Список всех классов:')

for i, klass in enumerate(klasses):
    print(f'{i + 1}. {klass.cl_num_lett}')
    for pupil in pupils:
        if klass.cl_num_lett == pupil.klass:  # заполнение классов учениками
            pupil.participate(klass)


# 2. Получить список всех учеников в указанном классе

kl_to_list = int(input("Выберите класс по номеру, чтобы получить список учеников-->"))
klasses[kl_to_list - 1].display_pupils_name_list()

input('Нажмите Enter для продолжения')

# 5. Получить список всех Учителей, преподающих в указанном классе

kl_to_list = int(input("Выберите класс по номеру, чтобы получить список учителей-->"))
klasses[kl_to_list - 1].display_teachers()

input('\nНажмите Enter для продолжения')

print("Все ученики школы:")
for i, pupil in enumerate(pupils):
    print(f'{i + 1}. {pupil.name}, {pupil.klass}')

# 4. Узнать ФИО родителей указанного ученика

print('Родители: ', pupils[int(input('Выберите ученика по номеру, чтобы узнать его родителей:-->')) - 1].parents)
input('\nНажмите Enter для продолжения')

# 3. Получить список всех предметов указанного ученика
#  (Ученик --> Класс --> Учителя --> Предметы)

chosen_pupil = pupils[int(input('Выберите ученика по номеру, чтобы узнать его предметы:-->')) - 1]
print(chosen_pupil.name, ', ', chosen_pupil.klass)
for klass in klasses:
    if chosen_pupil in klass.pupils:
        print(klass.display_teachers())
