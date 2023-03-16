from re import M
from tkinter import *
from tkinter import messagebox, ttk
import tkinter as tk
import datetime as dt
from tkinter import filedialog
tedad_f = 0
def Login():
    check = user_ent.get()
    check2 = pass_ent.get()
    if check == 'admin' and check2 == 'admin':
        root2.state('withdrawn')
        root.state('normal')
    else : 
        messagebox.showerror(title='Error', message='نام کابری یا رمز عبور اشتباه است')
        user_ent.delete(0,END)
        pass_ent.delete(0,END)
        user_ent.focus()

def hide(event = None):
    if pass_ent['show'] == '*' :
        pass_ent['show'] = ''
        eye_img['file'] = 'baz.png'
    elif pass_ent['show'] == '' :
        pass_ent['show'] = '*'
        eye_img['file'] = 'baste.png'
def getInfo() :
    pers = pers_ent.get()
    pr = pr_ent.get()
    na = na_ent.get()
    fa = f_ent.get()
    c = c_ent.get()
    nu = nu_ent.get()
    d = d_ent.get()
    v = ''
    if (var1.get() == 1):
        v = 'مجرد'
    elif (var2.get() == 1):
        v = 'متاهل'
    ch = ch_ent.get()
    ph = ph_ent.get()
    m = m_ent.get()
    co = combo.get()
    if pr_ent.get() == '' or pr_ent.get() == '' or na_ent.get() == '' or f_ent.get() == '' or c_ent.get() == '' or nu_ent.get() == '' or d_ent.get() == '' or ch_ent.get() == '' or ph_ent.get() == '' or m_ent.get() == '' :
        messagebox.showerror(title='Error', message='لطفا همه ی فیلد ها را پر کنید')
    else :               
        messagebox.askquestion('askquestion', 'آيا از ذخيره اطلاعات مطمئن هستيد؟')
        text = '{},{} ,{} ,{},{},{},{} ,{} ,{},{},{},{}\n'.format(pr,na,fa,c,nu,d,v,ch,ph,m,co,img_name)
        information = open('data.csv', mode = 'a', encoding="utf-8")
        information.write(text)
        information.close()
        pers_ent.focus
        var3 = IntVar()
        c1['variable'] = var3
        var4 = IntVar()
        c2['variable'] = var4
        combo.set("یک گزینه را انتخاب کنید")
        pr_img['file'] = 'img/pr.png'
        pers_ent.delete(0,END)
        pr_ent.delete(0,END)
        na_ent.delete(0,END)
        f_ent.delete(0,END)
        c_ent.delete(0,END)
        nu_ent.delete(0,END)
        d_ent.delete(0,END)
        ch_ent.delete(0,END)
        ph_ent.delete(0,END)
        m_ent.delete(0,END)
def sodor() :
    bonrekargari = 850000
    hmaskann = 650000
    hoqoq_paye = slip_ent1.get()
    tarikh_e = slip_ent2.get()
    tarikh_e = slip_ent2.get()
    ezefe = slip_ent3.get()
    shabi = slip_ent4.get()
    tatili = slip_ent5.get()
    tarikh['text'] = tarikh_e
    ezaf['text'] = ezefe
    shab['text'] = shabi
    tatil['text'] = tatili
    haqBime = int(hoqoq_paye) + bonrekargari + hmaskann
    bimeKoll = int(int(haqBime) * 0.3) 
    bimeKarfarma = int(int(haqBime) * 0.23)
    bimeKargar = int(int(haqBime) * 0.07)
    haqolad =   417000 * int(tedad_f)
    ezafe_kari = int(hoqoq_paye) / 220 * 1.4 * int(ezefe)
    shab_kari = int(hoqoq_paye) / 220 * 1.35 * int(shabi)
    taatil_kari = int(hoqoq_paye) / 220 * 1.4 * int(tatili)
    kosurat = int(bimeKargar) 
    daramad = int(hoqoq_paye) + int(ezafe_kari) + int(taatil_kari) + int(shab_kari) + int(bonrekargari) + int(hmaskann) + int(haqolad)
    rooozane = int(int(daramad) / 30)
    pardakhti = int(daramad) - int(kosurat)
    bimeKol['text'] =  '''{:,}'''.format(bimeKoll)
    karfarma['text'] =  '''{:,}'''.format(bimeKarfarma)
    kargar['text'] =  '''{:,}'''.format(bimeKargar)
    roozane['text'] =  '''{:,}'''.format(rooozane)
    bon['text'] =  '''{:,}'''.format(bonrekargari)
    maskan['text'] =  '''{:,}'''.format(hmaskann)
    olad['text'] =  '''{:,}'''.format(haqolad)
    daram['text'] =  '''{:,}'''.format(daramad)
    kosorat['text'] =  '''{:,}'''.format(kosurat)
    kol['text'] =  '''{:,}'''.format(pardakhti)
    asd = codePers['text']
    text = '{},{}\n'.format(asd,pardakhti)
    information = open('data2.csv', mode = 'a', encoding="utf-8")
    information.write(text)
    information.close()
    root5.state('withdrawn')
    root7.state('normal')
def getcode() :
    global tedad_f
    code_pers = code_ent.get()
    information = open('data.csv', mode = 'r', encoding="utf-8")
    info = information.readlines()
    information.close()
    for i in range(len(info)) :
        hoqoq = info[i].split(',')
        if hoqoq[0] == (code_pers) :
            root4.state('withdrawn')
            root5.state('normal')
            khane['text'] = hoqoq[1]
            code['text'] = hoqoq[4]
            date['text'] = hoqoq[5]
            codePers['text'] = hoqoq[0]
            name['text'] = hoqoq[1]
            shomerShenas['text'] = hoqoq[4]
            tedad['text'] = hoqoq[7]
            vaziat['text'] = hoqoq[6]
            tedad_f = hoqoq[7]
            education['text'] = hoqoq[9]
def List():
    read = open('data.csv' , mode = 'r' , encoding = 'utf-8')
    listkarmand = read.readlines()
    for i in range(len(listkarmand)) :
        karmand = listkarmand[i].split(',')
        if i==0:
            lbl1_n['text']='''{: ^22}'''.format(karmand[1])
            lbl1_nu['text']='''{: ^22}'''.format(karmand[0])
            lbl1_c['text']='''{: ^25}'''.format(karmand[4])
            lbl1_co['text']='''{: ^28}'''.format(karmand[10])
            lbl1_s['text']='''{: ^28}'''.format(karmand[8])
        elif i==1:
            lbl2_n['text']='''{: ^22}'''.format(karmand[1])
            lbl2_nu['text']='''{: ^22}'''.format(karmand[0])
            lbl2_c['text']='''{: ^25}'''.format(karmand[4])
            lbl2_co['text']='''{: ^28}'''.format(karmand[10])
            lbl2_s['text']='''{: ^28}'''.format(karmand[8])
        elif i==2:
            lbl3_n['text']='''{: ^22}'''.format(karmand[1])
            lbl3_nu['text']='''{: ^22}'''.format(karmand[0])
            lbl3_c['text']='''{: ^25}'''.format(karmand[4])
            lbl3_co['text']='''{: ^28}'''.format(karmand[10])
            lbl3_s['text']='''{: ^28}'''.format(karmand[8])
        elif i==3:
            lbl4_n['text']='''{: ^22}'''.format(karmand[1])
            lbl4_nu['text']='''{: ^22}'''.format(karmand[0])
            lbl4_c['text']='''{: ^25}'''.format(karmand[4])
            lbl4_co['text']='''{: ^28}'''.format(karmand[11])
            lbl4_s['text']='''{: ^28}'''.format(karmand[8])
        elif i==4:
            lbl5_n['text']='''{: ^22}'''.format(karmand[1])
            lbl5_nu['text']='''{: ^22}'''.format(karmand[0])
            lbl5_c['text']='''{: ^25}'''.format(karmand[4])
            lbl5_co['text']='''{: ^28}'''.format(karmand[10])
            lbl5_s['text']='''{: ^28}'''.format(karmand[8])
        elif i==5:
            lbl6_n['text']='''{: ^22}'''.format(karmand[1])
            lbl6_nu['text']='''{: ^22}'''.format(karmand[0])
            lbl6_c['text']='''{: ^25}'''.format(karmand[4])
            lbl6_co['text']='''{: ^28}'''.format(karmand[10])
            lbl6_s['text']='''{: ^28}'''.format(karmand[8])
        elif i==6:
            lbl7_n['text']='''{: ^22}'''.format(karmand[1])
            lbl7_nu['text']='''{: ^22}'''.format(karmand[0])
            lbl7_c['text']='''{: ^25}'''.format(karmand[4])
            lbl7_co['text']='''{: ^28}'''.format(karmand[10])
            lbl7_s['text']='''{: ^28}'''.format(karmand[8])
        elif i==7:
            lbl8_n['text']='''{: ^22}'''.format(karmand[1])
            lbl8_nu['text']='''{: ^22}'''.format(karmand[0])
            lbl8_c['text']='''{: ^25}'''.format(karmand[4])
            lbl8_co['text']='''{: ^28}'''.format(karmand[10])
            lbl8_s['text']='''{: ^28}'''.format(karmand[8])
        elif i==8:
            lbl9_n['text']='''{: ^22}'''.format(karmand[1])
            lbl9_nu['text']='''{: ^22}'''.format(karmand[0])
            lbl9_c['text']='''{: ^25}'''.format(karmand[4])
            lbl9_co['text']='''{: ^28}'''.format(karmand[10])
            lbl9_s['text']='''{: ^28}'''.format(karmand[8])
        elif i==9:
            lbl10_n['text']='''{: ^22}'''.format(karmand[1])
            lbl10_nu['text']='''{: ^22}'''.format(karmand[0])
            lbl10_c['text']='''{: ^25}'''.format(karmand[4])
            lbl10_co['text']='''{: ^28}'''.format(karmand[10])
            lbl10_s['text']='''{: ^28}'''.format(karmand[8])
        read.close()
        root6.state('normal')
        root.state('withdrawn')

def slip() :
    root4.state('normal')
    root.state('withdrawn')
def employee() :
    root3.state('normal')
    root.state('withdrawn')
def marital_status() :
    pass
def dropdown_opened() :
    pass
def change_image() :
    global img_name
    img_name = filedialog.askopenfilename()  
    pr_img['file'] = img_name
def home_root3() :
        root3.state('withdrawn')
        root.state('normal')
def home_root6() :
        root6.state('withdrawn')
        root.state('normal')
def home_root5() :
        root5.state('withdrawn')
        root.state('normal')
def home_root7() :
        root7.state('withdrawn')
        root.state('normal')
root  = Tk()
root.state('withdrawn')
root.geometry('1000x700+400+150')

backg = PhotoImage(file = 'img/back1.png')
back = Label(width = 1000 , height = 700 , image = backg )
back.place(x = 0 , y = 0)

all = LabelFrame(root , bg ='#DEE2E6',relief = 'flat' )
all.grid(row = 1 , column = 1 , padx = 130 , pady = 140)

top = LabelFrame(all , relief = 'flat' , bg = '#DEE2E6' , pady = 25 )
top.grid(row = 1 , column = 1)
date = dt.datetime.now()
date_lbl = Label(top , bg = '#DEE2E6',anchor = 'w' ,width = 42 ,  text=f"{date: %Y %B %d , %H:%M}", font=("tahoma" , 20))
date_lbl.grid(row = 1 , column = 1)
images = LabelFrame(all, bg ='#DEE2E6',relief = 'flat' , padx = 40)
images.grid(row = 2 , column = 1)

slip_img = PhotoImage(file = 'img/pay_slip2.png')
employee_img = PhotoImage(file = 'img/new_employee2.png')
list_img = PhotoImage(file = 'img/list2.png')
list = Label(images, image = list_img, bg ='#DEE2E6')
pay_slip = Label(images , image = slip_img, bg ='#DEE2E6' )
new_employee = Label(images , image = employee_img, bg ='#DEE2E6')
list.grid(row = 1 , column = 1 )
pay_slip.grid(row = 1 , column = 2, padx = 40)
new_employee.grid(row = 1 , column = 3 )

buttons = LabelFrame(all, bg ='#DEE2E6', relief = 'flat')
buttons.grid(row = 3 , column = 1 , pady = 30)
list_btim = PhotoImage(file = 'img/list_btn.png')
slip_btim = PhotoImage(file = 'img/slip_btn.png')
employee_btim = PhotoImage(file = 'img/employee_btn.png')
list_btn = Button(buttons , relief = 'flat' , bg ='#DEE2E6' , activebackground='#DEE2E6' , image = list_btim , command = List)
slip_btn = Button(buttons , relief = 'flat' , bg ='#DEE2E6' , activebackground='#DEE2E6' , image = slip_btim , command = slip)
employee_btn = Button(buttons , relief = 'flat' , bg ='#DEE2E6' , activebackground='#DEE2E6' , image = employee_btim , command = employee )
list_btn.grid(row = 1 , column = 1)
slip_btn.grid(row = 1 , column = 2 , padx = 80)
employee_btn.grid(row = 1 , column = 3)





root3  = Toplevel()
root3.state('withdrawn')

root3.geometry('1000x750+400+150')

back1_img = PhotoImage(file = 'img/head.png')
back1 = Label(root3 , image = back1_img)
back1.place(x = 28 , y = 30)

back2_img= PhotoImage(file = 'img/body.png')
back2 = Label(root3 , image = back2_img)
back2.place(x = 30 , y = 161)

pr_img = PhotoImage(file = 'img/pr.png')
pr_image = Label(root3 , image = pr_img)
pr_image.place(x = 100 , y = 38)

change_img = PhotoImage(file = 'img/change_img.png')
change_btn = Button(root3 , image = change_img , bg = '#DEE2E6',activebackground = '#DEE2E6' ,relief = 'flat' , command = change_image)
change_btn.place(x = 208 , y = 55)

sabt_img = PhotoImage(file = 'img/sabt.png')
sabt = Button(root3 , image = sabt_img , bg = '#DEE2E6',activebackground = '#DEE2E6' ,relief = 'flat' , command = getInfo)
sabt.place(x = 295 , y = 622 )
root3img = PhotoImage(file = 'img/root3_home.png')
root3_homee = Button(root3, image = root3img , bg = '#DEE2E6',activebackground = '#DEE2E6' ,relief = 'flat', command = home_root3)
root3_homee.place(x = 500 , y = 622)


pers_ent = Entry(root3, bg = '#E9ECEF', width = 20 , font = ('B Koodak' , 10) , relief = 'flat' , justify = 'right')
pr_ent = Entry(root3, bg = '#E9ECEF', width = 20 , font = ('B Koodak' , 10) , relief = 'flat' , justify = 'right')
na_ent = Entry(root3, bg = '#E9ECEF', width = 20 , font = ('B Koodak' , 10) , relief = 'flat' , justify = 'right')
f_ent = Entry(root3, bg = '#E9ECEF', width = 20 , font = ('B Koodak' , 10) , relief = 'flat' , justify = 'right')
c_ent = Entry(root3, bg = '#E9ECEF', width = 20 , font = ('B Koodak' , 10) , relief = 'flat' , justify = 'right')
nu_ent = Entry(root3, bg = '#E9ECEF', width = 20 , font = ('B Koodak' , 10) , relief = 'flat' , justify = 'right')
d_ent = Entry(root3, bg = '#E9ECEF', width = 20 , font = ('B Koodak' , 10) , relief = 'flat' , justify = 'right')
ch_ent = Entry(root3, bg = '#E9ECEF', width = 20 , font = ('B Koodak' , 10) , relief = 'flat' , justify = 'right')
ph_ent = Entry(root3, bg = '#E9ECEF', width = 20 , font = ('B Koodak' , 10) , relief = 'flat' , justify = 'right')
m_ent = Entry(root3, bg = '#E9ECEF', width = 20 , font = ('B Koodak' , 10) , relief = 'flat' , justify = 'right')
var1 = IntVar()
var2 = IntVar()
c1 = Checkbutton(root3,bg = '#DEE2E6',variable=var1, onvalue=1, offvalue=0, command=marital_status)
c1.place(x = 150 , y = 220)
c2 = Checkbutton(root3,bg = '#DEE2E6',variable=var2, onvalue=1, offvalue=0, command=marital_status)
c2.place(x = 82 , y = 220)

combo = ttk.Combobox(root3,width = 16,textvariable = 'asdsd' , font = ('B Koodak' , 12),values=["دولتی", "خصوصی", "مشاوره ای", "آزمایشی" , 'کارمزدی'])
combo.bind("<<ComboboxSelected>>", dropdown_opened)
combo.set("یک گزینه را انتخاب کنید")
combo.place(x=65, y=575)
#7 #6
pers_ent.place(x = 633 , y = 68)
pr_ent.place(x = 635 , y = 67)
na_ent.place(x = 635 , y = 219)
f_ent.place(x = 635 , y = 309)
c_ent.place(x = 635 , y = 397)
nu_ent.place(x = 635 , y = 485)
d_ent.place(x = 635 , y = 574)
ch_ent.place(x = 71 , y = 309)
ph_ent.place(x = 71 , y = 399)
m_ent.place(x = 71 , y = 489)




root4 = Toplevel()
root4.state('withdrawn')

root4.geometry('500x300+650+400')

back4_img = PhotoImage(file = 'img/back4.png')
back4 = Label(root4 ,image = back4_img)
back4.place(x = 0 , y = 0)

code_ent = Entry(root4, bg = '#E9ECEF', width = 15 , font = ('B Koodak' , 15) , relief = 'flat' , justify = 'right')
code_ent.place(x = 170, y = 120)

code_img = PhotoImage(file = 'img/code_btn.png')
code_btn = Button(root4 , image = code_img , bg = '#DEE2E6',activebackground = '#DEE2E6' ,relief = 'flat' , command = getcode)
code_btn.place(x = 118 , y = 183)







root5 = Toplevel()
root5.state('withdrawn')
root5.geometry('800x500+500+250')
back5_img = PhotoImage(file = 'img/back5.png')
back5 = Label(root5 ,image = back5_img)
back5.place(x = 0 , y = 0)
slip_ent1 = Entry(root5, bg = '#E3F2FD', width = 20 , font = ('B Koodak' , 10) , relief = 'flat' , justify = 'right')
slip_ent2 = Entry(root5, bg = '#E3F2FD', width = 20 , font = ('B Koodak' , 10) , relief = 'flat' , justify = 'right')
slip_ent3 = Entry(root5, bg = '#E3F2FD', width = 20 , font = ('B Koodak' , 10) , relief = 'flat' , justify = 'right')
slip_ent4 = Entry(root5, bg = '#E3F2FD', width = 20 , font = ('B Koodak' , 10) , relief = 'flat' , justify = 'right')
slip_ent5 = Entry(root5, bg = '#E3F2FD', width = 20 , font = ('B Koodak' , 10) , relief = 'flat' , justify = 'right')
#+10 #+4
slip_ent1.place(x = 135 , y = 113)
slip_ent2.place(x = 135 , y = 158)
slip_ent3.place(x = 135 , y = 200)
slip_ent4.place(x = 135 , y = 245)
slip_ent5.place(x = 135 , y = 287)

slip_btn2_img = PhotoImage(file = 'img/slip_btn2.png')
slip_btn2 = Button(root5 , image = slip_btn2_img , relief = 'flat' , activebackground = '#DEE2E6',command = sodor)
slip_btn2.place(x = 132 , y = 333)


khane = Label(root5  , text = ''  , width = 10, font = ('B Koodak' , 15) , bg  = '#42A5F5' , fg = '#CED4DA')
khane.place(x = 533 , y = 228)

code = Label(root5  , text = ''  , width = 10, font = ('B Koodak' , 10) , bg  = '#42A5F5' , fg = '#CED4DA')
date = Label(root5  , text = ''  , width = 10, font = ('B Koodak' , 10) , bg  = '#42A5F5' , fg = '#CED4DA')
education = Label(root5  , text = ''  , width = 10, font = ('B Koodak' , 10) , bg  = '#42A5F5' , fg = '#CED4DA')

code.place(x = 525 , y = 265)
date.place(x = 525 , y = 292)
education.place(x = 525 , y = 316)

root5img = PhotoImage(file = 'img/root5_home.png')
root5_homee = Button(root5, image = root5img , bg = '#FFFFFF',activebackground = '#DEE2E6' ,relief = 'flat', command = home_root5)
root5_homee.place(x = 276 , y = 333)



root6 = Toplevel()
root6.state('withdrawn')
root6.geometry('1000x666+400+200')
back3_img = PhotoImage(file = 'img/back3.png')
back3 = Label(root6 , image = back3_img)
back3.place(x = 0 , y = 0)
lbl1_n = Label(root6 , text = '' , font = ('B Koodak' , 13) , width = 12 )
lbl2_n = Label(root6 , text = '', font = ('B Koodak' , 13) , width = 12 , bg = '#CED4DA')
lbl3_n = Label(root6 , text = '', font = ('B Koodak' , 13) , width = 12)
lbl4_n = Label(root6 , text = '', font = ('B Koodak' , 13) , width = 12 , bg = '#CED4DA')
lbl5_n = Label(root6 , text = '', font = ('B Koodak' , 13) , width = 12)
lbl6_n = Label(root6 , text = '', font = ('B Koodak' , 13) , width = 12 , bg = '#CED4DA')
lbl7_n = Label(root6 , text = '', font = ('B Koodak' , 13) , width = 12)
lbl8_n = Label(root6 , text = '', font = ('B Koodak' , 13) , width = 12 , bg = '#CED4DA')
lbl9_n = Label(root6 , text = '', font = ('B Koodak' , 13) , width = 12)
lbl10_n = Label(root6 , text = '', font = ('B Koodak' , 13) , width = 12 , bg = '#CED4DA')
lbl1_n.place(x = 664 , y = 142 )
lbl2_n.place(x = 664 , y = 187 )
lbl3_n.place(x = 664 , y = 232 )
lbl4_n.place(x = 664 , y = 277 )
lbl5_n.place(x = 664 , y = 322 )
lbl6_n.place(x = 664 , y = 361 )
lbl7_n.place(x = 664 , y = 412 )
lbl8_n.place(x = 664 , y = 457 )
lbl9_n.place(x = 664 , y = 502 )
lbl10_n.place(x = 664 , y = 547 )

lbl1_nu = Label(root6 , text = '' , font = ('B Koodak' , 13) , width = 10)
lbl2_nu = Label(root6 , text = '', font = ('B Koodak' , 13) , width = 10 , bg = '#CED4DA')
lbl3_nu = Label(root6 , text = '', font = ('B Koodak' , 13) , width = 10)
lbl4_nu = Label(root6 , text = '', font = ('B Koodak' , 13) , width = 10 , bg = '#CED4DA')
lbl5_nu = Label(root6 , text = '', font = ('B Koodak' , 13) , width = 10)
lbl6_nu = Label(root6 , text = '', font = ('B Koodak' , 13) , width = 10 , bg = '#CED4DA')
lbl7_nu = Label(root6 , text = '', font = ('B Koodak' , 13) , width = 10)
lbl8_nu = Label(root6 , text = '', font = ('B Koodak' , 13) , width = 10 , bg = '#CED4DA')
lbl9_nu = Label(root6 , text = '', font = ('B Koodak' , 13) , width = 10)
lbl10_nu = Label(root6 , text = '', font = ('B Koodak' , 13) , width = 10 , bg = '#CED4DA')
lbl1_nu.place(x = 520 , y = 142 )
lbl2_nu.place(x = 520 , y = 187 )
lbl3_nu.place(x = 520 , y = 232 )
lbl4_nu.place(x = 520 , y = 277 )
lbl5_nu.place(x = 520 , y = 322 )
lbl6_nu.place(x = 520 , y = 361 )
lbl7_nu.place(x = 520 , y = 412 )
lbl8_nu.place(x = 520 , y = 457 )
lbl9_nu.place(x = 520 , y = 502 )
lbl10_nu.place(x = 520 , y = 547 )

lbl1_c = Label(root6 , text = '' , font = ('B Koodak' , 13) , width = 10)
lbl2_c = Label(root6 , text = '', font = ('B Koodak' , 13) , width = 10 , bg = '#CED4DA')
lbl3_c = Label(root6 , text = '', font = ('B Koodak' , 13) , width = 10)
lbl4_c = Label(root6 , text = '', font = ('B Koodak' , 13) , width = 10 , bg = '#CED4DA')
lbl5_c = Label(root6 , text = '', font = ('B Koodak' , 13) , width = 10)
lbl6_c = Label(root6 , text = '', font = ('B Koodak' , 13) , width = 10 , bg = '#CED4DA')
lbl7_c = Label(root6 , text = '', font = ('B Koodak' , 13) , width = 10)
lbl8_c = Label(root6 , text = '', font = ('B Koodak' , 13) , width = 10 , bg = '#CED4DA')
lbl9_c = Label(root6 , text = '', font = ('B Koodak' , 13) , width = 10)
lbl10_c = Label(root6 , text = '', font = ('B Koodak' , 13) , width = 10 , bg = '#CED4DA')
lbl1_c.place(x = 390 , y = 142 )
lbl2_c.place(x = 390 , y = 187 )
lbl3_c.place(x = 390 , y = 232 )
lbl4_c.place(x = 390 , y = 277 )
lbl5_c.place(x = 390 , y = 322 )
lbl6_c.place(x = 390 , y = 361 )
lbl7_c.place(x = 390 , y = 412 )
lbl8_c.place(x = 390 , y = 457 )
lbl9_c.place(x = 390 , y = 502 )
lbl10_c.place(x = 390 , y = 547 )

lbl1_co = Label(root6 , text = '' , font = ('B Koodak' , 13) , width = 10)
lbl2_co = Label(root6 , text = '', font = ('B Koodak' , 13) , width = 10 , bg = '#CED4DA')
lbl3_co = Label(root6 , text = '', font = ('B Koodak' , 13) , width = 10)
lbl4_co = Label(root6 , text = '', font = ('B Koodak' , 13) , width = 10 , bg = '#CED4DA')
lbl5_co = Label(root6 , text = '', font = ('B Koodak' , 13) , width = 10)
lbl6_co = Label(root6 , text = '', font = ('B Koodak' , 13) , width = 10 , bg = '#CED4DA')
lbl7_co = Label(root6 , text = '', font = ('B Koodak' , 13) , width = 10)
lbl8_co = Label(root6 , text = '', font = ('B Koodak' , 13) , width = 10 , bg = '#CED4DA')
lbl9_co = Label(root6 , text = '', font = ('B Koodak' , 13) , width = 10)
lbl10_co = Label(root6 , text = '', font = ('B Koodak' , 13) , width = 10 , bg = '#CED4DA')
lbl1_co.place(x = 274 , y = 142 )
lbl2_co.place(x = 274 , y = 187 )
lbl3_co.place(x = 274 , y = 232 )
lbl4_co.place(x = 274 , y = 277 )
lbl5_co.place(x = 274 , y = 322 )
lbl6_co.place(x = 274 , y = 361 )
lbl7_co.place(x = 274 , y = 412 )
lbl8_co.place(x = 274 , y = 457 )
lbl9_co.place(x = 274 , y = 502 )
lbl10_co.place(x = 274 , y = 547 )


lbl1_s = Label(root6 , text = '' , font = ('B Koodak' , 13) , width = 12)
lbl2_s = Label(root6 , text = '', font = ('B Koodak' , 13) , width = 12 , bg = '#CED4DA')
lbl3_s = Label(root6 , text = '', font = ('B Koodak' , 13) , width = 12)
lbl4_s = Label(root6 , text = '', font = ('B Koodak' , 13) , width = 12 , bg = '#CED4DA')
lbl5_s = Label(root6 , text = '', font = ('B Koodak' , 13) , width = 12)
lbl6_s = Label(root6 , text = '', font = ('B Koodak' , 13) , width = 12 , bg = '#CED4DA')
lbl7_s = Label(root6 , text = '', font = ('B Koodak' , 13) , width = 12)
lbl8_s = Label(root6 , text = '', font = ('B Koodak' , 13) , width = 12 , bg = '#CED4DA')
lbl9_s = Label(root6 , text = '', font = ('B Koodak' , 13) , width = 12)
lbl10_s = Label(root6 , text = '', font = ('B Koodak' , 13) , width = 12 , bg = '#CED4DA')
lbl1_s.place(x = 138 , y = 142 )
lbl2_s.place(x = 138 , y = 187 )
lbl3_s.place(x = 138 , y = 232 )
lbl4_s.place(x = 138 , y = 277 )
lbl5_s.place(x = 138 , y = 322 )
lbl6_s.place(x = 138 , y = 361 )
lbl7_s.place(x = 138 , y = 412 )
lbl8_s.place(x = 138 , y = 457 )
lbl9_s.place(x = 138 , y = 502 )
lbl10_s.place(x = 138 , y = 547 )

root6img = PhotoImage(file = 'img/root6_home.png')
root6_home = Button(root6, image = root6img , bg = '#DEE2E6',activebackground = '#DEE2E6' ,relief = 'flat', command = home_root6)
root6_home.place(x = 22 , y = 590)




root7 = Toplevel()
root7.geometry('1000x700+400+200')
root7.state('withdrawn')

back7_img = PhotoImage(file = 'img/back6.png')
back7 = Label(root7 ,image = back7_img)
back7.place(x = 0 , y = 0)

codePers = Label(root7, text = '', font = ('B Koodak' , 10) , width = 10 , bg = '#DEE2E6')
name = Label(root7, text = 'asdsd', font = ('B Koodak' , 10) , width = 10 , bg = '#DEE2E6')
shomerShenas = Label(root7, text = '', font = ('B Koodak' , 10) , width = 10 , bg = '#DEE2E6')
tedad = Label(root7, text = '', font = ('B Koodak' , 10) , width = 10 , bg = '#DEE2E6')
vaziat =Label(root7, text = '', font = ('B Koodak' , 10) , width = 10 , bg = '#DEE2E6')
tarikh = Label(root7, text = '', font = ('B Koodak' , 10) , width = 10 , bg = '#DEE2E6')
ezaf = Label(root7, text = '', font = ('B Koodak' , 10) , width = 10 , bg = '#DEE2E6')
shab = Label(root7, text = '', font = ('B Koodak' , 10) , width = 10 , bg = '#DEE2E6')
tatil = Label(root7, text = '', font = ('B Koodak' , 10) , width = 10 , bg = '#DEE2E6')
#40 #3
codePers.place(x = 745 , y = 83)
name.place(x = 745 , y = 110)
shomerShenas.place(x = 745 , y = 140)
tedad.place(x = 544 , y = 83)
vaziat.place(x = 544 , y = 110)
tarikh.place(x = 221 , y = 81)
ezaf.place(x = 221 , y = 110)
shab.place(x = 221 , y = 140)
tatil.place(x = 221 , y = 168)

bimeKol = Label(root7, text = '', font = ('B Koodak' , 13) , width = 10 , bg = '#DEE2E6')
karfarma = Label(root7, text = '', font = ('B Koodak' , 13) , width = 10 , bg = '#DEE2E6')
kargar = Label(root7, text = '', font = ('B Koodak' , 13) , width = 10 , bg = '#DEE2E6')
roozane = Label(root7, text = '', font = ('B Koodak' , 13) , width = 10 , bg = '#DEE2E6')
bon = Label(root7, text = '', font = ('B Koodak' , 13) , width = 10 , bg = '#DEE2E6')
olad = Label(root7, text = '', font = ('B Koodak' , 13) , width = 10 , bg = '#DEE2E6')
maskan = Label(root7, text = '', font = ('B Koodak' , 13) , width = 10 , bg = '#DEE2E6')
daram = Label(root7, text = '', font = ('B Koodak' , 12) , width = 10 , bg = '#DEE2E6')
kosorat = Label(root7, text = '', font = ('B Koodak' , 12) , width = 10 , bg = '#DEE2E6')
kol = Label(root7, text = '', font = ('B Koodak' , 17) , width = 10 , bg = '#DEE2E6')

bimeKol.place(x = 605 , y = 290)
karfarma.place(x = 605 , y = 321)
kargar.place(x = 605 , y = 357)
roozane.place(x = 160 , y = 290)
bon.place(x = 160    , y = 321)
olad.place(x = 160   , y = 395)
maskan.place(x = 160   , y = 357)
daram.place(x = 250  , y = 485)
kosorat.place(x = 624 , y = 485)
kol.place(x = 340 , y = 524)


root7img = PhotoImage(file = 'img/root7_home.png')
root7_homee = Button(root7, image = root7img , bg = '#FFFFFF',activebackground = '#DEE2E6' ,relief = 'flat', command = home_root7)
root7_homee.place(x = 310 , y = 603)

chap_img = PhotoImage(file = 'img/chap.png')
chap = Button(root7, image = chap_img , bg = '#FFFFFF',activebackground = '#DEE2E6' ,relief = 'flat')
chap.place(x = 518 , y = 603)


root2 = Toplevel()
# root2.state('withdrawn')
root2.geometry('600x600+600+200')
root2.configure(bg = '#e6e6e9')
eye_img = PhotoImage(file = 'img/baste.png')

login_img = PhotoImage(file = 'img/login.png')
login_bg = Label(root2, image = login_img)
login_bg.place(x = 0 , y = 0)


login = LabelFrame(root2 , text = 'ورود' ,labelanchor = 'ne' ,bg ='#DEE2E6',relief='raised',)


user_ent = Entry(root2 , width = 25, show = '', font = ('B Koodak' , 10) ,relief = 'flat')
user_ent.place(x = 160 , y = 165)

pass_ent = Entry(root2 , width = 25, show = '*', font = ('B Koodak' , 10) ,relief = 'flat')
pass_ent.place(x = 160 , y = 214)

eye = Button(root2,image = eye_img,relief = 'flat', bg = '#DEE2E6',activebackground = '#DEE2E6')
eye.place(x = 106 , y = 214)


vorud = PhotoImage(file = 'img/vorud.png')
enter = Button(root2 ,image = vorud , text = 'enter',relief='flat' , bg = '#DEE2E6',activebackground = '#DEE2E6', command = Login)
enter.place(x = 225 , y = 364)

mes = Label(root2, text = '', bg = '#DEE2E6')


user_ent.focus()
eye.bind('<Button-1>',hide)
eye.bind('<ButtonRelease>',hide)
root.mainloop()