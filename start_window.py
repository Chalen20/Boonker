import sys
if "tkinter" not in sys.modules:
    from tkinter import *
from PIL import Image, ImageTk
import Game
import Character


class Saver:
    def __init__(self, player_number, job, hobby, add_info, human_trait, phobia, biological, health, body_type):
        f = open("player" + str(player_number+1) + ".html", "w")
        message = """<html>
        <head>
                <style>
                 .card {
                  margin : auto ;
                  width : 400px;
                  height : 600px;
                  background-color: #f7d065;
                  border-radius: 40px;
                  }
                  tr{
                  padding : 20px 25px 20px 25px;
                  }
                  td{
                  padding : 20px 25px 20px 25px;
                  }
                  table{
                    width: 400px
                  }
</style>
        </head>
<body>
  <div class = "card">
        <table>
            <tbody>
                <tr>
                    <td>
                        Player number:
                    </td>
                    <td class="data">
                        """ + str(player_number+1) + """
                    </td>
                </tr>
                <tr>
                    <td>
                        Profession: 
                    </td>
                    <td class="data">
                        """ + job + """
                    </td>
                </tr>
                <tr>
                    <td>
                        Hobby: 
                    </td>
                    <td class="data">
                        """ + hobby + """
                    </td>
                </tr>
                <tr>
                    <td>
                        Dop. info: 
                    </td>
                    <td class="data">
                        """ + add_info + """
                    </td>
                </tr>
                <tr>
                    <td>
                        Human trait:
                    </td>
                    <td class="data">
                        """ + human_trait + """
                    </td>
                </tr>
                <tr>
                    <td>
                        Phobia:
                    </td>
                    <td class="data">
                        """ + phobia + """
                    </td>
                </tr>
                <tr>
                    <td>
                        Bio. Characteristic:
                    </td>
                    <td class="data">
                        """ + biological + """
                    </td>
                </tr>
                <tr>
                    <td>
                        Health: 
                    </td>
                    <td class="data">
                        """ + health + """
                    </td>
                </tr>
                <tr>
                    <td>
                        Body type: 
                    </td>
                    <td class="data">
                        """ + body_type + """
                    </td>
                </tr>
            </tbody>
        </table>
  </div>
</body>
</html>"""

        f.write(message)
        f.close()


class StartWindow:
    def __init__(self):
        self.window = Tk()
        self.window.title("Boonker")
        width = self.window.winfo_screenwidth()
        height = self.window.winfo_screenheight()
        width = width // 2
        height = height // 2
        width = width - 250
        height = height - 250
        self.player_number = 6
        self.window.geometry('500x500+{}+{}'.format(width, height))
        self.window.resizable(False, False)
        self.canvas = Canvas(self.window, height=500, width=500, bg="red")
        self.canvas.pack()
        self.stickman6 = Image.open("img/stickman6.png")
        self.stickman6 = self.stickman6.resize((600, 300), Image.ANTIALIAS)
        self.stickman6 = ImageTk.PhotoImage(self.stickman6)
        self.stickmans = self.canvas.create_image(250, 150, image=self.stickman6)

        self.stickman8 = Image.open("img/stickman8.png")
        self.stickman8 = self.stickman8.resize((600, 300), Image.ANTIALIAS)
        self.stickman8 = ImageTk.PhotoImage(self.stickman8)

        self.stickman10 = Image.open("img/stickman10.png")
        self.stickman10 = self.stickman10.resize((600, 300), Image.ANTIALIAS)
        self.stickman10 = ImageTk.PhotoImage(self.stickman10)

        self.stickman12 = Image.open("img/stickman12.png")
        self.stickman12 = self.stickman12.resize((600, 300), Image.ANTIALIAS)
        self.stickman12 = ImageTk.PhotoImage(self.stickman12)

        self.stickman14 = Image.open("img/stickman14.png")
        self.stickman14 = self.stickman14.resize((600, 300), Image.ANTIALIAS)
        self.stickman14 = ImageTk.PhotoImage(self.stickman14)

        self.gears_icon = Image.open("img/shesterna.png")
        self.gears = self.gears_icon.resize((50, 50), Image.ANTIALIAS)
        self.gears = ImageTk.PhotoImage(self.gears)
        self.gears_button = self.canvas.create_image(475, 25, image=self.gears)
        self.canvas.tag_bind(self.gears_button, "<Button-1>", self.settings)

        self.button6 = Button(self.canvas, width=10, height=3, bg="yellow", text=6, command=self.button6)
        self.button6.place(x=(6/2-3)*100+10, y=270)
        self.button8 = Button(self.canvas, width=10, height=3, bg="yellow", text=8, command=self.button8)
        self.button8.place(x=(8/2-3)*100+10, y=270)
        self.button10 = Button(self.canvas, width=10, height=3, bg="yellow", text=10, command=self.button10)
        self.button10.place(x=(10/2-3)*100+10, y=270)
        self.button12 = Button(self.canvas, width=10, height=3, bg="yellow", text=12, command=self.button12)
        self.button12.place(x=(12/2-3)*100+10, y=270)
        self.button14 = Button(self.canvas, width=10, height=3, bg="yellow", text=14, command=self.button14_b)
        self.button14.place(x=(14/2-3)*100+10, y=270)

        img2 = Image.open('img/start.png')
        img2 = ImageTk.PhotoImage(img2)
        self.start = self.canvas.create_image(75, 380, image=img2, anchor=NW)
        self.motion()
        self.canvas.tag_bind(self.start, "<Button-1>", lambda event: self.start_game(self.player_number, event))
        self.window.mainloop()

    def motion(self):
        self.canvas.move(self.start, 0, -1)
        if self.canvas.coords(self.start)[1] > 350:
            self.window.after(15, self.motion)

    def start_game(self, player_number, event):
        self.window.destroy()
        pers_cards = []
        pers = Character.Person()
        for i in range(0, player_number):
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
            pers_cards.append(pers_characteristics)

        for i in pers_cards:
            print(i)

        for i in range(len(pers_cards)):
            Saver(i, pers_cards[i][0] + ", " + str(pers_cards[i][1]), pers_cards[i][2] + ", " + str(pers_cards[i][3]),
                  pers_cards[i][4], pers_cards[i][5] + ", " + pers_cards[i][6], pers_cards[i][7],
                  pers_cards[i][8] + ", " + pers_cards[i][9] + ", " + pers_cards[i][10], pers_cards[i][11],
                  pers_cards[i][12] + ", " + str(pers_cards[i][13]) + ", " + str(pers_cards[i][14]))

        game = Game.Game(player_number, pers_cards)

    def settings(self, event):
        self.canvas.delete(self.gears_button)
        self.canvas_frame = Canvas(self.canvas, width=450, height=500, bg="blue")
        self.canvas_frame.place(x=0, y=0)
        self.frame2 = Canvas(self.canvas, width=50, height=500, bg="red")
        self.frame2.place(x=450, y=0)
        self.gears_button2 = self.frame2.create_image(25, 25, image=self.gears)
        self.frame2.tag_bind(self.gears_button2, "<Button-1>", self.close_settings)
        self.button14.destroy()

    def close_settings(self, event):
        self.canvas_frame.destroy()
        self.frame2.destroy()
        self.gears_button = self.canvas.create_image(475, 25, image=self.gears)
        self.button14 = Button(self.canvas, width=10, height=3, bg="yellow", text=14, command=self.button14_b)
        self.button14.place(x=(14 / 2 - 3) * 100 + 10, y=270)
        self.canvas.tag_bind(self.gears_button, "<Button-1>", self.settings)

    def button6(self):
        self.canvas.delete(self.stickmans)
        self.player_number = 6
        self.stickmans = self.canvas.create_image(250, 150, image=self.stickman6)
        self.canvas.delete(self.gears_button)
        self.gears_button = self.canvas.create_image(475, 25, image=self.gears)
        self.canvas.tag_bind(self.gears_button, "<Button-1>", self.settings)

    def button8(self):
        self.canvas.delete(self.stickmans)
        self.player_number = 8
        self.stickmans = self.canvas.create_image(250, 150, image=self.stickman8)
        self.canvas.delete(self.gears_button)
        self.gears_button = self.canvas.create_image(475, 25, image=self.gears)
        self.canvas.tag_bind(self.gears_button, "<Button-1>", self.settings)

    def button10(self):
        self.canvas.delete(self.stickmans)
        self.player_number = 10
        self.stickmans = self.canvas.create_image(250, 150, image=self.stickman10)
        self.canvas.delete(self.gears_button)
        self.gears_button = self.canvas.create_image(475, 25, image=self.gears)
        self.canvas.tag_bind(self.gears_button, "<Button-1>", self.settings)

    def button12(self):
        self.canvas.delete(self.stickmans)
        self.player_number = 12
        self.stickmans = self.canvas.create_image(250, 150, image=self.stickman12)
        self.canvas.delete(self.gears_button)
        self.gears_button = self.canvas.create_image(475, 25, image=self.gears)
        self.canvas.tag_bind(self.gears_button, "<Button-1>", self.settings)

    def button14_b(self):
        self.canvas.delete(self.stickmans)
        self.player_number = 14
        self.stickmans = self.canvas.create_image(250, 150, image=self.stickman14)
        self.canvas.delete(self.gears_button)
        self.gears_button = self.canvas.create_image(475, 25, image=self.gears)
        self.canvas.tag_bind(self.gears_button, "<Button-1>", self.settings)

StartWindow()