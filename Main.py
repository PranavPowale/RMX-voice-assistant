from tkinter import Tk, Frame, Label, Button
from VoiceLib import wishme , cycle

class Main(Tk):

    def __init__(self, screenName=None, baseName=None, useTk=1, sync=0, use=None):

        super().__init__(screenName=screenName, baseName=baseName, useTk=useTk, sync=sync, use=use)

        self.title("RMX")
        self.geometry("600x600")

        self.f1 = Frame(master=self)
        
        self.txt1 = Button(master=self.f1, text="Greet me", command=wishme)
        self.txt1.pack()

        self.txt2 = Button(master=self.f1, text="Start routine", command=cycle)
        self.txt2.pack()

        self.f1.pack()


if __name__ == "__main__":

    app = Main()
    app.mainloop()