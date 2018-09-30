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
    def __init__(self, cl_num_lett, quantity):
        self.cl_num_lett = cl_num_lett
        self.quantity = quantity
        self.teachers = set()

    def add_teacher(self, teacher):
        self.teachers.add(teacher)

    pass


class Pupil:
    def __init__(self, name, klass, parents):
        self.name = name
        self.klass = klass
        self.parents = parents

#    def participate(self, lesson):
#        """присоединится к лекции."""
#        lesson.add_pupil(self)

    def display_information(self):
        """Печатает информацию о студенте"""
        print('Pupil: ', self.name)
        print('Class:', self.klass)
        print('Parents: ', self.parents)
#        print("lessons:")
#        for l in lessons.lessons_by_student(self):
#            print(l)


class Teacher:
    def __init__(self, name, lesson):
        self.name = name
        self.lesson = lesson
        self.klasses = set()

    def participate(self, klass):
        self.klasses.add(klass)


    def display_information(self):
        print('Teacher: ', self.name)
        print('lesson: ', self.lesson)

class Teachers_collection:
    def __init__(self):
        self.teachers = []

pupils = [
          Pupil('Жуков И.А.', '1 А', 'Жукова Елена, Жуков Андрей'),
          Pupil('Ефремов О.Г.', '2 Б', 'Ефремова Оксана, Ефремов Григорий'),
          Pupil('Павлов Н.С.', '1 А', 'Павлова Мария, Павлов Сергей'),
          Pupil('Ватутина А.К.', '3 А', 'Ватутина Наталия, Ватутин Константин'),
          Pupil('Говоров Л.А.', '3 В', 'Говорова Екатерина, Говоров Андрей'),
          Pupil('Голиков Ф.И.', '3 В', 'Голикова Ольга, Голиков Илья'),
          Pupil('Голубев К.Д.', '1 Б', 'Голубева Ирина, Голубев Дмитрий'),
          Pupil('Горбатов А.В.', '2 А', 'Горбатова Екатерина, Горбатов Василий'),
          Pupil('Гореленко Ф.Д.', '3 Б', 'Гореленко Анна, Гореленко Данила'),
          Pupil('Ерёменко А.И.', '1 В', 'Ерёменко Марина, Ерёменко Иван'),
          Pupil('Жадов А.С', '1 Б', 'Жадова Людмила, Жадов Семён'),
          Pupil('Журавлёв Е.П.', '2 А', 'Журавлёва Наталья, Журавлёв Пётр'),
          Pupil('Зайцев В.А.', '2 В', 'Зайцева Василиса, Зайцев Александр'),
          Pupil('Иванов Ф.С.', '3 А', 'Иванова Евгения, Иванов Сергей')
         ]

teachers = [
            Teacher('Владимир Петрович', 'русский язык'),
            Teacher('Ольга Игоревна', 'русский язык'),
            Teacher('Вера Павловна', 'литература'),
            Teacher('Елена Прокофьевна', 'математика'),
            Teacher('Ирина Васильевна', 'математика'),
            Teacher('Игорь Маркович', 'физкультура'),
            Teacher('Ольга Андреевна', 'английский язык')
           ]



klass_list = set()
kl_to_list = Klass(input("Введите класс в формате 1 А (цифра пробел буква)-->"), 0)
print(f"Список учеников класса {kl_to_list.cl_num_lett}")
for pupil in pupils:
    klass_list.add(pupil.klass)
    if pupil.klass == kl_to_list.cl_num_lett:
        kl_to_list.quantity += 1
        print(kl_to_list.quantity, '. ', pupil.name)
print(f'Всего в классе {kl_to_list.cl_num_lett} - {kl_to_list.quantity} ученик(а, ов).')
input('Нажмите Enter')
print('Список всех классов:', sorted(klass_list))
input('Нажмите Enter')
print("Все ученики школы:")
for i, pupil in enumerate(pupils):
    print(f'{i + 1}. {pupil.name}')
print('Родители: ', pupils[int(input('Выберите ученика по номеру, чтобы узнать его родителей:-->')) - 1].parents)

# 3. Получить список всех предметов указанного ученика
#  (Ученик --> Класс --> Учителя --> Предметы)

chosen_pupil = pupils[int(input('Выберите ученика по номеру, чтобы узнать его предметы:-->')) - 1]
print(chosen_pupil.name, ', ', chosen_pupil.klass)

