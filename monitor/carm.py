# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'carm.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1128, 645)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 10, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 60, 181, 51))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(30, 130, 841, 441))
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(910, 180, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Algerian")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(910, 250, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Algerian")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(910, 320, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Algerian")
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(910, 390, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Algerian")
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(910, 470, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Algerian")
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(980, 580, 121, 41))
        self.pushButton.setStyleSheet("QPushButton {\n"
"    background-color: qlineargradient(spread:repeat, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 150, 145, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    border: 2px solid rgb(255, 170, 172);\n"
"    border-color: rgb(255, 120, 122);\n"
"    border-radius: 20px; /* 设置圆角半径，数值可根据按钮大小调整 */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(255, 164, 165); /* 设置鼠标悬停时的背景颜色 */\n"
"    border: 2px solid rgb(255, 100, 102); /* 设置鼠标悬停时的边框颜色 */\n"
"    color: black; /* 设置鼠标悬停时的文本颜色 */\n"
"    box-shadow: 5px 5px 10px rgba(0, 0, 0, 0.3); /* 设置鼠标悬停时的阴影效果 */\n"
"    cursor: pointer; /* 设置鼠标悬停时的指针样式 */\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(-10, -10, 1141, 661))
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(900, 170, 151, 361))
        self.frame.setStyleSheet("QFrame {\n"
"    border: 4px solid rgb(255, 202, 203); /* 设置边框宽度和颜色 */\n"
"    border-radius: 20px; /* 设置圆角半径，数值可以根据需要调整 */\n"
"    background-color: transparent; /* 设置背景色透明 */\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_9.raise_()
        self.frame.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        self.pushButton.raise_()

        self.retranslateUi(Dialog)
        self.pushButton.clicked.connect(Dialog.fanhui2) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "车流量检测"))
        self.label_2.setText(_translate("Dialog", "车流量实时统计："))
        self.label_4.setText(_translate("Dialog", "小汽车："))
        self.label_5.setText(_translate("Dialog", "卡车："))
        self.label_6.setText(_translate("Dialog", "巴士："))
        self.label_7.setText(_translate("Dialog", "摩托车："))
        self.label_8.setText(_translate("Dialog", "三轮车："))
        self.pushButton.setText(_translate("Dialog", "返回上一级"))
