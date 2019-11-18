# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(350, 436)
        Dialog.setMinimumSize(QtCore.QSize(350, 436))
        Dialog.setMaximumSize(QtCore.QSize(350, 436))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.gridLayout_3 = QtWidgets.QGridLayout(Dialog)
        self.gridLayout_3.setContentsMargins(15, 15, 15, 15)
        self.gridLayout_3.setSpacing(15)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.widget.setObjectName("widget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.q_lineEdit = QtWidgets.QLineEdit(self.widget)
        self.q_lineEdit.setMinimumSize(QtCore.QSize(0, 50))
        self.q_lineEdit.setStyleSheet("font: 20pt \"나눔손글씨 펜\";")
        self.q_lineEdit.setText("")
        self.q_lineEdit.setFrame(False)
        self.q_lineEdit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.q_lineEdit.setObjectName("q_lineEdit")
        self.gridLayout_2.addWidget(self.q_lineEdit, 0, 0, 1, 2)
        self.a_lineEdit = QtWidgets.QLineEdit(self.widget)
        self.a_lineEdit.setMinimumSize(QtCore.QSize(0, 50))
        self.a_lineEdit.setStyleSheet("font: 40pt \"나눔손글씨 펜\";")
        self.a_lineEdit.setFrame(False)
        self.a_lineEdit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.a_lineEdit.setObjectName("a_lineEdit")
        self.gridLayout_2.addWidget(self.a_lineEdit, 1, 0, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(221, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 2, 0, 1, 1)
        self.del_pushButton = QtWidgets.QPushButton(self.widget)
        self.del_pushButton.setMinimumSize(QtCore.QSize(90, 30))
        self.del_pushButton.setText("")
        self.del_pushButton.setObjectName("del_pushButton")
        self.gridLayout_2.addWidget(self.del_pushButton, 2, 1, 1, 1)
        self.gridLayout_3.addWidget(self.widget, 0, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.reset_pushButton = QtWidgets.QPushButton(Dialog)
        self.reset_pushButton.setMinimumSize(QtCore.QSize(0, 45))
        self.reset_pushButton.setStyleSheet("background-color: rgb(0, 255, 255);\n"
"color: rgb(255, 0, 127);\n"
"font: 35pt \"나눔손글씨 펜\";")
        self.reset_pushButton.setObjectName("reset_pushButton")
        self.gridLayout.addWidget(self.reset_pushButton, 0, 0, 1, 1)
        self.p_open_pushButton = QtWidgets.QPushButton(Dialog)
        self.p_open_pushButton.setMinimumSize(QtCore.QSize(0, 45))
        self.p_open_pushButton.setStyleSheet("background-color: rgb(0, 255, 255);\n"
"color: rgb(255, 0, 127);\n"
"font: 35pt \"나눔손글씨 펜\";")
        self.p_open_pushButton.setObjectName("p_open_pushButton")
        self.gridLayout.addWidget(self.p_open_pushButton, 0, 1, 1, 1)
        self.p_close_pushButton = QtWidgets.QPushButton(Dialog)
        self.p_close_pushButton.setMinimumSize(QtCore.QSize(0, 45))
        self.p_close_pushButton.setStyleSheet("background-color: rgb(0, 255, 255);\n"
"color: rgb(255, 0, 127);\n"
"font: 35pt \"나눔손글씨 펜\";")
        self.p_close_pushButton.setObjectName("p_close_pushButton")
        self.gridLayout.addWidget(self.p_close_pushButton, 0, 2, 1, 1)
        self.sign_pushButton_1 = QtWidgets.QPushButton(Dialog)
        self.sign_pushButton_1.setMinimumSize(QtCore.QSize(0, 45))
        self.sign_pushButton_1.setStyleSheet("background-color: rgb(0, 255, 255);\n"
"color: rgb(255, 0, 127);\n"
"font: 35pt \"나눔손글씨 펜\";")
        self.sign_pushButton_1.setObjectName("sign_pushButton_1")
        self.gridLayout.addWidget(self.sign_pushButton_1, 0, 3, 1, 1)
        self.num_pushButton_1 = QtWidgets.QPushButton(Dialog)
        self.num_pushButton_1.setMinimumSize(QtCore.QSize(0, 45))
        self.num_pushButton_1.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 35pt \"나눔손글씨 펜\";")
        self.num_pushButton_1.setObjectName("num_pushButton_1")
        self.gridLayout.addWidget(self.num_pushButton_1, 1, 0, 1, 1)
        self.num_pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.num_pushButton_2.setMinimumSize(QtCore.QSize(0, 45))
        self.num_pushButton_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 35pt \"나눔손글씨 펜\";")
        self.num_pushButton_2.setObjectName("num_pushButton_2")
        self.gridLayout.addWidget(self.num_pushButton_2, 1, 1, 1, 1)
        self.num_pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.num_pushButton_3.setMinimumSize(QtCore.QSize(0, 45))
        self.num_pushButton_3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 35pt \"나눔손글씨 펜\";")
        self.num_pushButton_3.setObjectName("num_pushButton_3")
        self.gridLayout.addWidget(self.num_pushButton_3, 1, 2, 1, 1)
        self.sign_pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.sign_pushButton_2.setMinimumSize(QtCore.QSize(0, 45))
        self.sign_pushButton_2.setStyleSheet("background-color: rgb(0, 255, 255);\n"
"color: rgb(255, 0, 127);\n"
"font: 35pt \"나눔손글씨 펜\";")
        self.sign_pushButton_2.setObjectName("sign_pushButton_2")
        self.gridLayout.addWidget(self.sign_pushButton_2, 1, 3, 1, 1)
        self.num_pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.num_pushButton_4.setMinimumSize(QtCore.QSize(0, 45))
        self.num_pushButton_4.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 35pt \"나눔손글씨 펜\";")
        self.num_pushButton_4.setObjectName("num_pushButton_4")
        self.gridLayout.addWidget(self.num_pushButton_4, 2, 0, 1, 1)
        self.num_pushButton_5 = QtWidgets.QPushButton(Dialog)
        self.num_pushButton_5.setMinimumSize(QtCore.QSize(0, 45))
        self.num_pushButton_5.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 35pt \"나눔손글씨 펜\";")
        self.num_pushButton_5.setObjectName("num_pushButton_5")
        self.gridLayout.addWidget(self.num_pushButton_5, 2, 1, 1, 1)
        self.num_pushButton_6 = QtWidgets.QPushButton(Dialog)
        self.num_pushButton_6.setMinimumSize(QtCore.QSize(0, 45))
        self.num_pushButton_6.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 35pt \"나눔손글씨 펜\";")
        self.num_pushButton_6.setObjectName("num_pushButton_6")
        self.gridLayout.addWidget(self.num_pushButton_6, 2, 2, 1, 1)
        self.sign_pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.sign_pushButton_3.setMinimumSize(QtCore.QSize(0, 45))
        self.sign_pushButton_3.setStyleSheet("background-color: rgb(0, 255, 255);\n"
"color: rgb(255, 0, 127);\n"
"font: 35pt \"나눔손글씨 펜\";")
        self.sign_pushButton_3.setObjectName("sign_pushButton_3")
        self.gridLayout.addWidget(self.sign_pushButton_3, 2, 3, 1, 1)
        self.num_pushButton_7 = QtWidgets.QPushButton(Dialog)
        self.num_pushButton_7.setMinimumSize(QtCore.QSize(0, 45))
        self.num_pushButton_7.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 35pt \"나눔손글씨 펜\";")
        self.num_pushButton_7.setObjectName("num_pushButton_7")
        self.gridLayout.addWidget(self.num_pushButton_7, 3, 0, 1, 1)
        self.num_pushButton_8 = QtWidgets.QPushButton(Dialog)
        self.num_pushButton_8.setMinimumSize(QtCore.QSize(0, 45))
        self.num_pushButton_8.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 35pt \"나눔손글씨 펜\";")
        self.num_pushButton_8.setObjectName("num_pushButton_8")
        self.gridLayout.addWidget(self.num_pushButton_8, 3, 1, 1, 1)
        self.num_pushButton_9 = QtWidgets.QPushButton(Dialog)
        self.num_pushButton_9.setMinimumSize(QtCore.QSize(0, 45))
        self.num_pushButton_9.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 35pt \"나눔손글씨 펜\";")
        self.num_pushButton_9.setObjectName("num_pushButton_9")
        self.gridLayout.addWidget(self.num_pushButton_9, 3, 2, 1, 1)
        self.sign_pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.sign_pushButton_4.setMinimumSize(QtCore.QSize(0, 45))
        self.sign_pushButton_4.setStyleSheet("background-color: rgb(0, 255, 255);\n"
"color: rgb(255, 0, 127);\n"
"font: 35pt \"나눔손글씨 펜\";")
        self.sign_pushButton_4.setObjectName("sign_pushButton_4")
        self.gridLayout.addWidget(self.sign_pushButton_4, 3, 3, 1, 1)
        self.per_pushButton = QtWidgets.QPushButton(Dialog)
        self.per_pushButton.setMinimumSize(QtCore.QSize(0, 45))
        self.per_pushButton.setStyleSheet("background-color: rgb(0, 255, 255);\n"
"color: rgb(255, 0, 127);\n"
"font: 35pt \"나눔손글씨 펜\";")
        self.per_pushButton.setObjectName("per_pushButton")
        self.gridLayout.addWidget(self.per_pushButton, 4, 0, 1, 1)
        self.num_pushButton_0 = QtWidgets.QPushButton(Dialog)
        self.num_pushButton_0.setMinimumSize(QtCore.QSize(0, 45))
        self.num_pushButton_0.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 35pt \"나눔손글씨 펜\";")
        self.num_pushButton_0.setObjectName("num_pushButton_0")
        self.gridLayout.addWidget(self.num_pushButton_0, 4, 1, 1, 1)
        self.dot_pushButton = QtWidgets.QPushButton(Dialog)
        self.dot_pushButton.setMinimumSize(QtCore.QSize(0, 45))
        self.dot_pushButton.setStyleSheet("background-color: rgb(0, 255, 255);\n"
"color: rgb(255, 0, 127);\n"
"font: 35pt \"나눔손글씨 펜\";")
        self.dot_pushButton.setObjectName("dot_pushButton")
        self.gridLayout.addWidget(self.dot_pushButton, 4, 2, 1, 1)
        self.result_pushButton = QtWidgets.QPushButton(Dialog)
        self.result_pushButton.setMinimumSize(QtCore.QSize(0, 45))
        self.result_pushButton.setStyleSheet("background-color: rgb(0, 85, 255);\n"
"color: rgb(255, 0, 127);\n"
"font: 35pt \"나눔손글씨 펜\";")
        self.result_pushButton.setObjectName("result_pushButton")
        self.gridLayout.addWidget(self.result_pushButton, 4, 3, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout, 1, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "계산기"))
        self.a_lineEdit.setText(_translate("Dialog", "0"))
        self.reset_pushButton.setText(_translate("Dialog", "C"))
        self.p_open_pushButton.setText(_translate("Dialog", "("))
        self.p_close_pushButton.setText(_translate("Dialog", ")"))
        self.sign_pushButton_1.setText(_translate("Dialog", "/"))
        self.num_pushButton_1.setText(_translate("Dialog", "1"))
        self.num_pushButton_2.setText(_translate("Dialog", "2"))
        self.num_pushButton_3.setText(_translate("Dialog", "3"))
        self.sign_pushButton_2.setText(_translate("Dialog", "*"))
        self.num_pushButton_4.setText(_translate("Dialog", "4"))
        self.num_pushButton_5.setText(_translate("Dialog", "5"))
        self.num_pushButton_6.setText(_translate("Dialog", "6"))
        self.sign_pushButton_3.setText(_translate("Dialog", "-"))
        self.num_pushButton_7.setText(_translate("Dialog", "7"))
        self.num_pushButton_8.setText(_translate("Dialog", "8"))
        self.num_pushButton_9.setText(_translate("Dialog", "9"))
        self.sign_pushButton_4.setText(_translate("Dialog", "+"))
        self.per_pushButton.setText(_translate("Dialog", "%"))
        self.num_pushButton_0.setText(_translate("Dialog", "0"))
        self.dot_pushButton.setText(_translate("Dialog", "."))
        self.result_pushButton.setText(_translate("Dialog", "="))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
