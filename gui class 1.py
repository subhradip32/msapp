from tkinter import *
window1 = Tk()
window1.title("fuck off boys")
window1.geometry("500x500")


def kick():
    print("KICKED")
    lb.config(text="kick")  # chage the text letters(strings)
    window2 = Tk()
    window2.title("Amarendra bahubaliiiiii")
    window2.geometry("200x200")
    window2.mainloop()
#labels
lb = Label(window1 ,text = "chal hat bahen k lau \n chal hat bahen k lau" )#Label is used for printing text in a window
lb.place(x=10,y=10)
lb.config(text = "sasaasasas") #chage the text letters(strings)

#button
ass = Button(window1,text = "kick your ass",command = kick )

ass.place(x=20,y=100)








window1.mainloop()