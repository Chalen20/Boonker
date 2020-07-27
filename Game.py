from tkinter import *
from PIL import Image, ImageTk
from random import *
from Character import Person

class Game:
    def __init__(self, number_of_player):
        self.window = Tk()
        self.window.attributes('-fullscreen', 1)
        self.width = self.window.winfo_screenwidth()
        self.height = self.window.winfo_screenheight()
        self.canvas = Canvas(self.window, height=self.height, width=self.width, bg="lightgreen")
        self.canvas.configure(scrollregion=(0, 0, self.width*number_of_player/6 - self.width/11*number_of_player/6,
                                            self.height))
        self.canvas.pack()

        self.width_rubashka = round(self.width / 4)

        pediatr = Image.open('img/pediatr.jpg')
        pediatr = pediatr.resize((round(self.width_rubashka * 0.7), round(self.width_rubashka * 0.7)), Image.ANTIALIAS)
        pediatr = ImageTk.PhotoImage(pediatr)

        trener = Image.open('img/trener.jpg')
        trener = trener.resize((round(self.width_rubashka * 0.7), round(self.width_rubashka * 0.7)), Image.ANTIALIAS)
        trener = ImageTk.PhotoImage(trener)

        police = Image.open('img/police.jpg')
        police = police.resize((round(self.width_rubashka * 0.7), round(self.width_rubashka * 0.7)), Image.ANTIALIAS)
        police = ImageTk.PhotoImage(police)

        phizik = Image.open('img/phizik.jpg')
        phizik = phizik.resize((round(self.width_rubashka * 0.7), round(self.width_rubashka * 0.7)), Image.ANTIALIAS)
        phizik = ImageTk.PhotoImage(phizik)

        biolog = Image.open('img/біолог.jpg')
        biolog = biolog.resize((round(self.width_rubashka * 0.7), round(self.width_rubashka * 0.7)), Image.ANTIALIAS)
        biolog = ImageTk.PhotoImage(biolog)

        himik = Image.open('img/химик.jpg')
        himik = himik.resize((round(self.width_rubashka * 0.7), round(self.width_rubashka * 0.7)), Image.ANTIALIAS)
        himik = ImageTk.PhotoImage(himik)

        philosoph = Image.open('img/філософ.jpg')
        philosoph = philosoph.resize((round(self.width_rubashka * 0.7), round(self.width_rubashka * 0.7)),
                                     Image.ANTIALIAS)
        philosoph = ImageTk.PhotoImage(philosoph)

        bloger = Image.open('img/блогер.jpg')
        bloger = bloger.resize((round(self.width_rubashka * 0.7), round(self.width_rubashka * 0.7)), Image.ANTIALIAS)
        bloger = ImageTk.PhotoImage(bloger)

        dietolog = Image.open('img/диетолог.jpg')
        dietolog = dietolog.resize((round(self.width_rubashka * 0.7), round(self.width_rubashka * 0.7)), Image.ANTIALIAS)
        dietolog = ImageTk.PhotoImage(dietolog)

        psiholog = Image.open('img/Психология.jpg')
        psiholog = psiholog.resize((round(self.width_rubashka * 0.7), round(self.width_rubashka * 0.7)),
                                   Image.ANTIALIAS)
        psiholog = ImageTk.PhotoImage(psiholog)

        sexolog = Image.open('img/сексолог.jpg')
        sexolog = sexolog.resize((round(self.width_rubashka * 0.7), round(self.width_rubashka * 0.7)),
                                   Image.ANTIALIAS)
        sexolog = ImageTk.PhotoImage(sexolog)

        stroitel = Image.open('img/строитель.jpg')
        stroitel = stroitel.resize((round(self.width_rubashka * 0.7), round(self.width_rubashka * 0.7)),
                                   Image.ANTIALIAS)
        stroitel = ImageTk.PhotoImage(stroitel)

        teacher = Image.open('img/вчитель.png')
        teacher = teacher.resize((round(self.width_rubashka * 0.7), round(self.width_rubashka * 0.7)),
                                   Image.ANTIALIAS)
        teacher = ImageTk.PhotoImage(teacher)

        army = Image.open('img/военний.jpg')
        army = army.resize((round(self.width_rubashka * 0.7), round(self.width_rubashka * 0.7)),
                                 Image.ANTIALIAS)
        army = ImageTk.PhotoImage(army)

        pilot = Image.open('img/пилот.jpg')
        pilot = pilot.resize((round(self.width_rubashka * 0.7), round(self.width_rubashka * 0.7)),
                           Image.ANTIALIAS)
        pilot = ImageTk.PhotoImage(pilot)

        art = Image.open('img/художник.png')
        art = art.resize((round(self.width_rubashka * 0.7), round(self.width_rubashka * 0.7)),
                           Image.ANTIALIAS)
        art = ImageTk.PhotoImage(art)

        self.prof_images = {
            "Педиатр": pediatr,
            "Фитнес тренер": trener,
            "Полицейский": police,
            "Физик-ядерщик": phizik,
            "Биолог": biolog,
            "Химик": himik,
            "Философ": philosoph,
            "Блогер": bloger,
            "Диетолог": dietolog,
            "Психолог": psiholog,
            "Сексолог": sexolog,
            "Строитель": stroitel,
            "Учитель": teacher,
            "Военний": army,
            "Пилот": pilot,
            "Художник": art,
        }

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
        pers = Person()
        for i in range(0, number_of_player):
            pers_characteristics = []
            pers.create_character()
            pers_characteristics.append(pers.random_job)
            pers_characteristics.append(pers.random_hobby)
            pers_characteristics.append(pers.random_dop_info)
            pers_characteristics.append(pers.random_human_trait)
            pers_characteristics.append(pers.phobia)
            pers_characteristics.append(pers.age)
            pers_characteristics.append(pers.biological)
            pers_characteristics.append(pers.childFree)
            pers_characteristics.append(pers.health)
            self.pers_cards.append(pers_characteristics)

        for i in self.pers_cards:
            print(i)

        self.x = randint(0, len(self.all_Rubashki)-1)
        self.rubashka = self.all_Rubashki[self.x][0]
        self.rubashka_animation1 = self.all_Rubashki[self.x][1]
        self.rubashka_animation2 = self.all_Rubashki[self.x][2]

        self.window.bind("<Escape>", self.main_window_func)
        self.number_of_player = number_of_player
        self.counter_for_flip = 2
        self.revert_counter_flip = 1

        self.continue_ = Image.open("img/Continue.png")
        self.continue_ = self.continue_.resize((round(self.width/5), round(self.height/9)), Image.ANTIALIAS)
        self.continue_ = ImageTk.PhotoImage(self.continue_)

        self.iconify = Image.open("img/Iconify.png")
        self.iconify = self.iconify.resize((round(self.width/5), round(self.height/9)), Image.ANTIALIAS)
        self.iconify = ImageTk.PhotoImage(self.iconify)

        self.exit = Image.open("img/Exit.png")
        self.exit = self.exit.resize((round(self.width/5), round(self.height/9)), Image.ANTIALIAS)
        self.exit = ImageTk.PhotoImage(self.exit)

        self.canvas.bind("<ButtonPress-1>", self.scroll_start)
        self.canvas.bind("<B1-Motion>", self.scroll_move)

        self.count = 0
        self.animation_number = 120
        self.count_number = 0
        self.animate(self.width/6*5-self.width*0.05, self.height*0.05)
        for i in self.allCards:
            self.canvas.tag_bind(i, "<Button-1>", lambda event, x=i: self.flip(x, event))
        self.window.mainloop()

    def main_window_func(self, event):
        self.main_window = Canvas(self.canvas, width=self.width / 5, height=self.height / 3, bg="lightblue")
        self.main_window.place(x=self.width*2/5, y=self.height/3)
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
        for i in range(0, 2):
            for j in range(0, round(self.number_of_player/2)):
                if j < 2:
                    self.canvas.move(self.allCards[counter],
                                     round((round(j * self.width / 3 + self.width / 12) - (
                                                start_x)) / self.animation_number),
                                     round((round(i * self.height / 2) -
                                           start_y)) / self.animation_number)
                    counter += 1
                elif j < 4:
                    self.canvas.move(self.allCards[counter],
                                     round((round(j * self.width / 3 + self.width/24) - (
                                                 start_x)) / self.animation_number),
                                     round((round(i * self.height / 2) -
                                            start_y)) / self.animation_number)
                    counter += 1
                elif j < 6:
                    self.canvas.move(self.allCards[counter],
                                     round((round(j * self.width / 3) - (
                                                 start_x)) / self.animation_number),
                                     round((round(i * self.height / 2) -
                                            start_y)) / self.animation_number)
                    counter += 1
                else:
                    self.canvas.move(self.allCards[counter],
                                     round((round(j * self.width / 3 - self.width/24) - (
                                                 start_x)) / self.animation_number),
                                     round((round(i * self.height / 2) -
                                            start_y)) / self.animation_number)
                    counter += 1

        self.count += 1
        if self.count < 120:
            self.canvas.after(30, lambda x=start_x, y=start_y: self.animate2(x, y))

    def animate3(self, start_x, start_y):
        column = self.count % (self.number_of_player / 2)
        if self.count >= self.number_of_player / 2:
            row = 1
        else:
            row = 0
        if column == 0 or column == 1 or column == self.number_of_player/2 or \
                column == self.number_of_player/2 + 1:
            self.canvas.move(self.allCards[self.count],
                             round((round(column * self.width / 3 + self.width / 12) - (
                                    start_x)) / self.animation_number),
                             round((round(row * self.height / 2 + self.height / 12) -
                                    start_y)) / self.animation_number)
        elif column == 2 or column == 3 or column == self.number_of_player/2 + 2 or \
                column == self.number_of_player/2 + 3:
            self.canvas.move(self.allCards[self.count],
                             round((round(column * self.width / 3 + self.width / 24) - (
                                    start_x)) / self.animation_number),
                             round((round(row * self.height / 2 + self.height / 12) -
                                    start_y)) / self.animation_number)
        elif column == 4 or column == 5 or column == self.number_of_player/2 + 4 or \
                column == self.number_of_player/2 + 5:
            self.canvas.move(self.allCards[self.count],
                             round((round(column * self.width / 3) - (
                                    start_x)) / self.animation_number),
                             round((round(row * self.height / 2 + self.height / 12) -
                                    start_y)) / self.animation_number)
        else:
            self.canvas.move(self.allCards[self.count],
                             round((round(column * self.width / 3 - self.width / 24) - (
                                    start_x)) / self.animation_number),
                             round((round(row * self.height / 2 + self.height / 12) -
                                    start_y)) / self.animation_number)
        self.count_number += 1
        if self.count_number < self.animation_number:
            self.canvas.after(10, lambda x=start_x, y=start_y: self.animate3(x, y))
        elif self.count_number == self.animation_number and self.count < self.number_of_player-1:
            self.count_number = 0
            print(self.canvas.coords(self.allCards[self.count]))
            self.count += 1
            self.canvas.after(10, lambda x=start_x, y=start_y: self.animate3(x, y))

    def flip(self, x, event):
        de = self.canvas.coords(x)
        self.canvas.delete(x)
        card = self.canvas.create_image(de[0] + self.width_rubashka/12 * 0.7, de[1], image=self.rubashka_animation1,
                                        anchor="nw")
        self.canvas.after(50, lambda card=card: self.flip2(card, x))

    def flip2(self, x, number):
        de = self.canvas.coords(x)
        self.canvas.delete(x)
        card0 = self.canvas.create_image(de[0]+self.width_rubashka/12 * 0.7, de[1],
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
        canvas2 = Canvas(self.canvas, width=self.width_rubashka/6 * self.revert_counter_flip * 0.7,
                         height=self.width_rubashka)
        canvas2.place(x=de[0]-self.width_rubashka/12, y=de[1], anchor='nw')
        self.revert_counter_flip += 1
        self.canvas.after(50, lambda canvas=canvas2, y=de[0],
                                         z=de[1]: self.flip4(canvas, y, z, number))

    def flip4(self, x, de, z, number):
        x.destroy()
        self.canvas2 = Canvas(self.canvas, width=self.width_rubashka / 6 * self.revert_counter_flip * 0.7,
                         height=self.width_rubashka)
        self.canvas2.place(x=de - self.width_rubashka / 12, y=z, anchor='nw')
        self.revert_counter_flip += 1
        if self.revert_counter_flip < 7:
            self.canvas.after(50, lambda x=self.canvas2, y=de-self.width_rubashka/15,
                                         z=z: self.flip4(x, y, z, number))
        else:
            self.revert_counter_flip = 0
            self.open_icon(self.canvas2, number)

    def open_icon(self, canvas, number):
        canvas.create_text(self.width_rubashka/2, self.width_rubashka * 0.7 + 10, text=self.pers_cards[number-1][0],
                           anchor='c', font=("Verdana", 20))
        canvas.create_image(0, 0, image=self.prof_images[self.pers_cards[number-1][0]], anchor='nw')

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

class Timer:
    def __init__(self, root, x, y, time_minutes, time_seconds, width, height):
        self.time = time
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        canvas = Canvas(root, width=self.width, height=self.height)
        canvas.place(x=self.x, y=self.y)
        canvas.create_text(text="")

Game(6)