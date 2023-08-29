from tkinter import *
from tkinter import ttk #theme of tk
from tkinter import messagebox

GUI = Tk() #หน้าจอหลักของโปรแกรม
GUI.title('โปรแกรมบันทึกข้อมูล') #ชื่อโปรแกรม
GUI.geometry('500x400') #ขนาดของโปรแกรม

L1= Label(GUI,text='โปรแกรมบันทึก',font=('Angsana New',22),fg='green')
L1.place(x=200,y=35)
'''
B1 = Button(GUI,text='เงินมีอยู่กี่บาท') #หมายความว่า Button ไปใส่ในโปรแกรมหลักที่ชื่อว่า GUI
B1.pack(ipadx=20,ipady=20) #ทำให้ปุ่มอยู่ตรงกลาง ด้านในคือการขยายปุ่ม x,y

'''
B1 = ttk.Button(GUI,text='เงินมีอยู่กี่บาท') 
B1.pack(ipadx=10,ipady=10) 

#########
def Button2() :
    text = 'ตอนนี้มีเงิน300บาท'
    messagebox.showinfo('เงินในบัญชี',text) #มี 3 show warining,error
    

FB1 = Frame(GUI) #คล้ายกระดาน
FB1.place(x=100,y=200)

B2 = ttk.Button(FB1,text='มีเงินเท่าไร',command=Button2) #เอามาผูกกับ button2
B2.pack(ipadx=20,ipady=20)
#จุดoringin อยู่ซ้ายบน
#########

GUI.mainloop()
