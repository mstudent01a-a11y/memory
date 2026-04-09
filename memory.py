from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QRadioButton, QHBoxLayout, QGroupBox, QButtonGroup
from random import*


app = QApplication([])
window = QWidget()
window.setWindowTitle('Memo card')
window.resize(400, 200)
window.total = 1
window.score = 0


'''Интерфейс приложения Memory Card'''
btn_OK = QPushButton('Ответить')
lb_Question = QLabel('тут будет вопрос')

RadioGroupBox = QGroupBox('Варианты ответа')
rbtn_1 = QRadioButton('Вариант 1')
rbtn_2 = QRadioButton('Вариант 2')
rbtn_3 = QRadioButton('Вариант 3')
rbtn_4 = QRadioButton('Вариант 4')

layout_ans1 = QVBoxLayout()
layout_ans2 = QHBoxLayout()
layout_ans3 = QHBoxLayout()
layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1)
#RadioGroupBox.hide()


AnsGroupBox = QGroupBox('Результат текста')
lb_Rezult = QLabel('Прав ты или нет?')
lb_Correct = QLabel('ответ будет тут!')
layout_res = QVBoxLayout()
layout_res.addWidget(lb_Rezult, alignment = (Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment = Qt.AlignCenter , stretch = 2)
AnsGroupBox.setLayout(layout_res)
AnsGroupBox.show()

layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()

layout_line1.addWidget(lb_Question, alignment = (Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(AnsGroupBox)
AnsGroupBox.hide()

layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch = 2)
layout_line3.addStretch(1)

layout_main = QVBoxLayout()

layout_main.addLayout(layout_line1, stretch = 2)
layout_main.addLayout(layout_line2, stretch = 8)
layout_main.addStretch
layout_main.addLayout(layout_line3, stretch = 1)
layout_main.addStretch(1)
layout_main.addSpacing(5)

window.setLayout(layout_main)


RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

class Question():
    def __init__(self, question, right, wrong_1, wrong_2, wrong_3):
        self.question = question
        self.right = right
        self.wrong_1 = wrong_1
        self.wrong_2 = wrong_2
        self.wrong_3 = wrong_3
questions = []
q1 = Question('Государственный язык Бразилии', 'Португальский', 'Бразильский', 'Русский', 'Японский')

questions.append(q1)

q2 = Question('Какого цвета нет на флаге России?', 'Оранжевый', 'Синий', 'Красный', 'Белый')
questions.append(q2)
questions.append(Question('Какой национальности не существует?', 'Смурфы', 'Алеуты', 'Чулымцы', 'Энцы'))

q3 = Question('Сколько рабочих дней в неделе?', '5', '7', '2', '6')
questions.append(q3)

q4 = Question('Во сколько лет поулчают первый паспорт ?', '14', '25', '15', '10')
questions.append(q4)

q5 = Question('Сколько месяцев в году?', '12', '15', '10', '5')
questions.append(q5)

q6 = Question('Каким цветом трава летом?', 'зелёная', 'коричневая', 'жёлтая', 'красная')
questions.append(q6)

def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Следующий вопрос')

def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Ответить')
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)    
    RadioGroup.setExclusive(True)

def test():
    if 'Ответить' == btn_OK.text():
        show_result()
    else:
        show_question()

answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

def ask(q: Question):
    '''функция записывает значения вопроса и ответов в соответсвующие виджеты,
    при этом варианты ответов рапределяются случайным образом'''
    shuffle(answers)
    answers[0].setText(q.right)
    answers[1].setText(q.wrong_1)
    answers[2].setText(q.wrong_2)
    answers[3].setText(q.wrong_3)
    lb_Question.setText(q.question)
    lb_Correct.setText(q.right)
    show_question()

def show_correct(res):
    lb_Rezult.setText(res)
    show_result()

def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно!')
        window.score += 1
        print('Статистика\n-Всего вопросов', window.total, '\n-Правильных ответов:', window.score)
        print('Рейтинг:', int(window.score / window.total*100), '%')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Неверно!')
            print('Статистика\n-Всего вопросов', window.total, '\n-Правильных ответов:', window.score)
            print('Рейтинг:', int(window.score / window.total*100), '%')

def next_question():
    window.total += 1
    print('Статистика\n-Всего вопросов', window.total, '\n-Правильных ответов:', window.score)
    window.cur_question = randint(0, len(questions)-1)
    window.cur_question += 1
    if window.cur_question >= len(questions):
        window.cur_question = 0
    q = questions[window.cur_question]
    ask(q)

def click_OK():
    if btn_OK.text() == 'Ответить':
        check_answer()
    else:
        next_question()
        
window.cur_question = -1 


btn_OK.clicked.connect(click_OK)

next_question()

window.show()
app.exec()



