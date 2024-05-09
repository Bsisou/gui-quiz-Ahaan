from tkinter import *

#**********************Starting Point of program*************************#
if __name__ == '__main__':
    root = Tk()
    bg=PhotoImage(file = "first.png")
    bglabel=Label(root,image=bg)
    bglabel.place(x=0,y=0)
    root.title("Spacial Awareness Quiz")
    root.geometry("500x500")
    root.mainloop()