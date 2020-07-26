import random

def persentage(text, start, finish):
    return text + str(random.randint(start, finish)*10)

#    //////////////////////////////Функція для перевірки на піддавання чомусь стадії ////////////////////////////////////        #
def check_for_stage(exeption_array, random_ability, ability_name, ability_stages):
    random_ability_stage = ability_stages[random.randint(0, len(ability_stages) - 1)]
    for i in exeption_array:
        if random_ability == i:
            print(ability_name + " = " + random_ability)
        else:
            print(ability_name + " = " + random_ability + " " + random_ability_stage)

class Body:
    def __init__(self):

        # //////////////////////////////////////Body///////////////////////////////////////////// #
        self.height = random.randint(155, 200)
        self.weight = random.randint(50, 110)
        imt = self.weight / (self.height / 100 * self.height / 100)
        if imt > 39:
            self.bodyType = "Ожирение"
        elif imt >= 16:
            self.bodyType = "Крепкое"
        else:
            self.bodyType = "Анарексия"
        self.body = "Телосложение: " + self.bodyType + ", Рост: " + str(self.height) + " cм" + ", Вес: " + str(
            self.weight) \
                    + " кг"
        print(self.body)

class Person:
    def __init__(self):

        self.job = ["Педиатр", "Фитнес тренер", "Полицейский", "Физик-ядерщик", "Биолог", "Химик", "Философ", "Блогер",
                    "Диетолог", "Психолог", "Сексолог", "Строитель", "Учитель", "Военний", "Пилот", "Художник"]
        # "Татуировщик", "Президент", "Повар", "Бурильщик", "Хакер", "Бариста", "Акушер", "БиоХимик",
        # "Кондитер", "Хирург", "Инжирен", "Инструктор по выживанию", "Бугалтер", "Ландшафтный дизайнер",
        # "Животновод", "Режисер", "Порноактер", "Ветеринар", "Матрос", "Водитель", "Космонавт", "Пожарник",
        # "Судья", "Имунолог", "Вирусолог", "Священник"]

        # //////////////////////////////////////Health///////////////////////////////////////////// #
        self.health = ["Совершенно здоров", "Совершенно здоров", "Совершенно здоров", "Совершенно здоров",
                       "Совершенно здоров", "Совершенно здоров", "Совершенно здоров", "Совершенно здоров",
                       "Совершенно здоров", "Алергия на шерсть", "Безплоден", "Ампутирована рука", "Слепота", "Псориаз"
                        , "Туберкулез", "Биполярное розстройство", "Альц Геймер", "Парализован ниже пояса", "Отсутствие"
                        " обояния", "Сахарный диабет", "Алергия", "Астма", "Алкоголизм", "Тремор", "Дальтонизм",
                       "Анальгия(Нечуствительность к боли)", "Безсонница", "Синтром Турета", "Шизофрения", "Грыжа",
                       "Синдром Мюнхаузена", "Ветрянка", "Епилепсия", "Дифект речи"]
        self.no_health_stages = ["Совершенно здоров"]
        print(len(self.health))

        self.health_stages = [" В ремисии", " В ремисии", " 10%", " 20%", " 30%", " 40%", " 50%", " 60%", " 70%",
                              " 80%", " 100%"]

        # //////////////////////////////////////Phobia///////////////////////////////////////////// #
        self.phobia = ["Без фобий", "Без фобий", "Без фобий", "Без фобий", "Без фобий", "Без фобий", "Мусофобия(боязнь крыс)"
                       "(Боязнь плателиновых мультиков)", "Венустрофобия (Страх красивых щенщин)", "Ергазиофобия (страх"
                       " оперировать)", "Коулрофобия(Страх клоунов)", "Интернетофобия(Боязнь интернета)"
                       "Арахнофобия(боязнь пауков)", "Клаустрофобия", "Ортофобия(Боязнь птиц и их оперения)"
                       , "Кинофобия(боязнь собак)", "Гемофобия(боязнь крови)", "Некрофобия(страх трупов и нежети)",
                       "Фобофобия(Боязнь чужих фобий)", "Демонофобия(Боязнь демонов)", "Тетрофобия(Боязнь числа 4 )",
                       "Спектрофобия(Боязнь призраков)", "Аквафобия(Боязнь воды)", "Танатофобия(Боязнь смерти)",
                       "Акустикофобия(Боязнь громких звуков)", "Боязнь шерсти", "Боязнь темноти", "Акрофобия(Боязнь "
                       "высоты)", "Аутофобия (Боязнь оставаться наедине)", "Боязнь грязи", "Боязнь костей"]
        print(len(self.phobia))


        # //////////////////////////////////////Hobby///////////////////////////////////////////// #
        self.hobby = ["Животноводство", "Парусний спорт", "Рибалка", "Бадминон", "Кепминг", "Футбол",
                      "Реставрация поверхностей", "Готовка", "Астрономия", "Радиосвязь", "Оригами", "Стенд ап", "Химия"
                      , "Решение задач по физике", "Очищение воды", "Просмотр фильмов", "Ориентирование на местности",
                      "Яой", "Копрофилия"]

        # //////////////////////////////////////item///////////////////////////////////////////// #
        self.item = ["Сборник 100 лутшых фильмов", "Удочка и снасти для рыбалки", "Инкубатор и набор яиц для выращивания"
                     , "Снайперская винтовка и 150 патронов", "Пистолет Макарова и 60 патронов", "Набор наручных часов",
                     "Покерный набор", "Аптечка первой помощи", "Набор фельшера", "Ноутбук", "5 Кг Кофе", "Грудной ребенок",
                     "Биноколь", "Генератор", "Канистра бензина", "Набор для рисования", "Средства для очистки воды",
                     "Средства от насекомых всех видов", "Словарь Даля", "Библия", "Игральные карты", "Самурайский меч",
                     "Набор семьян", "5 литров вина", "Собака", "Кошка", "Попугай"]

        self.dopInfo = ["Знал президента", "Переспал(ла) с порнозвездой", "Проходил курси психолога",
                        "Проходил курси сексолога", "Воевал в Сирии", "Обокрал деда", "Обокрал банк", "Получил красный"
                        "диплом в 15 лет", "Могу оказать первую мед помощ", "Перечитал все книги о властелине колец",
                        "Может спать неделю не просипаясь", "бу", "bu"]

        self.humanTrait = ["Параноик", "Зануда", "Конфликтный", "Настойчивый", "Жизнерадосний", "Скучний", "Понимающий",
                           "ЧСВ", "Чудесен", "Нимфоманка", "Пацифист", "Інтроверт", "Екстраверт", "Невротизм",
                           "Откровенность"]

        self.random_job = self.job[random.randint(0, len(self.job) - 1)]
        self.random_hobby = self.hobby[random.randint(0, len(self.hobby) - 1)]
        self.random_dop_info = self.dopInfo[random.randint(0, len(self.dopInfo) - 1)]
        self.random_human_trait = self.humanTrait[random.randint(0, len(self.humanTrait) - 1)]
        self.biological = "Мужчина"
        self.childFree = "Не чайлд фри"
        self.health = "Совершенно здоров"
        self.phobia = "Без фобий"
        self.random_age = 0
        self.stag = 0
        self.age = 0

        self.create_character()

    def create_character(self):
        self.random_job = self.job[random.randint(0, len(self.job) - 1)]
        self.job.remove(self.random_job)
        self.random_hobby = self.hobby[random.randint(0, len(self.hobby) - 1)]
        self.hobby.remove(self.random_hobby)
        self.random_dop_info = self.dopInfo[random.randint(0, len(self.dopInfo) - 1)]
        self.dopInfo.remove(self.random_dop_info)
        self.random_human_trait = self.humanTrait[random.randint(0, len(self.humanTrait) - 1)]
        self.humanTrait.remove(self.random_human_trait)

        # ///////bio////////    #
        if random.randint(0, 2) == 0:
            self.biological = "Мужчина"
        else:
            self.biological = "Женщина"

        if random.randint(0, 11) > 7:
            self.childFree = "Чайлд фри"
        else:
            self.childFree = "Не чайлд фри"

        self.random_age = random.randint(18, 80)
        self.stag = random.randint(0, self.random_age - 18)
        self.age = "Возрост - " + str(self.random_age) + " лет"

        # /////////////////////////Health///////////////////////////////////// #
        random_health = random.randint(1, 101)
        if random_health < 36:
            self.health = "Совершенно здоров"
        elif random_health < 40:
            self.health = "Алергия на шерсть"
        elif random_health < 44:
            self.health = "Безплоден"  # записуємо результат в масів і в кінці сравнюємо чи результат не дорівнює значенню масіву
        elif random_health < 48:
            self.health = "Ампутированая рука"
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

        # /////////////////////////Phobia///////////////////////////////////// #

        random_phobia = random.randint(1, 101)
        if random_phobia < 24:
            self.phobia = "Без фобий"
        elif random_phobia < 28:
            self.phobia = "Арахнофобия(Боязнь пауков)"
        elif random_phobia < 32:
            self.phobia = "Клаустрофобия"
        elif random_phobia < 36:
            self.phobia = "Ортофобия(боязнь птиц и их перьев)"
        elif random_phobia < 40:
            self.phobia = "Кинофобия(боязнь собак)"
        elif random_phobia < 44:
            self.phobia = "Гемофобия(страх крови)"
        elif random_phobia < 48:
            self.phobia = "Некрофобия(Страх трупов и нежети)"
        elif random_phobia < 52:
            self.phobia = "Фобофобия(боязнь чужих фобий)"
        elif random_phobia < 56:
            self.phobia = "Боязнь демонов"
        elif random_phobia < 60:
            self.phobia = "Тетрафобия(боязнь числа 4)"
        elif random_phobia < 64:
            self.phobia = "Боязнь призраков"
        elif random_phobia < 68:
            self.phobia = "Аквафобия"
        elif random_phobia < 72:
            self.phobia = "Танатофобия (Страх смерти)"
        elif random_phobia < 76:
            self.phobia = "Акустикофобия(Страх громких звуков)"
        elif random_phobia < 80:
            self.phobia = "Боязнь шерсти"
        elif random_phobia < 84:
            self.phobia = "Боязнь темноты"
        elif random_phobia < 88:
            self.phobia = "Акрофобия(Боязнь высоты)"
        elif random_phobia < 92:
            self.phobia = "Боязнь быть одному"
        elif random_phobia < 96:
            self.phobia = "Боязнь грязи"
        else:
            self.phobia = "Боязнь костей"

        print("\n" + "             Характеристики персонажа" + "\n")
        check_for_stage(self.no_health_stages, self.health, "Состояние здоровья", self.health_stages)
        print("Биологическая характеристика = " + str(self.age) + "  " + self.biological + "  " + self.childFree)
        print("Професия = " + self.random_job + ", стаж: " + str(self.stag))
        print("Хобби = " + self.random_hobby)
        print("Доп инфа = " + " " + self.random_dop_info)
        print("Человеческая черта = " + self.random_human_trait)
        print("Фобия = " + self.phobia)
        Body()
Person()

class Catastrophe:
    def __init__(self):
        self.population = persentage("Популяция людей составляет - ", 8, 27) + " милионов"

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
                            "первое правило робототехники - не навреди человеку, люди успели спастись в аналоговых бункерах "
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

        #print("\n" + "             Информация про катастрофу" + "\n")
        #print(catastrophe_name_random)
        #print(random_description)
        #print(self.population)

Catastrophe()

class Bunker:
    def __init__(self):
        self.inventory = ["Книги по строительству", "Книги по имунологии и врачебному делу", "Аптечка с литием(для "
        "душевно больных) на 1 год", "Станцыя для очистки воды", " ", "Набор настольных игр", "Любительская рация"
        " на 1 человека", "Аптечка первой помощи 5 штук", "Аптечка первой помощи 10 штук", "Запас вина на на 3 месяца на"
        "всех учасников бункера", "Аптечка с литием(для душевно больных) на 4 месяца на 2 человека"]

        self.rooms = ["Кухня-столовая", "Оборудованая теплица с набором семьян", "Оборудованая теплица", "Компютерная "
        "комната", "Оружейная", "Кухня", "Мастерская", " ", " "]

        self.size = persentage("Розмер бункера = ", 7, 17) + "м2"

        # //////////Initiation ////////////////// #
        random_inventory = self.inventory[random.randint(0, len(self.inventory) - 1)]
        random_rooms = self.rooms[random.randint(0, len(self.rooms) - 1)]

        #print("\n" + "             Информация про бункер" + "\n")
        #print("Инвентарь бункера: " + random_inventory)
        #print("Доступные комнати: " + random_rooms)
        #print(self.size)

Bunker()

def characteristic_chooser(text, array):
    random_characteristic = array[random.randint(0, len(array) - 1)]
    #print(text + random_characteristic)

#   ///////// Присети для кількості гравців ///////////// #



            #self.selected_health = []
            #switch = 1
            #for i in self.selected_health:
            #    if self.health != self.selected_health[i]:
            #        self.switch = 1
            #    else:
            #        self.switch = 0
            #        random_health()

            #if switch == 1:
            #    print("Здоровье = " + self.health)
            #    self.selected_health = self.selected_health.append(self.health)
            #    self.switch = 0