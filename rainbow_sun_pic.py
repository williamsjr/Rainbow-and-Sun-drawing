from tkinter import *
from time import *

class MyFrame(Frame):
    def __init__(self):
        Frame.__init__(self)

        self.myCanvas = Canvas(width=450, height=450, bg="skyblue")
        self.myCanvas.grid()

        self.myCanvas.create_arc(100, 100, 440, 440, style="arc",
            start=0, extent=180, fill="red", outline="red", width=20)

        self.myCanvas.create_arc(119, 119, 420, 420, style="arc",
            start=0, extent=180, fill="orange", outline="orange", width=21)            

        self.myCanvas.create_arc(139, 139, 400, 400, style="arc",
            start=0, extent=180, fill="yellow", outline="yellow", width=21)

        self.myCanvas.create_arc(159, 159, 380, 380, style="arc",
            start=0, extent=180, fill="green", outline="green", width=21)

        self.myCanvas.create_arc(179, 179, 360, 360, style="arc",
            start=0, extent=180, fill="blue", outline="blue", width=21)

        self.myCanvas.create_rectangle(0, 250, 450, 450, fill="darkgreen")

        # Create the sun and move it
        my_sun = self.myCanvas.create_oval(0, 160, 30, 190, fill="orange",
            outline="orange")

        for count in range(20):
            increment = 10*count
            self.myCanvas.coords(my_sun, 0 + increment, 160 - increment,
                30 + increment, 190 - increment)

            self.myCanvas.update()
            sleep(.25)   

frame02 = MyFrame()
frame02.mainloop()
