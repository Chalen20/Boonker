from tkinter import *
from PIL import Image, ImageTk
from random import *
import Character
import math

player_count = 12
class Game:
    def __init__(self, number_of_player):
        self.window = Tk()
        self.window.attributes('-fullscreen', 1)
        self.width = self.window.winfo_screenwidth()
        self.height = self.window.winfo_screenheight()
        self.canvas = Canvas(self.window, height=self.height, width=self.width, bg="lightgreen")
        if number_of_player <= 6:
            koef = 1
        elif number_of_player <= 9:

            koef = 3 / 2
        elif number_of_player <= 12:
            koef = 2
        elif number_of_player <= 15:
            koef = 5 / 2

        elif number_of_player <= 18:
            koef = 3
        self.canvas.configure(scrollregion=(0, 0, self.width,
                                            self.height * koef))
        self.canvas.pack()

        self.width_rubashka = round(self.width / 4)

        rub1 = Image.open("img/rubashka1.png")
        rub1 = rub1.resize((round(self.width_rubashka * 0.7), self.width_rubashka), Image.ANTIALIAS)
        rub1_animation = rub1.resize((round(self.width_rubashka / 12 * 7), self.width_rubashka), Image.ANTIALIAS)
        rub1_animation2 = rub1.resize((round(self.width_rubashka / 15 * 7), self.width_rubashka), Image.ANTIALIAS)
        rub1_animation3 = rub1.resize((round(self.width_rubashka / 20 * 7), self.width_rubashka), Image.ANTIALIAS)
        rub1_animation4 = rub1.resize((round(self.width_rubashka / 30 * 7), self.width_rubashka), Image.ANTIALIAS)
        rub1_animation5 = rub1.resize((round(self.width_rubashka / 60 * 7), self.width_rubashka), Image.ANTIALIAS)
        rub1_animation6 = rub1.resize((1, self.width_rubashka), Image.ANTIALIAS)

        rub1 = ImageTk.PhotoImage(rub1)
        rub1_animation = ImageTk.PhotoImage(rub1_animation)
        rub1_animation2 = ImageTk.PhotoImage(rub1_animation2)
        rub1_animation3 = ImageTk.PhotoImage(rub1_animation3)
        rub1_animation4 = ImageTk.PhotoImage(rub1_animation4)
        rub1_animation5 = ImageTk.PhotoImage(rub1_animation5)
        rub1_animation6 = ImageTk.PhotoImage(rub1_animation6)

        self.all_Rubashki = [
            [rub1, rub1_animation, rub1_animation2, rub1_animation3, rub1_animation4, rub1_animation5, rub1_animation6]
        ]

        self.pers_cards = []
        pers = Character.Person()
        for i in range(0, number_of_player):
            pers_characteristics = []
            pers.create_character()
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
            self.pers_cards.append(pers_characteristics)

        for i in self.pers_cards:
            print(i)

        self.x = randint(0, len(self.all_Rubashki) - 1)
        self.rubashka = self.all_Rubashki[self.x][0]
        print(self.rubashka)
        self.rubashka_animation1 = self.all_Rubashki[self.x][1]
        self.rubashka_animation2 = self.all_Rubashki[self.x][2]

        self.window.bind("<Escape>", self.main_window_func)
        self.number_of_player = number_of_player
        self.counter_for_flip = 2
        self.revert_counter_flip = 1

        self.continue_ = Image.open("img/Continue.png")
        self.continue_ = self.continue_.resize((round(self.width / 5), round(self.height / 9)), Image.ANTIALIAS)
        self.continue_ = ImageTk.PhotoImage(self.continue_)

        self.iconify = Image.open("img/Iconify.png")
        self.iconify = self.iconify.resize((round(self.width / 5), round(self.height / 9)), Image.ANTIALIAS)
        self.iconify = ImageTk.PhotoImage(self.iconify)

        self.exit = Image.open("img/Exit.png")
        self.exit = self.exit.resize((round(self.width / 5), round(self.height / 9)), Image.ANTIALIAS)
        self.exit = ImageTk.PhotoImage(self.exit)

        self.canvas.bind("<ButtonPress-1>", self.scroll_start)
        self.canvas.bind("<B1-Motion>", self.scroll_move)
        self.canvas.bind("<MouseWheel>", self.scroll_mouse_wheel)

        self.count = 0
        self.animation_number = 120
        self.count_number = 0
        self.animate(self.width / 6 * 5 - self.width * 0.05, self.height * 0.05)
        self.window.mainloop()

    def main_window_func(self, event):
        self.main_window = Canvas(self.canvas, width=self.width / 5, height=self.height / 3, bg="lightblue")
        self.main_window.place(x=self.width * 2 / 5, y=self.height / 3)
        continue_ = self.main_window.create_image(0, 0, image=self.continue_, anchor=NW)
        self.main_window.tag_bind(continue_, "<Button-1>", self.continue_func)
        iconify = self.main_window.create_image(0, round(self.height / 9), image=self.iconify, anchor=NW)
        self.main_window.tag_bind(iconify, "<Button-1>", self.iconify_func)
        exit = self.main_window.create_image(0, round(self.height / 9 * 2), image=self.exit, anchor=NW)
        self.main_window.tag_bind(exit, "<Button-1>", self.exit_func)
        self.window.unbind("<Escape>")
        self.window.bind("<Escape>", self.close_main_window)

    def close_main_window(self, event):
        self.main_window.destroy()
        self.window.unbind("<Escape>")
        self.window.bind("<Escape>", self.main_window_func)

    def animate(self, start_x, start_y):
        self.allCards = []
        for j in range(0, self.number_of_player):
            card = self.canvas.create_image(start_x, start_y, image=self.rubashka, anchor="nw")
            self.allCards.append(card)
        self.canvas.after(1000, lambda x=start_x, y=start_y: self.animate2(x, y))

    def animate2(self, start_x, start_y):
        counter = 0

        for i in range(0, math.floor(self.number_of_player / 3)):  # рядки
            for j in range(0, 3):  # стовбці
                if j < 2:
                    self.canvas.move(self.allCards[counter],
                                     round((round(j * self.width / 3 + self.width / 12) - (
                                         start_x)) / self.animation_number),
                                     round((round(i * self.height / 2) -
                                            start_y) + 70) / self.animation_number)
                    counter += 1
                elif j < 4:
                    self.canvas.move(self.allCards[counter],
                                     round((round(j * self.width / 3 + self.width / 12) - (
                                         start_x)) / self.animation_number),
                                     round((round(i * self.height / 2) -
                                            start_y) + 70) / self.animation_number)
                    counter += 1
                elif j < 6:
                    self.canvas.move(self.allCards[counter],
                                     round((round(j * self.width / 3 + self.width / 12) - (
                                         start_x)) / self.animation_number),
                                     round((round(i * self.height / 2) -
                                            start_y) + 70) / self.animation_number)
                    counter += 1
                else:
                    self.canvas.move(self.allCards[counter],
                                     round((round(j * self.width / 3 - self.width / 24) - (
                                         start_x)) / self.animation_number),
                                     round((round(i * self.height / 2) -
                                            start_y) + 70) / self.animation_number)
                    counter += 1

        for i in range(0, self.number_of_player % 3):
            self.canvas.move(self.allCards[counter],

                             round((round(i * self.width / 3 + self.width / 12) - (

                                 start_x)) / self.animation_number),
                             round((round(self.number_of_player // 3 * self.height / 2) -
                                    start_y)) / self.animation_number)
            counter += 1

        self.count += 1
        if self.count < 120:
            self.canvas.after(30, lambda x=start_x, y=start_y: self.animate2(x, y))
        else:
            for i in self.allCards:
                self.canvas.tag_bind(i, "<Button-1>", lambda event, x=i: self.flip(x, event))

    def animate3(self, start_x, start_y):
        column = self.count % (self.number_of_player / 3)
        if self.count % 3 == 0:
            row = 0
        elif self.count % 3 == 1:
            row = 1
        else:
            row = 2
        if column == 0 or column == 1 or column == self.number_of_player / 2 or \
                column == self.number_of_player / 2 + 1:
            self.canvas.move(self.allCards[self.count],
                             round((round(column * self.width / 3 + self.width / 12) - (
                                 start_x)) / self.animation_number),
                             round((round(row * self.height / 2 + self.height / 12) -
                                    start_y)) / self.animation_number)
        self.count_number += 1
        if self.count_number < self.animation_number:
            self.canvas.after(10, lambda x=start_x, y=start_y: self.animate3(x, y))
        elif self.count_number == self.animation_number and self.count < self.number_of_player - 1:
            self.count_number = 0
            print(self.canvas.coords(self.allCards[self.count]))
            self.count += 1
            self.canvas.after(10, lambda x=start_x, y=start_y: self.animate3(x, y))

    def flip(self, x, event):
        de = self.canvas.coords(x)
        self.canvas.delete(x)
        card = self.canvas.create_image(de[0] + self.width_rubashka / 12 * 0.7, de[1], image=self.rubashka_animation1,
                                        anchor="nw")
        self.canvas.after(50, lambda card=card: self.flip2(card, x))

    def flip2(self, x, number):
        de = self.canvas.coords(x)
        self.canvas.delete(x)
        card0 = self.canvas.create_image(de[0] + self.width_rubashka / 12 * 0.7, de[1],
                                         image=self.all_Rubashki[self.x][self.counter_for_flip], anchor="nw")
        self.counter_for_flip += 1
        if self.counter_for_flip < len(self.all_Rubashki[self.x]):
            self.canvas.after(50, lambda x=card0: self.flip2(x, number))
        else:
            self.counter_for_flip = 2
            self.canvas.after(50, lambda x=card0: self.flip3(x, number))

    def flip3(self, x, number):
        de = self.canvas.coords(x)
        self.canvas.delete(x)
        canvas2 = self.canvas.create_rectangle(de[0] - self.width_rubashka / 12, de[1],
                                               de[0] - self.width_rubashka / 12 +
                                               self.width_rubashka / 6 * self.revert_counter_flip * 0.7,
                                               self.width_rubashka + de[1], fill="white")

        self.revert_counter_flip += 1
        self.canvas.after(50, lambda canvas=canvas2, y=de[0],
                                     z=de[1]: self.flip4(canvas, y, z, number))

    def flip4(self, x, de, z, number):
        self.canvas.delete(x)
        self.canvas2 = self.canvas.create_rectangle(de - self.width_rubashka / 12, z,
                                                    de - self.width_rubashka / 12 +
                                                    self.width_rubashka / 6 * self.revert_counter_flip * 0.7,
                                                    z + self.width_rubashka, fill="white")
        self.revert_counter_flip += 1
        if self.revert_counter_flip < 7:
            self.canvas.after(50, lambda x=self.canvas2, y=de - self.width_rubashka / 15,
                                         z=z: self.flip4(x, y, z, number))
        else:
            self.revert_counter_flip = 1
            self.open_icon(self.canvas2, number)

    def open_icon(self, canvas, number):
        de = self.canvas.coords(canvas)
        texts = ["job", "hobby", "add_info", "human_trait", "phobia", "biological", "health", "body_type"]

        counter = self.width_rubashka / 8
        for i in range(0, 8):
            self.canvas.create_rectangle(de[0], de[1] + counter * i, de[2], de[1] + counter * (i + 1),
                                         tag=texts[i] + "_" + str(number))
            self.canvas.create_text(de[0] + self.width_rubashka * 0.7 / 2, de[1] + counter * i + counter / 2,
                                    text=texts[i], anchor="c", font=("Verdana", 15), tag=texts[i] + str(number))
            if i == 0:
                self.canvas.tag_bind("job" + str(number), "<Button-1>", lambda event: self.job_func(de, number, event))
                self.canvas.tag_bind("job_" + str(number), "<Button-1>", lambda event: self.job_func(de, number, event))
            else:
                self.canvas.tag_bind(texts[i] + str(number), "<Button-1>",
                                     lambda event, x=i: self.func_arg(texts, x, de, number, event))
                self.canvas.tag_bind(texts[i] + "_" + str(number), "<Button-1>",
                                     lambda event, x=i: self.func_arg(texts, x, de, number, event))

    def func_arg(self, texts, i, de, number, event):
        for j in range(1, 8):
            self.canvas.tag_unbind(texts[j] + str(number), "<Button-1>")
            self.canvas.tag_unbind(texts[j] + "_" + str(number), "<Button-1>")
        self.canvas.delete(texts[i] + str(number))
        if texts[i] == "hobby":
            self.canvas.create_text(de[0] + self.width_rubashka * 0.35,
                                    de[1] + self.width_rubashka / 8 * i + self.width_rubashka / 16,
                                    text=str(self.pers_cards[number - 1][2]) + ", " +
                                         str(self.pers_cards[number - 1][3]),
                                    anchor="c", font=("Verdana", 20), tag=texts[i] + str(number))

        elif texts[i] == "add_info":
            self.canvas.create_text(de[0] + self.width_rubashka * 0.35,
                                    de[1] + self.width_rubashka / 8 * i + self.width_rubashka / 16,
                                    text=str(self.pers_cards[number - 1][4]),
                                    anchor="c", font=("Verdana", 20), tag=texts[i] + str(number))

        elif texts[i] == "human_trait":
            self.canvas.create_text(de[0] + self.width_rubashka * 0.35,
                                    de[1] + self.width_rubashka / 8 * i + self.width_rubashka / 16,
                                    text=str(self.pers_cards[number - 1][5]) + ", " +
                                         str(self.pers_cards[number - 1][6]),
                                    anchor="c", font=("Verdana", 20), tag=texts[i] + str(number))

        elif texts[i] == "phobia":
            self.canvas.create_text(de[0] + self.width_rubashka * 0.35,
                                    de[1] + self.width_rubashka / 8 * i + self.width_rubashka / 16,
                                    text=str(self.pers_cards[number - 1][7]),
                                    anchor="c", font=("Verdana", 20), tag=texts[i] + str(number))

        elif texts[i] == "biological":
            self.canvas.create_text(de[0] + self.width_rubashka * 0.35,
                                    de[1] + self.width_rubashka / 8 * i + self.width_rubashka / 16,
                                    text=str(self.pers_cards[number - 1][8]) + ", " + str(
                                        self.pers_cards[number - 1][9])
                                         + ", " + str(self.pers_cards[number - 1][10]),
                                    anchor="c", font=("Verdana", 20), tag=texts[i] + str(number))
        elif texts[i] == "health":
            self.canvas.create_text(de[0] + self.width_rubashka * 0.35,
                                    de[1] + self.width_rubashka / 8 * i + self.width_rubashka / 16,
                                    text=str(self.pers_cards[number - 1][11]),
                                    anchor="c", font=("Verdana", 20), tag=texts[i] + str(number))

        elif texts[i] == "body_type":
            self.canvas.create_text(de[0] + self.width_rubashka * 0.35,
                                    de[1] + self.width_rubashka / 8 * i + self.width_rubashka / 16,
                                    text=str(
                                        self.pers_cards[number - 1][12] + ", " + str(self.pers_cards[number - 1][13])
                                        + ", " + str(self.pers_cards[number - 1][14])),
                                    anchor="c", font=("Verdana", 20), tag=texts[i] + str(number))

    def job_func(self, de, number, event):
        number = number - 1
        if self.pers_cards[number][1] == 1:
            years = "год"
        elif self.pers_cards[number][1] <= 4:
            years = "года"
        else:
            years = "лет"
        self.canvas.delete("job" + str(number + 1))
        text = str(self.pers_cards[number][0]) + ", " + str(self.pers_cards[number][1]) + " " + years
        if len(text) >= 22:
            for i in range(len(text)-1, 0, -1):
                if text[i] == " ":
                    text = text[:i] + "\n" + text[i:]
                    self.canvas.create_text(de[0] + self.width_rubashka * 0.7 / 2, de[1] + self.width_rubashka / 8 / 2.5,
                                            text=text,
                                            anchor="c", font=("Verdana", 14), tag="job" + str(number + 1))
                    break
        else:
            self.canvas.create_text(de[0] + self.width_rubashka * 0.7 / 2, de[1] + self.width_rubashka / 8 / 2,
                                    text=text,
                                    anchor="c", font=("Verdana", 20), tag="job" + str(number + 1))
        self.canvas.tag_unbind("job" + str(number + 1), "<Button-1>")
        self.canvas.tag_unbind("job_" + str(number + 1), "<Button-1>")

    def exit_func(self, event):
        self.window.quit()

    def continue_func(self, event):
        self.main_window.destroy()

    def iconify_func(self, event):
        self.window.iconify()

    def scroll_start(self, event):
        self.canvas.scan_mark(event.x, event.y)

    def scroll_move(self, event):
        self.canvas.scan_dragto(event.x, event.y, gain=1)

    def scroll_mouse_wheel(self, event):
        self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
        return "break"


class Timer:
    def __init__(self, root, x, y, time_minutes, time_seconds, width, height, color_bg, color_text):
        self.minutes = time_minutes
        self.seconds = time_seconds
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.root = root
        self.color_text = color_text
        canv = root.create_rectangle(self.x - width / 2, self.y, self.x + width / 2, self.y + height, fill=color_bg)
        root.lift(canv)
        if self.seconds < 10:
            self.text = root.create_text(self.x - width / 3, 18,
                                         text=str(self.minutes) + ": 0" + str(self.seconds),
                                         font=("Verdana", 20), anchor='nw')
        else:
            self.text = root.create_text(self.x - width / 3, 18,
                                         text=str(self.minutes) + ": " + str(self.seconds),
                                         font=("Verdana", 20), anchor='nw')
        root.after(100, self.time)

    def time(self):
        self.seconds -= 1
        if self.seconds < 0:
            self.seconds += 60
            self.minutes -= 1
        self.root.delete(self.text)
        if self.seconds < 10:
            self.text = self.root.create_text(self.x - self.width / 3, 18,
                                              text=str(self.minutes) + ": 0" + str(self.seconds),
                                              font=("Verdana", 20), anchor='nw', fill=self.color_text)
        else:
            self.text = self.root.create_text(self.x - self.width / 3, 18,
                                              text=str(self.minutes) + ": " + str(self.seconds),
                                              font=("Verdana", 20), anchor='nw', fill=self.color_text)
        if self.seconds != 0 or self.minutes != 0:
            self.root.after(100, self.time)


Game(player_count)

class Saver:
    def __init__(self, player_number, job, hobby, add_info, human_trait, phobia, biological, health, body_type):
        f = open('players.html', 'w')
        message = """<html>
        <head>
                <style> .card {
                  margin : auto ;
                  width : 400px;
                  height : 600px;
                  background-color: #f7d065;
                  border-radius: 40px;}
                  p {
                  padding : 20px 0 0 25px
                  }
</style>
        </head>
<body>
  <div class = "card">
          <p>""" + player_number + """</p>
          <p>""" + job + """</p>
          <p>""" + hobby + """</p>
          <p>""" + add_info + """</p>
          <p>""" + human_trait + """</p>
          <p>""" + phobia + """</p>
          <p>""" + biological + """</p>
          <p>""" + health + """</p>
          <p>""" + body_type + """</p>
  </div></body>
</html>"""

        f.write(message)
        f.close()