from re import M
from tkinter import * 
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox, ttk
import tkinter as tk
import datetime as dt
import sqlite3 as sql
from PIL import Image, ImageTk
import io
class Page(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
    
    def show(self):
        self.lift()

class HomePage(Page):
    def __init__(self, parent, controller):
        Page.__init__(self, parent, controller)

        self.backg = PhotoImage(file = 'img/back11.png')
        self.back = Label(self,width = 1000 , height = 750 , image = self.backg )
        self.back.place(x = 0 , y = 0)


        self.date = dt.datetime.now()
        self.date_lbl = Label(self , bg = '#DEE2E6',anchor = 'w' ,width = 42 ,  text=f"{self.date: %Y %B %d , %H:%M}", font=("tahoma" , 20))
        self.date_lbl.place(x = 190 , y = 192)

        self.slip_img = PhotoImage(file = 'img/pay_slip2.png')
        self.employee_img = PhotoImage(file = 'img/new_employee2.png')
        self.list_img = PhotoImage(file = 'img/list2.png')
        self.listt = Label(self, image = self.list_img, bg ='#DEE2E6')
        self.pay_slip = Label(self , image = self.slip_img, bg ='#DEE2E6' )
        self.new_employee = Label(self , image = self.employee_img, bg ='#DEE2E6')
        self.listt.place(x = 190 , y = 267 )
        self.pay_slip.place(x = 410 , y = 267)
        self.new_employee.place(x = 630 , y = 267 )


        self.list_btim = PhotoImage(file = 'img/list_btn.png')
        self.slip_btim = PhotoImage(file = 'img/slip_btn.png')
        self.employee_btim = PhotoImage(file = 'img/employee_btn.png')
        self.list_btn = Button(self , relief = 'flat' , bg ='#DEE2E6' , activebackground='#DEE2E6' , image = self.list_btim , command = lambda: controller.show_page(employeeList))
        self.slip_btn = Button(self , relief = 'flat' , bg ='#DEE2E6' , activebackground='#DEE2E6' , image = self.slip_btim , command = self.fill_getcode)
        self.employee_btn = Button(self , relief = 'flat' , bg ='#DEE2E6' , activebackground='#DEE2E6' , image = self.employee_btim , command = lambda: controller.show_page(addemployee))

        self.list_btn.place(x = 210 , y = 488)
        self.slip_btn.place(x = 430 , y = 488)
        self.employee_btn.place(x = 650 , y = 488)

        self.list_btn.bind('<Button-1>',self.fillTreeview)

    def fillTreeview(self,eevnt = None) :
        employeeListt = self.controller.pages[employeeList]
        self.controller.show_page(employeeList)
        self.stocklst = []
        self.stock_count=0
        self.con=sql.connect('mydb.db')
        self.cur=self.con.cursor()
        self.row=self.cur.execute('SELECT * FROM info')
        for i in self.row :
            self.stocklst.append(i)
        for i in self.stocklst:
            employeeListt.info.insert(parent='',index='end',iid=self.stock_count,text='',
            values=(i[8],i[3],i[5],i[0],i[1],str(self.stock_count+1)))
            self.stock_count += 1
    def fill_getcode(self) :
        self.controller.small()
        self.controller.show_page(getCode)

class addemployee(Page):
    def __init__(self, parent, controller):
        Page.__init__(self, parent, controller)


        self.back1_img = PhotoImage(file = 'img/back2.png')
        self.back1 = Label(self , image = self.back1_img)
        self.back1.place(x = 0 , y = 0)

        self.pr_img = PhotoImage(file = 'img/pr.png')
        self.photo_label = Label(self, image=self.pr_img, width=80, height=80)
        self.photo_label.place(x=100, y=38)   


        self.change_img = PhotoImage(file = 'img/change_img.png')
        self.change_btn = Button(self , image = self.change_img , bg = '#DEE2E6',activebackground = '#DEE2E6' ,relief = 'flat' )
        self.change_btn.place(x = 208 , y = 55)

        self.sabt_img = PhotoImage(file = 'img/sabt.png')
        self.sabt = Button(self , image = self.sabt_img , bg = '#DEE2E6',activebackground = '#DEE2E6' ,relief = 'flat' , command = self.getInfo)
        self.sabt.place(x = 295 , y = 622 )
        self.root3img = PhotoImage(file = 'img/root3_home.png')
        self.root3_homee = Button(self, image = self.root3img , bg = '#DEE2E6',activebackground = '#DEE2E6' ,relief = 'flat', command=lambda: controller.show_page(HomePage))
        self.root3_homee.place(x = 500 , y = 622)

        self.pr_ent = Entry(self, bg = '#FFFFFF', width = 20 , font = ('B Koodak' , 10) , relief = 'flat' , justify = 'right')
        self.na_ent = Entry(self, bg = '#FFFFFF', width = 20 , font = ('B Koodak' , 10) , relief = 'flat' , justify = 'right')
        self.f_ent = Entry(self, bg = '#FFFFFF', width = 20 , font = ('B Koodak' , 10) , relief = 'flat' , justify = 'right')
        self.c_ent = Entry(self, bg = '#FFFFFF', width = 20 , font = ('B Koodak' , 10) , relief = 'flat' , justify = 'right')
        self.nu_ent = Entry(self, bg = '#FFFFFF', width = 20 , font = ('B Koodak' , 10) , relief = 'flat' , justify = 'right')
        self.d_ent = Entry(self, bg = '#FFFFFF', width = 20 , font = ('B Koodak' , 10) , relief = 'flat' , justify = 'right')
        self.ch_ent = Entry(self, bg = '#FFFFFF', width = 20 , font = ('B Koodak' , 10) , relief = 'flat' , justify = 'right')
        self.ph_ent = Entry(self, bg = '#FFFFFF', width = 20 , font = ('B Koodak' , 10) , relief = 'flat' , justify = 'right')
        self.m_ent = Entry(self, bg = '#FFFFFF', width = 20 , font = ('B Koodak' , 10) , relief = 'flat' , justify = 'right')
        self.var1 = IntVar()
        self.var2 = IntVar()
        self.c1 = Checkbutton(self,bg = '#DEE2E6',variable=self.var1, onvalue=1, offvalue=0, command=self.marital_status)
        self.c1.place(x = 150 , y = 220)
        self.c2 = Checkbutton(self,bg = '#DEE2E6',variable=self.var2, onvalue=1, offvalue=0, command=self.marital_status)
        self.c2.place(x = 82 , y = 220)

        self.combo = ttk.Combobox(self,width = 16,textvariable = 'asdsd' , font = ('B Koodak' , 12),values=["دولتی", "خصوصی", "مشاوره ای", "آزمایشی" , 'کارمزدی'])
        self.combo.bind("<<ComboboxSelected>>", self.dropdown_opened)
        self.combo.set("یک گزینه را انتخاب کنید")
        self.combo.place(x=65, y=575)

        self.pr_ent.place(x = 635 , y = 65)
        self.na_ent.place(x = 635 , y = 219)
        self.f_ent.place(x = 635 , y = 309)
        self.c_ent.place(x = 635 , y = 397)
        self.nu_ent.place(x = 635 , y = 485)
        self.d_ent.place(x = 635 , y = 574)
        self.ch_ent.place(x = 71 , y = 309)
        self.ph_ent.place(x = 71 , y = 399)
        self.m_ent.place(x = 71 , y = 489)
    def getInfo(self) :
        self.pr = self.pr_ent.get()
        self.na = self.na_ent.get()
        self.fa = self.f_ent.get()
        self.c = self.c_ent.get()
        self.nu = self.nu_ent.get()
        self.d = self.d_ent.get()
        self.v = ''
        if (self.var1.get() == 1):
            self.v = 'مجرد'
        elif (self.var2.get() == 1):
            self.v = 'متاهل'
        self.ch = self.ch_ent.get()
        self.ph = self.ph_ent.get()
        self.m = self.m_ent.get()
        self.co = self.combo.get()
        if self.pr_ent.get() == '' or self.pr_ent.get() == '' or self.na_ent.get() == '' or self.f_ent.get() == '' or self.c_ent.get() == '' or self.nu_ent.get() == '' or self.d_ent.get() == '' or self.ch_ent.get() == '' or self.ph_ent.get() == '' or self.m_ent.get() == '' :
            messagebox.showerror(title='Error', message='لطفا همه ی فیلد ها را پر کنید')
        else :               
            messagebox.askquestion('askquestion', 'آيا از ذخيره اطلاعات مطمئن هستيد؟')
            con = sql.connect('mydb.db')
            cur=con.cursor()
            data=(self.pr,self.na,self.fa,self.c,self.nu,self.d,self.v,self.ch,self.ph,self.m,self.co)
            cur.execute('''CREATE TABLE IF NOT EXISTS info (id   ,name TEXT ,father_name TEXT,codemeli TEXT
            ,shenasname TEXT,date TEXT,situation TEXT,children TEXT,phone TEXT,education TEXT,Contract TEXT)''')
            cur.execute('INSERT INTO info(id,name,father_name,codemeli,shenasname,date,situation,children,phone,education,Contract) VALUES(?,?,?,?,?,?,?,?,?,?,?)',data)
            con.commit()
            self.pr_ent.delete(0,END)
            self.na_ent.delete(0,END)
            self.f_ent.delete(0,END)
            self.c_ent.delete(0,END)
            self.nu_ent.delete(0,END)
            self.d_ent.delete(0,END)
            self.ch_ent.delete(0,END)
            self.ph_ent.delete(0,END)
            self.m_ent.delete(0,END)
    def marital_status(self) :
        pass
    def dropdown_opened(self) :
        pass

class getCode(Page):
    def __init__(self, parent, controller):
        Page.__init__(self, parent, controller)


        self.back4_img = PhotoImage(file = 'img/back4.png')
        self.back4 = Label(self ,image = self.back4_img)
        self.back4.place(x = 0 , y = 0)

        self.code_ent = Entry(self, bg = '#FFFFFF', width = 15 , font = ('B Koodak' , 15) , relief = 'flat' , justify = 'right')
        self.code_ent.place(x = 170, y = 120)

        self.code_img = PhotoImage(file = 'img/code_btn.png')
        self.code_btn = Button(self , image = self.code_img , bg = '#DEE2E6',activebackground = '#DEE2E6' ,relief = 'flat' , command = self.enterCode)
        self.code_btn.place(x = 118 , y = 183)
    def enterCode(self) :
        enterIncomeP = self.controller.pages[enterIncome]
        paySlipP = self.controller.pages[paySlip]
        code_pers = self.code_ent.get()
        con = sql.connect('mydb.db')
        cur = con.cursor()
        row = cur.execute('SELECT * FROM info WHERE id="{}"'.format(code_pers))    
        row = list(row)
        paySlipP.codePers["text"] = row[0][0]
        paySlipP.name["text"] = row[0][1]
        paySlipP.shomerShenas["text"] = row[0][4]
        paySlipP.tedad["text"] = row[0][7]
        paySlipP.vaziat["text"] = row[0][6]
        
        enterIncomeP.khane["text"] = row[0][1]
        enterIncomeP.code["text"] = row[0][0]
        enterIncomeP.date["text"] = row[0][5]
        enterIncomeP.education["text"] = row[0][9]
        self.controller.normal()
        self.controller.show_page(enterIncome)
class enterIncome(Page):
    def __init__(self, parent, controller):
        Page.__init__(self, parent, controller)

        self.back5_img = PhotoImage(file = 'img/back5.png')
        self.back5 = Label(self ,image = self.back5_img)
        self.back5.place(x = 0 , y = 0)

        self.slip_ent1 = Entry(self, bg = '#E3F2FD', width = 30 , font = ('B Koodak' , 10) , relief = 'flat' , justify = 'right')
        self.slip_ent2 = Entry(self, bg = '#E3F2FD', width = 30 , font = ('B Koodak' , 10) , relief = 'flat' , justify = 'right')
        self.slip_ent3 = Entry(self, bg = '#E3F2FD', width = 30 , font = ('B Koodak' , 10) , relief = 'flat' , justify = 'right')
        self.slip_ent4 = Entry(self, bg = '#E3F2FD', width = 30 , font = ('B Koodak' , 10) , relief = 'flat' , justify = 'right')
        self.slip_ent5 = Entry(self, bg = '#E3F2FD', width = 30 , font = ('B Koodak' , 10) , relief = 'flat' , justify = 'right')

        self.slip_ent1.place(x = 160 , y = 242) 
        self.slip_ent2.place(x = 160 , y = 287)
        self.slip_ent3.place(x = 160 , y = 329)
        self.slip_ent4.place(x = 160 , y = 374)
        self.slip_ent5.place(x = 160 , y = 416)

        self.slip_btn2_img = PhotoImage(file = 'img/slip_btn2.png')
        self.slip_btn2 = Button(self , image = self.slip_btn2_img , relief = 'flat' , activebackground = '#DEE2E6',command = self.sodor)
        self.slip_btn2.place(x = 191 , y = 494)


        self.khane = Label(self  , text = ''  , width = 15, font = ('B Koodak' , 20) , bg  = '#42A5F5' , fg = '#CED4DA')
        self.khane.place(x = 600 , y = 340)

        self.code = Label(self  , text = ''  , width = 10, font = ('B Koodak' , 14) , bg  = '#42A5F5' , fg = '#CED4DA')
        self.date = Label(self  , text = ''  , width = 10, font = ('B Koodak' , 14) , bg  = '#42A5F5' , fg = '#CED4DA')
        self.education = Label(self  , text = ''  , width = 10, font = ('B Koodak' , 14) , bg  = '#42A5F5' , fg = '#CED4DA')

        self.code.place(x = 620 , y = 410)
        self.date.place(x = 620 , y = 442)
        self.education.place(x = 620 , y = 474)

        self.root5img = PhotoImage(file = 'img/root5_home.png')
        self.root5_homee = Button(self, image = self.root5img , bg = '#FFFFFF',activebackground = '#DEE2E6' ,relief = 'flat', command = lambda: controller.show_page(HomePage))
        self.root5_homee.place(x = 356 , y = 494)
    def sodor(self) :
        self.controller.show_page(paySlip)
        patslipp = self.controller.pages[paySlip]
        self.bonrekargari = 850000
        self.hmaskann = 650000
        self.hoqoq_paye = self.slip_ent1.get()
        self.tarikh_e = self.slip_ent2.get()
        self.tarikh_e = self.slip_ent2.get()
        self.ezefe = self.slip_ent3.get()
        self.shabi = self.slip_ent4.get()
        self.tatili = self.slip_ent5.get()

        patslipp.tarikh['text'] = self.tarikh_e
        patslipp.ezaf['text'] = self.ezefe
        patslipp.shab['text'] = self.shabi 
        patslipp.tatil['text'] = self.tatili

        self.tedad_f = 1 # dorost beshe
        self.haqBime = int(self.hoqoq_paye) + self.bonrekargari + self.hmaskann
        self.bimeKoll = int(int(self.haqBime) * 0.3) 
        self.bimeKarfarma = int(int(self.haqBime) * 0.23)
        self.bimeKargar = int(int(self.haqBime) * 0.07)
        self.haqolad =   417000 * int(self.tedad_f)
        self.ezafe_kari = int(self.hoqoq_paye) / 220 * 1.4 * int(self.ezefe)
        self.shab_kari = int(self.hoqoq_paye) / 220 * 1.35 * int(self.shabi)
        self.taatil_kari = int(self.hoqoq_paye) / 220 * 1.4 * int(self.tatili)
        self.kosurat = int(self.bimeKargar) 
        self.daramad = int(self.hoqoq_paye) + int(self.ezafe_kari) + int(self.taatil_kari) + int(self.shab_kari) + int(self.bonrekargari) + int(self.hmaskann) + int(self.haqolad)
        self.rooozane = int(int(self.daramad) / 30)
        self.pardakhti = int(self.daramad) - int(self.kosurat)

        patslipp.bimeKol['text'] =  '''{:,}'''.format(self.bimeKoll)
        patslipp.karfarma['text'] =  '''{:,}'''.format(self.bimeKarfarma)
        patslipp.kargar['text'] =  '''{:,}'''.format(self.bimeKargar)
        patslipp.roozane['text'] =  '''{:,}'''.format(self.rooozane)
        patslipp.bon['text'] =  '''{:,}'''.format(self.bonrekargari)
        patslipp.maskan['text'] =  '''{:,}'''.format(self.hmaskann)
        patslipp.olad['text'] =  '''{:,}'''.format(self.haqolad)
        patslipp.daram['text'] =  '''{:,}'''.format(self.daramad)
        patslipp.kosorat['text'] =  '''{:,}'''.format(self.kosurat)
        patslipp.kol['text'] =  '''{:,}'''.format(self.pardakhti)

class paySlip(Page):
    def __init__(self, parent, controller):
        Page.__init__(self, parent, controller)

        self.back7_img = PhotoImage(file = 'img/back7.png')
        self.back7 = Label(self ,image = self.back7_img)
        self.back7.place(x = 0 , y = 0)

        self.codePers = Label(self, text = '', font = ('B Koodak' , 10) , width = 10 , bg = '#DEE2E6')
        self.name = Label(self, text = '', font = ('B Koodak' , 10) , width = 10 , bg = '#DEE2E6')
        self.shomerShenas = Label(self, text = '', font = ('B Koodak' , 10) , width = 10 , bg = '#DEE2E6')
        self.tedad = Label(self, text = '', font = ('B Koodak' , 10) , width = 10 , bg = '#DEE2E6')
        self.vaziat =Label(self, text = '', font = ('B Koodak' , 10) , width = 10 , bg = '#DEE2E6')
        self.tarikh = Label(self, text = '', font = ('B Koodak' , 10) , width = 10 , bg = '#DEE2E6')
        self.ezaf = Label(self, text = '', font = ('B Koodak' , 10) , width = 10 , bg = '#DEE2E6')
        self.shab = Label(self, text = '', font = ('B Koodak' , 10) , width = 10 , bg = '#DEE2E6')
        self.tatil = Label(self, text = '', font = ('B Koodak' , 10) , width = 10 , bg = '#DEE2E6')
        #40 #3
        self.codePers.place(x = 745 , y = 83)
        self.name.place(x = 745 , y = 110)
        self.shomerShenas.place(x = 745 , y = 140)
        self.tedad.place(x = 544 , y = 83)
        self.vaziat.place(x = 544 , y = 110)
        self.tarikh.place(x = 221 , y = 81)
        self.ezaf.place(x = 221 , y = 110)
        self.shab.place(x = 221 , y = 140)
        self.tatil.place(x = 221 , y = 168)

        self.bimeKol = Label(self, text = '', font = ('B Koodak' , 13) , width = 10 , bg = '#DEE2E6')
        self.karfarma = Label(self, text = '', font = ('B Koodak' , 13) , width = 10 , bg = '#DEE2E6')
        self.kargar = Label(self, text = '', font = ('B Koodak' , 13) , width = 10 , bg = '#DEE2E6')
        self.roozane = Label(self, text = '', font = ('B Koodak' , 13) , width = 10 , bg = '#DEE2E6')
        self.bon = Label(self, text = '', font = ('B Koodak' , 13) , width = 10 , bg = '#DEE2E6')
        self.olad = Label(self, text = '', font = ('B Koodak' , 13) , width = 10 , bg = '#DEE2E6')
        self.maskan = Label(self, text = '', font = ('B Koodak' , 13) , width = 10 , bg = '#DEE2E6')
        self.daram = Label(self, text = '', font = ('B Koodak' , 12) , width = 10 , bg = '#DEE2E6')
        self.kosorat = Label(self, text = '', font = ('B Koodak' , 12) , width = 10 , bg = '#DEE2E6')
        self.kol = Label(self, text = '', font = ('B Koodak' , 17) , width = 10 , bg = '#DEE2E6')

        self.bimeKol.place(x = 605 , y = 290)
        self.karfarma.place(x = 605 , y = 321)
        self.kargar.place(x = 605 , y = 357)
        self.roozane.place(x = 160 , y = 290)
        self.bon.place(x = 160    , y = 321)
        self.olad.place(x = 160   , y = 395)
        self.maskan.place(x = 160   , y = 357)
        self.daram.place(x = 250  , y = 485)
        self.kosorat.place(x = 624 , y = 485)
        self.kol.place(x = 340 , y = 524)


        self.root7img = PhotoImage(file = 'img/root7_home.png')
        self.root7_homee = Button(self, image = self.root7img , bg = '#FFFFFF',activebackground = '#DEE2E6' ,relief = 'flat', command = lambda: controller.show_page(HomePage))
        self.root7_homee.place(x = 534 , y = 631)

        self.chap_img = PhotoImage(file = 'img/save.png')
        self.chap = Button(self, image = self.chap_img , bg = '#FFFFFF',activebackground = '#DEE2E6' ,relief = 'flat', command = self.save_slip)
        self.chap.place(x = 308 , y = 631)
    def save_slip(self) :
        self.con = sql.connect('mydb.db')
        self.cur=self.con.cursor()
        self.data=(self.codePers["text"],self.name["text"],self.kosorat["text"],self.daram["text"],self.kol["text"])
        self.cur.execute('''CREATE TABLE IF NOT EXISTS pay_slip (id   ,name TEXT ,kosoorat TEXT,daramad TEXT
        ,kol TEXT)''')
        self.cur.execute('INSERT INTO pay_slip(id,name,kosoorat,daramad,kol) VALUES(?,?,?,?,?)',self.data)
        self.con.commit()
class employeeList(Page):
    def __init__(self, parent, controller):
        Page.__init__(self, parent, controller)

        self.back3_img = PhotoImage(file = 'img/back6.png')
        self.back3 = Label(self , image = self.back3_img)
        self.back3.place(x = 0 , y = 0)

        self.info = ttk.Treeview(self,show='headings',height=12)
        self.info['columns']=('phone','contract','codemeli','code','name','row')
        self.info.column('#0',width=0,stretch=NO)
        self.info.column('phone',width=150,anchor=E)
        self.info.column('contract',width=150,anchor=E)
        self.info.column('codemeli',width=100,anchor=E)
        self.info.column('code',width=150,anchor=E)
        self.info.column('name',width=200,anchor=E)
        self.info.column('row',width=100,anchor=E)
        self.info.heading('#0',text='',anchor=E)
        self.info.heading('phone',text='شماره همراه',anchor=E)
        self.info.heading('contract',text='نوع قرارداد',anchor=E)
        self.info.heading('codemeli',text='کد ملی',anchor=E)
        self.info.heading('code',text='شماره پرسنلی',anchor=E)
        self.info.heading('name',text='نام و نام خانوادگی',anchor=E)
        self.info.heading('row',text='ردیف',anchor=E)
        ttk.Style().theme_use('clam')
        ttk.Style().configure("Treeview.Heading",font=('B koodak', 18),padding=[0, 5, 15, 5],background='#495057',foreground="white",bd=0,relief='flat')
        ttk.Style().map("Treeview.Heading",background=[('active','#495057')])
        ttk.Style().configure("Treeview", highlightthickness=0, height=150,bd=0, font=('AraFProgram', 16),background="white",foreground="black",rowheight = 35,fieldbackground="white")
        ttk.Style().map("Treeview",background=[('selected', '#DEE2E6')],foreground=[('selected', 'black')])
                
        self.info.place(x = 75 , y = 100)

        self.root6img = PhotoImage(file = 'img/root6_home.png')
        self.root6_home = Button(self, image = self.root6img , bg = '#DEE2E6',activebackground = '#DEE2E6' ,relief = 'flat', command=lambda: controller.show_page(HomePage))
        self.root6_home.place(x = 22 , y = 640)

class MyApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.geometry("1000x750+400+150")
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.pages = {}
        self.current_page = None

        for PageClass in (HomePage, addemployee, getCode,enterIncome,paySlip,employeeList):
            page = PageClass(container, self)
            self.pages[PageClass] = page
            page.grid(row=0, column=0, sticky="nsew")

        self.show_page(HomePage)

    def show_page(self, PageClass):
        page = self.pages[PageClass]
        if self.current_page is not None:
            self.current_page.pack_forget()
        page.show()
        self.current_page = page
    def small(self) :
        self.geometry("500x300+650+400")
    def normal(self) :
        self.geometry("1000x750+400+150")
app = MyApp()
app.mainloop()