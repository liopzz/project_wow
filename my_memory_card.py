from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from random import shuffle, randint

app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Опрос')
mega_question = QLabel('Ты дурак?')
main_win.resize(800, 600)

button = QPushButton("sdgdsg")



RadioGroupBox = QGroupBox('Варианты')

rbtn_1 = QRadioButton('да')
rbtn_2 = QRadioButton('нет')
rbtn_3 = QRadioButton('немного')
rbtn_4 = QRadioButton('сам такой')

RadioGroup = QButtonGroup() 
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

lo1 = QHBoxLayout()
lo2 = QVBoxLayout()
lo3 = QVBoxLayout()

lo2.addWidget(rbtn_1)
lo2.addWidget(rbtn_2)

lo3.addWidget(rbtn_3)
lo3.addWidget(rbtn_4)

lo1.addLayout(lo2)
lo1.addLayout(lo3)



RadioGroupBox.setLayout(lo1)




'''ЕЩЕ ОДИН ГРУПБОКС'''

ansgroupbox = QGroupBox()
lb_result = QLabel('Ты дурак или нет')
correct = QLabel('Ответ')

layout_res = QVBoxLayout()
layout_res.addWidget(lb_result)
layout_res.addWidget(correct,alignment = Qt.AlignCenter)
ansgroupbox.setLayout(layout_res)






layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()

layout_line1.addWidget(mega_question,alignment=Qt.AlignCenter)
layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(ansgroupbox)
layout_line3.addWidget(button) # кнопка должна быть большой

 

 


layout_vert = QVBoxLayout()
layout_vert.addLayout(layout_line1)
layout_vert.addLayout(layout_line2)
layout_vert.addLayout(layout_line3)


main_win.setLayout(layout_vert)
ansgroupbox.hide()


RadioGroup.setExclusive(False) # сняли ограничения, чтобы можно было сбросить выбор радиокнопки
rbtn_1.setChecked(False)
rbtn_2.setChecked(False)
rbtn_3.setChecked(False)
rbtn_4.setChecked(False)
RadioGroup.setExclusive(True) # вернули ограничения, теперь только одна радиокнопка может быть выбрана
answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]
class sprQuestion():
    def __init__(self,question,right_answer,wrong1,wrong2,wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3 
def show_question():
    ansgroupbox.hide()
    RadioGroupBox.show()
    
    button.setText("Ответ")
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)   
def ask(q:sprQuestion):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    mega_question.setText(q.question) #задали текст вопроса
    correct.setText(q.right_answer) #задали текст ответа
    show_question()


def next_question():
    print("*****")
    print('Всего вопросов:',main_win.total +1)
    print('Правильных ответов',main_win.score)
    cur_question = randint(0,len(question_list)-1)
    q = question_list[cur_question]
    ask(q)



def show_result():
    ansgroupbox.show()
    RadioGroupBox.hide()
    button.setText("Следующий вопрос")

def show_correct(res):
    lb_result.setText(res)
    show_result()


main_win.cur_question = -1
def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно')
        main_win.score += 1



    else:
        if answers[1].isChecked or answers[2].isChecked or answers[3].isChecked:
            show_correct('Неверно')

def click_ok():
    if button.text()== 'Ответ':
        check_answer()
    else:
        next_question()


q = sprQuestion('Ты дурак?','4','3','2','1')


main_win.total =0
main_win.score = 0






question_list = []
q1 = sprQuestion("номер дома",'1','2','3','4')
question_list.append(q1)
q2 = sprQuestion('ваа?','vaaa','vaaaa','vaaaaa','vaaaaaa')
question_list.append(q2)
q3 = sprQuestion('Vaaa?','вааа','ва','ваааа','нет')
question_list.append(q3)

















main_win.setWindowTitle('Memo Card')
button.clicked.connect(click_ok)
next_question()


main_win.show()
app.exec_()

