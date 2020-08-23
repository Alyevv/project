class Students:

   def __init__(self, code,  name, surname, email, tell_number):  #telebe melumatlari
        self.code = code
        self.name = name
        self.surname = surname
        self.email = email
        self.tell_number = tell_number

        
class Sinif:



    number_of_students = 0    #telebelerin sayi
    max_students = 10  # max tələbələrin sayı

    def __init__(self, name, max_students):  #sinifin melumatlari
        self.name = name
        self.max_students = max_students
        self.students = []
        Sinif.number_of_students += 1


    def add_student(self, student):
        if len(self.students) < self.max_students:  #telebenin sayi max telebe sayindan azdirsa teze telebe elave etmek olar
            self.students.append(student)
            return True
        if len(self.students > self.max_students):
            self.students.remove(student)
            return True
        return False

    def get_code(self):
        pass




Telebe_1 = Students(192, "Cavid", "Əliyev", "markmarkul@mail.ru", +994515542854)
Telebe_2 = Students(743, "Fidan", "Nağıyeva", "fidannagiyeva@mail.ru", +994552788554)
Telebe_3 = Students(254, "Rüstəm", "Ismayıllı", "rustemismayil23@gmail.com", +994504567632)
Telebe_4 = Students(248, "Jalə", "Məmmədova", "jaelmmdva@gmail.com", +994512334321)
Telebe_5 = Students(456, "İlqar", "Yoldaşov", "ilqaryoldash65@mai;.ru", +994515523422)
Telebe_6 = Students(642, "Mamed", "Əzizov", "mamedaziz4545@mail.ru", +994514732173)
Telebe_7 = Students(744, "Aytən", "Kərimli", "aytenkharim@mail.ru", +994553246624)
Telebe_8 = Students(871, "Ziyadxan", "Ziyadxanov", "zikoqusar2233@mail.ru", +994506774821)
Telebe_9 = Students(524, "Nihad", "Sadıqov", "nidahxpert@gmail.ru", +994502245634)
Telebe_10 = Students(623, "Nurlan", "Novruzov", "nurlannovruz@mail.ru", +994504723277)


sinif = Sinif("Pragmatech", 10)

sinif.add_student(Telebe_1)
sinif.add_student(Telebe_2)
sinif.add_student(Telebe_3)
sinif.add_student(Telebe_4)
sinif.add_student(Telebe_5)
sinif.add_student(Telebe_6)
sinif.add_student(Telebe_7)
sinif.add_student(Telebe_8)
sinif.add_student(Telebe_9)
sinif.add_student(Telebe_10)



print(Telebe_9.name)      # telebenin adi gosterilir
print(Telebe_2.surname)   # telebenin soyadi gpsterilir
print(Telebe_8.code)      # telebenin kodu gosterilir

