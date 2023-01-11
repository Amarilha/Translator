from tkinter import *
from tkinter import ttk,messagebox

import Translator

root=Tk()
root.title("Google Translator")
root.geometry("1080x400")
root.resizable(False,False)
root.configure(background="white")

#icon
image_icon =PhotoImage(file="")
root.iconphoto(False,image_icon)

#arrow
arrow_image=PhotoImage(file="")
image_label=Label(root,image=arrow_image,width=150)
image_label.place(x=460, y=50)

language = Translator.language
languageV=list(language.values())
lang1=language.Keys()

#first combobox
combo1=ttk.Combobox(root,values=languageV,font="Roboto 14",state="r")
combo1.place(x=110,y=20)
combo1.set("ENGLISH")

root.mainloop()