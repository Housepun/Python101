from tkinter import *
from tkinter import ttk #theme of tk
from tkinter import messagebox

GUI = Tk() 
GUI.title('โปรแกรมบันทึกข้อมูล') 
GUI.geometry('500x400') 
#B1.pack(ipadx=20,ipady=20)#expand size of button 
L1 = Label(GUI,text='โปรแกรมบันทึกลง CSV file format',font=('Angsana New',30),fg='green')
L1.place(x=30,y=20)
####################################

def Button2():
    text = 'readcsv'
    messagebox.showinfo('ข้อมูลใน Data.csv',text)

FB1 = Frame(GUI)
FB1.place(x=100,y=80)
B2 = ttk.Button(FB1,text='แสดงข้อมูลในไฟล์ที่บันทึก',command=Button2)
B2.pack(ipadx=20,ipady=20)


###########################
def Button3():
    text ='Python 101, Math'
    messagebox.showinfo('วิชาที่เรียนวันที่ 10-20 ก.พ.',text)

FB2 = Frame(GUI) #คล้ายกระดาน
FB2.place(x=90,y=100)
B3 = ttk.Button(FB1,text='บันทึกข้อมูล',command=Button3)
B3.pack(ipadx=20,ipady=20)

GUI.mainloop()
