from tkinter import *
import logging as log
import signing as sign

root = Tk()
root.title("Food Frenzy")
root.iconbitmap("lunch-box.ico")
positionRight = int(root.winfo_screenwidth()/2 - 300/2)
positionDown = int(root.winfo_screenheight()/2.2 - 300/2)
root.geometry("+{}+{}".format(positionRight, positionDown))
root.resizable(0,0)

def login():
  root.destroy()
  log.logging_in()

def signup():
  root.destroy()
  sign.signing_up()
  
welcome_lbl = Label(root, text="FOOD FRENZY")
log_in = Button(root, text="Log-in", command=login)
sign_up = Button(root, text="Sign-up", command=signup)

welcome_lbl.place(x=125, y=5)
log_in.place(x=125, y=20)
sign_up.place(x=125, y=50)

root.mainloop()
