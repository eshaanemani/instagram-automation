from tkinter import *
from PIL import Image,ImageTk
import os
from tkinter.ttk import Combobox
from openpyxl import workbook
import pathlib

root=Tk()  #k is small
root.title('login')
root.geometry('1000x600+170+100')
root.iconbitmap('icon.ico')
 #its x not multiplication

right_frame1 =Frame(root, borderwidth=1, bg='#C13584', relief="solid", highlightthickness=2)
right_frame1.pack(side="top", expand=False, fill="y")
container1 =Frame(right_frame1, borderwidth=1, bg="white", relief="solid")
container1.pack(expand=True, fill="y", padx=5, pady=5)
Label(container1,text='PROFILE',width=140,bg='white',fg='#C13584',font=('Helvetica', 30, 'bold')).pack(side=TOP,fill=X)

f=Frame(root,bd=3,bg="black",width=700,height=460,relief=GROOVE)
f.place(x=270,y=100)
lbl=Label(f,text='PROFILE PICTURE',height=1,bg='white',fg='#C13584',font=('Helvetica', 10, 'bold'))
lbl.pack()

my_pic = Image.open("wp7810664.webp")
resized = my_pic.resize((700,460),Image.ANTIALIAS)
new_pic = ImageTk.PhotoImage(resized)
my_label=Label(f, image=new_pic,bg='white')
my_label.pack(pady=2,padx=0)


Button(root,text="Name",width=19,height=2,font="arial 12 bold",fg='white',bg="#C13584").place(x=10,y=100)
B=Entry(root,width=25,fg='black',border=2,bg="white",font=('Microsoft YaHie UI Light',11))
B.place(x=10,y=160)
B.insert(0,'ARINA JOSH')
savebutton=Button(root,text="Username",width=19,height=2,font="arial 12 bold",fg='white',bg="#C13584")
savebutton.place(x=10,y=210)
Ba=Entry(root,width=25,fg='black',border=2,bg="white",font=('Microsoft YaHie UI Light',11))
Ba.place(x=10,y=270)
Ba.insert(0,'artistic_space8')
Button(root,text="About",width=19,height=2,font="arial 12 bold",fg='white',bg="#C13584").place(x=10,y=320)

Button(root,text="Settings",width=19,height=2,font="arial 12 bold",fg='white',bg="#C13584").place(x=10,y=400)
def home():
    root.destroy()
    import homepage
Button(root,text="Home",width=19,height=2,font="arial 12 bold",fg='white',command=home,bg="#C13584").place(x=10,y=480)

root.mainloop()