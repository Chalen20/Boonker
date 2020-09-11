# coding:utf-8
import telebot
import config
import random
import threading
import Character
import time

# Створення основних змінних
bot = telebot.TeleBot(config.TOKEN)
pers = Character.Person()
bunker = Character.Bunker()
catastrophe = Character.Catastrophe()
special_cards = Character.SpecialCards(5)

# ідентифікатор повідомлення з таймером
timer_message_id = 0

# додатковеий час для конкретного гравця
time_value = 0

# тимчасова змінна для передачі стартового повідомлення до
# інших функцій (get_ex_callback, start_)
res = 0

# ідентифікатор чату, в якому почалася гра
chat_id = 0

# масив гравців, які зареєструвалися в гру (усі дані)
active_users = []

# масив ідентифікаторів гравців
active_users_id = []

# мінімальна кількість гравців для початку гри
min_users = 0

# час затримки для реєстрації гравців
time_that_start_new_game = 15.0

# список додаткового часу для кожного гравця
list_of_add_time = {}

# номер поточного раунда
round_counter = 1

# список усіх властивостей і параметрів для всіх гравців (по ідентифікатору)
request = {}

# кількість відкритих професій
job_counter = 0

# час на 1 раунд для 1 гравця
time_per_round = 10

# гравець, який зараз вибирає карти
player_that_say = 0

# список типів карт
types = ["Професія", "Хобі", "Додаткова інформація", "Риса характеру", "Фобія", "Біологічна характеристика",
         "Здоров'я", "Статура", "Спеціальна карта 1", "Спеціальна карта 2"]

# список можливих карт для першого раунда
list_for_round1 = [types[0], types[8], types[9]]

# список невідкритих характеристик людей в 1 раунді
list_of_list_of_round1 = {}

# список можливих карт гравців починаючи з 2 раунда
list_for_round2 = [types[0], types[1], types[2], types[3], types[4], types[5], types[6], types[7], types[8], types[9]]

# список невідкритих характеристик гравців починаюси з другого раунда
list_of_list_for_round2 = {}

# Список живих гравців
live_person = []

# тимсчасова зміна для передачі повідомлення відкриття карт
# в особистих повідомленнях, використовується в функціях
# (give_say_to_next_person, start_)
person = 0

# непонятна змінна, але десь використовується
some_counter = 0

# тимчасова змінна, яка використовується для передачі часу
# виклику між функціями (виключення таймера переходу)
timer = 0


# Команда, яка спрацьовує при виклику команди /start
# або початку використання боту
# або додавання нового гравця до бота
# Друкує стартове повідомлення
@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, """Це бот для гри у "Бункер",\n/help - список можливих команд;
/rules - правила гри.""")


# Команда, яка спрацьовує при виклику команди /help
# або натискання на напис /help
# Виводить повідомлення з описом можливих команд
@bot.message_handler(commands=["help"])
def start(message):
    bot.send_message(message.chat.id, "/start - початок використання \n"
                                      "/help - допомога, список можливих команд \n"
                                      "/rules - правила гри \n"
                                      "/start_new_game - розпочати нову гру \n"
                                      "/off - завершити поточну гру і вимкнуи бота \n")


# Створення інлайнової (під повідомленням)
# клавіатури з кнопкою Enter
keyboard = telebot.types.InlineKeyboardMarkup()
keyboard.row(
    telebot.types.InlineKeyboardButton('Enter', callback_data='Enter')
)


# Команда, яка спрацьовує при виклику команди /start_new_game
# Розпочинає нову гру у чатах і суперчатах
@bot.message_handler(commands=['start_new_game'])
def exchange_command(message):
    global chat_id
    chat_id = message.chat.id
    if message.chat.type == "group" or message.chat.type == "supergroup":
        t = threading.Timer(time_that_start_new_game, lambda: start_(message))
        t.start()
        global res
        try:
            res = bot.send_message(chat_id=message.chat.id, text='Зареєстровані гравці :',
                                   reply_markup=keyboard)
            # Запінює повідомлення про початок гри
            bot.pin_chat_message(chat_id=message.chat.id, message_id=res.message_id, disable_notification=False)
        except:
            bot.send_message(chat_id=message.chat.id, text="У бота недостатньо прав для запінювання повідомлень"
                                                           " (надайте їх йому)")
    else:
        bot.send_message(chat_id=message.chat.id, text="Ця команда доступна лише в групових чатах")


# Викликається при натисканні на кнопку
@bot.callback_query_handler(func=lambda call: True)
def iq_callback(query):
    data = query.data

    # Викликається при натисканні на кнопку Enter
    if data.startswith('Enter'):
        get_ex_callback(query)

    # Викликається при натисканні на кнопку Професія
    elif data.startswith(types[0]):
        get_prof_callback(query)

    # Викликається при натисканні на кнопку Спеціальна карта 1
    elif data.startswith(types[8]):
        open_special(types[8], query)

    # Викликається при натисканні на кнопку Спеціальна карта 2
    elif data.startswith(types[9]):
        open_special(types[9], query)

    # Викликається при натисканні на кнопку Хоббі
    elif data.startswith(types[1]):
        get_round_begins_from_two(types[1], query)

    # Викликається при натисканні на кнопку Додаткова інформація
    elif data.startswith(types[2]):
        get_round_begins_from_two(types[2], query)

    # Викликається при натисканні на кнопку Риса характеру
    elif data.startswith(types[3]):
        get_round_begins_from_two(types[3], query)

    # Викликається при натисканні на кнопку Фобія
    elif data.startswith(types[4]):
        get_round_begins_from_two(types[4], query)

    # Викликається при натисканні на кнопку Біологічна характеристика
    elif data.startswith(types[5]):
        get_round_begins_from_two(types[5], query)

    # Викликається при натисканні на кнопку Здоров'я
    elif data.startswith(types[6]):
        get_round_begins_from_two(types[6], query)

    # Викликається при натисканні на кнопку Статура
    elif data.startswith(types[7]):
        get_round_begins_from_two(types[7], query)

    # Викликається при натисканні на кнопку Додати час
    elif data.startswith("add_time"):
        add_time(query)


# Відкриває спеціальну карту
def open_special(type_str, query):
    global some_counter
    keyboard_1 = telebot.types.InlineKeyboardMarkup()
    # Видалити відкриту курту з масивів невідкритих карт
    if len(list_of_list_of_round1[query.from_user.id]) == 3 or \
            (len(list_of_list_of_round1[query.from_user.id]) == 2 and
             types[0] not in list_of_list_of_round1[query.from_user.id]):
        some_variable = list_of_list_of_round1[query.from_user.id]
        print(list_for_round1.index(type_str))
        del some_variable[list_for_round1.index(type_str) - some_counter]
        list_of_list_of_round1[query.from_user.id] = some_variable
        some_variable2 = list_of_list_for_round2[query.from_user.id]
        del some_variable2[list_for_round1.index(type_str) - some_counter]
        list_of_list_for_round2[query.from_user.id] = some_variable2
        some_counter += 1
    # Відкрита лише карта у поточному раунді
    if len(list_of_list_of_round1[query.from_user.id]) == 2:
        keyboard_1.row(
            telebot.types.InlineKeyboardButton(list_of_list_of_round1[query.from_user.id][0],
                                               callback_data=str(list_of_list_of_round1[query.from_user.id][0]))
        )
        print(list_of_list_of_round1[query.from_user.id])
        # Замінити кнопку на кнопку з процесією
        bot.edit_message_text(text=query.message.text, message_id=query.message.message_id,
                              chat_id=query.message.chat.id,
                              reply_markup=keyboard_1)
        bot.send_message(chat_id, "@" + query.from_user.username + " - " +
                         str(request[query.from_user.id][list_for_round2.index(type_str)]))
    # Вже була відкрита одна карта спеціальних умов і відкривається ще одна карта у поточному раунді
    elif len(list_of_list_of_round1[query.from_user.id]) == 1:
        bot.edit_message_text(text=query.message.text, message_id=query.message.message_id,
                              chat_id=query.message.chat.id, reply_markup=None)
        bot.send_message(chat_id, "@" + query.from_user.username + " - " +
                         str(request[query.from_user.id][list_for_round2.index(type_str)]))


# Поки безполезна функція (доробити)
def get_round_begins_from_two(type_str, query):
    global job_counter
    list_of_list_for_round2[query.from_user.id].remove(type_str)
    keyboard_1 = telebot.types.InlineKeyboardMarkup()
    for i in list_of_list_for_round2[query.from_user.id]:
        keyboard_1.row(
            telebot.types.InlineKeyboardButton(i, callback_data=str(i))
        )
    bot.edit_message_text(text=query.message.text, message_id=query.message.message_id,
                          chat_id=query.message.chat.id,
                          reply_markup=keyboard_1)
    bot.send_message(chat_id, "@" + query.from_user.username + " - " +
                     str(request[query.from_user.id][0]))
    job_counter += 1
    if job_counter == len(live_person):
        bot.send_message(chat_id, "Дискусія: \n"
                                  "бла \n "
                                  "бла \n "
                                  "бла \n ")


# Функція, яка відкриває професію
def get_prof_callback(query):
    global timer_message_id
    global job_counter
    global round_counter
    global some_counter
    global timer
    keyboard_1 = telebot.types.InlineKeyboardMarkup()
    # Видаляє з масивів використані карти
    if len(list_of_list_of_round1[query.from_user.id]) == 3 or \
            (len(list_of_list_of_round1[query.from_user.id]) == 2 and
             types[0] in list_of_list_of_round1[query.from_user.id]):
        some_variable = list_of_list_of_round1[query.from_user.id]
        del some_variable[0]
        list_of_list_of_round1[query.from_user.id] = some_variable
        some_variable2 = list_of_list_for_round2[query.from_user.id]
        del some_variable2[0]
        list_of_list_for_round2[query.from_user.id] = some_variable2
        some_counter += 1
    # Відкрита лише карта професії
    if len(list_of_list_of_round1[query.from_user.id]) == 2:
        keyboard_1.row(
            telebot.types.InlineKeyboardButton(list_of_list_of_round1[query.from_user.id][0],
                                               callback_data=str(list_of_list_of_round1[query.from_user.id][0]))
        )
        keyboard_1.row(
            telebot.types.InlineKeyboardButton(list_of_list_of_round1[query.from_user.id][1],
                                               callback_data=str(list_of_list_of_round1[query.from_user.id][1]))
        )
        bot.edit_message_text(text=query.message.text, message_id=query.message.message_id,
                              chat_id=query.message.chat.id,
                              reply_markup=keyboard_1)
        bot.send_message(chat_id, "@" + query.from_user.username + " - " +
                         str(request[query.from_user.id][0]))
        job_counter += 1
        timer = threading.Timer(time_per_round, lambda: give_say_to_next_person(query, 1))
        timer.start()
    # Відкрита одна спеціальна карта і карта професій
    elif len(list_of_list_of_round1[query.from_user.id]) == 1:
        bot.edit_message_text(text=query.message.text, message_id=query.message.message_id,
                              chat_id=query.message.chat.id, reply_markup=None)
        bot.send_message(chat_id, "@" + query.from_user.username + " - " +
                         str(request[query.from_user.id][0]))
        timer = threading.Timer(time_per_round, lambda: give_say_to_next_person(query, 1))
        timer.start()
        job_counter += 1
    # Створюється таймер після обговорення
    timer_message = bot.send_message(text="Таймер до кінця раунду", chat_id=query.message.chat.id)
    timer_message_id = timer_message.message_id
    timer_in_button(query, time_per_round, timer_message.message_id, timer_message)
    # Всі відкрили свої професії
    if job_counter == len(active_users):
        bot.send_message(chat_id, "Дискусія: \n"
                                  "бла \n "
                                  "бла \n "
                                  "бла \n ")


# Видалити повідомлення з вибором характеристик у попереднього гравця,
# надати його наступному гравцеві
def give_say_to_next_person(query, from_func):
    time.sleep(3)
    global person
    global player_that_say
    global some_counter
    global timer
    global round_counter
    if from_func == 0:
        timer.cancel()
        print("Cancel")
    some_counter = 0
    print(round_counter)
    if round_counter == 1:
        if player_that_say < len(active_users):
            # Створити кнопки
            keyboard_1 = telebot.types.InlineKeyboardMarkup()
            print(list_of_list_of_round1[active_users[player_that_say].id])
            print("nothing")
            for i in (list_of_list_of_round1[active_users[player_that_say].id]):
                keyboard_1.row(
                    telebot.types.InlineKeyboardButton(i, callback_data=str(i))
                )
            # keyboard_1.row(
            #     telebot.types.InlineKeyboardButton(list_for_round1[0], callback_data=str(list_for_round1[0]))
            # )
            # keyboard_1.row(
            #     telebot.types.InlineKeyboardButton(list_for_round1[1], callback_data=str(list_for_round1[1]))
            # )
            # keyboard_1.row(
            #     telebot.types.InlineKeyboardButton(list_for_round1[2], callback_data=str(list_for_round1[2]))
            # )
            bot.delete_message(chat_id=query.message.chat.id, message_id=person.message_id)
            person = bot.send_message(chat_id=active_users[player_that_say].id,
                                      text="Відкрити карту іншим гравцям (раунд 1)",
                                      reply_markup=keyboard_1)
            for i in range(player_that_say + 1, len(active_users)):
                # ////////////////////////////////////////////////////
                bot.send_message(chat_id=active_users[i].id,
                                 text="Відкриває карти і пояснює свою необхідність гравець - @"
                                      + active_users[player_that_say].username)
            player_that_say += 1
        else:
            round_counter += 1
            bot.send_message(chat_id=chat_id, text="Розпочинається раунд " + str(round_counter))
            player_that_say = 0
    else:
        keyboard_1 = telebot.types.InlineKeyboardMarkup()
        for i in (list_of_list_for_round2[active_users[player_that_say].id]):
            keyboard_1.row(
                telebot.types.InlineKeyboardButton(i, callback_data=str(i))
            )
        if player_that_say < len(active_users):
            bot.delete_message(chat_id=query.message.chat.id, message_id=person.message_id)
            person = bot.send_message(chat_id=active_users[player_that_say].id,
                                      text="Відкрити карту іншим гравцям (раунд " + str(round_counter) + ")",
                                      reply_markup=keyboard_1)
            for i in range(player_that_say + 1, len(active_users)):
                # ////////////////////////////////////////////////////
                bot.send_message(chat_id=active_users[i].id,
                                 text="Відкриває карти і пояснює свою необхідність гравець - @"
                                      + active_users[player_that_say].username)
            player_that_say += 1
        else:
            round_counter += 1
            bot.send_message(chat_id=chat_id, text="Розпочинається раунд " + str(round_counter))
            player_that_say = 0


# Функція, яка створить діючий таймер в кнопці під повідомленням
def timer_in_button(query, time_number, message_id, timer_message):
    global time_value
    time_value = time_number
    # Створить 2 кнопки "Достроково закінчити обговорення" і сам таймер
    keyboard_1 = telebot.types.InlineKeyboardMarkup()
    keyboard_1.row(telebot.types.InlineKeyboardButton("Достроково закінчити обговорення", callback_data="add_time"))
    keyboard_1.row(telebot.types.InlineKeyboardButton(str(time_number), callback_data="timer"))
    try:
        bot.edit_message_text(text=timer_message.text, chat_id=query.message.chat.id, reply_markup=keyboard_1,
                              message_id=message_id)

        if time_number != 0:
            # Рекурсивно викликає цю функцію і обновляє кнопку з таймером
            t = threading.Timer(1.0, lambda: timer_in_button(query, time_number - 1, message_id, timer_message))
            t.start()
        else:
            # Видалення повідомлення з таймером
            try:
                bot.delete_message(chat_id=query.chat.id, message_id=timer_message_id)
                give_say_to_next_person(query, 0)
            except:
                bot.delete_message(chat_id=query.message.chat.id, message_id=timer_message_id)
                give_say_to_next_person(query, 0)
    except:
        print("Exception 250")


# Закоментована функція створить діючий таймер в повідомлені

# def timer_in_message(query, seconds_count, message_id):
#     bot.edit_message_text(text=str(seconds_count), chat_id=query.message.chat.id, message_id=message_id)
#     if seconds_count != 0:
#         t = threading.Timer(1.0, lambda: timer_in_message(query, seconds_count - 1, message_id=message_id))
#         t.start()

# Команда, яка спрацьовує при виклику команди /next_player
# Додає невикористаний час до запасу і видаляє повідомлення з таймером
@bot.message_handler(commands=["next_player"])
def add_time(query):
    global timer_message_id
    list_of_add_time[query.from_user.id] += time_value
    print(list_of_add_time)
    #  удалєніє сообщенія з таймером
    try:
        print(query)
        bot.delete_message(chat_id=query.message.chat.id, message_id=timer_message_id)
        give_say_to_next_person(query, 0)
    except:
        pass
        # bot.delete_message(chat_id=query.chat.id, message_id=timer_message_id)
        # give_say_to_next_person(query, 0)


# def round_(query):
#     global round_counter
#     keyboard_1 = telebot.types.InlineKeyboardMarkup()
#     round_counter += 1
#     for i in list_of_list_for_round2[query.from_user.id]:
#         keyboard_1.row(
#             telebot.types.InlineKeyboardButton(i, callback_data=str(i))
#         )
#     bot.send_message(chat_id=query.from_user.id, text="Відкрити карту іншим гравцям (раунд 2)",
#                      reply_markup=keyboard_1)


# Обробляє напискання на реєстрацію на гру
# Записує у повідомлення реєстрації нікнейм або ім'я або anonymous

def get_ex_callback(query):
    global res, active_users, active_users_id
    bot.answer_callback_query(query.id)
    if query.from_user.username.strip() != "" and query.from_user.id not in active_users_id:
        res.text = res.text + "\n" + "      @" + query.from_user.username
        active_users.append(query.from_user)
        active_users_id.append(query.from_user.id)
        res = bot.edit_message_text(text=res.text, message_id=res.message_id, chat_id=res.chat.id,
                                    reply_markup=keyboard)
    elif query.from_user.username.strip() == "" or query.from_user.id not in active_users_id:
        try:
            res.text = res.text + "\n" + "      " + query.from_user.first_name + " " + query.from_user.last_name
            active_users.append(query.from_user)
            active_users_id.append(query.from_user.id)
            res = bot.edit_message_text(text=res.text, message_id=res.message_id, chat_id=res.chat.id,
                                        reply_markup=keyboard)
        except:
            try:
                res.text = res.text + "\n" + "      " + query.from_user.last_name
                active_users.append(query.from_user)
                active_users_id.append(query.from_user.id)
                res = bot.edit_message_text(text=res.text, message_id=res.message_id, chat_id=res.chat.id,
                                            reply_markup=keyboard)
            except:
                try:
                    res.text = res.text + "\n" + "      " + query.from_user.first_name
                    active_users.append(query.from_user)
                    active_users_id.append(query.from_user.id)
                    res = bot.edit_message_text(text=res.text, message_id=res.message_id, chat_id=res.chat.id,
                                                reply_markup=keyboard)
                except:
                    res.text = res.text + "\n" + "      anonymous"
                    active_users.append(query.from_user)
                    active_users_id.append(query.from_user.id)
                    res = bot.edit_message_text(text=res.text, message_id=res.message_id, chat_id=res.chat.id,
                                                reply_markup=keyboard)


# Функція, яка починається після початку гри і
# кінця часу відведеного на реєстрацію
# Ініціалізує масиви початковими значеннями і надсилає першому
# зареєстрованому гравцеві вибір карт для першого раунду
def start_(message):
    global res, player_that_say, person
    # ініціалізує список невідкритих властивостей для першого раунду
    for i in range(0, len(active_users)):
        some_variable = list_for_round1.copy()
        list_of_list_of_round1[active_users[i].id] = some_variable
    # ініціалізує список невідкритих властивостей для другого раунду
    for i in range(0, len(active_users)):
        some_variable = list_for_round2.copy()
        list_of_list_for_round2[active_users[i].id] = some_variable
    # ініціалізує список додаткового часу для кожного гравця
    for i in range(0, len(active_users)):
        list_of_add_time[active_users[i].id] = 0
    try:
        # видаляє повідомлення реєстрації
        bot.delete_message(message.chat.id, res.message_id)
        bot.delete_message(message.chat.id, message.message_id)
    except:
        print("Exception 333")
    pers_cards = []
    # для кожного зареєстрованого гравця
    # створюється масив його характеристик
    for i in range(0, len(active_users)):
        pers_characteristics = []
        # створити нового персонажа
        pers.create_character()
        # додати роботу
        pers_characteristics.append(pers.random_job)
        # додати стаж
        pers_characteristics.append(pers.stag)
        # додати хоббі
        pers_characteristics.append(pers.random_hobby)
        # додати стаж хоббі
        pers_characteristics.append(pers.random_hobby_stage)
        # додати додаткову інформацію
        pers_characteristics.append(pers.random_dop_info)
        # додати рису характера
        pers_characteristics.append(pers.random_human_trait)
        # додати стаж риси характера
        pers_characteristics.append(pers.random_humanTrait_stage)
        # додати фобію
        pers_characteristics.append(pers.random_phobia)
        # додати вік
        pers_characteristics.append(pers.age)
        # додати біологічну характеристику
        pers_characteristics.append(pers.biological)
        # додати чайлфрі
        pers_characteristics.append(pers.childFree)
        # додати здоров'я
        pers_characteristics.append(pers.random_health)
        # додати статуру
        pers_characteristics.append(pers.bodyType)
        # додати ріст
        pers_characteristics.append(pers.height)
        # додати вагу
        pers_characteristics.append(pers.weight)
        # створити спеціальну карту 1
        special_cards.get_random_card()
        # додати спеціальну карту 1
        pers_characteristics.append(special_cards.random_card)
        # створити спеціальну карту 2
        special_cards.get_random_card()
        # додати спеціальну карту 2
        pers_characteristics.append(special_cards.random_card)
        pers_cards.append(pers_characteristics)

    # якщо кількість гравців більше ніж мінімальна,
    # напишить у груповий чат загальний опис : катастрофу, бункер
    # напишить у особисті повідомлення усі особисті властивості для даного гравця
    if len(active_users) > min_users:
        bot.send_message(message.chat.id, "Гра починається.")
        bot.send_message(message.chat.id, "Тип катастрофи - " + catastrophe.catastrophe_name_random + """. \n""" +
                         catastrophe.random_description +
                         "Бункер: " + "інвентар - " + bunker.random_inventory + "; \n"
                                                                                "Спеціальні кімнати - " + bunker.random_rooms + "; \n" +
                         bunker.size + "; \n" +
                         bunker.random_live_time + ";")
        for i in range(len(active_users)):
            bot.send_message(active_users[i].id,
                             types[0] + ": " + pers_cards[i][0] + ", " + str(pers_cards[i][1]) + "\n" + "\n" +
                             types[1] + ": " + pers_cards[i][2] + ", " + str(pers_cards[i][3]) + "\n" + "\n" +
                             types[2] + ": " + pers_cards[i][4] + "\n" + "\n" +
                             types[3] + ": " + pers_cards[i][5] + ", " + pers_cards[i][6] + "\n" + "\n" +
                             types[4] + ": " + pers_cards[i][7] + "\n" + "\n" +
                             types[5] + ": " + pers_cards[i][8] + ", " + pers_cards[i][9] + ", " + pers_cards[i][
                                 10] + "\n" + "\n" +
                             types[6] + ": " + pers_cards[i][11] + "\n" + "\n" +
                             types[7] + ": " + pers_cards[i][12] + ", " + str(pers_cards[i][13]) + ", " + str(
                                 pers_cards[i][14]) + "\n" + "\n" +
                             types[8] + ": " + pers_cards[i][15] + "\n" + "\n" +
                             types[9] + ": " + pers_cards[i][16])
            # записати в основний список масив характеристик
            array_data = [pers_cards[i][0] + ", " + str(pers_cards[i][1]),
                          pers_cards[i][2] + ", " + str(pers_cards[i][3]), pers_cards[i][4],
                          pers_cards[i][5] + ", " + pers_cards[i][6], pers_cards[i][7],
                          pers_cards[i][8] + ", " + pers_cards[i][9] + ", " + pers_cards[i][10], pers_cards[i][11],
                          pers_cards[i][12] + ", " + str(pers_cards[i][13]) + ", " + str(pers_cards[i][14]),
                          pers_cards[i][15], pers_cards[i][16]]
            request[active_users[i].id] = array_data
        keyboard_1 = telebot.types.InlineKeyboardMarkup()
        keyboard_1.row(
            telebot.types.InlineKeyboardButton(list_for_round1[0], callback_data=str(list_for_round1[0]))
        )
        keyboard_1.row(
            telebot.types.InlineKeyboardButton(list_for_round1[1], callback_data=str(list_for_round1[1]))
        )
        keyboard_1.row(
            telebot.types.InlineKeyboardButton(list_for_round1[2], callback_data=str(list_for_round1[2]))
        )
        time.sleep(5)
        person = bot.send_message(chat_id=active_users[player_that_say].id,
                                  text="Відкрити карту іншим гравцям (раунд 1)",
                                  reply_markup=keyboard_1)
        for i in range(player_that_say + 1, len(active_users)):
            bot.send_message(chat_id=active_users[i].id, text="Відкриває карти і пояснює свою необхідність гравець - @"
                                                              + active_users[player_that_say].username)
        player_that_say += 1
    else:
        bot.send_message(message.chat.id, "На жаль, не можливо провести гру з такою кількістю гравців((\n"
                                          "Мінімальна кількість гравців - " + str(min_users)) + " ."
    try:
        # відкріпити повідомлення з реєстрацією
        # (видалилося воно на початку цього методу)
        bot.unpin_chat_message(chat_id=message.chat.id)
    except:
        print("Exception 417")

    # наступний метод видаляє повідомлення з чату
    # (працює довго і видаляє всі повідомлення з чату)

    # for i in range(0, message.message_id*100):
    #    try:
    #        bot.delete_message(message.chat.id, i)
    #        print("delete")
    #    except:
    #        pass


# Команда, яка спрацьовує при виклику команди /off
# Зупиняє бота і закінчує поточну гру (доробити)
@bot.message_handler(commands=["off"])
def start(message):
    bot.send_message(message.chat.id, "А може не треба?")


# Команда, яка спрацьовує при виклику команди /settings
# Вмикає меню налаштувань бота
@bot.message_handler(commands=["settings"])
def start(message):
    bot.send_message(message.chat.id, "А може не треба?")


# Команда, яка спрацьовує при виклику команди /rules
# Виводить повідомлення з правила гри (доробити / скоротити)
@bot.message_handler(commands=["rules"])
def start(message):
    bot.send_message(
        message.chat.id,
        """ "Бункер" - це дискусійна  карточна гра з постапокалістиним сюжетом.\n
📌 Сюжет: \n
На Землі відбулася катастрофа. Частина людей знаходиться в спеціальному бункері й кожен мріє залишитися в
ньому і вижити. Але кількість місць обмежена: у бункері залишиться лише половина, інші повинні його покинути. \n
Кожної ночі відбувається голосування, на якому учасники вирішують, хто з людей залишиться в бункері.
Фіналісти будуть відроджувати населення Землі. \n
Гравці повинні вибрати найкорисніших учасників для відродження життя на постапокаліптичній планеті.
Саме вони залишаться в бункері. \n
У кожного персонажа є набір характеристик: професія, здоров'я, біологічні характристики, хобі, фобії, 
додаткова інформація, риси характеру. За ними учасники цінюють персонажа, наскільки він буде корисним 
після виходу з бункера. Зброї і насилля немає, лише дискусія і обґрунтування своєї важливості і необхідності.\n
📌 Правила гри: \n
Кількість гравців: не меньше """ + str(min_users) +
        """. Ігрові характеристики розбиті на категорії: \n
☢ Катастрофи - """ + str(len(catastrophe.catastropheName)) + """.
 Вибір катастрофи для гри. Кожна катастрофа має свої характеристики (населення тощо).
 Характеристики персонажа: 
👮️ Професії - """ + str(len(pers.job)) + """ .
🧬 Здоров'я - """ + str(len(pers.health)) + """ .
‍♀ Біологічні характеристики - """ + str(len(pers.biological)) + """ .
❗  Додаткова інформація - """ + str(len(pers.dopInfo)) + """ .
🎭 Риси характеру - """ + str(len(pers.humanTrait)) + """ .
🎳 Хобі - """ + str(len(pers.hobby)) + """ .
🕷Фобії - """ + str(len(pers.phobia)) + """ .
💼 Речі - """ + str(len(pers.item)) + """.
❓ Спеціальних умов - """ + str(len(special_cards.special_cards)) + """ .Вводять нову інформацію для гравців під час гри.
 Характеристики бункера:
🔹 Інвентар - """ + str(len(bunker.inventory)) + """. 
🔸 Спеціальні кімнати - """ + str(len(bunker.rooms)) + """ .
🔹 Розмір - """ + str(len(bunker.size)) + """.""")
    bot.send_message(message.chat.id, """
📌 Правила гри на 14 учасників: 7 з 14 потраплять до бункера, інші 7 залишаться в лісі.
🔸Крок 1 - вибір катастрофи.
Катастрофа - визначає характеристики світу після катастрофи і кількість вижившших на Землі. 
Вибір цієї карти відбувається випадковим чином. \n
Крок 2:
🔹 Кожен гравець отримує характеристики: професію, здоров'я біологічні характеристики, хобі, фобію, додаткову 
інформацію, основну рису характеру, додаткову інформацію (загалом  характеристик) та 2 карти "Cпеціальні умови",
які можна використати підчас гри. Вони не є характеристиками персонажа, а додовнюють гру (імунітет гравця,
заміна професії). Усі характеристи і карти теж видаються в випадковому порядку. 
На початку гри гравець знеособлений і вживається в свого персонажа поступово, з кожною ніччю. У нього немає статі,
віку і інших характеристик, доки він не відкриє перед всіма ігроками відповідну характеристику.
🔸 Крок 3:
1 ніч: Кожний гравець по черзі відкриває характеристику професія і пояснює свою необхідність потрапити в бункер.
Наприклад, карточка з професією "лікар" у гравця 1.
Гравець 1: "Я повинен потрапити в бункер, так як моя професія просто необхідна: ми не перестанемо хворіти,
отримквати травми. Людина без спеціальної освіти не зможе вам допомогти. В 16 столітті люди помирали від простої рани,
необхідно недопустити цього і залишити мене в бункері.
Гравці висловлюються, час відведений на це - 1 хвилина.
Важливо в першу ніч оперувати лише професійними характеристиками, так як ми ще нічого не знаємо про персонажа.
🔹 Крок 4:
Тепере кожен учасник сам вибирає, яку характеристику він хоче відкрити іншим. Гравець може не показувати одну з них до 
кінця гри.
Гравець 1: Відкриває стан здоров'я.
"Я повинен залишитися в бункері, я лікар і я абсолютно здоровий, що говорить про те, що я роботоспрособний і можу 
продовжувати рід."
На це пояснення дається 1 хвилина.
🔸 Крок 5:
Після того як всі відкрили свої 2 характристики, учасники голосуванням видвигають одного кандидата на вибування. Гравці,
котрі набрали найбільшу кількість голосів мають право захищатися: кожному з номінантів дається по 20 секунд, щоб 
виправдати себе. Після чого проходить фінальне голосуання на вибування. Гравець, який вибуває не відкриває свої карти і 
не бере участі в обговорені і голосуванні. """)
    bot.send_message(
        message.chat.id, """🔹 Крок 6:
Гравці відкривають свою наступну карту, яку бажать показати.
Гравець 1: "Я повнен залишитися в бункері. Я лікар, ідеально здоровий, комунікабельний. Це говорить про мою адекватність 
і придатність після виходу з бункера, а також я відкриваю свою карту спеціальної умови. Тепер я можу вигнати  з бункера 
будь-якого гравця, я обираю гравця 3. "
На це - 30 секунд.
🔸 Крок 7:
Гравці відкривають четверту карту якувони хотять озвучити.
Гравець 1: "Я повинен залишитися в бункері, так як я лікар, ідеально здоровий, комунікабульний, і моє хлобі  - рибілка.
Це також є важливим навиком: я вмію добувати їжу і зможу прокормити нас."
🔹 Крок 8:
Після того  як всі гравці озвучили свої карти, час вдвинути кандидатів на вибування. Ті, в свою чергу защощаються.
Голосування - і ще один персонаж опиняється ззовні.
На це дається 20 секунд на кожного гравця.
🔸 Крок 9:
Гравці по черзі відкривають 5 карту, яку вони вибрали.
Гравець 1: "Я повнен залишитися в бункері. Так як я лікар, ідеально здоровий, моє хобі - рибалка, це також є важливим 
навиком, я вмію говорити на 5 мовах, так як ми поки не знаємо чи всі виживші вміють говорити на нашій мові. Нам важливо
мати в бункері людина, яка вміє говорити на інших мовах.
🔹 Крок 10:
Після того я к всі відкрили свої карти, час видвинути кандидатів на вибування, ті в свою чергу захищаються.
Голосування - і ще один персонаж покидає бункер.
🔸 Крок 11:
Гравці по черзі відкривають свою наступну карту.
Гравець 1: "Я повинен залишитися в бункері, так як я лікар, ідеально здоровий, комунікабельний, і моє хобі - рибалка. 
Це також є важливим навиком, я вмію добувати собі їжу, мій додатковий навийк - це зання 5 мов, так як ми поки е знаємо,
чи всі виживші знають нашу мову. Нам важливо мати в букері людину, яка вміє розмовляти на інших мовах. Також я чоловік 
25 років, гетеросексуальний, готовий ло заселення планети.
🔹 Крок 12:
Після того як всі озвучили всої карти, час видвинути кандидатів на вибування, тепере їх відразу 2. Вони починають 
захищатися.
Голосування - і ще 2 персонажа потрапляють до лісу.
Ви зробили свій вибір і знаєте, хто залишається у бункері. У кожного гравця залишилося по одні карті, яку він відкриває.
Гравці по черзі озвучують 7 карту.
Гравець 1: "Я повинен залишитися в бункері, так як я лікар, ідеально здоровий, комунікабельний, і моє хобі - рибалка. 
Це також є важливим навиком, я вмію добувати собі їжу, мій додатковий навийк - це зання 5 мов, так як ми поки е знаємо,
чи всі виживші знають нашу мову. Нам важливо мати в букері людину, яка вміє розмовляти на інших мовах. Також я чоловік 
25 років, гетеросексуальний, готовий ло заселення планети, але у мене є фобія - клаустрофобія. Це боязнь замкнутого
простору, тому у бункері я зійду з розуму.
Гравці зробили неправильний вибір і залишилися без лікаря. Вибувші гравці відкривають свої карти і оцінюють правильність
рішень за всю гру.
Карточка "Спеціальної умови" може бути відкрита гравцем на будь-якому етапі, але лише 1 за етап. 
""")


# Команда, яка спрацьовує при написанні тексту у чат з ботом
# (як груповий так і особистий)
# Рудимент (доробити) зараз просто виводить це вовідомлення
# і дає можливість відповісти на нього з консолі
@bot.message_handler(content_types=['text'])
def send_text(message):
    print(message.text)
    bot.send_message(message.chat.id, input())
    #    if message.text == 'Привет':
    #        bot.send_message(message.chat.id, 'Привет, мой создатель')
    #    elif message.text == 'Пока':
    #        bot.send_message(message.chat.id, 'Прощай, создатель')


# Команда, яка спрацьовує при відправленні стікера у чат з ботом
# (як груповий так і особистий)
# Рудимент (доробити)
@bot.message_handler(content_types=['sticker'])
def sticker(message):
    random_number = random.randint(0, 1)
    if random_number == 1:
        bot.send_message(message.chat.id, 'Нащо це?')
    elif random_number == 0:
        bot.send_message(message.chat.id, 'Давай без цього?')
    print(message)


# Команда, яка спрацьовує при відправленні фото у чат з ботом
# (як груповий так і особистий)
# Рудимент (доробити)
@bot.message_handler(content_types=['photo'])
def photo(message):
    random_number = random.randint(0, 1)
    if random_number == 1:
        bot.send_message(message.chat.id, 'Какой красавчик, але це не точно')
    elif random_number == 0:
        bot.send_message(message.chat.id, 'Какой красавчик))')
    print(message)


# Команда, яка спрацьовує при відправленні локації у чат з ботом
# (як груповий так і особистий)
# Рудимент (доробити)
@bot.message_handler(content_types=['location'])
def geo_location(message):
    print(message)
    bot.send_message(message.chat.id, 'Це дє?')


if __name__ == "__main__":
    bot.polling()
