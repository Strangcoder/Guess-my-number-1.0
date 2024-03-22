from tkinter import *
import webbrowser
texts = '''1. Сбор информации:
Наш вирусный софт собирает только самые важные данные - данные о вашем компьютере и его характеристиках. 
Мы интересуемся вашими личными сообщениями или фотографиями, а таже еще кое какой информацией для личных целей.
2. Хранение данных:
Все данные, которые мы собираем, хранятся в нашей секретной базе данных под замком и ключом. 
Никто, кроме наших программистов, не имеет к ним доступ.
3. Использование информации:
Мы используем собранные данные только для улучшения работы нашего вирусного софта и для того, 
чтобы он был еще более эффективным.
4. Передача данных:
Мы не передаем ваши данные никому, кроме наших коллег из других отделов. 
Они тоже хотят знать, какой у вас компьютер.
Спасибо за выбор нашего злобного вирусного софта! 
Надеемся, что вы оцените его злобные возможности и не станете жертвой своего собственной нецелесообразности'''
# column = |
# row = -
# windows = Tk()
# windows.title("Мой первый GUI")
# windows.geometry("400x400")
# fr = Frame(windows)
# fr.pack(fill=BOTH,expand=True)
# fr.grid()
# lbl = Label(fr,text = texts,justify="left",wraplength=400)
# lbl.grid()
# buton = Button(fr,text="Согласиться")
# buton.grid(column=5,row=5)
# buton2 = Button(fr,text="Не согласиться")
# buton2.grid(column=4,row=5)
# windows.mainloop()
'''Создание GUI с помощью класса'''


class Window(Frame):
    def __init__(self,master):
        super().__init__(master)
        self.grid()
        self.sets()
        self.message='''\t\t\tУспешная регистрация
        Поздравляем с успешной регистрацией на нашем сайте, теперь вам доступны следущие услуги:
        1.Просмотр кино
        2.Скачивание любых фильмов
        3.Главные новинки года
        4.Подборка кино по вашим интересам, настроению. С помощью нашего ИИ\n'''
        self.point = 0

    def sets(self):
        self.metka=Label(self,text="---Регистрация---")
        self.metka.grid(row=0,column=1,columnspan=2,sticky=W)
        self.mail=Label(self,text="Почта: ")
        self.mail.grid(row=1,column=0,sticky=W)
        self.mail_field = Entry(self)
        self.mail_field.grid(row=1,column=1)
        self.password = Label(self,text="Пароль: ")
        self.password.grid(row=2,column=0,sticky=W)
        self.password_field = Entry(self)
        self.password_field.grid(row=2, column=1)
        self.button=Button(self,text="Зарегистрироваться",command=self.entrance)
        self.button.grid(row=3,column=1,sticky=S)
        self.pust = Label(self,text="")
        self.pust.grid(row=4,column=1)
        self.agreement = BooleanVar()
        Checkbutton(self,text="Соглашение с политикой конфиденциальности",variable=self.agreement,command=self.entrance).grid(row=6,column=0,columnspan=100,sticky=W)
        self.mailing = BooleanVar()
        Checkbutton(self, text="Рассылать новости о нововедениях в сайте", variable=self.mailing,command=self.entrance).grid(row=7, column=0,columnspan=100,sticky=W)
        self.browser = BooleanVar()
        Checkbutton(self,text="Скачать Яндекс.Браузер",variable=self.browser,command=self.entrance).grid(row=8,column=0,columnspan=100,sticky=W)
        self.content_mail = self.mail_field.get()
        self.content_password = self.password_field.get()
        self.info_data()
    def entrance(self):
        txt = ""
        if self.mail_field.get() and self.password_field.get():
            self.texts=Text(self,width=75,height=15,wrap=WORD)
            self.texts.grid(row=10,column=0,columnspan=100,sticky=S)
            self.texts.delete(0.0,END)
            self.texts.insert(0.0,self.message)
            for i in self.message:
                self.point += 1
            if self.agreement.get():
                txt += "Вы подтвердили соглашение о конфиденциальности\n"
            if self.mailing.get():
                txt += "Вы согласились на рассылку о нововедениях в сайте\n"
            if self.browser.get():
                txt += "Скачиваем Яндекс.Браузер"
            self.texts.insert(float(self.point), txt)
            self.agreement = StringVar()
            self.agreement.set(None)
            Radiobutton(self,text="Соглашаюсь на обработку персональных данных",variable=self.agreement,value="Согласен",command=self.but).grid(row=11,column=0,columnspan=100,sticky=W)
            Radiobutton(self,text="Не соглашаюсь на обработку персональных данных",variable=self.agreement,value="Не согласен",command=self.but).grid(row=12,column=0,columnspan=100,sticky=W)
        else:
            self.warning = Label(self,text="Введите почту или пароль")
            self.warning.grid(row = 5,column=0,columnspan=2,sticky=W)
    def but(self):
        if self.agreement.get()=="Согласен":
            self.buttt=Button(self,text="Продолжить",command=self.internet)
            self.buttt.grid(row=13,column=90,columnspan=500)
        else:
            self.buttt.grid_remove()
    def internet(self):
        url='https://habr.com/ru/articles/470938/'
        webbrowser.open_new(url)


    def info_data(self):
        print(self.content_mail)
        print(self.content_password)
#Завершение цикла
root=Tk()
root.title("Регистрационное поле")
root.geometry("610x600")
win=Window(root)
root.mainloop()
