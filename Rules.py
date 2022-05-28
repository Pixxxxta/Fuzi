from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
import matplotlib.pyplot as plt
import numpy as np

Form, Window = uic.loadUiType("fuzi.ui")

app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
window.show()

app.exec()


S = 0
H = 0
A = 0
DY = 0
HB = 0


def on_click1():
    print(age(), hb(), dyspnea(), head(), sim())
    y = hazi(int(age()), int(hb()), dyspnea(), head(), sim())
    print('- - - - ')
    graph(y)


def on_click():
    if gr1_is_checked() and gr2_is_checked() and gr3_is_checked() and l1_is_checked() and l2_is_checked():
        print(age(), hb(), dyspnea(), head(), sim())
        y = hazi(int(age()), int(hb()), dyspnea(), head(), sim())
        print('- - - - ')
        graph(y)
    else:
        form.label_6.setText("Вы ввели что-то не то")


def gr1_is_checked():
    if form.radioButton_2.isChecked() or form.radioButton.isChecked():
        return True
    else:
        return False


def gr2_is_checked():
    if form.radioButton_3.isChecked() or form.radioButton_4.isChecked():
        return True
    else:
        return False


def gr3_is_checked():
    if form.radioButton_5.isChecked() or form.radioButton_6.isChecked():
        return True
    else:
        return False


def l1_is_checked():
    if form.lineEdit.text().isnumeric():
        return True
    else:
        return False


def l2_is_checked():
    if form.lineEdit_2.text().isnumeric():
        return True
    else:
        return False


def sim():
    if form.radioButton.isChecked():
        S = 0
        return S
    if form.radioButton_2.isChecked():
        S = 1
        return S


def head():
    if form.radioButton_3.isChecked():
        H = 1
        return H
    if form.radioButton_4.isChecked():
        H = 0
        return H


def dyspnea():
    if form.radioButton_5.isChecked():
        DY = 1
        return DY
    if form.radioButton_6.isChecked():
        DY = 0
        return DY


def age():
    A = form.lineEdit_2.text()
    return A


def hb():
    HB = form.lineEdit.text()
    return HB


def hazi(A, HB, DY, H, S):
    print(A, HB, DY, H, S)

    def left(a, b, x):
        if x <= a:
            return 1
        if x >= b:
            return 0
        return (b - x) / (b - a)

    def right(a, b, x):
        if x <= a:
            return 0
        if x >= b:
            return 1
        return (x - a) / (b - a)

    def S_yes(x):
        return left(0, 1, x)

    def S_no(x):
        return right(0, 1, x)

    def H_yes(x):
        return right(0, 1, x)

    def H_no(x):
        return left(0, 1, x)

    def A_young(x):
        return left(12, 18, x)

    def A_old(x):
        return right(12, 18, x)

    def DY_yes(x):
        return right(0, 1, x)

    def DY_no(x):
        return left(0, 1, x)

    def HB_norm(x):
        return left(90, 100, x)

    def HB_bad(x):
        return right(90, 100, x)

    rules = []
    rules.append(["S_no", "H_yes", "A_old", 'DY_yes', "HB_bad", 4])
    rules.append(["S_no", "H_yes", "A_old", 'DY_yes', "HB_norm", 3])
    rules.append(["S_no", "H_yes", "A_old", 'DY_no', "HB_bad", 3])
    rules.append(["S_no", "H_yes", "A_old", 'DY_no', "HB_norm", 2])
    rules.append(["S_no", "H_yes", "A_young", 'DY_yes', "HB_bad", 3])
    rules.append(["S_no", "H_yes", "A_young", 'DY_yes', "HB_norm", 2])
    rules.append(["S_no", "H_yes", "A_young", 'DY_no', "HB_bad", 2])
    rules.append(["S_no", "H_yes", "A_young", 'DY_no', "HB_norm", 1])
    rules.append(["S_no", "H_no", "A_old", 'DY_yes', "HB_bad", 3])
    rules.append(["S_no", "H_no", "A_old", 'DY_yes', "HB_norm", 2])
    rules.append(["S_no", "H_no", "A_old", 'DY_no', "HB_bad", 2])
    rules.append(["S_no", "H_no", "A_old", 'DY_no', "HB_norm", 2])
    rules.append(["S_no", "H_no", "A_young", 'DY_yes', "HB_bad", 3])
    rules.append(["S_no", "H_no", "A_young", 'DY_yes', "HB_norm", 2])
    rules.append(["S_no", "H_no", "A_young", 'DY_no', "HB_bad", 2])
    rules.append(["S_no", "H_no", "A_young", 'DY_no', "HB_norm", 1])
    rules.append(["S_yes", "H_yes", "A_old", 'DY_yes', "HB_bad", 3])
    rules.append(["S_yes", "H_yes", "A_old", 'DY_yes', "HB_norm", 2])
    rules.append(["S_yes", "H_yes", "A_old", 'DY_no', "HB_bad", 2])
    rules.append(["S_yes", "H_yes", "A_old", 'DY_no', "HB_norm", 1])
    rules.append(["S_yes", "H_yes", "A_young", 'DY_yes', "HB_bad", 2])
    rules.append(["S_yes", "H_yes", "A_young", 'DY_yes', "HB_norm", 1])
    rules.append(["S_yes", "H_yes", "A_young", 'DY_no', "HB_bad", 1])
    rules.append(["S_yes", "H_yes", "A_young", 'DY_no', "HB_norm", 0])
    rules.append(["S_yes", "H_no", "A_old", 'DY_yes', "HB_bad", 2])
    rules.append(["S_yes", "H_no", "A_old", 'DY_yes', "HB_norm", 1])
    rules.append(["S_yes", "H_no", "A_old", 'DY_no', "HB_bad", 1])
    rules.append(["S_yes", "H_no", "A_old", 'DY_no', "HB_norm", 1])
    rules.append(["S_yes", "H_no", "A_young", 'DY_yes', "HB_bad", 2])
    rules.append(["S_yes", "H_no", "A_young", 'DY_yes', "HB_norm", 1])
    rules.append(["S_yes", "H_no", "A_young", 'DY_no', "HB_bad", 1])
    rules.append(["S_yes", "H_no", "A_young", 'DY_no', "HB_norm", 0])

    def S_is(x):
        if x == 'S_yes':
            return S_yes(S)
        else:
            return S_no(S)

    def H_is(x):
        if x == 'H_yes':
            return H_yes(H)
        else:
            return H_no(H)

    def A_is(x):
        if x == 'A_old':
            return A_old(A)
        else:
            return A_young(A)

    def DY_is(x):
        if x == 'DY_yes':
            return DY_yes(DY)
        else:
            return DY_no(DY)

    def HB_is(x):
        if x == 'HB_norm':
            return HB_norm(HB)
        else:
            return HB_bad(HB)

    a = []
    for i in range(32):
        a.append(S_is(rules[i][0]))
        a.append(H_is(rules[i][1]))
        a.append(A_is(rules[i][2]))
        a.append(DY_is(rules[i][3]))
        a.append(HB_is(rules[i][4]))

    c = []
    for i in range(32):
        b = []
        b.append(a[i * 5 + 0])
        b.append(a[i * 5 + 1])
        b.append(a[i * 5 + 2])
        b.append(a[i * 5 + 3])
        b.append(a[i * 5 + 4])
        c.append(min(b))

    sum_numerator = 0
    sum_denominator = 0
    for i in range(32):
        sum_numerator += c[i] * rules[i][5]
        sum_denominator += c[i]

    result = sum_numerator / sum_denominator

    if result <= 1:
        form.label_6.setText("У вас нет тахикардии " + str(result))
    elif result <= 2:
        form.label_6.setText("У вас скорее всего нет тахикардии " + str(result))
    elif result <= 3:
        form.label_6.setText("У вас скорее всего есть тахикардия " + str(result))
    elif result <= 4:
        form.label_6.setText("У вас есть тахикардия " + str(result))
    gr = [DY_yes(DY), HB_bad(HB), A_old(A), S_no(S), H_yes(H)]
    return gr


def graph(y):
    x_list = list(range(0, 5))
    y1_list = y
    x_indexes = np.arange(len(x_list))
    plt.title("График")

    plt.xticks(x_indexes, ["Одышка", "Пульс", "Возраст", "Симуляторы", "Голова"])
    plt.bar(x_list, y1_list, label="значения")
    plt.legend()
    plt.show()


form.pushButton.clicked.connect(on_click)

app.exec()
