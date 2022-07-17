from tkinter import *
from PIL import Image, ImageTk
import os

def viewer():

    

    root = Tk()
    root.title("Python Calculator")
    root.resizable(0, 0)

    root.geometry("400x500")


    view_area = Text(root,width= 18,height= 2,font= ('Calibri 30'),bg='Green',fg='black')
    view_area.place(x =19, y =20)


    def calculation(x):

        try:
            view_area.delete('1.0',END)
            ans = eval(x)
            view_area.insert("end",ans)

        except:
            view_area.delete('1.0',END)
            error = '   \n     -------Error---------     '
            view_area.insert("end",error)


    def text_area(x):
        
        view_area.insert('end',x)


    # configure the image to the Label in frame
    def backslach():
        b = '('
        text_area(b)

    def frontslach():
        b = ')'
        text_area(b)

    def percentage():
        b = '%'
        text_area(b)

    def clear():
        view_area.delete('1.0',END)

    def answer():
         expre = view_area.get("1.0",END)
         calculation(expre)
         

    def seven():
        b ='7'
        text_area(b)

    def eight():
        b = '8'
        text_area(b)

    def nine():
        b = '9'
        text_area(b)

    def division():
        b = '/'
        text_area(b)

    def four():
        b = '4'
        text_area(b)

    def five():
        b = '5'
        text_area(b)

    def six():
        b = '6'
        text_area(b)

    def multiplication():
        b = '*'
        text_area(b)

    def one():
        b = '1'
        text_area(b)

    def two():
        b = '2'
        text_area(b)

    def three():
        b = '3'
        text_area(b)

    def subtraction():
        b = '-'
        text_area(b)

    def zero():
        b = '0'
        text_area(b)

    def dot():
        b = '.'
        text_area(b)

    def addition():
        b = '+'
        text_area(b)

    def previous():
        pass
        
    def next():
        global i
        i = i + 1
        try:
            image_label.config(image=images[i])
        except:
            i = -1
            next()


    # create buttons    
    btn1 = Button(root, text="(", width=6, activebackground ='orange' , activeforeground ='Black',bg='#3E065F', fg='white', font=('ariel 15 bold'), relief=GROOVE, command=backslach)
    btn1.place(x = 15 , y = 140)

    btn2 = Button(root, text=")", width=6, activebackground ='orange' , activeforeground ='Black', bg='#3E065F', fg='white', font=('ariel 15 bold'), relief=GROOVE, command=frontslach)
    btn2.place(x=110,y=140)

    btn3 = Button(root, text="%", width=6,  activebackground ='orange' ,  activeforeground ='Black',bg='#3E065F', fg='white', font=('ariel 15 bold'), relief=GROOVE, command=percentage)
    btn3.place(x=205, y=140)

    btn4 = Button(root, text="CE",width=6, activebackground ='orange' , activeforeground ='Black',bg='#3E065F', fg='white', font=('ariel 15 bold'), relief=GROOVE, command=clear)
    btn4.place(x=300, y=140)

    btn5 = Button(root, text="7", width=6, activebackground ='orange' , activeforeground ='Black', bg='#3E065F', fg='white', font=('ariel 15 bold'), relief=GROOVE, command=seven)
    btn5.place(x=15,y=200)

    btn6 = Button(root, text="8", width=6, activebackground ='orange' , activeforeground ='Black', bg='#3E065F', fg='white', font=('ariel 15 bold'), relief=GROOVE, command=eight)
    btn6.place(x=110, y=200)

    btn7 = Button(root, text="9",width=6,  activebackground ='orange' , activeforeground ='Black',bg='#3E065F', fg='white', font=('ariel 15 bold'), relief=GROOVE, command=nine)
    btn7.place(x=205, y=200)

    btn8 = Button(root, text="/", width=6, activebackground ='orange' , activeforeground ='Black', bg='#3E065F', fg='white', font=('ariel 15 bold'), relief=GROOVE, command=division)
    btn8.place(x=300,y=200)

    btn9 = Button(root, text="4", width=6, activebackground ='orange' , activeforeground ='Black', bg='#3E065F', fg='white', font=('ariel 15 bold'), relief=GROOVE, command=four)
    btn9.place(x=15, y=260)

    btn10 = Button(root, text="5",width=6, activebackground ='orange' , activeforeground ='Black', bg='#3E065F', fg='white', font=('ariel 15 bold'), relief=GROOVE, command=five)
    btn10.place(x=110, y=260)

    btn12 = Button(root, text="6", width=6, activebackground ='orange' , activeforeground ='Black', bg='#3E065F', fg='white', font=('ariel 15 bold'), relief=GROOVE, command=six)
    btn12.place(x=205,y=260)

    btn13 = Button(root, text="*", width=6, activebackground ='orange' , activeforeground ='Black', bg='#3E065F', fg='white', font=('ariel 15 bold'), relief=GROOVE, command=multiplication)
    btn13.place(x=300, y=260)

    btn14 = Button(root, text="1",width=6, activebackground ='orange' , activeforeground ='Black', bg='#3E065F', fg='white', font=('ariel 15 bold'), relief=GROOVE, command=one)
    btn14.place(x = 15 , y=320)

    btn15 = Button(root, text="2", width=6, activebackground ='orange' , activeforeground ='Black', bg='#3E065F', fg='white', font=('ariel 15 bold'), relief=GROOVE, command=two)
    btn15.place(x=110,y=320)

    btn16 = Button(root, text="3", width=6, activebackground ='orange' , activeforeground ='Black', bg='#3E065F', fg='white', font=('ariel 15 bold'), relief=GROOVE, command=three)
    btn16.place(x=205, y=320)

    btn17 = Button(root, text="-",width=6, activebackground ='orange' , activeforeground ='Black', bg='#3E065F', fg='white', font=('ariel 15 bold'), relief=GROOVE, command=subtraction)
    btn17.place(x=300 , y=320)

    btn18 = Button(root, text="0", width=6, activebackground ='orange' , activeforeground ='Black', bg='#3E065F', fg='white', font=('ariel 15 bold'), relief=GROOVE, command=zero)
    btn18.place(x=15, y=380)

    btn19 = Button(root, text=".", width=6, activebackground ='orange' , activeforeground ='Black', bg='#3E065F', fg='white', font=('ariel 15 bold'), relief=GROOVE, command=dot)
    btn19.place(x=110, y=380)

    btn20 = Button(root, text="=",width=6, activebackground ='orange' , activeforeground ='Black', bg='#3E065F', fg='white', font=('ariel 15 bold'), relief=GROOVE, command=answer)
    btn20.place(x=205 , y=380)

    btn21 = Button(root, text="+", width=6, activebackground ='orange' , activeforeground ='Black', bg='#3E065F', fg='white', font=('ariel 15 bold'), relief=GROOVE, command=addition)
    btn21.place(x=300,y=380)

    btn22 = Button(root, text="on/off", width=6, activebackground ='orange' , activeforeground ='Black', bg='#3E065F', fg='white', font=('ariel 15 bold'), relief=GROOVE, command=root.destroy)
    btn22.place(x=300, y=440)

    root.mainloop()


       
        
viewer()
