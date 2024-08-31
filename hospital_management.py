from tkinter import *
from tkinter import ttk
import random 
import time
import datetime
from tkinter import messagebox
from colorama import Cursor
import mysql.connector

#main class of the Hospital Management 
class hospital:
    def __init__(self , root):
        
        self.root = root
        self.root.title('Hospital management System ')
        self.root.geometry("1540x800+0+0")
        self.width_screen = 1540
        self.height_screen = 800
        
        #Creatinig variable to store the data of diffrent feild 
        self.name_of_tablet =StringVar()
        self.patient_name =StringVar()
        self.dob =StringVar()
        self.address =StringVar()
        self.patient_id =StringVar()
        self.contact_number =StringVar()
        self.relative_name =StringVar()
        self.relative_contact =StringVar()
        self.reference_no =StringVar()
        self.further_info =StringVar()
        self.dose =StringVar()
        self.number_of_tablet =StringVar()
        self.expiry_date =StringVar()
        self.issue_date =StringVar()
        self.storage_advice =StringVar()
        self.daily_dose =StringVar()
        self.side_effect =StringVar()
        self.medication =StringVar()

        self.list_of_variables = [
            self.name_of_tablet ,
            self.patient_name ,
            self.dob ,
            self.address,
            self.patient_id ,
            self.contact_number ,
            self.relative_name ,
            self.relative_contact ,
            self.reference_no ,
            self.further_info ,
            self.dose ,
            self.number_of_tablet ,
            self.expiry_date ,
            self.issue_date ,
            self.storage_advice ,
            self.daily_dose ,
            self.side_effect ,
            self.medication ,
        ]
        self.table_columns = [  
                                self.name_of_tablet,
                                self.patient_id,
                                self.patient_name,
                                self.dob,
                                self.contact_number,
                                self.relative_name,
                                self.relative_contact,
                                self.reference_no,
                                self.dose,
                                self.number_of_tablet,
                                self.issue_date,
                                self.expiry_date,
                                self.storage_advice,
                                self.medication
                            ]

        
        lbtitle = Label(self.root , bd = 10 , relief = RIDGE , text='HOSPITAL MANAGEMENT SYSTEM',fg = 'blue' , bg = 'white', font = ('times new roman' , 50 , 'bold'))
        lbtitle.pack(side =TOP , fill = 'x') 


        #----------------------------data frame----------------------------
        
        dataframe = Frame(self.root , bd =5 ,padx=5 ,relief=RIDGE)
        dataframe.place(x = 0 , y = 100 , width=self.width_screen , height=self.height_screen/2)

        lablelleft = LabelFrame(dataframe, bd =5 ,padx=5,relief=RIDGE, font = ('times new roman' , 20 , 'bold'),text='Patient Information')
        lablelleft.place(x = 0 , y = 5 , width=self.width_screen*0.6 , height=self.height_screen*0.95*0.5)
        
        lablelright = LabelFrame(dataframe, bd =5 ,padx=5,relief=RIDGE, font = ('times new roman' , 20 , 'bold'),text='prescription\'s')
        lablelright.place(x = self.width_screen*0.6 + 3 , y = 5 , width=self.width_screen*0.37 , height=self.height_screen*0.95*0.5)


        # ----------------------------- buttons ------------------------------
        
        buttonframe = Frame(self.root , bd = 5 , padx = 5 , relief=RIDGE)
        buttonframe.place(x = 0 , y = 500 , width=self.width_screen , height=50)


        # ---------------------------- table frame----------------------------
        
        detailsframe = Frame(self.root , bd = 5 , padx = 5 , relief=RIDGE)
        detailsframe.place(x = 0 , y = 550 , width=self.width_screen, height=self.height_screen*0.5 - 80)

        #------------------------------data entries at left-------------------
        
        tabletname = Label(lablelleft , text='Tablets Name' ,  font = ('times new roman' , 13 , 'bold') , padx=2 ,pady=5 , )
        tabletname.grid(row = 0,  column=0 ,sticky=W)

        tablet_container = ttk.Combobox(lablelleft , font = ('times new roman' , 13 , 'bold'),width=29 ,textvariable=self.name_of_tablet)

        tablet_container["values"] = ('Nice' , 'Corona vaccine' , 'Paracitamol' , 'Electrol powder' ,'Iodex', 'Croseen')
        tablet_container.grid(row=0 , column=1)


        list_of_entries1 = ['Patient Name:','Date Of Birth:' , 'Address:' ,'Patient Id:' ,'Contact Number:' , 'Relative Name:', 'Relative Contact:','Refrence no:','Further Info:']
        for i in range(len(list_of_entries1)):
            self.inputs_label(lablelleft, list_of_entries1[i], i+1,0 , self.list_of_variables[i+1])
            
        temp = len(list_of_entries1)    
        list_of_entries2 = ['Dose:' , 'Number of Tablets:' , 'Issue Date:' , 'Expire Date:' ,'Storage Advice:', 'Daily dose:' , 'Side Effect:','Medication:']
        for i in range(len(list_of_entries2)):
            self.inputs_label(lablelleft, list_of_entries2[i], i,2 , self.list_of_variables[i+temp+1])
        
        #----------------------------prescription Box--------------------------
        
        self.txt_prescription = Text(lablelright ,   font = ('times new roman' , 13 , 'bold') , padx=2 ,pady=5  , width=60 , height=17)
        self.txt_prescription.grid(row=0 , column=0)

        # ----------------------------button------------------------------------

        #btn-1 
        btn_prescription = Button(buttonframe, command=self.prescription , text='Prescription' ,bg='green' , fg = 'white' ,font = ('arial' , 12 , 'bold') ,width=30, padx=2 , pady=4 )
        btn_prescription.grid(row=0 , column=0)
        
        #btn-2
        btn_prescribe = Button(buttonframe , command=self.prescribe ,text='Prescribe it' ,bg='green' , fg = 'white' ,font = ('arial' , 12 , 'bold') ,width=30, padx=2 , pady=4 )
        btn_prescribe.grid(row=0 , column=1)

        #btn-3
        btn_update = Button(buttonframe , command=self.update ,text='Update' ,bg='green' , fg = 'white' ,font = ('arial' , 12 , 'bold') ,width=30, padx=2 , pady=4 )
        btn_update.grid(row=0 , column=2)

        #btn-4
        btn_delete = Button(buttonframe , command=self.delete ,text='Delete' ,bg='green' , fg = 'white' ,font = ('arial' , 12 , 'bold') ,width=30, padx=2 , pady=4 )
        btn_delete.grid(row=0 , column=3)

        #btn-5
        btn_clear = Button(buttonframe , command=self.clear ,text='Clear' ,bg='green' , fg = 'white' ,font = ('arial' , 12 , 'bold') ,width=30, padx=2 , pady=4 )
        btn_clear.grid(row=0 , column=4)

        #-------------------------------table--------------------------------------
        scroll_x = ttk.Scrollbar(detailsframe , orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(detailsframe , orient=VERTICAL)
        self.hospital_table=ttk.Treeview(detailsframe ,columns = self.list_of_tables,xscrollcommand=scroll_x , yscrollcommand=scroll_y)
        scroll_x.pack(side=BOTTOM , fill=X)
        scroll_y.pack(side=RIGHT , fill=Y)
        scroll_x = ttk.Scrollbar(command=self.hospital_table.xview)
        scroll_y = ttk.Scrollbar(command=self.hospital_table.yview)

        for i,j in zip( self.table_column_name , self.list_of_tables):
            self.hospital_table.heading(j , text=i)
            self.hospital_table.column(j,width=100)
        
        self.hospital_table['show'] = "headings"
        self.hospital_table.pack(fill=BOTH , expand=1)
            
        self.hospital_table.bind("<ButtonRelease-1>",  self.get_cursor)
            
        #showing all the data
        self.fetch_data()



    # for input labels
    def inputs_label(self, labelfeild ,feild , row_no,column_no , item):
    
        tablename = Label(labelfeild , text=feild ,  font = ('times new roman' , 13 , 'bold') , padx=2 ,pady=5)
        tablename.grid(row = row_no,  column=column_no ,sticky=W)
        txtbox = Entry(labelfeild, font = ('times new roman' , 13 , 'bold'),textvariable=item,width=30)
        txtbox.grid(row = row_no,  column=column_no+1)

    #-----------------------------data base functinality---------------------------
    
    def prescription(self):

        for i in range(len(self.table_column_name)):
            self.txt_prescription.insert(END ,self.table_column_name[i]+":-\t\t"+self.table_columns[i].get()+'\n')



    def prescribe(self):
        
        if self.name_of_tablet.get() == "" or self.patient_id.get() == "" or self.patient_name.get() == "" or self.relative_name.get() == "" or self.relative_contact.get() == "":
            messagebox.showerror('Error' , "All Feilds are Required")
        else:
            conn = mysql.connector.connect(host = "localhost" , user = "root",passwd = 'Ansh@123',database = 'hospital_management')
            my_cursor = conn.cursor()
            
            my_cursor.execute("insert into hospital_data values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)" , [i.get() for i in self.table_columns])
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Success" ,"Record has been inserted")


    def fetch_data(self):
        conn = mysql.connector.connect(host = "localhost" , user = "root",passwd = 'Ansh@123',database = 'hospital_management')
        my_cursor = conn.cursor()
        my_cursor.execute('select * from hospital_data')
        rows = my_cursor.fetchall()
        if(len(rows)!=0):
            self.hospital_table.delete(*self.hospital_table.get_children())
            for i in rows:
                self.hospital_table.insert("",END ,values=i)
            conn.commit()
        
        conn.close()

    def get_cursor(self,event=""):
        cursor_row = self.hospital_table.focus()
        content = self.hospital_table.item(cursor_row);
        row = content['values']
        
        for i in range(len(self.table_columns)):
            self.table_columns[i].set(row[i])
        
        
    def update(self):
        conn = mysql.connector.connect(host = "localhost" , user = "root",passwd = 'Ansh@123',database = 'hospital_management')
        my_cursor = conn.cursor()
        for i in range(len(self.table_columns)):
            my_cursor.execute('update hospital_data set name_of_tablet = %s, patient_id= %s,patient_name= %s,dob= %s,contact_number= %s, relative_name= %s,relative_contact= %s,reference_no= %s,dose= %s,number_of_tablet= %s,issue_date= %s,expiry_date= %s,storage_advice= %s,medication= %s where patient_id = %s;' , 
                                [i.get() for i in self.table_columns] + [self.patient_id.get()]
                                )
        conn.commit()
        conn.close()
        self.fetch_data()
        messagebox.showinfo("Success" ,"Record has been updated")

        
    def delete(self):
        conn = mysql.connector.connect(host = "localhost" , user = "root",passwd = 'Ansh@123',database = 'hospital_management')
        my_cursor = conn.cursor()
        query = "delete from hospital_data where patient_id = %s"
        values =(self.patient_id.get(),)
        my_cursor.execute(query , values)
        conn.commit()
        conn.close()
        self.fetch_data()
        messagebox.showinfo("Delete" ,"Record has been deleted")

    def clear(self):
        for i in self.list_of_variables:
            i.set("")
        
        self.txt_prescription.delete('1.0',END)



# creating object 
root = Tk()
obj = hospital(root)
root.mainloop()
