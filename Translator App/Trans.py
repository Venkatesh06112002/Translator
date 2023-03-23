from googletrans import Translator
from gtts import gTTS
from tkinter import *
import os

window= Tk()
window.geometry('600x280')
window.config(bg="black")

e1=Entry(window, bg="white", fg="red",font=("Arial",25,"bold"))
e1.place(x=20,y=20)

def convertlang():
    a1=e1.get()
    t1=Translator()
    t2=click_option.get()

    if t2=="English":
        convert="en"
    elif t2=="Hindi":
        convert="hi"
    elif t2=="German":
        convert="de"
    elif t2=="French":
        convert="fr"
    elif t2=="Spanish":
        convert="es"
    elif t2=="Tamil":
        convert="ta"
    elif t2=="Telugu":
        convert="te"
    elif t2=="Urudu":
        convert="ur"
    elif t2=="Russian":
        convert="ru"


    trans_text=t1.translate(a1,dest=convert)
    trans_text=trans_text.text
    
    ob1=gTTS(text=trans_text, slow=False, lang=convert)
    label2.config(text=trans_text)
    
    


choices = [
    "English",
    "Hindi",
    "German",
    "French",
    "Spanish",
    "Tamil",
    "Telugu",
    "Urudu",
    "Russian"
    ]
        
click_option=StringVar()
click_option.set("Select Language")

list_drop=OptionMenu(window, click_option, *choices)
list_drop.configure(background="green",foreground="white",font=('Arial', 15,"bold"))
list_drop.place(x=400,y=20)
label2=Label(window, text="\t\t\t\t\t\t\t",bg="black",fg="white",font=('Arial',40,"bold"))
label2.place(x=0,y=120)
label2=Label(window, text="Translated Text",bg="black",fg="white",font=('Arial',40,"bold"))
label2.place(x=180,y=120)
Button1=Button(window, text="Translate",bg="red",fg="white",font=('Arial',25,"bold"),command=convertlang)
Button1.place(x=220,y=200)





window.mainloop()
