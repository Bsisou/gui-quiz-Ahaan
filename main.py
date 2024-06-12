from tkinter import *

#class to determine what goes on the screen
class SpatialStart:
    def __init__(self, start):
        #name label
        self.name_label: Label = Label(start, text="Please enter Name ")
        self.name_label.place(x=200,y=300)

        #name entry
        self.name_entry = Entry(start)
        self.name_entry.place(x=175,y=325)
       
#this is the button to continue to second page#
        self.startbtn=Button(start, text="start", font=("arial", 8), background="black", foreground = "white" , command=self.Start)
        self.startbtn.place(x=330, y=323)
    def Start(self):
        self.name_label.destroy()
        self.name_entry.destroy() 
        self.startbtn.destroy()
        bglabel.destroy()
        #opent next window (create an instance of questions class)
class Questions:
    def __init__(self, start):
        pass

#**********************Starting Point of program*************************#
if __name__ == '__main__':
    start = Tk()
    bg=PhotoImage(file = "first.png")
    bglabel=Label(start,image=bg)
    bglabel.place(x=0,y=0)
    start.title("Spacial Awareness Quiz")
    start.geometry("500x500")
    SpatialStart(start) #class to start the program
    start.mainloop()
    questions =  Tk()