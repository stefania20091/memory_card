from PyQt5.QtCore import Qt 
from PyQt5.OtWidget import( 
    QApplication, QWidget, QTableWidget, QListWidget, 
     QLineEdit, QFormLoyout, QHBoxLayout, 
      QVBoxLayout, QGroupBox, QButtonGroup, 
      QPushButton, QLabel, QRadioButton, QSpinBox) 
app= QApplication([]) 
btn_Menu= QPushButton('Меню') 
btn_Relax= QPushButton('Відпочити') 
btn_Answer= QPushButton('Відповісти') 
box_Minutes= QSpinBox() 
box_Minutes.setValue(30) 
lb_Question= QLabel('') 
 
radio_Group = QGroupBox('Варіанти відповідей') 
radio_Answer = QButtonGroup() 
 
rbtn_1= QRadioButton('') 
rbtn_2= QRadioButton('') 
rbtn_3= QRadioButton('') 
rbtn_4= QRadioButton('') 
 
RadioGroup.addButton(rbtn_1) 
RadioGroup.addButton(rbtn_2) 
RadioGroup.addButton(rbtn_3) 
RadioGroup.addButton(rbtn_4) 
 
ans_Group_Box =QGroupBox('Результат тесту') 
lb_Result = QLabel('')#ця части коду віддповідає за відповідь вірно або ні 
lb_Corect = QLabel('')#ця частина показує лише правильну відповідь 
 
layout_ans1= QHBoxLayout() 
layout_ans2= QVBoxLayout()
layout_ans3= QVBoxLayout()

layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1)

layout_line1= QHBoxLayout() 
layout_line2= QHBoxLayout()
layout_line3= QHBoxLayout()
layout_line4= QHBoxLayout()

layout_line1.addWidget(btn_Menu)
layout_line1.addStretch(1)
layout_line1.addWidget(btn_Relax)
layout_line1.addWidget(box_Minutes)
layout_line1.addWidget(QLabel("minutes"))

layout_line2.addWidget(lb_Question, alignment= (Qt.AlignHCentre | Qt.AlignVCentre))
layout_line3.addWidget(radio_Group)
layout_line3.addWidget(ans_Group_Box)

layout_line4.addWidget(btn_Answer, alignment= (Qt.AlignHCentre | Qt.AlignVCentre))

layout_card = QVBoxLayout()
layout_card.addLayout(layout_line1, strech = 1)
layout_card.addLayout(layout_line2, strech = 1)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, strech = 6)
layout_card.addStretch(1)
layout_card.addLayout(layout_line4, strech = 1)

def show_result():
    radio_Group.hide()
    ans_Group_Box.show()
    btn_Answer.setText("Далі")

def show_question():
    radio_Group.show()
    ans_Group_Box.hide()
    btn_Answer.setText("Відповісти")
    radio_Answer.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    radio_Answer.setExclusive(True):
