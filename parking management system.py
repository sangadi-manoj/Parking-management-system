import tkinter 
from tkinter import *
from tkinter import ttk
import time

root = tkinter.Tk()  #defining main window
root.title("Parking Management System")
root.geometry('1028x400')
root.config(bg = "#091833")
root.resizable(0,0)
#fonts
font11 = "{U.S.101} 20 bold"
font2 = "{Segoe UI} 13 bold"
font3 = "Arial 13 bold"
font4 = "{Courier New} 10 bold"
font5 = "{Courier New} 10 normal"

localtime = time.asctime(time.localtime(time.time()))
#defining labels

a1 = tkinter.Label(root,text="PARKING MANAGEMENT SYSYTEM", bg="#091833",fg="orange",font=font11)
a1.place(relx = 0.268, rely = 0.02, height = 51, width=507)
a2 = tkinter.Label(root,text="Select the type of vehicle",bg="#091833",fg="white",font= font2)
a2.place(x = 410, y = 90)
a = tkinter.Label(root,text=localtime,bg="#091833",fg="steel blue",font=font2)
a.place(x = 410, y = 50)

#define the fuction


#define the function
def fourwheels():

    #defining the another window
    newwindow = tkinter.Toplevel(root)
    newwindow.title("Four wheeler Parking")
    newwindow.geometry('750x450+600+40')
    newwindow.config(bg="#091833")
    
    a3 = tkinter.Label(newwindow,text="Four wheeler parking details",bg="#091833",fg="white", font=("Aries",15,"bold"))
    a3.place(x = 200, y = 25)
    a4 = tkinter.Label(newwindow,text = "Enter the vehicle number",bg = "#091833",fg = "white", font = font2)
    a4.place(x =150 , y = 60)

    num_entry = StringVar()
    num_entry = tkinter.Entry(newwindow,textvariable = num_entry,width = 25)
    num_entry.place(x = 400, y = 65)

    a5 = tkinter.Label(newwindow,text = "Enter the name of the driver",bg = "#091833",fg = "white", font = font3)
    a5.place(x =150 , y = 95)

    name_entry = StringVar()
    name_entry = tkinter.Entry(newwindow,textvariable = name_entry,width = 25)
    name_entry.place(x = 400, y = 100)

    a6 = tkinter.Label(newwindow,text="Time at which vehicle entered ",bg = "#091833",fg = "white", font = font3)
    a6.place(x =150 , y = 130)

    time_entry1 = IntVar()
    time_entry1 = tkinter.Entry(newwindow,textvariable = time_entry1,width = 25)
    time_entry1.place(x = 400, y = 135)

    a7 = tkinter.Label(newwindow,text = "Time at which vehicle left ",bg = "#091833",fg = "white", font = font3)
    a7.place(x =150 , y = 165)

    time_entry2 = IntVar()
    time_entry2 = tkinter.Entry(newwindow,textvariable = time_entry2,width = 25)
    time_entry2.place(x = 400, y = 170)

    
    def print_bill():
        num = float(time_entry1.get())
        num0 = float(time_entry2.get())
        result = (num0-num)*50
        total = str(result)
            
        p = tkinter.Label(newwindow,text="vehicle number: " + num_entry.get(),bg = "#091833",fg = "white",font = font3, width = 30)
        p.place(x = 250, y = 230)

        p1 = tkinter.Label(newwindow,text="vehicle owner: " + name_entry.get(),bg = "#091833",fg = "white",font = font3,width = 30)
        p1.place(x = 250, y = 255)

        p2 = tkinter.Label(newwindow,text="vehicle entry time: " + time_entry1.get(),bg = "#091833",fg = "white",font = font3, width = 30)
        p2.place(x = 250, y = 280)
        
        p3 = tkinter.Label(newwindow,text="vehicle exit time: " + time_entry2.get(),bg = "#091833",fg = "white",font = font3,width = 30)
        p3.place(x = 250, y = 310)

        p4 = tkinter.Label(newwindow,text = "vehicle parking fee: " + total,bg = "#091833",fg = "white",font = font3,width = 30)
        p4.place(x = 250, y = 340)
        
        def save_info():
        
            reg_no = num_entry.get()
            driver_name = name_entry.get()
            entry_time = time_entry1.get()
            exit_time = time_entry2.get()
            parking_fee = total

            print("Vehicle number",reg_no)
            print("Vehicle driver name",driver_name)
            print("Vehicle entry time",entry_time)
            print("Vehicle exit time",exit_time)

            file = open("four.txt","a")

            file.write("vehicle registration number: " + reg_no)

            file.write("\n")

            file.write("vehicle driver name: " + driver_name)

            file.write("\n")

            file.write("vehicle entering time: " + str(entry_time))

            file.write("\n")

            file.write("vehicle leaving time: " + str(exit_time))

            file.write("\n")

            file.write("Vehicle parking fee: " + parking_fee)

            file.write("\n")

            file.close()
            
        return save_info()

    bill_btn1 = tkinter.Button(newwindow,text="Print bill",command=print_bill)
    bill_btn1.place(x = 400, y = 200)
    
    

def twowheels():

    #defining the another window
    newwindow1 = tkinter.Toplevel(root)
    newwindow1.title("Two wheeler Parking")
    newwindow1.geometry('750x450+400+60')
    newwindow1.config(bg="#091833")

    b = tkinter.Label(newwindow1,text="Details of Two wheeler Parking",bg="#091833",fg="white",font=font2)
    b.place(x = 200, y = 25)

    b1 = tkinter.Label(newwindow1,text="Enter the vehicle number",bg="#091833",fg="white",font=font2)
    b1.place(x =150 , y = 60)

    text_entry1 = tkinter.Entry(newwindow1,width=25)
    text_entry1.place(x = 400, y = 65)

    b2 = tkinter.Label(newwindow1,text="Enter the name of the driver",bg="#091833",fg="white",font=font2)
    b2.place(x =150 , y = 95)

    text_entry2 = tkinter.Entry(newwindow1,width=25)
    text_entry2.place(x = 400, y = 100)

    b3 = tkinter.Label(newwindow1,text="Time at which vehicle entered ",bg="#091833",fg="white",font=font2)
    b3.place(x =150 , y = 130)

    time_entry3 = tkinter.Entry(newwindow1,width=25)
    time_entry3.place(x = 400, y = 135)

    b4 = tkinter.Label(newwindow1,text="Time at which vehicle left ",bg="#091833",fg="white",font=font2)
    b4.place(x =150 , y = 165)

    time_entry4 = tkinter.Entry(newwindow1,width=25)
    time_entry4.place(x = 400, y = 170)
    
    def print_bill1():
        num1 = float(time_entry3.get())
        num2 = float(time_entry4.get())
        result = (num2-num1)*25
        total = str(result)
            
        q = tkinter.Label(newwindow1,text="vehicle number: " + text_entry1.get(),bg="#091833",fg="white",font=("Aries",10), width= 30)
        q.place(x = 250, y = 230)

        q1 = tkinter.Label(newwindow1,text="vehicle owner: " + text_entry2.get(),bg="#091833",fg="white",font=("Aries",10),width = 30)
        q1.place(x = 250, y = 255)

        q2 = tkinter.Label(newwindow1,text="vehicle entry time: " + time_entry3.get(),bg="#091833",fg="white",font=("Aries",10), width = 30)
        q2.place(x = 250, y = 280)

        q3 = tkinter.Label(newwindow1,text="vehicle exit time: " + time_entry4.get(),bg="#091833",fg="white",font=("Aries",10),width = 30)
        q3.place(x = 250, y = 310)

        q4 = tkinter.Label(newwindow1,text="vehicle parking fee: " + total,bg="#091833",fg="white",font=("Aries",10),width = 30)
        q4.place(x = 250, y = 340)
        
        
        def save_info2():
        
            reg_no = text_entry1.get()
            driver_name = text_entry2.get()
            entry_time = time_entry3.get()
            exit_time = time_entry4.get()
            parking_fee = total

            print("vehicle number:",reg_no)
            print("Vehicle driver name:",driver_name)
            print("Vehicle entry time:",entry_time)
            print("vehicle exit time",exit_time)
            print("parking fee:" , parking_fee)

            file = open("two.txt","a")
           
            file.write("vehicle registration number: " + reg_no)

            file.write("\n")

            file.write("vehicle driver name: " + driver_name)

            file.write("\n")

            file.write("vehicle entering time: " + str(entry_time))

            file.write("\n")

            file.write("vehicle leaving time: " + str(exit_time))

            file.write("\n")
            
            file.write("Vehicle parking fee: " + parking_fee)

            file.write("\n")

            file.close()
            
        return save_info2()

    bill_btn2 = tkinter.Button(newwindow1,text="Print bill",command=print_bill1)
    bill_btn2.place(x = 400, y = 200)

def threewheels():

    #defining the another window
    newwindow2 = tkinter.Toplevel(root)
    newwindow2.title("Three wheeler Parking")
    newwindow2.geometry('750x450+400+40')
    newwindow2.config(bg="#091833")

    c0 = tkinter.Label(newwindow2,text="Details of Three wheeler Parking",bg="#091833",fg="white",font=font3)
    c0.place(x = 200, y = 25)

    c1 = tkinter.Label(newwindow2,text="Enter the vehicle number",bg="#091833",fg="white",font=font2)
    c1.place(x =150 , y = 60)

    text_entry1 = StringVar()
    text_entry1 = tkinter.Entry(newwindow2,textvariable=text_entry1,width=25)
    text_entry1.place(x = 400, y = 65)

    c2 = tkinter.Label(newwindow2,text="Enter the name of the driver",bg="#091833",fg="white",font=font2)
    c2.place(x =150 , y = 95)

    text_entry2 = StringVar()
    text_entry2 = tkinter.Entry(newwindow2,textvariable=text_entry2,width=25)
    text_entry2.place(x = 400, y = 100)

    c3 = tkinter.Label(newwindow2,text="Time at which vehicle entered",bg="#091833",fg="white",font=font2)
    c3.place(x =150 , y = 130)

    time_entry3 = IntVar()
    time_entry3 = tkinter.Entry(newwindow2,textvariable=time_entry3,width=25)
    time_entry3.place(x = 400, y = 135)

    c4 = tkinter.Label(newwindow2,text="Time at which vehicle left",bg="#091833",fg="white",font=font2)
    c4.place(x =150 , y = 165)

    time_entry4 = IntVar()
    time_entry4 = tkinter.Entry(newwindow2,textvariable=time_entry4,width=25)
    time_entry4.place(x = 400, y = 170)

    def print_bill2():
        num3 = float(time_entry3.get())
        num4 = float(time_entry4.get())
        result = (num4-num3)*35
        total = str(result)
            
        r = tkinter.Label(newwindow2,text="vehicle number: " + text_entry1.get(),bg="#091833",fg="white",font=font4, width= 30)
        r.place(x = 250, y = 230)

        r1 = tkinter.Label(newwindow2,text="vehicle owner: " + text_entry2.get(),bg="#091833",fg="white",font=font4,width = 30)
        r1.place(x = 250, y = 255)

        r2 = tkinter.Label(newwindow2,text="vehicle entry time: " + time_entry3.get(),bg="#091833",fg="white",font=font4, width = 30)
        r2.place(x = 250, y = 280)

        r3 = tkinter.Label(newwindow2,text="vehicle exit time: " + time_entry4.get(),bg="#091833",fg="white",font=font4,width = 30)
        r3.place(x = 250, y = 310)

        r4 = tkinter.Label(newwindow2,text="vehicle parking fee: " + total,bg="#091833",fg="white",font=font4,width = 30)
        r4.place(x = 250, y = 340)
        
        def save_info3():
        
            reg_no = text_entry1.get()
            driver_name = text_entry2.get()
            entry_time = time_entry3.get()
            exit_time = time_entry4.get()
            parking_fee = total

            print("vehicle number:",reg_no)
            print("Vehicle driver name:",driver_name)
            print("Vehicle entry time:",entry_time)
            print("vehicle exit time",exit_time)
            print("parking fee:" , parking_fee)

            file = open("three.txt","a")
            
            file.write("vehicle registration number: " + reg_no)

            file.write("\n")

            file.write("vehicle driver name: " + driver_name)

            file.write("\n")

            file.write("vehicle entering time: " + str(entry_time))

            file.write("\n")

            file.write("vehicle leaving time: " + str(exit_time))

            file.write("\n")
            
            file.write("vehicle parking fee: " + parking_fee)

            file.write("\n")
            
            file.close()
            
        return save_info3()

    bill_btn3 = tkinter.Button(newwindow2,text="Print bill",command=print_bill2)
    bill_btn3.place(x = 400, y = 200)



def others():

    #defining the another window
    newwindow3 = tkinter.Toplevel(root)
    newwindow3.title("Other Parking")
    newwindow3.geometry('750x450+400+40')
    newwindow3.config(bg="#091833")

    d0 = tkinter.Label(newwindow3,text="Details of other types of vehicle Parking",bg="#091833",fg="white",font=font2)
    d0.place(x = 200, y = 25)

    d1 = tkinter.Label(newwindow3,text="Enter the vehicle number",bg="#091833",fg="white",font=font2)
    d1.place(x =150 , y = 60)

    text_entry1 = StringVar()
    text_entry1 = tkinter.Entry(newwindow3,textvariable=text_entry1,width=25)
    text_entry1.place(x = 400, y = 65 )

    d2 = tkinter.Label(newwindow3,text="Enter the name of the driver",bg="#091833",fg="white",font=font2)
    d2.place(x = 150, y = 95)


    text_entry2 = StringVar()
    text_entry2 = tkinter.Entry(newwindow3,textvariable=text_entry2,width=25)
    text_entry2.place(x = 400, y = 100)
    

    d3 = tkinter.Label(newwindow3,text = "Time at which vehicle entered ",bg = "#091833",fg = "white",font = font2)
    d3.place(x = 150, y = 130)

    time_entry3 = IntVar()
    time_entry3 = tkinter.Entry(newwindow3,textvariable = time_entry3,width=25)
    time_entry3.place(x = 400, y = 135)

    d4 = tkinter.Label(newwindow3,text = "Time at which vehicle left ",bg = "#091833",fg = "white",font = font2)
    d4.place(x = 150, y = 165)

    time_entry4 = IntVar()
    time_entry4 = tkinter.Entry(newwindow3,textvariable = time_entry4,width = 25)
    time_entry4.place(x = 400, y = 170)

    
    
    
    def print_bill():
            
        
        num1=float(time_entry3.get())
        num2=float(time_entry4.get())
        result=(num2-num1)*50
        total = str(result)
            
        s = tkinter.Label(newwindow3,text="vehicle number: " + text_entry1.get(),bg="#091833",fg="white",font=font4, width= 30)
        s.place(x = 250, y = 230)

        s1 = tkinter.Label(newwindow3,text="vehicle owner: " + text_entry2.get(),bg="#091833",fg="white",font=font4,width = 30)
        s1.place(x = 250, y = 255)

        s2 = tkinter.Label(newwindow3,text="vehicle entry time: " + time_entry3.get(),bg="#091833",fg="white",font=font4, width = 30)
        s2.place(x = 250, y = 280)

        s3 = tkinter.Label(newwindow3,text="vehicle exit time: " + time_entry4.get(),bg="#091833",fg="white",font=font4,width = 30)
        s3.place(x = 250, y = 310)

        s4 = tkinter.Label(newwindow3,text="vehicle parking fee: " + total,bg="#091833",fg="white",font=font4,width = 30)
        s4.place(x = 250, y = 340)
        
       
        def save_info1():
        
            reg_no = text_entry1.get()
            driver_name = text_entry2.get()
            entry_time = time_entry3.get()
            exit_time = time_entry4.get()
            parking_fee = total
            
            print("vehicle number:",reg_no)
            print("Vehicle driver name:",driver_name)
            print("Vehicle entry time:",entry_time)
            print("vehicle exit time",exit_time)
            print("parking fee:" , parking_fee)
            
            file = open("others.txt","a")
            
            file.write("vehicle registration number: " + reg_no)

            file.write("\n")

            file.write("vehicle driver name: " + driver_name)

            file.write("\n")

            file.write("vehicle entering time: " + str(entry_time))

            file.write("\n")

            file.write("vehicle leaving time: " + str(exit_time))

            file.write("\n")

            file.write("parking fee: " + total)

            file.write("\n")
            
            file.close()
            
        return save_info1()

    bill_btn1 = tkinter.Button(newwindow3,text="Print bill",command=print_bill)
    bill_btn1.place(x = 400, y = 200)

    


#defining buttons

btn1 = tkinter.Button(root, text= "Two wheeler",borderwidth = 5,width = 10, command = twowheels)
btn1.place(x = 470, y = 150)

btn2 = tkinter.Button(root,text = "Three wheeler",borderwidth = 5,width = 10, command = threewheels)
btn2.place(x = 470, y = 200)

btn3 = tkinter.Button(root,text = "Four wheeler",borderwidth = 5,width = 10,command = fourwheels)
btn3.place(x = 470, y = 250)

btn4 = tkinter.Button(root,text = "Others",borderwidth = 5,width = 10,command = others)
btn4.place(x = 470, y = 300)





root.mainloop()
