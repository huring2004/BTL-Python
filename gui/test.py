# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui2.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1366, 727)
        font = QtGui.QFont()
        font.setFamily("MS UI Gothic")
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color:#EBEBEB;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frameVienDo = QtWidgets.QFrame(self.centralwidget)
        self.frameVienDo.setGeometry(QtCore.QRect(0, 0, 1366, 58))
        self.frameVienDo.setStyleSheet("background-color:#BB2019;")
        self.frameVienDo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameVienDo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameVienDo.setObjectName("frameVienDo")
        self.label_HTDD = QtWidgets.QLabel(self.frameVienDo)
        self.label_HTDD.setGeometry(QtCore.QRect(106, 10, 235, 38))
        font = QtGui.QFont()
        font.setPointSize(19)
        self.label_HTDD.setFont(font)
        self.label_HTDD.setStyleSheet("color: white;\n"
"")
        self.label_HTDD.setObjectName("label_HTDD")
        self.label_logoPTIT = QtWidgets.QLabel(self.frameVienDo)
        self.label_logoPTIT.setGeometry(QtCore.QRect(30, 9, 42, 42))
        font = QtGui.QFont()
        font.setPointSize(1)
        self.label_logoPTIT.setFont(font)
        self.label_logoPTIT.setStyleSheet("background-color:#BB2019;")
        self.label_logoPTIT.setText("")
        self.label_logoPTIT.setPixmap(QtGui.QPixmap("../gui/resources/ptitLogo.png"))
        self.label_logoPTIT.setScaledContents(True)
        self.label_logoPTIT.setObjectName("label_logoPTIT")
        self.frame_TKe = QtWidgets.QFrame(self.centralwidget)
        self.frame_TKe.setGeometry(QtCore.QRect(185, 188, 313, 350))
        self.frame_TKe.setStyleSheet("background-color: white;\n"
"border-radius: 100px;   \n"
"padding: 10px;")
        self.frame_TKe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_TKe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_TKe.setObjectName("frame_TKe")
        self.label_ThongKe = QtWidgets.QLabel(self.frame_TKe)
        self.label_ThongKe.setGeometry(QtCore.QRect(70, 270, 172, 42))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_ThongKe.setFont(font)
        self.label_ThongKe.setStyleSheet("background-color:white;")
        self.label_ThongKe.setAlignment(QtCore.Qt.AlignCenter)
        self.label_ThongKe.setObjectName("label_ThongKe")
        self.label_HinhTke = QtWidgets.QLabel(self.frame_TKe)
        self.label_HinhTke.setGeometry(QtCore.QRect(70, 40, 198, 204))
        self.label_HinhTke.setText("")
        self.label_HinhTke.setPixmap(QtGui.QPixmap("../gui/resources/file.png"))
        self.label_HinhTke.setScaledContents(True)
        self.label_HinhTke.setObjectName("label_HinhTke")
        self.pushButtonThongKe = QtWidgets.QPushButton(self.frame_TKe)
        self.pushButtonThongKe.setGeometry(QtCore.QRect(40, 30, 241, 231))
        self.pushButtonThongKe.setStyleSheet("background-color: transparent;")
        self.pushButtonThongKe.setText("")
        self.pushButtonThongKe.setObjectName("pushButtonThongKe")
        self.frame_DDanh = QtWidgets.QFrame(self.centralwidget)
        self.frame_DDanh.setGeometry(QtCore.QRect(845, 188, 312, 350))
        self.frame_DDanh.setStyleSheet("background-color:white;\n"
"border-radius: 100px;")
        self.frame_DDanh.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_DDanh.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_DDanh.setObjectName("frame_DDanh")
        self.label_Ddanh = QtWidgets.QLabel(self.frame_DDanh)
        self.label_Ddanh.setGeometry(QtCore.QRect(70, 270, 172, 42))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_Ddanh.setFont(font)
        self.label_Ddanh.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Ddanh.setObjectName("label_Ddanh")
        self.label_HinhDdanh = QtWidgets.QLabel(self.frame_DDanh)
        self.label_HinhDdanh.setGeometry(QtCore.QRect(60, 40, 198, 204))
        self.label_HinhDdanh.setText("")
        self.label_HinhDdanh.setPixmap(QtGui.QPixmap("../gui/resources/wirte.png"))
        self.label_HinhDdanh.setScaledContents(True)
        self.label_HinhDdanh.setObjectName("label_HinhDdanh")
        self.pushButtonDiemDanh = QtWidgets.QPushButton(self.frame_DDanh)
        self.pushButtonDiemDanh.setGeometry(QtCore.QRect(30, 30, 251, 231))
        self.pushButtonDiemDanh.setStyleSheet("background-color: transparent;")
        self.pushButtonDiemDanh.setText("")
        self.pushButtonDiemDanh.setObjectName("pushButtonDiemDanh")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_HTDD.setText(_translate("MainWindow", "Hệ thống điểm danh"))
        self.label_ThongKe.setText(_translate("MainWindow", "Thống kê"))
        self.label_Ddanh.setText(_translate("MainWindow", "Điểm danh"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())