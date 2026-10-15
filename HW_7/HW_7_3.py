#3. Создайте программу, имитирующую работу клиники. Создайте базовый
#класс Doctor с методом treat(). От него создайте три дочерних класса:
#Surgeon, Dentist и Therapist. В каждом дочернем классе
#переопределите метод treat(), чтобы каждый врач выводил сообщение
#о своём способе лечения.
#Создайте класс Patient, содержащий атрибуты treatment_plan — код
#плана лечения и doctor — назначенный пациенту врач. В классе
#Therapist реализуйте метод назначения врача пациенту. Если код плана
#лечения равен 1, пациенту назначается хирург; если код равен 2 —
#дантист; при любом другом значении — терапевт.
#После назначения врача необходимо сохранить соответствующий объект
#врача в patient.doctor и вызвать у него метод treat(). Создайте
#пациента, задайте ему план лечения и продемонстрируйте работу
#программы.


class Doctor:
    def treat(self):
        print("I'm a Doctor")


class Surgeon(Doctor):
    def treat(self):
        print("План лечения: 1. Предоперационная подготовка \n 2.Хирургическое вмешательство \n "
              "3.Послеоперационный контроль")


class Dentist(Doctor):
    def treat(self):
        print("План лечения: Первичный осмотр и диагностика")


class Therapist(Doctor):
    def treat(self):
        print("План лечения: Направление на диагностику")

    @staticmethod
    def method_of_treatment(patient :Patient):
        if patient.treatment_plan == 1:
            patient.doctor = Surgeon()
            print(f"Пациент: {patient.name} направлен/а к специалисту: Хирург")
        elif patient.treatment_plan == 2:
            patient.doctor = Dentist()
            print(f"Пациент: {patient.name} направлен/а  к специалисту: Стоматолог")
        else:
            patient.doctor = Therapist()
            print(f"Пациент: {patient.name} направлен/а   к специалисту: Терапевт")



class Patient:
    doctor = Doctor()

    def __init__(self, name, treatment_plan):
        self.name = name
        self.treatment_plan = treatment_plan


user = Patient('Пальчикова Галина Сергеевна', 1)
Therapist.method_of_treatment(user)

user_2 = Patient('Зубков Перт Иванович', 2)
Therapist.method_of_treatment(user_2)
