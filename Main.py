from tkinter import Tk, Frame, Label
from VoiceAi import wishme

class Main(Tk):

    def __init__(self, screenName=None, baseName=None, useTk=1, sync=0, use=None):

        super().__init__(screenName=screenName, baseName=baseName, useTk=useTk, sync=sync, use=use)

        self.title("RMX")

        self.f1 = Frame(master=self)
        
        self.txt1 = Label(master=self.f1, text="RMX")
        self.txt1.pack()

        self.f1.pack()

        wishme()

if __name__ == "__main__":

    app = Main()
    app.mainloop()