from tkinter import*
from tkinter import messagebox
import mysql.connector

background="#06283D"
frambebg="#EDEDED"
framefg="#06283D"

root=Tk()
root.title("Login Page")
root.geometry("1250x700+210+100")
root.config(bg=background)
root.resizable(False,False)

#icon

image_icon=PhotoImage(file="image/one.png")
root.iconphoto(False,image_icon)

#backgroundimage

frame=Frame(root,bg="red")
frame.pack(fill=Y)

backgroundimage=PhotoImage(file="image/log.png")
Label(frame,image=backgroundimage).pack()

#user entry

def user_enter(e):
    user.delete(0,"end")



user=Entry(frame,width=15,fg="#fff",border=1,bg="#042770",font=("Arial Bold",24),foreground="#F4F6F6")
user.insert(0,"UserID")
user.bind("<FocusIn>",user_enter)

user.place(x=75,y=245)

#password entry

password=Entry(frame,width=15,fg="#fff",border=1,bg="#042770",font=("Arial Bold",24),foreground="#F4F6F6")
password.insert(0,"Password")
password.place(x=75,y=345)








root.mainloop()