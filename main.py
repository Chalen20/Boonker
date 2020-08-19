# coding:utf-8
import telebot
import config
import random
import threading
import Character
import time

bot = telebot.TeleBot(config.TOKEN)
pers = Character.Person()
bunker = Character.Bunker()
catastrophe = Character.Catastrophe()
special_cards = Character.SpecialCards(5)

res = 0
chat_id = 0
active_users = []
active_users_id = []
min_users = 0
time_that_start_new_game = 15.0
round_counter = 1
request = {}
job_counter = 0
types = ["Професія", "Хобі", "Додаткова інформація", "Риса характеру", "Фобія", "Біологічна характеристика",
         "Здоров'я", "Статура", "Спеціальна карта 1", "Спеціальна карта 2"]
list_for_round1 = [types[0], types[8], types[9]]
list_of_list_of_round1 = {}
list_for_round2 = [types[0], types[1], types[2], types[3], types[4], types[5], types[6], types[7], types[8], types[9]]
list_of_list_for_round2 = {}


@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "Привіт")


@bot.message_handler(commands=["help"])
def start(message):
    bot.send_message(message.chat.id, "/start - початок використання"
                                      "/help - допомога"
                                      "/rules - правила гри"
                                      "/off - завершити поточну гру і вимкнуи бота")


keyboard = telebot.types.InlineKeyboardMarkup()
keyboard.row(
    telebot.types.InlineKeyboardButton('Enter', callback_data='Enter')
)


@bot.message_handler(commands=['start_new_game'])
def exchange_command(message):
    global chat_id
    chat_id = message.chat.id
    if message.chat.type == "group" or message.chat.type == "supergroup":
        t = threading.Timer(time_that_start_new_game, lambda: start_(message))
        t.start()
        global res
        res = bot.send_message(chat_id=message.chat.id, text='Start the game window. \nEnter if you want to play:',
                               reply_markup=keyboard)
        bot.pin_chat_message(chat_id=message.chat.id, message_id=res.message_id, disable_notification=False)
    else:
        bot.send_message(chat_id=message.chat.id, text="Ця команда доступна лише в групових чатах")


@bot.callback_query_handler(func=lambda call: True)
def iq_callback(query):
    data = query.data
    if data.startswith('Enter'):
        get_ex_callback(query)
    elif data.startswith(types[0]):
        get_prof_callback(types[0], query)
    elif data.startswith(types[8]):
        if len(list_of_list_of_round1[query.from_user.id]) != 1 and round_counter == 1:
            get_prof_callback(types[8], query)
        else:
            get_round_begins_from_two(types[8], query)
    elif data.startswith(types[9]):
        if len(list_of_list_of_round1[query.from_user.id]) != 1 and round_counter == 1:
            get_prof_callback(types[9], query)
        else:
            get_round_begins_from_two(types[9], query)
    elif data.startswith(types[1]):
        get_round_begins_from_two(types[1], query)
    elif data.startswith(types[2]):
        get_round_begins_from_two(types[2], query)
    elif data.startswith(types[3]):
        get_round_begins_from_two(types[3], query)
    elif data.startswith(types[4]):
        get_round_begins_from_two(types[4], query)
    elif data.startswith(types[5]):
        get_round_begins_from_two(types[5], query)
    elif data.startswith(types[6]):
        get_round_begins_from_two(types[6], query)
    elif data.startswith(types[7]):
        get_round_begins_from_two(types[7], query)


def get_round_begins_from_two(type_str, query):
    list_of_list_for_round2[query.from_user.id].remove(type_str)


def get_prof_callback(type_str, query):
    global job_counter
    keyboard_1 = telebot.types.InlineKeyboardMarkup()
    if len(list_of_list_of_round1[query.from_user.id]) == 3 or\
            (len(list_of_list_of_round1[query.from_user.id]) == 2 and
             types[0] == type_str and types[0] in list_of_list_of_round1[query.from_user.id]) or\
            (len(list_of_list_of_round1[query.from_user.id]) == 2 and
             types[0] not in list_of_list_of_round1[query.from_user.id]):
        some_variable = list_of_list_of_round1[query.from_user.id]
        del some_variable[list_for_round1.index(type_str)]
        list_of_list_of_round1[query.from_user.id] = some_variable
        list_of_list_for_round2[query.from_user.id].remove(type_str)
    if len(list_of_list_of_round1[query.from_user.id]) == 2 and \
            types[0] not in list_of_list_of_round1[query.from_user.id]:
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
                         str(request[query.from_user.id][types.index(type_str)]))
        job_counter += 1
        t = threading.Timer(time_that_start_new_game, lambda: round_(query))
        t.start()
    elif len(list_of_list_of_round1[query.from_user.id]) == 2 and\
            types[0] in list_of_list_of_round1[query.from_user.id]:
        keyboard_1.row(
            telebot.types.InlineKeyboardButton(list_of_list_of_round1[query.from_user.id][0],
                                               callback_data=str(list_of_list_of_round1[query.from_user.id][0]))
        )
        bot.edit_message_text(text=query.message.text, message_id=query.message.message_id,
                              chat_id=query.message.chat.id,
                              reply_markup=keyboard_1)
        bot.send_message(chat_id, "@" + query.from_user.username + " - " +
                         str(request[query.from_user.id][types.index(type_str)]))
        t = threading.Timer(time_that_start_new_game, lambda: round_(query))
        t.start()
    elif len(list_of_list_of_round1[query.from_user.id]) == 1 and\
            types[0] not in list_of_list_of_round1[query.from_user.id]:
        bot.edit_message_text(text=query.message.text, message_id=query.message.message_id,
                              chat_id=query.message.chat.id, reply_markup=None)
        bot.send_message(chat_id, "@" + query.from_user.username + " - " +
                         str(request[query.from_user.id][types.index(type_str)]))
        job_counter += 1
        print(3)
    if job_counter == len(active_users):
        bot.send_message(chat_id, "Дискусія: \n"
                                  "бла \n "
                                  "бла \n "
                                  "бла \n ")


def round_(query):
    global round_counter
    keyboard_1 = telebot.types.InlineKeyboardMarkup()
    round_counter += 1
    for i in list_of_list_for_round2[query.from_user.id]:
        keyboard_1.row(
            telebot.types.InlineKeyboardButton(i, callback_data=str(i))
        )
    bot.send_message(chat_id=query.from_user.id, text="Відкрити карту іншим гравцям (раунд 2)",
                     reply_markup=keyboard_1)


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


def start_(message):
    global res
    for i in range(0, len(active_users)):
        some_variable = list_for_round1.copy()
        list_of_list_of_round1[active_users[i].id] = some_variable
    for i in range(0, len(active_users)):
        some_variable = list_for_round2.copy()
        list_of_list_for_round2[active_users[i].id] = some_variable
    try:
        bot.delete_message(message.chat.id, res.message_id)
        bot.delete_message(message.chat.id, message.message_id)
    except:
        pass
    pers_cards = []
    for i in range(0, len(active_users)):
        pers_characteristics = []
        pers.create_character()
        special_cards.get_random_card()
        pers_characteristics.append(pers.random_job)
        pers_characteristics.append(pers.stag)
        pers_characteristics.append(pers.random_hobby)
        pers_characteristics.append(pers.random_hobby_stage)
        pers_characteristics.append(pers.random_dop_info)
        pers_characteristics.append(pers.random_human_trait)
        pers_characteristics.append(pers.random_humanTrait_stage)
        pers_characteristics.append(pers.random_phobia)
        pers_characteristics.append(pers.age)
        pers_characteristics.append(pers.biological)
        pers_characteristics.append(pers.childFree)
        pers_characteristics.append(pers.random_health)
        pers_characteristics.append(pers.bodyType)
        pers_characteristics.append(pers.height)
        pers_characteristics.append(pers.weight)
        pers_characteristics.append(special_cards.random_card)
        special_cards.get_random_card()
        pers_characteristics.append(special_cards.random_card)
        pers_cards.append(pers_characteristics)

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
                             types[0] + ": " + pers_cards[i][0] + ", " + str(pers_cards[i][1]) + "\n" +
                             types[1] + ": " + pers_cards[i][2] + ", " + str(pers_cards[i][3]) + "\n" +
                             types[2] + ": " + pers_cards[i][4] + "\n" +
                             types[3] + ": " + pers_cards[i][5] + ", " + pers_cards[i][6] + "\n" +
                             types[4] + ": " + pers_cards[i][7] + "\n" +
                             types[5] + ": " + pers_cards[i][8] + ", " + pers_cards[i][9] + ", " + pers_cards[i][
                                 10] + "\n" +
                             types[6] + ": " + pers_cards[i][11] + "\n" +
                             types[7] + ": " + pers_cards[i][12] + ", " + str(pers_cards[i][13]) + ", " + str(
                                 pers_cards[i][14]) + "\n" +
                             types[8] + ": " + pers_cards[i][15] + "\n" +
                             types[9] + ": " + pers_cards[i][16])
            array_data = []
            array_data.append(pers_cards[i][0] + ", " + str(pers_cards[i][1]))
            array_data.append(pers_cards[i][2] + ", " + str(pers_cards[i][3]))
            array_data.append(pers_cards[i][4])
            array_data.append(pers_cards[i][5] + ", " + pers_cards[i][6])
            array_data.append(pers_cards[i][7])
            array_data.append(pers_cards[i][8] + ", " + pers_cards[i][9] + ", " + pers_cards[i][10])
            array_data.append(pers_cards[i][11])
            array_data.append(pers_cards[i][12] + ", " + str(pers_cards[i][13]) + ", " + str(pers_cards[i][14]))
            array_data.append(pers_cards[i][15])
            array_data.append(pers_cards[i][16])
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
        for i in range(len(active_users)):
            bot.send_message(chat_id=active_users[i].id, text="Відкрити карту іншим гравцям (раунд 1)",
                             reply_markup=keyboard_1)
    else:
        bot.send_message(message.chat.id, "На жаль, не можливо провести гру з такою кількістю гравців((\n"
                                          "Мінімальна кількість гравців - " + str(min_users)) + " ."
    try:
        bot.unpin_chat_message(chat_id=message.chat.id)
    except:
        pass

    # for i in range(0, message.message_id*100):
    #    try:
    #        bot.delete_message(message.chat.id, i)
    #        print("delete")
    #    except:
    #        pass


@bot.message_handler(commands=["off"])
def start(message):
    bot.send_message(message.chat.id, "А може не треба?")


@bot.message_handler(commands=["settings"])
def start(message):
    bot.send_message(message.chat.id, "А може не треба?")


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


@bot.message_handler(content_types=['text'])
def send_text(message):
    print(message.text)
    bot.send_message(message.chat.id, input())
    #    if message.text == 'Привет':
    #        bot.send_message(message.chat.id, 'Привет, мой создатель')
    #    elif message.text == 'Пока':
    #        bot.send_message(message.chat.id, 'Прощай, создатель')


@bot.message_handler(content_types=['sticker'])
def sticker(message):
    random_number = random.randint(0, 1)
    if random_number == 1:
        bot.send_message(message.chat.id, 'Нащо це?')
    elif random_number == 0:
        bot.send_message(message.chat.id, 'Давай без цього?')
    print(message)


@bot.message_handler(content_types=['photo'])
def photo(message):
    random_number = random.randint(0, 1)
    if random_number == 1:
        bot.send_message(message.chat.id, 'Какой красавчик, але це не точно')
    elif random_number == 0:
        bot.send_message(message.chat.id, 'Какой красавчик))')
    print(message)


@bot.message_handler(content_types=['location'])
def geo_location(message):
    print(message)
    bot.send_message(message.chat.id, 'Це дє?')


if __name__ == "__main__":
    bot.polling()
