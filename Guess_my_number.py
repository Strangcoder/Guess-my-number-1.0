#Игра угадай число
#Импортирую библиотеки
from tkinter import*
import random
import webbrowser
def random_number():
    '''Функция которая возращает рандомное число'''
    number=random.randrange(1,101)
    return number

class Window(Frame):
    '''Создаем рамку'''
    def __init__(self,root):
        super().__init__(root)
        self.grid()
        self.entrance()
        self.entr=None
        #self.bttn=None
        self.numb=None
    def entrance(self):
        '''Метод начального экрана игры'''
        Label(self,text="Угадай число",font='Times 20').grid(row=0,column=1,columnspan=2,sticky=W,padx=(160))
        self.scores = Label(self,text="Очки: ",font='Times 15')
        self.scores.grid(row=0,column=3)
        self.score_txt = Text(self,width=2,height=0.5)
        self.score_txt.grid(row=0,column=4,columnspan=2)

        self.bttn=Button(self,text="Начать игру",command=self.game,width=20,height=1)
        self.bttn.grid(row=2,column=1,columnspan=2)

    def game(self):
        '''Метод основной части игры'''
        self.a = 5
        self.score = 0
        self.rand_num=random_number()
        self.bttn.grid_remove()
        self.entr=Entry(self,width=20,justify='center')
        self.entr.grid(row=2,column=1,rowspan=2,columnspan=2)
        self.bttn_2=Button(self,text="Подтвердить",command=self.comparison,overrelief=SUNKEN)
        self.bttn_2.grid(row=4,column=1,columnspan=2,pady=(10))
        self.bttn_help = Button(self,text='Подсказка:',overrelief=SUNKEN,command=self.helps)
        self.bttn_help.grid(row=7,column=3,columnspan=2,sticky=W)
        self.my_lable = Label(self,text="5")
        self.my_lable.grid(row=7,column=6,columnspan=2)
        self.help_txt=Text(self,width=7,height=0)
        self.help_txt.grid(row=8, column=3,pady=(5))
        Label(self,text=" ").grid(row=5,column=1)
        self.learn = Button(self, text="?",font='Times 10', command=self.git,width=3)
        self.learn.grid(row=10, column=0,columnspan=2)
    def comparison(self):
        '''Метод который сравнивает внесенное число и загаданное'''
        self.numb = int(self.entr.get())
        if self.numb==self.rand_num:
            Label(self,text='Вы отгадали',width=20).grid(row=5,column=1,columnspan=2)
            self.score+=10
            self.score_text = str(self.score)
            self.score_txt.delete(0.0, END)
            self.score_txt.insert(0.0, self.score_text)
            self.rand_num = random_number()
        else:
            Label(self, text='Вы не отгадали', width=20).grid(row=5, column=1,columnspan=2)
        s = 10
    def helps(self):
        '''Метод подсказки'''
        self.help_num=str(self.a)
        self.help_rand_num = str(self.rand_num)
        if self.a<=0:
            Label(self,text="Подсказки закончились!").grid(row=9,column=1,columnspan=2)
            self.my_lable.configure(text="0")
        else:
            self.a -= 1
            self.my_lable.configure(text=self.help_num)
            self.help_txt.delete(0.0, END)
            self.help_txt.insert(0.0, self.help_rand_num)
    def git(self):
        '''Метод с ссылкой на репозиторий GitHub с данным проектом'''
        url='https://github.com/Strangcoder?tab=repositories'
        webbrowser.open(url)

#Основная часть
root=Tk()
root.title("Guess my number")
w = root.winfo_screenwidth()
h = root.winfo_screenheight()
w = w//2 # середина экрана
h = h//2
w = w - 200 # смещение от середины
h = h - 200
root.geometry('580x250+{}+{}'.format(w, h))
root.resizable(False,False)
win=Window(root)
root.mainloop()