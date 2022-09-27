

""" ###############
    Simple Simon game in Python
    Created by: Ech012
    ###############"""




import ctypes as c
import tkinter as tk
import random 
import time

class Simon:
    #All the basic variables
    def __init__(self, root):
        self.root = root
        self.root.title("Simon")
        self.root.geometry("900x900")
        self.countYellow = 0
        self.countBlue = 0
        self.countRed = 0
        self.countGreen = 0
        self.ClickRED = 0
        self.ClickBLUE = 0
        self.ClickYELLOW = 0
        self.ClickGREEN = 0
        self.OrderList = []
        self.PlayerList = []
        self.Place = 0
    
    
    #keep the window open
    def main(self):
        self.root.mainloop()
    
    #When the button is clicked it will check if the color is the same as the color in the list
    def OnClickBlue(self):
        try:
            self.PlayerList.append(1)
            while True:
                if self.PlayerList[self.Place] == self.OrderList[self.Place]:
                    self.Place += 1
                else:
                    break
        except IndexError:
            pass

        
    def OnClickRed(self):
        try:
            self.PlayerList.append(2)
            while True:
                if self.PlayerList[self.Place] == self.OrderList[self.Place]:
                    self.Place += 1
                else:
                    print("No!")
                    break
        except IndexError:
            pass

    def OnClickYellow(self):
        try:
            self.PlayerList.append(3)
            while True:
                if self.PlayerList[self.Place] == self.OrderList[self.Place]:
                    self.Place += 1
                else:
                    break
        except IndexError:
            pass

    def OnClickGreen(self):
        try:
            self.PlayerList.append(4)
            while True:
                if self.PlayerList[self.Place] == self.OrderList[self.Place]:
                    self.Place += 1
                else:
                    break
        except IndexError:
            pass

    


    #Choose a random color
    def random_color(self):
        a = random.randint(1, 4)
        self.OrderList.append(a)

    
    #Check the level if the sequence is correct
    def check_the_level(self):
        if self.OrderList == self.PlayerList:
            c.windll.user32.MessageBoxW(0, " ", "You passed the level", 1)
        else:
            c.windll.user32.MessageBoxW(0, "", "you failed, goodbye!", 1)
            self.root.destroy()
    #check the order list and change the color of the button
    def checklist(self):
        self.random_color()
        try:
            self.PlayerList.clear()
        except IndexError:
            pass
        for i in self.OrderList:
            if i == 1:
                self.button1["bg"] = "blue"
                self.root.update()
                time.sleep(1)
                self.button1["bg"] = "light blue"
                self.root.update()
                time.sleep(1)
                self.button1["bg"] = "blue"
                self.root.update()
            elif i == 2:
                self.button2["bg"] = "red"
                self.root.update()
                time.sleep(1)
                self.button2["bg"] = "pink"
                self.root.update()
                time.sleep(1)
                self.button2["bg"] = "red"
                self.root.update()
            elif i == 3:
                self.button3["bg"] = "yellow"
                self.root.update()
                time.sleep(1)
                self.button3["bg"] = "light yellow"
                self.root.update()
                time.sleep(1)
                self.button3["bg"] = "yellow"
                self.root.update()
            elif i == 4:
                self.button4["bg"] = "green"
                self.root.update()
                time.sleep(1)
                self.button4["bg"] = "light green"
                self.root.update()
                time.sleep(1)
                self.button4["bg"] = "green"
                self.root.update()
    #create the buttons
    def buttuns(self):
        self.button1 = tk.Button(self.root, bg="blue", width=10, height=5, command=self.OnClickBlue)
        self.button1.place(x=650, y=50)
        self.button2 = tk.Button(self.root, bg="red", width=10, height=5, command=self.OnClickRed)
        self.button2.place(x=570, y=50)
        self.button3 = tk.Button(self.root, bg="yellow", width=10, height=5, command=self.OnClickYellow)
        self.button3.place(x=650, y=130)
        self.button4 = tk.Button(self.root, bg="green", width=10, height=5, command=self.OnClickGreen)
        self.button4.place(x=570, y=130)
        self.srartbt = tk.Button(self.root, text="Start", width=10, height=5, command=self.checklist)
        self.srartbt.place(x=650, y=210)
        self.CheckLevel = tk.Button(self.root, text="Check Level", width=10, height=5, command=self.check_the_level)
        self.CheckLevel.place(x=570, y=210)
    #to start the game
    def game(self):
        self.buttuns()
        self.main()

def main():
    root = tk.Tk()
    simon = Simon(root)
    simon.game()