# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface_test_tool_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1052, 995)
        MainWindow.setMaximumSize(QtCore.QSize(10777215, 10777215))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(250, 20, 481, 51))
        font = QtGui.QFont()
        font.setFamily("Aharoni")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(220, 110, 361, 24))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 100, 161, 51))
        self.label_2.setStyleSheet(" background-color: #89CFF0;border-width: 2px; border-style: solid;")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(650, 110, 51, 31))
        self.label_3.setStyleSheet(" background-color: #89CFF0;border-width: 2px; border-style: solid;")
        self.label_3.setObjectName("label_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(730, 110, 61, 24))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(40, 170, 161, 31))
        self.label_4.setStyleSheet(" background-color: #89CFF0;border-width: 2px; border-style: solid;")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(220, 170, 171, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(40, 420, 161, 31))
        self.label_5.setStyleSheet(" background-color: #89CFF0;border-width: 2px; border-style: solid;")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(40, 620, 161, 31))
        self.label_6.setStyleSheet(" background-color: #89CFF0;border-width: 2px; border-style: solid;")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(322, 900, 151, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(610, 900, 131, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(40, 290, 161, 31))
        self.label_7.setStyleSheet(" background-color: #89CFF0;border-width: 2px; border-style: solid;")
        self.label_7.setObjectName("label_7")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(220, 290, 741, 91))
        self.textEdit.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(220, 420, 741, 181))
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_3 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_3.setGeometry(QtCore.QRect(220, 620, 741, 181))
        self.textEdit_3.setObjectName("textEdit_3")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(40, 220, 161, 51))
        self.label_8.setStyleSheet(" background-color: #89CFF0;border-width: 2px; border-style: solid;")
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(220, 230, 731, 24))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(40, 830, 161, 31))
        self.label_9.setStyleSheet(" background-color: #89CFF0;border-width: 2px; border-style: solid;")
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(231, 834, 731, 21))
        self.label_10.setObjectName("label_10")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1052, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "光荣之路接口测试工具"))
        self.lineEdit.setText(_translate("MainWindow", "http://124.223.167.147"))
        self.label_2.setText(_translate("MainWindow", "接口服务器 URL 地址"))
        self.label_3.setText(_translate("MainWindow", "端口"))
        self.lineEdit_2.setText(_translate("MainWindow", "8080"))
        self.label_4.setText(_translate("MainWindow", "http 请求方法"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Post"))
        self.comboBox.setItemText(1, _translate("MainWindow", "get"))
        self.comboBox.setItemText(2, _translate("MainWindow", "put"))
        self.comboBox.setItemText(3, _translate("MainWindow", "delete"))
        self.comboBox.setItemText(4, _translate("MainWindow", "head"))
        self.comboBox.setItemText(5, _translate("MainWindow", "trace"))
        self.label_5.setText(_translate("MainWindow", "接口请求的数据"))
        self.label_6.setText(_translate("MainWindow", "接口响应的结果"))
        self.pushButton.setText(_translate("MainWindow", "测试当前接口"))
        self.pushButton_2.setText(_translate("MainWindow", "保存当前测试结果"))
        self.label_7.setText(_translate("MainWindow", "请求的 Header 信息"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" background-color:rgba(245,246,249,0.4);\">{</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" background-color:rgba(245,246,249,0.4);\">    &quot;User-Agent&quot;: &quot;Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36&quot;,</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" background-color:rgba(245,246,249,0.4);\">    &quot;Content-Type&quot;: &quot;application/json&quot;</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" background-color:rgba(245,246,249,0.4);\">}</span></p></body></html>"))
        self.label_8.setText(_translate("MainWindow", "接口 URL 地址"))
        self.lineEdit_3.setText(_translate("MainWindow", "/register/"))
        self.label_9.setText(_translate("MainWindow", "接口响应时间"))
        self.label_10.setText(_translate("MainWindow", "0 ms"))