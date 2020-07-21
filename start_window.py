from tkinter import *
from PIL import Image, ImageTk

class Start_window:
    def __init__(self):
        self.window = Tk()
        self.window.title("Game")
        width = self.window.winfo_screenwidth()
        height = self.window.winfo_screenheight()
        width = width // 2
        height = height // 2
        width = width - 250
        height = height - 250
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
        self.window.mainloop()

    def motion(self):
        self.canvas.move(self.start, 0, -1)
        if self.canvas.coords(self.start)[1] > 350:
            self.window.after(15, self.motion)

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
        self.stickmans = self.canvas.create_image(250, 150, image=self.stickman6)
        self.canvas.delete(self.gears_button)
        self.gears_button = self.canvas.create_image(475, 25, image=self.gears)
        self.canvas.tag_bind(self.gears_button, "<Button-1>", self.settings)

    def button8(self):
        self.canvas.delete(self.stickmans)
        self.stickmans = self.canvas.create_image(250, 150, image=self.stickman8)
        self.canvas.delete(self.gears_button)
        self.gears_button = self.canvas.create_image(475, 25, image=self.gears)
        self.canvas.tag_bind(self.gears_button, "<Button-1>", self.settings)

    def button10(self):
        self.canvas.delete(self.stickmans)
        self.stickmans = self.canvas.create_image(250, 150, image=self.stickman10)
        self.canvas.delete(self.gears_button)
        self.gears_button = self.canvas.create_image(475, 25, image=self.gears)
        self.canvas.tag_bind(self.gears_button, "<Button-1>", self.settings)

    def button12(self):
        self.canvas.delete(self.stickmans)
        self.stickmans = self.canvas.create_image(250, 150, image=self.stickman12)
        self.canvas.delete(self.gears_button)
        self.gears_button = self.canvas.create_image(475, 25, image=self.gears)
        self.canvas.tag_bind(self.gears_button, "<Button-1>", self.settings)

    def button14_b(self):
        self.canvas.delete(self.stickmans)
        self.stickmans = self.canvas.create_image(250, 150, image=self.stickman14)
        self.canvas.delete(self.gears_button)
        self.gears_button = self.canvas.create_image(475, 25, image=self.gears)
        self.canvas.tag_bind(self.gears_button, "<Button-1>", self.settings)

Start_window()