from cgitb import text
import tkinter as tk
from tkinter import *
from tkinter import font
import pyttsx3

engine=pyttsx3.init()

def speaknow():
    engine.say(textv.get())
    engine.runAndWait()
    engine.stop()

root=Tk()

textv=StringVar()

obj=LabelFrame(root,text="Text to Speech Python", font=20,bd=2)
obj.pack(fill="both",expand="yes",padx=10,pady=10)

lbl=Label(obj,text="Text", font=30)
lbl.pack(side=tk.LEFT,padx=5)

text=Entry(obj,textvariable=textv,font=30,width=25,bd=5)
text.pack(side=tk.LEFT,padx=10)

btn=Button(obj,text="Speak",font=20,bg="white",fg="black",command=speaknow)
btn.pack(side=tk.LEFT,padx=5)

root.title("Text to Speech in Python")
root.geometry("450x250")
root.resizable(False,False)
root.mainloop()