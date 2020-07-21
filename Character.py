import random

def persentage( text, start, finish):
    return text + str(random.randint(start, finish)*10)


class Person:
    def __init__(self):
        self.job = ["Педиатр", "Фитнес тренер", "Полицейский", "Физик-ядерщик", "Биолог", "Химик", "Философ", "Блогер",
                    "Диетолог", "Психолог", "Сексолог", "Строитель", "Учитель", "Военний", "Пилот", "Художник",
                    "Татуировщик", "Президент", "Повар", "Бурильщик", "Хакер", "Бариста", "Акушер", "БиоХимик",
                    "Кондитер", "Хирург", "Инжирен", "Инструктор по выживанию", "Бугалтер", "Ландшафтный дизайнер",
                    "Животновод", "Режисер", "Порноактер", "Ветеринар", "Матрос", "Водитель", "Космонавт", "Пожарник",
                    "Судья", "Имунолог", "Вирусолог"]
        self.hobby = ["Животноводство", "Парусний спорт", "Рибалка", "Бадминон", "Кепминг", "Футбол",
                      "Реставрация поверхностей", "Готовка", "Астрономия", "Радиосвязь", "Оригами", "Стенд ап"]
        self.age = "Возрост = "+str(random.randint(18, 91)) + "лет"

        # ///////bio////////    #
        if random.randint(0, 2) == 0:
            self.biological = "Мужчина"
        else:
            self.biological = "Женщина"

        if random.randint(0, 11) > 7:
            self.childFree = "Чайлд фри"
        else:
            self.childFree = "Не чайлд фри"
        self.dopInfo = ["Знал президента", "Переспал(ла) с порнозвездой", "Проходил курси психолога",
                        "Проходил курси сексолога", "Воевал в Сирии", "Обокрал деда", "Обокрал банк", "Получил красный"
                        "диплом в 15 лет", "Могу оказать первую мед помощ", "Перечитал все книги о властелине колец"]
        self.humanTrait = ["Параноик", "Зануда", "Конфликтный", "Настойчивый", "Жизнерадосний", "Скучний", "Понимающий",
                           "ЧСВ", "Чудесен", "Нимфоманка", "Пацифист"]


        self.phobia = ["Арахнофобия", "Без фобий", "Клаустрофобия", "Ортофобия(боязнь птиц и их перьев)", "Кинофобия",
                       "Фобофобия(боязнь чужих фобий)", "Боязнь демонов", "Боязнь числа 4", "Боязнь призраков",
                       "Боязнь шерсти", "Боязнь темноты", "Боязнь высоты", "Боязнь быть одному"]


        random_health = random.randint(1, 101)
        if random_health < 40:
            self.health = "Совершенно здоров"
        elif random_health < 44:
            self.health = "Безплоден"
        elif random_health < 48:
            self.health = "Потерял левую руку"
        elif random_health < 52:
            self.health = "Слепота"
        elif random_health < 56:
            self.health = "Псориаз"
        elif random_health < 60:
            self.health = "Туберкульоз"
        elif random_health < 64:
            self.health = "Биполярка"
        elif random_health < 68:
            self.health = "Альц Геймер"
        elif random_health < 72:
            self.health = "Парализован ниже пояса"
        elif random_health < 76:
            self.health = "Отсутствие обояния"
        elif random_health < 80:
            self.health = "Сахарный диабет"
        elif random_health < 84:
            self.health = "Алергия"
        elif random_health < 88:
            self.health = "Астма"
        elif random_health < 92:
            self.health = "Алкоголизм"
        elif random_health < 96:
            self.health = "Тремор"
        else:
            self.health = "Дальтонизм"

            # //////////Initiation ////////////////// #
        random_job = self.job[random.randint(0, len(self.job)-1)]
        random_hobby = self.hobby[random.randint(0, len(self.hobby)-1)]
        random_dop_info = self.dopInfo[random.randint(0, len(self.dopInfo)-1)]
        random_human_trait = self.humanTrait[random.randint(0, len(self.humanTrait)-1)]
        random_phobia = self.phobia[random.randint(0, len(self.phobia)-1)]

        print("Робота = "+random_job)
        print("Хобби = " + random_hobby)
        print("Доп инфа = " + random_dop_info)
        print("Человеческая черта = " + random_human_trait)
        print("Фобия = " + random_phobia)
        print("Биологическая характеристика = " + str(self.age)+"  " + self.biological+"  " + self.childFree)
        print("Здоровье = " + self.health)


Person()
class Body:
    def __init__(self):
        self.height = random.randint(150, 200)
        self.weight = random.randint(40, 150)
        IMT = self.weight/(self.height*self.height/100)
        

class Catastrophe:
    def __init__(self):
        self.catastropheName = ["Падение метеорита", "Всемирный потоп", "Зомби-апокалипсис", "Востание машин"]
                                #"Ядерная война", "Химическая война", "Ядерная зима", "Нападения демонов",
                                #"Колонизация марса", "Планета захвачена приматами", "Извержение вулканов", "Епидемия",
                                #"Епидемия мозговых червей", "Вспышки на солнце", "Гражданская война"]

        catastrophe_name_random = self.catastropheName[random.randint(0, len(self.catastropheName)-1)]

        self.description = {"Падение метеорита": persentage("Ученые не смогли предотвратить падение метеорита"
                            ", инфраструктура нарушена, небольшой процент населения успел спрятаться в бункери, "
                            "разрушения местности - ", 4, 8)+" %. "+"Наблюдаються"
                            "проблеми с очисткой почвы и ее плодородностю, продолжением рода и обеспечением пищи после "
                            "выхода из бункера и позобновлением инфраструктури.",
                            # ////////////////////////////// Новий сценарій////////////////////////////////////////// #
                            "Всемирный потоп": persentage("В последствие глобального потепления вся планета "
                            "покрыта водой, процент суши - ", 0, 2)+" %."
                            " Наблюдаються проблеми с очисткой воды, продолжением рода и обеспечением пищи после"
                            " выхода из бункера.",
                            # ////////////////////////////// Новий сценарій////////////////////////////////////////// #
                            "Зомби-апокалипсис": persentage("Богатая корпорация не удержала испытания вируса под"
                            " контролем и породила зомби епидемию, розрушения - ", 5, 9) +
                            "% . Люди после выхода нуждаються в самозащите, "
                            "продолжением рода и обеспечением себя пищей. ",
                            # ////////////////////////////// Новий сценарій////////////////////////////////////////// #
                            "Востание машин": persentage("Скайнет вышел из под контроля и роботы смогли отключить "
                            "первое правило робототехники - не навреди человеку, "
                            "глобальные розрушения -  ", 6, 9) +
                            "% . Люди после выхода"
                            " сильно нуждаются в защите человечества, обеспечении еди, продолжения рода, и возвращение"
                            " земли.",
                            # ////////////////////////////// Новий сценарій////////////////////////////////////////// #
                            "Ядерная война": persentage("", 6, 9) + "Люди после выхода"
                            " сильно нуждаются в защите человечества, обеспечении еди, продолжения рода, и возвращение"
                            " земли",
                            }

        random_description = self.description[catastrophe_name_random]
        print(random_description)


Catastrophe()