# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Window.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(606, 665)
        MainWindow.setIconSize(QtCore.QSize(30, 30))
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tr = QtWidgets.QPushButton(self.centralwidget)
        self.tr.setGeometry(QtCore.QRect(500, 110, 101, 111))
        font = QtGui.QFont()
        font.setFamily("Candara Light")
        font.setPointSize(11)
        self.tr.setFont(font)
        self.tr.setObjectName("tr")
        self.rt = QtWidgets.QPushButton(self.centralwidget)
        self.rt.setGeometry(QtCore.QRect(500, 220, 101, 111))
        font = QtGui.QFont()
        font.setFamily("Candara Light")
        font.setPointSize(11)
        self.rt.setFont(font)
        self.rt.setObjectName("rt")
        self.avr = QtWidgets.QPushButton(self.centralwidget)
        self.avr.setGeometry(QtCore.QRect(500, 330, 101, 111))
        font = QtGui.QFont()
        font.setFamily("Candara Light")
        font.setPointSize(11)
        self.avr.setFont(font)
        self.avr.setObjectName("avr")
        self.ng = QtWidgets.QPushButton(self.centralwidget)
        self.ng.setGeometry(QtCore.QRect(500, 440, 101, 111))
        font = QtGui.QFont()
        font.setFamily("Candara Light")
        font.setPointSize(11)
        self.ng.setFont(font)
        self.ng.setObjectName("ng")
        self.ckrb = QtWidgets.QPushButton(self.centralwidget)
        self.ckrb.setGeometry(QtCore.QRect(500, 550, 101, 111))
        font = QtGui.QFont()
        font.setFamily("Candara Light")
        font.setPointSize(11)
        self.ckrb.setFont(font)
        self.ckrb.setAutoExclusive(False)
        self.ckrb.setObjectName("ckrb")
        self.tj_yhui = QtWidgets.QPushButton(self.centralwidget)
        self.tj_yhui.setGeometry(QtCore.QRect(400, 570, 101, 91))
        font = QtGui.QFont()
        font.setFamily("Candara Light")
        font.setPointSize(11)
        self.tj_yhui.setFont(font)
        self.tj_yhui.setObjectName("tj_yhui")
        self.mj_yuan = QtWidgets.QPushButton(self.centralwidget)
        self.mj_yuan.setGeometry(QtCore.QRect(0, 570, 101, 91))
        font = QtGui.QFont()
        font.setFamily("Candara Light")
        font.setPointSize(11)
        self.mj_yuan.setFont(font)
        self.mj_yuan.setObjectName("mj_yuan")
        self.tj_fang = QtWidgets.QPushButton(self.centralwidget)
        self.tj_fang.setGeometry(QtCore.QRect(100, 570, 101, 91))
        font = QtGui.QFont()
        font.setFamily("Candara Light")
        font.setPointSize(11)
        self.tj_fang.setFont(font)
        self.tj_fang.setObjectName("tj_fang")
        self.tj_yuan = QtWidgets.QPushButton(self.centralwidget)
        self.tj_yuan.setGeometry(QtCore.QRect(200, 570, 101, 91))
        font = QtGui.QFont()
        font.setFamily("Candara Light")
        font.setPointSize(11)
        self.tj_yuan.setFont(font)
        self.tj_yuan.setObjectName("tj_yuan")
        self.tj_yzhu = QtWidgets.QPushButton(self.centralwidget)
        self.tj_yzhu.setGeometry(QtCore.QRect(300, 570, 101, 91))
        font = QtGui.QFont()
        font.setFamily("Candara Light")
        font.setPointSize(11)
        self.tj_yzhu.setFont(font)
        self.tj_yzhu.setObjectName("tj_yzhu")
        self.mj_tixg = QtWidgets.QPushButton(self.centralwidget)
        self.mj_tixg.setGeometry(QtCore.QRect(400, 480, 101, 91))
        font = QtGui.QFont()
        font.setFamily("Candara Light")
        font.setPointSize(11)
        self.mj_tixg.setFont(font)
        self.mj_tixg.setObjectName("mj_tixg")
        self.zc_fang = QtWidgets.QPushButton(self.centralwidget)
        self.zc_fang.setGeometry(QtCore.QRect(0, 480, 101, 91))
        font = QtGui.QFont()
        font.setFamily("Candara Light")
        font.setPointSize(11)
        self.zc_fang.setFont(font)
        self.zc_fang.setObjectName("zc_fang")
        self.zc_yuan = QtWidgets.QPushButton(self.centralwidget)
        self.zc_yuan.setGeometry(QtCore.QRect(100, 480, 101, 91))
        font = QtGui.QFont()
        font.setFamily("Candara Light")
        font.setPointSize(11)
        self.zc_yuan.setFont(font)
        self.zc_yuan.setObjectName("zc_yuan")
        self.mj_fang = QtWidgets.QPushButton(self.centralwidget)
        self.mj_fang.setGeometry(QtCore.QRect(200, 480, 101, 91))
        font = QtGui.QFont()
        font.setFamily("Candara Light")
        font.setPointSize(11)
        self.mj_fang.setFont(font)
        self.mj_fang.setObjectName("mj_fang")
        self.mj_sanj = QtWidgets.QPushButton(self.centralwidget)
        self.mj_sanj.setGeometry(QtCore.QRect(300, 480, 101, 91))
        font = QtGui.QFont()
        font.setFamily("Candara Light")
        font.setPointSize(11)
        self.mj_sanj.setFont(font)
        self.mj_sanj.setObjectName("mj_sanj")
        self.EnterButton = QtWidgets.QPushButton(self.centralwidget)
        self.EnterButton.setGeometry(QtCore.QRect(0, 110, 501, 71))
        font = QtGui.QFont()
        font.setFamily("Corbel Light")
        font.setPointSize(20)
        self.EnterButton.setFont(font)
        self.EnterButton.setObjectName("EnterButton")
        self.key7 = QtWidgets.QPushButton(self.centralwidget)
        self.key7.setGeometry(QtCore.QRect(0, 180, 101, 101))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei Light")
        font.setPointSize(20)
        self.key7.setFont(font)
        self.key7.setObjectName("key7")
        self.key8 = QtWidgets.QPushButton(self.centralwidget)
        self.key8.setGeometry(QtCore.QRect(100, 180, 101, 101))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei Light")
        font.setPointSize(20)
        self.key8.setFont(font)
        self.key8.setObjectName("key8")
        self.key9 = QtWidgets.QPushButton(self.centralwidget)
        self.key9.setGeometry(QtCore.QRect(200, 180, 101, 101))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei Light")
        font.setPointSize(20)
        self.key9.setFont(font)
        self.key9.setObjectName("key9")
        self.key3 = QtWidgets.QPushButton(self.centralwidget)
        self.key3.setGeometry(QtCore.QRect(200, 380, 101, 101))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei Light")
        font.setPointSize(20)
        self.key3.setFont(font)
        self.key3.setObjectName("key3")
        self.key1 = QtWidgets.QPushButton(self.centralwidget)
        self.key1.setGeometry(QtCore.QRect(0, 380, 101, 101))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei Light")
        font.setPointSize(20)
        self.key1.setFont(font)
        self.key1.setObjectName("key1")
        self.key2 = QtWidgets.QPushButton(self.centralwidget)
        self.key2.setGeometry(QtCore.QRect(100, 380, 101, 101))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei Light")
        font.setPointSize(20)
        self.key2.setFont(font)
        self.key2.setObjectName("key2")
        self.key6 = QtWidgets.QPushButton(self.centralwidget)
        self.key6.setGeometry(QtCore.QRect(200, 280, 101, 101))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei Light")
        font.setPointSize(20)
        self.key6.setFont(font)
        self.key6.setObjectName("key6")
        self.key4 = QtWidgets.QPushButton(self.centralwidget)
        self.key4.setGeometry(QtCore.QRect(0, 280, 101, 101))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei Light")
        font.setPointSize(20)
        self.key4.setFont(font)
        self.key4.setObjectName("key4")
        self.key5 = QtWidgets.QPushButton(self.centralwidget)
        self.key5.setGeometry(QtCore.QRect(100, 280, 101, 101))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei Light")
        font.setPointSize(20)
        self.key5.setFont(font)
        self.key5.setObjectName("key5")
        self.key0 = QtWidgets.QPushButton(self.centralwidget)
        self.key0.setGeometry(QtCore.QRect(300, 380, 101, 101))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei Light")
        font.setPointSize(20)
        self.key0.setFont(font)
        self.key0.setObjectName("key0")
        self.num_dot = QtWidgets.QPushButton(self.centralwidget)
        self.num_dot.setGeometry(QtCore.QRect(400, 380, 101, 101))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei Light")
        font.setPointSize(20)
        self.num_dot.setFont(font)
        self.num_dot.setObjectName("num_dot")
        self.Plus = QtWidgets.QPushButton(self.centralwidget)
        self.Plus.setGeometry(QtCore.QRect(300, 180, 101, 101))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei Light")
        font.setPointSize(20)
        self.Plus.setFont(font)
        self.Plus.setObjectName("Plus")
        self.Times = QtWidgets.QPushButton(self.centralwidget)
        self.Times.setGeometry(QtCore.QRect(400, 180, 101, 101))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei Light")
        font.setPointSize(20)
        self.Times.setFont(font)
        self.Times.setObjectName("Times")
        self.Minus = QtWidgets.QPushButton(self.centralwidget)
        self.Minus.setGeometry(QtCore.QRect(300, 280, 101, 101))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei Light")
        font.setPointSize(20)
        self.Minus.setFont(font)
        self.Minus.setObjectName("Minus")
        self.division = QtWidgets.QPushButton(self.centralwidget)
        self.division.setGeometry(QtCore.QRect(400, 280, 101, 101))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei Light")
        font.setPointSize(20)
        self.division.setFont(font)
        self.division.setObjectName("division")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(0, 0, 601, 111))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei Light")
        font.setPointSize(18)
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setObjectName("plainTextEdit")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.tr.setText(_translate("MainWindow", "tr\n"
"植树问题"))
        self.rt.setText(_translate("MainWindow", "rt\n"
"机率"))
        self.avr.setText(_translate("MainWindow", "avr\n"
"平均值"))
        self.ng.setText(_translate("MainWindow", "ng\n"
"浓度"))
        self.ckrb.setText(_translate("MainWindow", "ckrb\n"
"鸡兔同笼"))
        self.tj_yhui.setText(_translate("MainWindow", "tj-yhui\n"
"圆锥体积"))
        self.mj_yuan.setText(_translate("MainWindow", "mj-yuan\n"
"圆形面积"))
        self.tj_fang.setText(_translate("MainWindow", "tj-fang\n"
"方体体积"))
        self.tj_yuan.setText(_translate("MainWindow", "tj-yuan\n"
"球体体积"))
        self.tj_yzhu.setText(_translate("MainWindow", "tj-yzhu\n"
"圆柱体积"))
        self.mj_tixg.setText(_translate("MainWindow", "mj-tixg\n"
"梯形面积"))
        self.zc_fang.setText(_translate("MainWindow", "zc-fang\n"
"平行四边形\n"
"周长"))
        self.zc_yuan.setText(_translate("MainWindow", "zc-yuan\n"
"圆形周长"))
        self.mj_fang.setText(_translate("MainWindow", "mj-fang\n"
"平行四边形\n"
"面积"))
        self.mj_sanj.setText(_translate("MainWindow", "mj-sanj\n"
"三角形面积"))
        self.EnterButton.setText(_translate("MainWindow", "E n t e r"))
        self.key7.setText(_translate("MainWindow", "7"))
        self.key8.setText(_translate("MainWindow", "8"))
        self.key9.setText(_translate("MainWindow", "9"))
        self.key3.setText(_translate("MainWindow", "3"))
        self.key1.setText(_translate("MainWindow", "1"))
        self.key2.setText(_translate("MainWindow", "2"))
        self.key6.setText(_translate("MainWindow", "6"))
        self.key4.setText(_translate("MainWindow", "4"))
        self.key5.setText(_translate("MainWindow", "5"))
        self.key0.setText(_translate("MainWindow", "0"))
        self.num_dot.setText(_translate("MainWindow", "."))
        self.Plus.setText(_translate("MainWindow", "＋"))
        self.Times.setText(_translate("MainWindow", "×"))
        self.Minus.setText(_translate("MainWindow", "－"))
        self.division.setText(_translate("MainWindow", "÷"))
        self.plainTextEdit.setPlainText(_translate("MainWindow", "\n"
""))