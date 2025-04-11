import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLineEdit, QLabel, QWidget, QMessageBox, QVBoxLayout, QTextEdit, QPushButton
import cmath as cmt
import math
import matplotlib.pyplot as plt


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        # Создаём кнопки калькулятора, поля ввода и вывода
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1021, 736)
        font = QtGui.QFont()
        font.setFamily("Liberation Serif")
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.Clear = QtWidgets.QPushButton(parent=self.centralwidget)
        self.Clear.setGeometry(QtCore.QRect(840, 240, 91, 91))
        font = QtGui.QFont()
        font.setFamily("Liberation Serif")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.Clear.setFont(font)
        self.Clear.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        self.Clear.setObjectName("Clear")

        self.num3 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.num3.setGeometry(QtCore.QRect(840, 330, 91, 91))
        font = QtGui.QFont()
        font.setFamily("Liberation Serif")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.num3.setFont(font)
        self.num3.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        self.num3.setObjectName("num3")

        self.num2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.num2.setGeometry(QtCore.QRect(750, 330, 91, 91))
        font = QtGui.QFont()
        font.setFamily("Liberation Serif")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.num2.setFont(font)
        self.num2.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        self.num2.setObjectName("num2")

        self.num6 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.num6.setGeometry(QtCore.QRect(840, 420, 91, 91))
        font = QtGui.QFont()
        font.setFamily("Liberation Serif")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.num6.setFont(font)
        self.num6.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        self.num6.setObjectName("num6")

        self.num5 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.num5.setGeometry(QtCore.QRect(750, 420, 91, 91))
        font = QtGui.QFont()
        font.setFamily("Liberation Serif")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.num5.setFont(font)
        self.num5.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        self.num5.setObjectName("num5")

        self.sqrt = QtWidgets.QPushButton(parent=self.centralwidget)
        self.sqrt.setGeometry(QtCore.QRect(660, 240, 91, 91))
        font = QtGui.QFont()
        font.setFamily("Liberation Serif")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.sqrt.setFont(font)
        self.sqrt.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        self.sqrt.setObjectName("sqrt")

        self.num1 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.num1.setGeometry(QtCore.QRect(660, 330, 91, 91))
        font = QtGui.QFont()
        font.setFamily("Liberation Serif")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.num1.setFont(font)
        self.num1.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        self.num1.setObjectName("num1")

        self.num4 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.num4.setGeometry(QtCore.QRect(660, 420, 91, 91))
        font = QtGui.QFont()
        font.setFamily("Liberation Serif")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.num4.setFont(font)
        self.num4.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        self.num4.setObjectName("num4")

        self.sin = QtWidgets.QPushButton(parent=self.centralwidget)
        self.sin.setGeometry(QtCore.QRect(570, 240, 91, 91))
        font = QtGui.QFont()
        font.setFamily("Liberation Serif")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.sin.setFont(font)
        self.sin.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        self.sin.setObjectName("sin")

        self.degree = QtWidgets.QPushButton(parent=self.centralwidget)
        self.degree.setGeometry(QtCore.QRect(750, 240, 91, 91))
        font = QtGui.QFont()
        font.setFamily("Liberation Serif")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.degree.setFont(font)
        self.degree.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        self.degree.setObjectName("degree")

        self.degree1 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.degree1.setGeometry(QtCore.QRect(390, 240, 91, 91))
        font = QtGui.QFont()
        font.setFamily("Liberation Serif")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.degree1.setFont(font)
        self.degree1.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        self.degree1.setObjectName("degree1")

        self.cos = QtWidgets.QPushButton(parent=self.centralwidget)
        self.cos.setGeometry(QtCore.QRect(570, 330, 91, 91))
        font = QtGui.QFont()
        font.setFamily("Liberation Serif")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.cos.setFont(font)
        self.cos.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        self.cos.setObjectName("cos")

        self.tan = QtWidgets.QPushButton(parent=self.centralwidget)
        self.tan.setGeometry(QtCore.QRect(570, 420, 91, 91))
        font = QtGui.QFont()
        font.setFamily("Liberation Serif")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.tan.setFont(font)
        self.tan.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        self.tan.setObjectName("tan")

        self.num7 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.num7.setGeometry(QtCore.QRect(660, 510, 91, 91))
        font = QtGui.QFont()
        font.setFamily("Liberation Serif")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.num7.setFont(font)
        self.num7.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        self.num7.setObjectName("num7")

        self.num8 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.num8.setGeometry(QtCore.QRect(750, 510, 91, 91))
        font = QtGui.QFont()
        font.setFamily("Liberation Serif")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.num8.setFont(font)
        self.num8.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        self.num8.setObjectName("num8")

        self.num9 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.num9.setGeometry(QtCore.QRect(840, 510, 91, 91))
        font = QtGui.QFont()
        font.setFamily("Liberation Serif")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.num9.setFont(font)
        self.num9.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        self.num9.setObjectName("num9")

        self.natural_log = QtWidgets.QPushButton(parent=self.centralwidget)
        self.natural_log.setGeometry(QtCore.QRect(570, 510, 91, 91))
        font = QtGui.QFont()
        font.setFamily("Liberation Serif")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.natural_log.setFont(font)
        self.natural_log.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        self.natural_log.setObjectName("natural_log")

        self.equals = QtWidgets.QPushButton(parent=self.centralwidget)
        self.equals.setGeometry(QtCore.QRect(840, 600, 91, 91))
        font = QtGui.QFont()
        font.setFamily("Liberation Serif")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.equals.setFont(font)
        self.equals.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        self.equals.setObjectName("equals")

        self.num0 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.num0.setGeometry(QtCore.QRect(750, 600, 91, 91))
        font = QtGui.QFont()
        font.setFamily("Liberation Serif")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.num0.setFont(font)
        self.num0.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        self.num0.setObjectName("num0")

        self.instruction = QtWidgets.QPushButton(parent=self.centralwidget)
        self.instruction.setGeometry(QtCore.QRect(800, 10, 200, 30))
        font = QtGui.QFont()
        font.setFamily("Liberation Serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.instruction.setFont(font)
        self.instruction.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        self.instruction.setObjectName("инструкция")

        self.graph = QtWidgets.QPushButton(parent=self.centralwidget)
        self.graph.setGeometry(QtCore.QRect(20, 500, 300, 30))
        font = QtGui.QFont()
        font.setFamily("Liberation Serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.graph.setFont(font)
        self.graph.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        self.graph.setObjectName("построение чисел на плоскости")

        self.conjugate = QtWidgets.QPushButton(parent=self.centralwidget)
        self.conjugate.setGeometry(QtCore.QRect(660, 600, 91, 91))
        font = QtGui.QFont()
        font.setFamily("Liberation Serif")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.conjugate.setFont(font)
        self.conjugate.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        self.conjugate.setObjectName("conjugate")

        self.log = QtWidgets.QPushButton(parent=self.centralwidget)
        self.log.setGeometry(QtCore.QRect(570, 600, 91, 91))
        font = QtGui.QFont()
        font.setFamily("Liberation Serif")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.log.setFont(font)
        self.log.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        self.log.setObjectName("log")

        self.Clear1elem = QtWidgets.QPushButton(parent=self.centralwidget)
        self.Clear1elem.setGeometry(QtCore.QRect(930, 240, 91, 91))
        font = QtGui.QFont()
        font.setFamily("Liberation Serif")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.Clear1elem.setFont(font)
        self.Clear1elem.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        self.Clear1elem.setObjectName("Clear1elem")

        self.addition = QtWidgets.QPushButton(parent=self.centralwidget)
        self.addition.setGeometry(QtCore.QRect(930, 330, 91, 91))
        font = QtGui.QFont()
        font.setFamily("Liberation Serif")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.addition.setFont(font)
        self.addition.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        self.addition.setObjectName("addition")

        self.substraction = QtWidgets.QPushButton(parent=self.centralwidget)
        self.substraction.setGeometry(QtCore.QRect(930, 420, 91, 91))
        font = QtGui.QFont()
        font.setFamily("Liberation Serif")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.substraction.setFont(font)
        self.substraction.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        self.substraction.setObjectName("substraction")

        self.multiplic = QtWidgets.QPushButton(parent=self.centralwidget)
        self.multiplic.setGeometry(QtCore.QRect(930, 510, 91, 91))
        font = QtGui.QFont()
        font.setFamily("Liberation Serif")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.multiplic.setFont(font)
        self.multiplic.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        self.multiplic.setObjectName("multiplic")

        self.div = QtWidgets.QPushButton(parent=self.centralwidget)
        self.div.setGeometry(QtCore.QRect(930, 600, 91, 91))
        font = QtGui.QFont()
        font.setFamily("Liberation Serif")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.div.setFont(font)
        self.div.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        self.div.setObjectName("div")

        self.atan = QtWidgets.QPushButton(parent=self.centralwidget)
        self.atan.setGeometry(QtCore.QRect(480, 420, 91, 91))
        font = QtGui.QFont()
        font.setFamily("Liberation Serif")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.atan.setFont(font)
        self.atan.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        self.atan.setObjectName("atan")

        self.Greatest_common_divisor = QtWidgets.QPushButton(parent=self.centralwidget)
        self.Greatest_common_divisor.setGeometry(QtCore.QRect(390, 330, 91, 91))
        font = QtGui.QFont()
        font.setFamily("Liberation Serif")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.Greatest_common_divisor.setFont(font)
        self.Greatest_common_divisor.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        self.Greatest_common_divisor.setObjectName("Greatest_common_divisor")

        self.norm = QtWidgets.QPushButton(parent=self.centralwidget)
        self.norm.setGeometry(QtCore.QRect(480, 600, 91, 91))
        font = QtGui.QFont()
        font.setFamily("Liberation Serif")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.norm.setFont(font)
        self.norm.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        self.norm.setObjectName("norm")

        self.asin = QtWidgets.QPushButton(parent=self.centralwidget)
        self.asin.setGeometry(QtCore.QRect(480, 240, 91, 91))
        font = QtGui.QFont()
        font.setFamily("Liberation Serif")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.asin.setFont(font)
        self.asin.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        self.asin.setObjectName("asin")

        self.acos = QtWidgets.QPushButton(parent=self.centralwidget)
        self.acos.setGeometry(QtCore.QRect(480, 330, 91, 91))
        font = QtGui.QFont()
        font.setFamily("Liberation Serif")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.acos.setFont(font)
        self.acos.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        self.acos.setObjectName("acos")

        self.arg = QtWidgets.QPushButton(parent=self.centralwidget)
        self.arg.setGeometry(QtCore.QRect(390, 510, 91, 91))
        font = QtGui.QFont()
        font.setFamily("Liberation Serif")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.arg.setFont(font)
        self.arg.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        self.arg.setObjectName("arg")

        self.module = QtWidgets.QPushButton(parent=self.centralwidget)
        self.module.setGeometry(QtCore.QRect(480, 510, 91, 91))
        font = QtGui.QFont()
        font.setFamily("Liberation Serif")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.module.setFont(font)
        self.module.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        self.module.setObjectName("module")

        self.del_all = QtWidgets.QPushButton(parent=self.centralwidget)
        self.del_all.setGeometry(QtCore.QRect(390, 600, 91, 91))
        font = QtGui.QFont()
        font.setFamily("Liberation Serif")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.del_all.setFont(font)
        self.del_all.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        self.del_all.setObjectName("dot")

        self.pi = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pi.setGeometry(QtCore.QRect(390, 420, 91, 91))
        font = QtGui.QFont()
        font.setFamily("Liberation Serif")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.pi.setFont(font)
        self.pi.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        self.pi.setObjectName("pi")

        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 550, 360, 91))
        font = QtGui.QFont()
        font.setFamily("Liberation Serif")
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")



        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 20, 441, 91))
        font = QtGui.QFont()
        font.setFamily("Liberation Serif")
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:rgb(200, 200, 200)")
        self.label_2.setObjectName("label_2")

        self.add_n1 = QtWidgets.QLabel(parent=self.centralwidget)
        self.add_n1.setGeometry(QtCore.QRect(700, 40, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.add_n1.setFont(font)
        self.add_n1.setObjectName("add_n1")

        self.add_n2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.add_n2.setGeometry(QtCore.QRect(700, 100, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.add_n2.setFont(font)
        self.add_n2.setObjectName("add_n2")

        self.imag_1 = QtWidgets.QLabel(parent=self.centralwidget)
        self.imag_1.setGeometry(QtCore.QRect(830, 40, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.imag_1.setFont(font)
        self.imag_1.setObjectName("imag_1")

        self.imag_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.imag_2.setGeometry(QtCore.QRect(830, 100, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.imag_2.setFont(font)
        self.imag_2.setObjectName("imag_2")

        self.im_1 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.im_1.setGeometry(QtCore.QRect(740, 50, 81, 22))
        font = QtGui.QFont()
        font.setFamily("Liberation Serif")
        self.im_1.setFont(font)
        self.im_1.setObjectName("im_1")

        self.line = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.line.setGeometry(QtCore.QRect(690, 200, 320, 30))
        font = QtGui.QFont()
        font.setFamily("Liberation Serif")
        self.line.setFont(font)
        self.line.setObjectName("line")

        self.im_2 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.im_2.setGeometry(QtCore.QRect(740, 110, 81, 22))
        font = QtGui.QFont()
        font.setFamily("Liberation Serif")
        font.setPointSize(8)
        self.im_2.setFont(font)
        self.im_2.setObjectName("im_2")

        self.re_1 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.re_1.setGeometry(QtCore.QRect(600, 50, 81, 22))
        font = QtGui.QFont()
        font.setFamily("Liberation Serif")
        self.re_1.setFont(font)
        self.re_1.setObjectName("re_1")

        self.re_2 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.re_2.setGeometry(QtCore.QRect(600, 110, 81, 22))
        font = QtGui.QFont()
        font.setFamily("Liberation Serif")
        font.setPointSize(8)
        self.re_2.setFont(font)
        self.re_2.setText("")
        self.re_2.setObjectName("re_2")

        self.trig = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.trig.setGeometry(QtCore.QRect(20, 620, 281, 60))
        font = QtGui.QFont()
        font.setFamily("Liberation Serif")
        self.trig.setFont(font)
        self.trig.setObjectName("trig")

        self.comp_1 = QtWidgets.QLabel(parent=self.centralwidget)
        self.comp_1.setGeometry(QtCore.QRect(530, 50, 21, 16))
        self.comp_1.setObjectName("comp_1")

        self.comp_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.comp_2.setGeometry(QtCore.QRect(530, 110, 21, 16))
        self.comp_2.setObjectName("comp_2")

        self.eq_1 = QtWidgets.QLabel(parent=self.centralwidget)
        self.eq_1.setGeometry(QtCore.QRect(570, 50, 21, 16))
        self.eq_1.setObjectName("eq_1")

        self.eq_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.eq_2.setGeometry(QtCore.QRect(570, 110, 21, 16))
        self.eq_2.setObjectName("eq_2")

        self.add_n3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.add_n3.setGeometry(QtCore.QRect(700, 160, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.add_n3.setFont(font)
        self.add_n3.setObjectName("add_n3")

        self.re_3 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.re_3.setGeometry(QtCore.QRect(600, 170, 81, 22))
        font = QtGui.QFont()
        font.setFamily("Liberation Serif")
        font.setPointSize(8)
        self.re_3.setFont(font)
        self.re_3.setText("")
        self.re_3.setObjectName("re_3")

        self.eq_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.eq_3.setGeometry(QtCore.QRect(570, 170, 21, 16))
        self.eq_3.setObjectName("eq_3")

        self.comp_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.comp_3.setGeometry(QtCore.QRect(530, 170, 21, 16))
        self.comp_3.setObjectName("comp_3")

        self.imag_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.imag_3.setGeometry(QtCore.QRect(830, 160, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.imag_3.setFont(font)
        self.imag_3.setObjectName("imag_3")

        self.im_3 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.im_3.setGeometry(QtCore.QRect(740, 170, 81, 22))
        font = QtGui.QFont()
        font.setFamily("Liberation Serif")
        font.setPointSize(8)
        self.im_3.setFont(font)
        self.im_3.setObjectName("im_3")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1021, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        # Делаем надписи на кнопках и в QLabel
        MainWindow.setWindowTitle(_translate("MainWindow", "Калькулятор с использованием комплексных чисел"))
        self.Clear.setText(_translate("MainWindow", "CE"))
        self.num3.setText(_translate("MainWindow", "3"))
        self.num2.setText(_translate("MainWindow", "2"))
        self.num6.setText(_translate("MainWindow", "6"))
        self.num5.setText(_translate("MainWindow", "5"))
        self.sqrt.setText(_translate("MainWindow", "√"))
        self.num1.setText(_translate("MainWindow", "1"))
        self.num4.setText(_translate("MainWindow", "4"))
        self.sin.setText(_translate("MainWindow", "sin()"))
        self.degree.setText(_translate("MainWindow", "^2"))
        self.degree1.setText(_translate("MainWindow", "^3"))
        self.cos.setText(_translate("MainWindow", "cos()"))
        self.tan.setText(_translate("MainWindow", "tan()"))
        self.num7.setText(_translate("MainWindow", "7"))
        self.num8.setText(_translate("MainWindow", "8"))
        self.num9.setText(_translate("MainWindow", "9"))
        self.natural_log.setText(_translate("MainWindow", "lg10"))
        self.equals.setText(_translate("MainWindow", "="))
        self.num0.setText(_translate("MainWindow", "0"))
        self.instruction.setText(_translate("MainWindow", "Инструкция"))
        self.graph.setText(_translate("MainWindow", "Построение чисел на плоскости"))
        self.conjugate.setText(_translate("MainWindow", " z ¯"))
        self.log.setText(_translate("MainWindow", "log"))
        self.Clear1elem.setText(_translate("MainWindow", "<="))
        self.line.setText(_translate("MainWindow", ""))
        self.addition.setText(_translate("MainWindow", "+"))
        self.substraction.setText(_translate("MainWindow", "-"))
        self.multiplic.setText(_translate("MainWindow", "*"))
        self.div.setText(_translate("MainWindow", "/"))
        self.atan.setText(_translate("MainWindow", "atan()"))
        self.Greatest_common_divisor.setText(_translate("MainWindow", "НОД()"))
        self.norm.setText(_translate("MainWindow", "N(z)"))
        self.asin.setText(_translate("MainWindow", "asin()"))
        self.acos.setText(_translate("MainWindow", "acos()"))
        self.arg.setText(_translate("MainWindow", "arg"))
        self.module.setText(_translate("MainWindow", "|z|"))
        self.del_all.setText(_translate("MainWindow", "Del_all"))
        self.pi.setText(_translate("MainWindow", "π"))
        self.label_2.setText(_translate("MainWindow", "TextLabel"))
        self.label_3.setText(_translate("MainWindow", "Тригонометрическая форма записи числа:"))
        self.add_n1.setText(_translate("MainWindow", "+"))
        self.add_n1.setText(_translate("MainWindow", "+"))
        self.add_n2.setText(_translate("MainWindow", "+"))
        self.imag_1.setText(_translate("MainWindow", "i"))
        self.imag_2.setText(_translate("MainWindow", "i"))
        self.comp_1.setText(_translate("MainWindow", "z1"))
        self.comp_2.setText(_translate("MainWindow", "z2"))
        self.eq_1.setText(_translate("MainWindow", "="))
        self.eq_2.setText(_translate("MainWindow", "="))
        self.add_n3.setText(_translate("MainWindow", "+"))
        self.eq_3.setText(_translate("MainWindow", "="))
        self.comp_3.setText(_translate("MainWindow", "z3"))
        self.imag_3.setText(_translate("MainWindow", "i"))


class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # Делаем кликабельными все кнопки
        self.ui.num0.clicked.connect(lambda: self.Number(0))
        self.ui.num1.clicked.connect(lambda: self.Number(1))
        self.ui.num2.clicked.connect(lambda: self.Number(2))
        self.ui.num3.clicked.connect(lambda: self.Number(3))
        self.ui.num4.clicked.connect(lambda: self.Number(4))
        self.ui.num5.clicked.connect(lambda: self.Number(5))
        self.ui.num6.clicked.connect(lambda: self.Number(6))
        self.ui.num7.clicked.connect(lambda: self.Number(7))
        self.ui.num8.clicked.connect(lambda: self.Number(8))
        self.ui.num9.clicked.connect(lambda: self.Number(9))
        self.ui.pi.clicked.connect(lambda: self.Number(3.14))
        self.ui.Clear.clicked.connect(self.Clearr)
        self.ui.equals.clicked.connect(self.Equals)
        self.ui.log.clicked.connect(self.Log)
        self.ui.natural_log.clicked.connect(self.Lg10)
        self.ui.sin.clicked.connect(self.Sin)
        self.ui.cos.clicked.connect(self.Cos)
        self.ui.tan.clicked.connect(self.Tan)
        self.ui.asin.clicked.connect(self.Arcsin)
        self.ui.acos.clicked.connect(self.Arccos)
        self.ui.atan.clicked.connect(self.Arctan)
        self.ui.sqrt.clicked.connect(self.Sqrt)
        self.ui.Clear1elem.clicked.connect(self.Delete1elem)
        self.ui.addition.clicked.connect(self.Add)
        self.ui.multiplic.clicked.connect(self.Mul)
        self.ui.substraction.clicked.connect(self.Sub)
        self.ui.div.clicked.connect(self.Div)
        self.ui.degree.clicked.connect(self.Degree)
        self.ui.norm.clicked.connect(self.Norma)
        self.ui.conjugate.clicked.connect(self.Con)
        self.ui.module.clicked.connect(self.Mod)
        self.ui.arg.clicked.connect(self.Argument)
        self.ui.Greatest_common_divisor.clicked.connect(self.NOD)
        self.ui.del_all.clicked.connect(self.Delall)
        self.ui.degree1.clicked.connect(self.Degree1)
        self.ui.instruction.clicked.connect(self.Rules)
        self.ui.graph.clicked.connect(self.Graphik)

        # Выводим картинку
        self.image = "complex2.png"
        self.lbl = QLabel(self)
        self.lbl.setPixmap(QPixmap(self.image))
        self.lbl.setGeometry(10, 150, 360, 300)
        self.show()

    def Equals(self):
        # Делаем так, что при нажатии этой кнопки, написанное перемещается в label_2
        self.ui.label_2.setText(self.ui.line.text())
        self.ui.line.clear()

    def Clearr(self):
        # Очищает значение в line
        self.ui.line.clear()

    def Delall(self):
        # При нажатии очищаются все поля
        self.ui.line.clear()
        self.ui.im_1.clear()
        self.ui.re_1.clear()
        self.ui.im_2.clear()
        self.ui.re_2.clear()
        self.ui.im_3.clear()
        self.ui.re_3.clear()
        self.ui.trig.clear()


    def Number(self, num):
        # Создаём функцию для вывода в поле line цифр
        x = str(num)
        self.ui.line.setText(self.ui.line.text() + x)

    def Log(self):
        try:
            text = self.ui.line.text()
            # Для того, чтобы нужно было вводить обязательно комплексные числа
            value1 = self._parse_complex(text)
            c = cmt.log(value1)
            print(c)
            self.ui.line.setText(str(c))
            # Предотвращает ошибки
        except ValueError as e:
            QMessageBox.warning(self, "Ошибка", f"Неверный формат числа: {e}")
        except Exception as e:
            QMessageBox.warning(self, "Ошибка", f"Произошла ошибка: {e}")


    def Lg10(self):
        try:
            text = self.ui.line.text()
            # Для того, чтобы нужно было вводить обязательно комплексные числа
            value1 = self._parse_complex(text)
            c = cmt.log10(value1)
            print(c)
            self.ui.line.setText(str(c))
            # Предотвращает ошибки
        except ValueError:
            QMessageBox.warning(self, "Ошибка", "Пожалуйста, введите числа!")
        except Exception as e:  # Обработка других возможных ошибок
            QMessageBox.warning(self, "Ошибка", f"Произошла ошибка: {e}")

    def Sin(self):
        try:
            text = self.ui.line.text()
            # Для того, чтобы нужно было вводить обязательно комплексные числа
            value1 = self._parse_complex(text)
            c = cmt.sin(value1)
            print(c)
            self.ui.line.setText(str(c))
            # Предотвращает ошибки
        except ValueError:
            QMessageBox.warning(self, "Ошибка", "Пожалуйста, введите числа!")
        except Exception as e:  # Обработка других возможных ошибок
            QMessageBox.warning(self, "Ошибка", f"Произошла ошибка: {e}")

    def Cos(self):
        try:
            text = self.ui.line.text()
            # Для того, чтобы нужно было вводить обязательно комплексные числа
            value1 = self._parse_complex(text)
            c = cmt.cos(value1)
            print(c)
            self.ui.line.setText(str(c))
            # Предотвращает ошибки
        except ValueError:
            QMessageBox.warning(self, "Ошибка", "Пожалуйста, введите числа!")
        except Exception as e:  # Обработка других возможных ошибок
            QMessageBox.warning(self, "Ошибка", f"Произошла ошибка: {e}")

    def Tan(self):
        try:
            text = self.ui.line.text()
            # Для того, чтобы нужно было вводить обязательно комплексные числа
            value1 = self._parse_complex(text)
            c = cmt.tan(value1)
            print(c)
            self.ui.line.setText(str(c))
            # Предотвращает ошибки
        except ValueError:
            QMessageBox.warning(self, "Ошибка", "Пожалуйста, введите числа!")
        except Exception as e:  # Обработка других возможных ошибок
            QMessageBox.warning(self, "Ошибка", f"Произошла ошибка: {e}")

    def Arcsin(self):
        try:
            text = self.ui.line.text()
            # Для того, чтобы нужно было вводить обязательно комплексные числа
            value1 = self._parse_complex(text)
            c = cmt.asin(value1)
            print(c)
            self.ui.line.setText(str(c))
            # Предотвращает ошибки
        except ValueError:
            QMessageBox.warning(self, "Ошибка", "Пожалуйста, введите числа!")
        except Exception as e:  # Обработка других возможных ошибок
            QMessageBox.warning(self, "Ошибка", f"Произошла ошибка: {e}")

    def Arccos(self):
        try:
            text = self.ui.line.text()
            # Для того, чтобы нужно было вводить обязательно комплексные числа
            value1 = self._parse_complex(text)
            c = cmt.acos(value1)
            print(c)
            self.ui.line.setText(str(c))
            # Предотвращает ошибки
        except ValueError:
            QMessageBox.warning(self, "Ошибка", "Пожалуйста, введите числа!")
        except Exception as e:  # Обработка других возможных ошибок
            QMessageBox.warning(self, "Ошибка", f"Произошла ошибка: {e}")

    def Arctan(self):
        try:
            text = self.ui.line.text()
            # Для того, чтобы нужно было вводить обязательно комплексные числа
            value1 = self._parse_complex(text)
            c = cmt.atan(value1)
            print(c)
            self.ui.line.setText(str(c))
            # Предотвращает ошибки
        except ValueError:
            QMessageBox.warning(self, "Ошибка", "Пожалуйста, введите числа!")
        except Exception as e:  # Обработка других возможных ошибок
            QMessageBox.warning(self, "Ошибка", f"Произошла ошибка: {e}")

    def Sqrt(self):
        try:
            text = self.ui.line.text()
            # Для того, чтобы нужно было вводить обязательно комплексные числа
            value1 = self._parse_complex(text)
            c = cmt.sqrt(value1)
            print(c)
            self.ui.line.setText(str(c))
            # Предотвращает ошибки
        except ValueError:
            QMessageBox.warning(self, "Ошибка", "Пожалуйста, введите числа!")
        except Exception as e:  # Обработка других возможных ошибок
            QMessageBox.warning(self, "Ошибка", f"Произошла ошибка: {e}")

    def Delete1elem(self):
        s = self.ui.line.text()
        s = s[:-1]
        self.ui.line.setText(s)

    def Add(self):
        try:
            value1 = float(self.ui.im_1.text())  # Преобразуем в число с плавающей точкой
            value2 = float(self.ui.im_2.text()) # Аналогично для второго поля ввода
            value3 = float(self.ui.re_1.text())
            value4 = float(self.ui.re_2.text())
            result1 = value1 + value2
            result2 = value3 + value4
            self.ui.im_3.setText(str(result1))# Выводим результат
            self.ui.re_3.setText(str(result2))
            # Предотвращает ошибки
        except ValueError:
            QMessageBox.warning(self, "Ошибка", "Пожалуйста, введите числа!")
        except Exception as e:  # Обработка других возможных ошибок
            QMessageBox.warning(self, "Ошибка", f"Произошла ошибка: {e}")

    def Mul(self):
        try:
            value1 = float(self.ui.im_1.text())
            value2 = float(self.ui.im_2.text())
            value3 = float(self.ui.re_1.text())
            value4 = float(self.ui.re_2.text())
            result1 = value3 * value4 - value1 * value2
            result2 = value3 * value2 + value4 * value1
            self.ui.im_3.setText(str(result2))  # Выводим результат
            self.ui.re_3.setText(str(result1))
            # Предотвращает ошибки
        except ValueError:
            QMessageBox.warning(self, "Ошибка", "Пожалуйста, введите числа!")
        except Exception as e:  # Обработка других возможных ошибок
            QMessageBox.warning(self, "Ошибка", f"Произошла ошибка: {e}")

    def Sub(self):
        try:
            value1 = float(self.ui.im_1.text())  # Преобразуем в число с плавающей точкой
            value2 = float(self.ui.im_2.text())  # Аналогично для второго поля ввода
            value3 = float(self.ui.re_1.text())
            value4 = float(self.ui.re_2.text())
            result1 = value1 - value2
            result2 = value3 - value4
            self.ui.im_3.setText(str(result1))  # Выводим результат
            self.ui.re_3.setText(str(result2))
            # Предотвращает ошибки
        except ValueError:
            QMessageBox.warning(self, "Ошибка", "Пожалуйста, введите числа!")
        except Exception as e:  # Обработка других возможных ошибок
            QMessageBox.warning(self, "Ошибка", f"Произошла ошибка: {e}")

    def Div(self):
        try:
            value1 = float(self.ui.im_1.text())  # Преобразуем в число с плавающей точкой
            value2 = float(self.ui.im_2.text())  # Аналогично для второго поля ввода
            value3 = float(self.ui.re_1.text())
            value4 = float(self.ui.re_2.text())
            result1 = value3 * value4 + value1 * value2
            result2 = value4 ** 2 + value2 ** 2
            result3 = result1 / result2
            result4 = value4 * value1 - value3 * value2
            result5 = result4 / result2
            self.ui.im_3.setText(str(result5))  # Выводим результат
            self.ui.re_3.setText(str(result3))
            # Предотвращает ошибки
        except ValueError:
            QMessageBox.warning(self, "Ошибка", "Пожалуйста, введите числа!")
        except Exception as e:  # Обработка других возможных ошибок
            QMessageBox.warning(self, "Ошибка", f"Произошла ошибка: {e}")

    def Degree(self):
        try:
            value1 = float(self.ui.im_1.text())  # Преобразуем в число с плавающей точкой # Аналогично для второго поля ввода
            value2 = float(self.ui.re_1.text())
            arg = cmt.phase(complex(value2, value1))# Конвертация аргумента в градусы для удобства
            z = ((value2 ** 2 + value1 ** 2) ** 0.5) ** 2
            self.ui.trig.setText(f"{str(z)} (cos({arg * 2}) + j * sin({arg * 2})")
            # Предотвращает ошибки
        except ValueError:
            QMessageBox.warning(self, "Ошибка", "Пожалуйста, введите числа!")
        except Exception as e:  # Обработка других возможных ошибок
            QMessageBox.warning(self, "Ошибка", f"Произошла ошибка: {e}")

    def Degree1(self):
        try:
            value1 = float(self.ui.im_1.text())  # Преобразуем в число с плавающей точкой # Аналогично для второго поля ввода
            value2 = float(self.ui.re_1.text())
            arg = cmt.phase(complex(value2, value1))# Конвертация аргумента в градусы для удобства
            z = ((value2 ** 2 + value1 ** 2) ** 0.5) ** 3
            self.ui.trig.setText(f"{str(z)} (cos({arg * 3}) + j * sin({arg * 3})")
            # Предотвращает ошибки
        except ValueError:
            QMessageBox.warning(self, "Ошибка", "Пожалуйста, введите числа!")
        except Exception as e:  # Обработка других возможных ошибок
            QMessageBox.warning(self, "Ошибка", f"Произошла ошибка: {e}")

    def Norma(self):
        try:
            value1 = float(self.ui.re_1.text())
            value2 = float(self.ui.im_1.text())
            z = value1 ** 2 + value2 ** 2
            self.ui.line.setText(str(z))
            # Предотвращает ошибки
        except ValueError:
            QMessageBox.warning(self, "Ошибка", "Пожалуйста, введите числа!")
        except Exception as e:  # Обработка других возможных ошибок
            QMessageBox.warning(self, "Ошибка", f"Произошла ошибка: {e}")

    def Con(self):
        try:
            value1 = float(self.ui.re_1.text())
            value2 = float(self.ui.im_1.text())
            self.ui.re_3.setText(str(value1))
            self.ui.im_3.setText(str(-1 * value2))
            # Предотвращает ошибки
        except ValueError:
            QMessageBox.warning(self, "Ошибка", "Пожалуйста, введите числа!")
        except Exception as e:  # Обработка других возможных ошибок
            QMessageBox.warning(self, "Ошибка", f"Произошла ошибка: {e}")


    def Mod(self):
        try:
            value1 = float(self.ui.re_1.text())
            value2 = float(self.ui.im_1.text())
            z = (value1 ** 2 + value2 ** 2) ** 0.5
            self.ui.line.setText(str(z))
            # Предотвращает ошибки
        except ValueError:
            QMessageBox.warning(self, "Ошибка", "Пожалуйста, введите числа!")
        except Exception as e:  # Обработка других возможных ошибок
            QMessageBox.warning(self, "Ошибка", f"Произошла ошибка: {e}")

    def Argument(self):
        try:
            value1 = float(self.ui.re_1.text())
            value2 = float(self.ui.im_1.text())
            a = complex(value1, value2)
            c = cmt.phase(a)
            print(c)
            self.ui.line.setText(str(c))
            # Предотвращает ошибки
        except ValueError:
            QMessageBox.warning(self, "Ошибка", "Пожалуйста, введите числа!")
        except Exception as e:  # Обработка других возможных ошибок
            QMessageBox.warning(self, "Ошибка", f"Произошла ошибка: {e}")

    def NOD(self):
        # Вычисляет НОД действительных и мнимых частей комплексных чисел
        # Обрабатывает случаи нецелых чисел, возвращая 1 если возникла ошибка
        try:
            re1 = float(self.ui.re_1.text())  # Действительная часть первого числа
            im1 = float(self.ui.im_1.text())  # Мнимая часть первого числа
            re2 = float(self.ui.re_2.text())  # Действительная часть второго числа
            im2 = float(self.ui.im_2.text())  # Мнимая часть второго числа

            # Обработка нецелых чисел:
            real_gcd = math.gcd(int(re1), int(re2)) if re1.is_integer() and re2.is_integer() else 1
            imag_gcd = math.gcd(int(im1), int(im2)) if im1.is_integer() and im2.is_integer() else 1

            self.ui.line.setText(f"НОД(Действительные): {real_gcd}, НОД(Мнимые): {imag_gcd}")

        except ValueError:
            QMessageBox.warning(self, "Ошибка", "Пожалуйста, введите корректные числа.")
        except Exception as e:
            QMessageBox.warning(self, "Ошибка", f"Произошла ошибка: {e}")


    def Rules(self):
        self.rule = Instruction()
        self.rule.show()

    def Graphik(self):
        self.plane = Complex_plane()
        self.plane.show()


    def _parse_complex(self, text):
        # Парсит строку, пытаясь преобразовать её в вещественное или комплексное число
        text = text.strip()  # Удаляем пробелы

        try:
            return float(text)  # Сначала пытаемся преобразовать в вещественное число
        except ValueError:
            try:
                # Пытаемся преобразовать в комплексное число.  Поддерживаем форматы:
                # 3+2j, 3-2j, 3j, -3j, 3+2J, 3-2J, 3J, -3J
                return complex(text)
            except ValueError:
                raise ValueError(
                    "Неверный формат числа.  Ожидается вещественное или комплексное число (например, '3+2j')")


class Instruction(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Инструкция")
        self.setGeometry(600, 100, 800, 800)

        # Создаем вертикальный layout
        layout = QVBoxLayout()

        # Создаем QTextEdit для отображения текста
        self.rule_text = QTextEdit(self)
        self.rule_text.setReadOnly(True)  # Делаем текстовое поле только для чтения

        # Загружаем содержимое текстового файла
        try:
            with open('Инструкция.txt', 'r', encoding='utf-8') as file:
                content = file.read()
                self.rule_text.setPlainText(content)  # Устанавливаем текст в QTextEdit

                # Увеличиваем размер шрифта в два раза
                font = self.rule_text.font()  # Получаем текущий шрифт
                font.setPointSize(font.pointSize() * 2)  # Увеличиваем размер шрифта в два раза
                self.rule_text.setFont(font)  # Устанавливаем измененный шрифт

        except FileNotFoundError:
            self.rule_text.setPlainText("Файл с инструкциями не найден.")
        except Exception as e:
            self.rule_text.setPlainText(f"Произошла ошибка при загрузке файла: {e}")

        # Добавляем QTextEdit в layout
        layout.addWidget(self.rule_text)

        # Устанавливаем layout для виджета
        self.setLayout(layout)


class Complex_plane(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        self.setWindowTitle("Построение чисел на плоскости")
        self.setGeometry(600, 100, 800, 800)

        # Поле для ввода комплексных чисел
        self.complex1 = QLabel(self)
        self.complex1.setText("Введите комплексное число (например, 3+4j):")
        self.complex1.resize(350, 20)
        self.complex1.move(300, 250)

        self.complex4 = QLineEdit(self)
        self.complex4.resize(250, 30)
        self.complex4.move(300, 330)

        # Кнопка для построения графика
        self.complex5 = QPushButton('Построить', self)
        self.complex5.resize(100, 50)
        self.complex5.move(360, 400)
        self.complex5.clicked.connect(self.on_plot_button_clicked)

        # Устанавливаем layout в виджет
        self.setLayout(layout)


    def on_plot_button_clicked(self):
        # Получаем введенные данные и строим график
        input_text = self.complex4.text()

        try:
            complex_numbers = self.get_complex_numbers(input_text)
            self.plot_complex_numbers(complex_numbers)
        except ValueError:
            QMessageBox.warning(self, "Ошибка", "Пожалуйста, введите корректные числа.")
        except Exception as e:
            QMessageBox.warning(self, "Ошибка", f"Произошла ошибка: {e}")


    def plot_complex_numbers(self, complex_numbers):
        # Строит график комплексных чисел на комплексной плоскости
        plt.figure(figsize=(8, 8))

        for z in complex_numbers:
            plt.plot([0, z.real], [0, z.imag], marker='o', linestyle='-')
            plt.text(z.real, z.imag, f'{z}', fontsize=12, ha='right')

        plt.axhline(0, color='black', linewidth=0.5, ls='--')
        plt.axvline(0, color='black', linewidth=0.5, ls='--')

        plt.xlim(-20, 20)
        plt.ylim(-20, 20)

        plt.xlabel('Действительная часть')
        plt.ylabel('Мнимая часть')
        plt.title('Комплексные числа на плоскости')

        plt.grid(True)
        plt.show()


    def get_complex_numbers(self, input_text):
        # Запрашивает у пользователя указанные комплексные числа
        complex_nums = []

        # Разделяем введенные значения по запятой и преобразуем в комплексные числа
        for item in input_text.split(','):
            item = item.strip()  # Убираем лишние пробелы
            if item:  # Проверяем не пустая ли строка
                complex_nums.append(complex(item))  # Преобразуем строку в комплексное число

        return complex_nums


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    application = Window()
    application.show()
    sys.exit(app.exec())
