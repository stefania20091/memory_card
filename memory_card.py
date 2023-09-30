from PyQt5.QtCore import Qt 
from PyQt5.OtWidget import( 
    QApplication, QWidget, QTableWidget, QListWidget, 
     QLineEdit, QFormLoyout, QHBoxLayout, 
      QVBoxLayout, QGroupBox, QButtonGroup, 
      QPushButton, QLabel, QRadioButton, QSpinBox) 
from memo_cart import*

list_question = QListView()
widget_ans = QWidget()
widget-ans.setLayout(layout_form)
btn_add = QPushButton("нове запитання")
btn_del = QPushButton("видалити")
btn_start = QPushButton("Початок тесту")

qst_col = QVBoxLayout()#question collume(стовпчик з питаннями)
qst.col.addWidget(btn_add)
qst_col.addWidget(list_question)

ans_col = QVBoxLayout()
ans.col.addWidget(widget_ans)
ans.col.addWidget(btn_del)

btn_line = QHBoxLayout()
btn_line.addLayout(qst_col)
btn_line.addLayout(ans_col)

test_line = QHBoxLayout()
test_line.addStretch(1)
test_line.addWidget(btn_start, stretch = 2)
test_line.addStretch(1)

layout_screen = QVBoxLayout()
layout_screen. addLayout(test_line)
