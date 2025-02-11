import sqlite3
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
import tkinter.messagebox as mb
con = sqlite3.connect("gym.db")  
#con.execute("drop database if exists gym ") 
print("Database opened successfully in login")  
con.execute("drop table if exists account ") 
con.execute("create table if not exists account ( name TEXT NOT NULL, email TEXT  NOT NULL, password TEXT NOT NULL)")  
  
print("Table account created successfully") 

con.execute("insert into account(name,email,password) values ( 'Charushri','ch','54321')") 
con.execute("insert into account(name,email,password) values ( 'Madhuri','madhuri1245@gmail.com','54321')")
con.execute("insert into account(name,email,password) values ( 'Gunika','gunika1245@gmail.com','54321')")
con.execute("insert into account(name,email,password) values ( 'Surabhi','surabhi1245@gmail.com','54321')") 

s='''create table if not exists member (ID INTEGER PRIMARY KEY AUTOINCREMENT, NAME TEXT NOT NULL, 
  ADDRESS CHAR(50),AGE INT NOT NULL,EMAIL TEXT NOT NULL,MOBILE INT NOT NULL,
  FOODTYPE TEXT NOT NULL,
  GENDER TEXT NOT NULL,
  COURSE TEXT NOT NULL,
  COST INT NOT NULL,
  SLOT TEXT NOT NULL,
  TRAINER_NAME TEXT NOT NULL)'''  
con.execute("create table if not exists member (ID INTEGER PRIMARY KEY AUTOINCREMENT, NAME TEXT NOT NULL, ADDRESS CHAR(50),AGE INT NOT NULL,EMAIL TEXT NOT NULL,MOBILE INT NOT NULL,FOODTYPE TEXT NOT NULL,GENDER TEXT NOT NULL,COURSE TEXT NOT NULL,COST INT NOT NULL,SLOT TEXT NOT NULL,TRAINER_NAME TEXT NOT NULL)")
print("Table member created successfully") 

con.commit()
class Member(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.original_frame = parent
        self.title('POWERHUB GYM - MEMBER DETAILS ')
        self.geometry("1350x750+0+0")
        self.lblHeading =tk.Label(self,text="EMPLOYEE LOGIN",  width="500", height="2",font=("Helvetica", 16),bg="yellow",fg="white")
        

        self.lbluname = tk.Label(self,text="Enter Member Email ID:", font=("Helvetica", 10),bg="blue",fg="yellow")
        self.txtuname = tk.Entry(self,width=60,bg='pink',font= ('bold',12))
        self.btn_login=tk.Button(self, text="Show",width=20,font=("Helvetica", 15),bg="yellow",fg="blue",command=self.showdata)
        self.btn_exit=tk.Button(self, text="Back",width=20,font=("Helvetica", 15),bg="yellow",fg="blue" , command=self.mexit)


        self.lblHeading.place(relx=0, rely=0.09, height=41, width=1350)
        self.lbluname.place(relx=0.235, rely=0.289, height=21, width=106)
        self.txtuname.place(relx=0.417, rely=0.289,height=20, relwidth=0.273)
        self.btn_login.place(relx=0.35, rely=0.489, height=30, width=70)
        self.btn_exit.place(relx=0.65, rely=0.489, height=30, width=70)
    def showdata(self):
        em=self.txtuname.get()
        con=sqlite3.connect("gym.db")    
        cur=con.cursor()
        cur.execute("SELECT * FROM book WHERE Movie_ID=? OR Movie_Name=? OR Release_Date=? OR Director=? OR Cast=? OR Budget=? OR Duration=? OR Rating=?",(Movie_ID,Movie_Name,Release_Date,Director,Cast,Budget,Duration,Rating))
        rows=cur.fetchall()
        con.close()    
        return rows
class Admission(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.original_frame = parent
        self.title('POWERHUB GYM - MEMBER ADMISSION FORM ')
        self.geometry("1350x750+0+0")
        global photo    
        photo = tk.PhotoImage(file = 'C:\\Users\\PC\\Desktop\\Mokshda .py\\Project1\\POWERHUB GYM\\member.png')
        self.panel = tk.Label(self, image=photo)
        self.panel.place(x=10,y=70)
        self.label = tk.Label(self, text=" * * * MEMBER ADMISSION FORM * * * ", bg="Light Green", fg='black' ,width="300", height="2", font=("Bell MT", 18))
        self.label.pack()
        self.em3=tk.Label(self,text="")
        self.em3.pack()

        self.label_1= tk.Label(self , text= 'NAME', anchor='w',width=10, font= ('bold',15))
        self.label_1.place(x=155, y=100)
        self.entry_1= tk.Entry(self, width=30, bg='pink',font= ('bold',15))
        self.entry_1.place(x=300, y=100)
        
        self.label_2= tk.Label(self , text= 'ADDRESS', anchor='w', width=10, font= ('bold',15))
        self.label_2.place(x=155, y=150)
        self.entry_2= tk.Entry(self,width=30, bg='pink',font= ('bold',15))
        self.entry_2.place(x=300, y=150)
        
        self.label_3= tk.Label(self , text= 'AGE',  anchor='w',width=10, font= ('bold',15))
        self.label_3.place(x=155, y=200)
        self.entry_3= tk.Entry(self,width=30, bg='pink',font= ('bold',15))
        self.entry_3.place(x=300, y=200)
        
        self.label_4= tk.Label(self , text= 'EMAIL',  anchor='w',width=10, font= ('bold',15))
        self.label_4.place(x=155, y=250)
        self.entry_4= tk.Entry(self,width=30, bg='pink',font= ('bold',15))
        self.entry_4.place(x=300, y=250)

        self.label_5= tk.Label(self , text= 'MOBILE',  anchor='w',width=10, font= ('bold',15))
        self.label_5.place(x=155, y=300)
        self.entry_5= tk.Entry(self,width=30, bg='pink',font= ('bold',15))
        self.entry_5.place(x=300, y=300)

        self.label_6= tk.Label(self , text= 'DIET', anchor='w', width=10, font= ('bold',15))
        self.label_6.place(x=155, y=350)
        food_list=['Veg','Non Veg']
        self.ft=tk.StringVar()
        self.foodtype= tk.OptionMenu(self,self.ft, *food_list)#, command= sel_std)
        self.foodtype.config(width=20,bg='pink',font= ('bold',15))
        self.ft.set('Select Food type')
        self.foodtype.place(x=300, y=350)

        self.label_7= tk.Label(self , text= 'GENDER', anchor='w', width=10, font= ('bold',15))
        self.label_7.place(x=155, y=400)
        self.gen= tk.StringVar()
        self.R1=tk.Radiobutton(self, text= 'Male',  font= ('bold',15),variable=self.gen,value='Male').place(x=300, y=400)
        self.R2=tk.Radiobutton(self, text= 'Female',  font= ('bold',15), variable=self.gen,value='Female').place(x=400, y=400)
        self.R3=tk.Radiobutton(self, text= 'Others',   font= ('bold',15), variable=self.gen,value='Others').place(x=500, y=400)
        self.gen.set(False)
        
        self.label_8= tk.Label(self , text= 'COURSE', anchor='w', width=10, font= ('bold',15))
        self.label_8.place(x=155, y=450)
        course_list=['Cardio Running','Cardio Stairs Climber','Cardio Jumping Rope','Cardio Kettlebells','Cardio Cycling','Cardio Sprinting']
        self.cr=tk.StringVar()
        self.course= tk.OptionMenu(self, self.cr, *course_list)#, command= sel_std)
        self.course.config(width=20,bg='pink',font= ('bold',15))
        self.cr.set('Select Course type')
        self.course.place(x=300, y=450)

        self.label_9= tk.Label(self , text= 'COST',  anchor='w',width=10, font= ('bold',15))
        self.label_9.place(x=155, y=500)
        self.entry_9= tk.Entry(self,width=30, bg='pink',font= ('bold',15))
        self.entry_9.place(x=300, y=500)

        self.label_10= tk.Label(self , text= 'SLOT', anchor='w', width=10, font= ('bold',15))
        self.label_10.place(x=155, y=550)
        timeslot_list=['9-19 AM','10-11 AM','11-12 PM','4-5 PM','5-6 PM','6-7 PM']
        self.slot=tk.StringVar()
        self.timeslot= tk.OptionMenu(self, self.slot, *timeslot_list)#, command= sel_std)
        self.timeslot.config(width=20,bg='pink',font= ('bold',15))
        self.slot.set('Select slot')
        self.timeslot.place(x=300, y=550)

        self.label_11= tk.Label(self , text= 'TRAINER',  anchor='w',width=10, font= ('bold',15))
        self.label_11.place(x=155, y=600)
        self.entry_11= tk.Entry(self,width=30, bg='pink',font= ('bold',15))
        self.entry_11.place(x=300, y=600)
        self.b1= tk.Button(self , text= 'SAVE', width=10,height=1, bg="Light Green",font=('Arial', 12, 'bold'),command=self.add)
        self.b1.place(x=150, y=650)
        self.b2= tk.Button(self , text= 'SHOW', width=10,height=1, bg="Light Green",font=('Arial', 12, 'bold'),command=self.show)
        self.b2.place(x=350, y=650)
        self.b3= tk.Button(self , text= 'CLEAR', width=10,height=1, bg="Light Green",font=('Arial', 12, 'bold'),command=self.clearm)
        self.b3.place(x=550, y=650)
        self.b3= tk.Button(self , text= 'EXIT', width=10,height=1, bg="Light Green",font=('Arial', 12, 'bold'),command=self.exitm)
        self.b3.place(x=750, y=650)
    def clearm(self):
        self.entry_1.delete(0, tk.END)
        self.entry_2.delete(0, tk.END)
        self.entry_3.delete(0, tk.END)
        self.entry_4.delete(0, tk.END)
        self.entry_5.delete(0, tk.END)
        self.entry_9.delete(0, tk.END)
        self.entry_11.delete(0, tk.END)
        
        self.entry_1.focus_set()
    def exitm(self):
        MsgBox = mb.askquestion('POWERHUB GYM', 'Are you sure you want to exit the application',
                                    icon='warning')
        if MsgBox == 'yes':
            self.destroy()      
    def backm(self):
        self.withdraw()
        window = MainMenu(self)
        window.grab_set()
    def add(self):
        name = self.entry_1.get()  
        address = self.entry_2.get()
        age = self.entry_3.get() 
        email = self.entry_4.get()  
        mobile = self.entry_5.get()
        foodtype=self.ft.get()
        print(foodtype)
        gender=self.gen.get()
        course=self.cr.get() 
        cost=self.entry_9.get()
        slot=self.slot.get()
        trainer=self.entry_11.get()
        print('name=',name)
        if name == "":
            showinfo('POWERHUB GYM MANAGEMENT SYSTEM', "Please Enter member name")
            self.entry_1.focus_set()
            return
        if address == "":
            showinfo('POWERHUB GYM MANAGEMENT SYSTEM', "Please Enter member address")
            self.entry_2.focus_set()
            return
        if age == "":
            showinfo('POWERHUB GYM MANAGEMENT SYSTEM', "Please Enter member age")
            self.entry_3.focus_set()
            return
        if email == "":
            showinfo('POWERHUB GYM MANAGEMENT SYSTEM', "Please Enter member email")
            self.entry_4.focus_set()
            return
        if mobile == "":
            showinfo('POWERHUB GYM MANAGEMENT SYSTEM', "Please Enter member mobile")
            self.entry_5.focus_set()
            return
        if cost == "":
            showinfo('POWERHUB GYM MANAGEMENT SYSTEM', "Please Enter course cost")
            self.entry_9.focus_set()
            return
        if trainer == "":
            showinfo('POWERHUB GYM MANAGEMENT SYSTEM', "Please Enter trainer name")
            self.entry_11.focus_set()
            return
        else:
            con = sqlite3.connect("gym.db")
            cursor = con.cursor() 
            s='INSERT INTO member(name,address,age,email,mobile,foodtype,gender,course,cost,slot,TRAINER_NAME) VALUES ( %s, %s, %s,%s,%s,%s, %s, %s,%s,%s,%s)', (name,address,age,email,mobile,foodtype,gender,course,cost,slot,trainer)
            print(s)
            my_data=( name,address,age,email,mobile,foodtype,gender,course,cost,slot,trainer)
            my_query="INSERT INTO member(name,address,age,email,mobile,foodtype,gender,course,cost,slot,TRAINER_NAME) VALUES ( ?,?,?,?,?,?,?,?,?,?,?)"
            con.execute(my_query,my_data)
            con.commit()
            showinfo('POWERHUB GYM MANAGEMENT SYSTEM', 'You have successfully registered !, Welcome to powerhub gym.')
     
    def show(self):
        self.withdraw()
        window = ShowAdm(self)
        window.grab_set()
class ShowAdm(tk.Toplevel):
    def __init__(self, parent):
       super().__init__(parent)
       self.original_frame = parent
       self.title('POWERHUB GYM - SHOW MEMBERS ')
       self.geometry("1350x850+0+0")
       self.config(bg='white')
       
       self.lblHeading =tk.Label(self,text="MEMBER LIST",  width="500", height="2",font=("Helvetica", 16),bg="pink",fg="blue")
       self.lblHeading.pack()
       # Create an instance of Style widget
       self.style=ttk.Style()
       self.style.theme_use('clam')
       
       cl = ("#1", "#2", "#3", "#4", "#5", "#6", "#7","#8","#9","#10","#11","#12")
       self.tvMember= ttk.Treeview(self,show="headings",height="15",columns=cl)
       self.tvMember.heading('#1', text='ID',anchor='center')
       self.tvMember.column('#1', width=20,stretch=False)
       self.tvMember.heading('#2', text='NAME', anchor='center')
       self.tvMember.column('#2', stretch=False)
       self.tvMember.heading('#3', text='ADDRESS', anchor='center')
       self.tvMember.column('#3',stretch=False)
       self.tvMember.heading('#4', text='AGE::', anchor='center')
       self.tvMember.column('#4',  stretch=False)
       self.tvMember.heading('#5', text='EMAIL', anchor='center')
       self.tvMember.column('#5', stretch=False)
       self.tvMember.heading('#6', text='MOBILE', anchor='center')
       self.tvMember.column('#6', stretch=False)
       self.tvMember.heading('#7', text='DIET', anchor='center')
       self.tvMember.column('#7', stretch=False)
       self.tvMember.heading('#8', text='GENDER', anchor='center')
       self.tvMember.column('#8',  stretch=False)
       self.tvMember.heading('#9', text='COURSE', anchor='center')
       self.tvMember.column('#9',  stretch=False)
       self.tvMember.heading('#10', text='COST', anchor='center')
       self.tvMember.column('#10',  stretch=False)
       self.tvMember.heading('#11', text='SLOT', anchor='center')
       self.tvMember.column('#11', stretch=False)
       self.tvMember.heading('#12', text='TRAINER', anchor='center')
       self.tvMember.column('#12', stretch=False)
       
      
       #Scroll bars are set up below considering placement position(x&y) ,height and width of treeview widget
       #self.vsb= ttk.Scrollbar(self, orient=tk.VERTICAL,command=self.tvMember.yview)
       #self.vsb.place(x=1340, y=90, height=470)
       #self.tvMember.configure(yscroll=self.vsb.set)
       self.hsb = ttk.Scrollbar(self, orient=tk.HORIZONTAL, command=self.tvMember.xview)
       self.hsb.place(x=1 , y=370, width=1340)
       self.tvMember.configure(xscroll=self.hsb.set)
       self.tvMember.pack()
       self.tvMember.bind("<<TreeviewSelect>>", self.delete_selected_record) 
       self.b1 = tk.Button(self,text="VIEW MEMBERS", width=20,height=1, bg="orange",font=('Arial', 12, 'bold'),command=self.showrecord)
       self.b1.pack()
       self.b2 = tk.Button(self,text="<<<<BACK>>>>", width=20,height=1, bg="orange",font=('Arial', 12, 'bold'),command=self.iback)
       self.b2.pack(pady=10)
       self.b3 = tk.Button(self,text="<<<<EXIT>>>>", width=20,height=1, bg="orange",font=('Arial', 12, 'bold'),command=self.iexit)
       self.b3.pack(pady=10)
		
    def delete_selected_record(self, event):
        selectedItem = self.tvMember.selection()[0]
        print('selected row',selectedItem)
        
        id=self.tvMember.item(selectedItem)['values'][0]
        print('selected member id=',id)
        
        MsgBox = mb.askquestion('Delete Record', 'Are you sure! you want to delete selected member record', icon='warning')
        if MsgBox == 'yes':
            print('Delete')
            con=sqlite3.connect("gym.db")    
            cur=con.cursor()
            cur.execute("DELETE FROM member WHERE id=?", (id,))
            con.commit()
            con.close() 
            con = sqlite3.connect("gym.db")
            cur=con.cursor()
            cur.execute("SELECT * FROM member")
            rows=cur.fetchall()
            con.close()
            id=""
            name = "" 
            address = ""
            age = "" 
            email = ""  
            mobile = ""
            foodtype=""
            gender=""
            course=""
            cost=""
            slot=""
            trainer=""
            self.tvMember.delete(*self.tvMember.get_children())
            for row in rows:
                print(row)
                id=row[0]
                name = row[1]
                address = row[2]
                age = row[3]
                email = row[4]
                mobile = row[5]
                foodtype=row[6]
                gender=row[7]
                course=row[8]
                cost=row[9]
                slot=row[10]
                trainer=row[11]
                self.tvMember.insert("", tk.END, values=row)
            #self.tvMember.insert("", 'end', text=RollNo, values=(id, name,address,age,email,mobile,foodtype,gender,course,cost,slot,trainer))
    def iback(self):
        self.withdraw()
        window = Admission(self)
        window.grab_set()
    def iexit(self):
        MsgBox = mb.askquestion('POWERHUB GYM', 'Are you sure you want to exit the application',
                                    icon='warning')
        if MsgBox == 'yes':
            self.destroy()
    def showrecord(self):
       
        con = sqlite3.connect("gym.db")
        cur=con.cursor()
        cur.execute("SELECT * FROM member")
        rows=cur.fetchall()
        con.close()
        id=""
        name = "" 
        address = ""
        age = "" 
        email = ""  
        mobile = ""
        foodtype=""
        gender=""
        course=""
        cost=""
        slot=""
        trainer=""
        for row in rows:
            print(row)
            id=row[0]
            name = row[1]
            address = row[2]
            age = row[3]
            email = row[4]
            mobile = row[5]
            foodtype=row[6]
            gender=row[7]
            course=row[8]
            cost=row[9]
            slot=row[10]
            trainer=row[11]
            self.tvMember.insert("", tk.END, values=row)
            #self.tvMember.insert("", 'end', text=RollNo, values=(id, name,address,age,email,mobile,foodtype,gender,course,cost,slot,trainer))


         
class MainMenu(tk.Tk):
    def __init__(self):
        super().__init__()

        # configure the root window
        self.title('POWERHUB GYM ')
       
        self.geometry("1350x750+0+0")
        self.config(bg='white')
        global photo   
		

        self.label = tk.Label(self, text=" * * * WELCOME TO POWERHUB GYM * * * ", bg="pink", width="300", height="2", font=("Bell MT", 18))
        self.label.pack()
        self.em3=tk.Label(self,text="")
        self.em3.pack()
        global bg
        bg = tk.PhotoImage(file = "C:\\Users\\PC\\Desktop\\Mokshda .py\\Project1\\POWERHUB GYM\\logo.png") #image
  
        # Show image using label
        self.p1 = tk.Label( self, image = bg)
        self.p1.pack(side="top", fill="both") 
        

        self.em2=tk.Label(self,text="")
        self.em2.pack()
        self.b2=tk.Button(self,text="EMPLOYEE", height="2", width="30",  bg="pink",command=self.employee)
        self.b2.pack()
        self.em1=tk.Label(self,text="")
        self.em1.pack()
        self.b3=tk.Button(self,text="EXIT", height="2", width="30",  bg="pink",command=self.ex)
        
        self.b3.pack()
    
    def member(self):
       #showinfo(title='POWERHUB GYM MANAGEMENT SYSTEM', message='Hello, MEMBER!')
       self.withdraw()
       window = Member(self)
       window.grab_set()
    def employee(self):
       self.withdraw()
       window = LoginApp(self)
       window.grab_set()
       #showinfo(title='EMPLOYEE', message='Hello, EMPLOYEE!')
    def ex(self):
        MsgBox = mb.askquestion('POWERHUB GYM', 'Are you sure you want to exit the application',
                                    icon='warning')
        if MsgBox == 'yes':
            self.destroy()
        
class LoginApp(tk.Toplevel):
    def __init__(self, parent):
       super().__init__(parent)
       self.original_frame = parent
       self.title('POWERHUB GYM - EMPLOYEE LOGIN ')
       self.geometry("1350x750+0+0")
       self.config(bg='lightblue')
       
       self.lblHeading =tk.Label(self,text="EMPLOYEE LOGIN",  width="500", height="2",font=("Helvetica", 16),bg="pink",fg="black")
       #global photo    
       #photo = tk.PhotoImage(file = 'login.png')
       #self.panel = tk.Label(self, image=photo)
       #self.panel.pack(side="top", fill="both")

       self.lbluname = tk.Label(self,text="Enter UserName:", font=("Helvetica", 10),bg="Light Green",fg="black")
       self.lblpsswd = tk.Label(self,text="Enter Password:", font=("Helvetica", 10),bg="Light Green",fg="black")
       self.txtuname = tk.Entry(self,width=60,bg='pink',font= ('bold',12))
       self.txtpasswd = tk.Entry(self,width=60, show="*",bg='pink',font= ('bold',12))
       self.btn_login=tk.Button(self, text="Login",width=20,font=("Helvetica", 15),bg="pink",fg="black",command=self.login)
       self.btn_clear=tk.Button(self, text="Clear",width=20,font=("Helvetica", 15),bg="pink",fg="black",command=self.clear_form)
       self.btn_exit=tk.Button(self, text="Exit",width=20,font=("Helvetica", 15),bg="pink",fg="black" , command=self.exit)


       self.lblHeading.place(relx=0, rely=0.09, height=41, width=1350)
       self.lbluname.place(relx=0.235, rely=0.289, height=21, width=106)
       self.lblpsswd.place(relx=0.235, rely=0.378, height=21, width=106)
       self.txtuname.place(relx=0.417, rely=0.289,height=20, relwidth=0.273)
       #self.panel.place(relx=0.417, rely=0.289,height=22, relwidth=0.273)
       self.txtpasswd.place(relx=0.417, rely=0.378,height=20, relwidth=0.273)
       self.btn_login.place(relx=0.35, rely=0.489, height=30, width=70)
       self.btn_clear.place(relx=0.50, rely=0.489, height=30, width=70)
       self.btn_exit.place(relx=0.65, rely=0.489, height=30, width=70)


    def show(self):
       """"""
       self.update()
       self.deiconify()

    def login(self):
       


       try:
           global username
           username = str(self.txtuname.get())  # Retrieving entered username
           passwd = str(self.txtpasswd.get())  # Retrieving entered password
           if username == "" :
               showinfo('POWERHUB GYM MANAGEMENT SYSTEM', "Please Enter Username")
               self.txtuname.focus_set()
               return
           if passwd == "" :
               showinfo('POWERHUB GYM MANAGEMENT SYSTEM', "Please Enter Password")
               self.txtpasswd.focus_set()
               return

           print(username)
           print(passwd)
           con = sqlite3.connect("gym.db")  
           print("Database opened successfully in login")  
           con.row_factory = sqlite3.Row  
           cur = con.cursor()  
           cur.execute('SELECT * FROM account WHERE email = ? AND password = ?', (username, passwd, ))  
           rows = cur.fetchone()
           if rows:
              showinfo('POWERHUB GYM MANAGEMENT SYSTEM', "Login Successfully")
              self.withdraw()
              window = Admission(self)
              window.grab_set()
           else:
              showinfo('POWERHUB GYM MANAGEMENT SYSTEM', "Login failed,Invalid Username or Password.Try again!!!")
       except:
        # Closing Connection
           showinfo('POWERHUB GYM MANAGEMENT SYSTEM', "There are some error,Try again!!!")


    def clear_form(self):
        self.txtuname.delete(0, tk.END)
        self.txtpasswd.delete(0, tk.END)
        self.txtuname.focus_set()

    def exit(self):
        MsgBox = mb.askquestion('POWERHUB GYM', 'Are you sure you want to exit the application',
                                    icon='warning')
        if MsgBox == 'yes':
            self.destroy()

if __name__ == "__main__":
    app = MainMenu()
    app.mainloop()