from datetime import datetime
from itertools import count

from PyQt5 import QtCore, QtGui, QtWidgets
import cv2
import numpy as np
import face_recognition
import os
import sys
import pickle
import cvzone
from face_recognition import face_locations
# from pyparsing import withClass
from gui import layout_adjuster

file = open("Mahoa.p", "rb")
enList = pickle.load(file)
file.close()
encode, stdIds = enList

# variable global
mp = {}
r1, g1, b1 = 0, 255, 0
r2, g2, b2 = 255, 255, 255
camera_num = 0


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
        self.frameVienDo.setGeometry(QtCore.QRect(0, 0, 16777215, 60))
        self.frameVienDo.setMinimumSize(QtCore.QSize(0, 0))
        self.frameVienDo.setStyleSheet("background-color:#BB2019;")
        self.frameVienDo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameVienDo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameVienDo.setObjectName("frameVienDo")
        self.label_logoPTIT = QtWidgets.QLabel(self.frameVienDo)
        self.label_logoPTIT.setGeometry(QtCore.QRect(30, 8, 45, 45))
        self.label_logoPTIT.setMaximumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setPointSize(1)
        self.label_logoPTIT.setFont(font)
        self.label_logoPTIT.setStyleSheet("background-color:#BB2019;")
        self.label_logoPTIT.setText("")
        self.label_logoPTIT.setPixmap(QtGui.QPixmap("../gui/resources/ptitLogo.png"))
        self.label_logoPTIT.setScaledContents(True)
        self.label_logoPTIT.setObjectName("label_logoPTIT")
        self.label_HTDD = QtWidgets.QLabel(self.frameVienDo)
        self.label_HTDD.setGeometry(QtCore.QRect(90, 0, 621, 58))
        self.label_HTDD.setMinimumSize(QtCore.QSize(250, 58))
        self.label_HTDD.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_HTDD.setFont(font)
        self.label_HTDD.setStyleSheet("color: white;\n"
                                      "")
        self.label_HTDD.setObjectName("label_HTDD")
        self.pushButton_KetThuc = QtWidgets.QPushButton(self.frameVienDo)
        self.pushButton_KetThuc.setGeometry(QtCore.QRect(1220, 10, 131, 38))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton_KetThuc.setFont(font)
        self.pushButton_KetThuc.setStyleSheet("color: white;\n"
                                              "background-color: transparent;")
        self.pushButton_KetThuc.setObjectName("pushButton_KetThuc")
        self.frame_TKe = QtWidgets.QFrame(self.centralwidget)
        self.frame_TKe.setGeometry(QtCore.QRect(10, 160, 440, 470))
        self.frame_TKe.setStyleSheet("background-color: white;\n"
                                     "border-radius: 100px;   \n"
                                     "padding: 10px;")
        self.frame_TKe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_TKe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_TKe.setObjectName("frame_TKe")
        self.label_ThongKe = QtWidgets.QLabel(self.frame_TKe)
        self.label_ThongKe.setGeometry(QtCore.QRect(60, 360, 321, 91))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label_ThongKe.setFont(font)
        self.label_ThongKe.setStyleSheet("background-color:white;\n"
                                         "margin: -10px;")
        self.label_ThongKe.setAlignment(QtCore.Qt.AlignCenter)
        self.label_ThongKe.setObjectName("label_ThongKe")
        self.label_HinhTke = QtWidgets.QLabel(self.frame_TKe)
        self.label_HinhTke.setGeometry(QtCore.QRect(120, 90, 220, 220))
        self.label_HinhTke.setText("")
        self.label_HinhTke.setPixmap(QtGui.QPixmap("../gui/resources/file.png"))
        self.label_HinhTke.setScaledContents(True)
        self.label_HinhTke.setObjectName("label_HinhTke")
        self.pushButtonThongKe = QtWidgets.QPushButton(self.frame_TKe)
        self.pushButtonThongKe.setGeometry(QtCore.QRect(60, 50, 321, 391))
        self.pushButtonThongKe.setStyleSheet("background-color: transparent;")
        self.pushButtonThongKe.setText("")
        self.pushButtonThongKe.setObjectName("pushButtonThongKe")
        self.frame_DDanh = QtWidgets.QFrame(self.centralwidget)
        self.frame_DDanh.setGeometry(QtCore.QRect(460, 160, 440, 470))
        self.frame_DDanh.setStyleSheet("background-color:white;\n"
                                       "border-radius: 100px;")
        self.frame_DDanh.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_DDanh.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_DDanh.setObjectName("frame_DDanh")
        self.label_Ddanh = QtWidgets.QLabel(self.frame_DDanh)
        self.label_Ddanh.setGeometry(QtCore.QRect(60, 360, 341, 81))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label_Ddanh.setFont(font)
        self.label_Ddanh.setStyleSheet("background-color:white;\n"
                                       "margin: -10px;")
        self.label_Ddanh.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Ddanh.setObjectName("label_Ddanh")
        self.label_HinhDdanh = QtWidgets.QLabel(self.frame_DDanh)
        self.label_HinhDdanh.setGeometry(QtCore.QRect(120, 90, 220, 220))
        self.label_HinhDdanh.setText("")
        self.label_HinhDdanh.setPixmap(QtGui.QPixmap("../gui/resources/wirte.png"))
        self.label_HinhDdanh.setScaledContents(True)
        self.label_HinhDdanh.setObjectName("label_HinhDdanh")
        self.pushButtonDiemDanh = QtWidgets.QPushButton(self.frame_DDanh)
        self.pushButtonDiemDanh.setGeometry(QtCore.QRect(60, 60, 341, 371))
        self.pushButtonDiemDanh.setStyleSheet("background-color: transparent;")
        self.pushButtonDiemDanh.setText("")
        self.pushButtonDiemDanh.setObjectName("pushButtonDiemDanh")

        # graphicView để hiển thị camera
        self.viewCamera = QtWidgets.QGraphicsView(self.centralwidget)
        self.viewCamera.setGeometry(QtCore.QRect(0, self.frameVienDo.height(), 1366, 667))
        self.viewCamera.setStyleSheet("background-color: transparent;")
        self.viewCamera.setObjectName("viewCamera")
        self.viewCamera.hide()

        # Setting chọn camera
        self.frame_setting = QtWidgets.QFrame(self.centralwidget)
        self.frame_setting.setGeometry(QtCore.QRect(910, 160, 440, 470))
        self.frame_setting.setStyleSheet("background-color:white;\n"
                                         "border-radius: 100px;")
        self.frame_setting.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_setting.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_setting.setObjectName("frame_setting")
        self.label_Setting = QtWidgets.QLabel(self.frame_setting)
        self.label_Setting.setGeometry(QtCore.QRect(60, 360, 341, 81))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label_Setting.setFont(font)
        self.label_Setting.setStyleSheet("background-color:white;\n"
                                         "margin: -10px;")
        self.label_Setting.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Setting.setObjectName("label_Setting")
        self.label_HinhSetting = QtWidgets.QLabel(self.frame_setting)
        self.label_HinhSetting.setGeometry(QtCore.QRect(120, 90, 210, 210))
        self.label_HinhSetting.setText("")
        self.label_HinhSetting.setPixmap(QtGui.QPixmap("../gui/resources/setting.png"))
        self.label_HinhSetting.setScaledContents(True)
        self.label_HinhSetting.setObjectName("label_HinhSetting")
        self.pushButtonSetting = QtWidgets.QPushButton(self.frame_setting)
        self.pushButtonSetting.setGeometry(QtCore.QRect(70, 50, 311, 391))
        self.pushButtonSetting.setStyleSheet("background-color: transparent;")
        self.pushButtonSetting.setText("")
        self.pushButtonSetting.setObjectName("pushButtonSetting")

        # 2 option camera
        self.option_cam = QtWidgets.QFrame(self.centralwidget)
        self.option_cam.setGeometry(QtCore.QRect(40, self.frameVienDo.height() + 20, 711, 251))
        self.option_cam.setStyleSheet("background-color: transparent;")
        self.option_cam.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.option_cam.setFrameShadow(QtWidgets.QFrame.Raised)
        self.option_cam.setObjectName("option_cam")
        self.buttonCam1 = QtWidgets.QPushButton(self.option_cam)
        self.buttonCam1.setGeometry(QtCore.QRect(30, 60, 250, 100))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.buttonCam1.setFont(font)
        self.buttonCam1.setStyleSheet("""
            QPushButton {
                background-color: white;
                border-radius: 30px;
            }
            QPushButton:pressed {
                background-color: #33CC33; 
            }
        """)
        self.buttonCam1.setObjectName("buttonCam1")

        self.buttonCam2 = QtWidgets.QPushButton(self.option_cam)
        self.buttonCam2.setGeometry(QtCore.QRect(430, 60, 250, 100))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.buttonCam2.setFont(font)
        self.buttonCam2.setStyleSheet("""
            QPushButton {
                background-color: white;
                border-radius: 30px;
            }
            QPushButton:pressed {
                background-color: #33CC33; 
            }
        """)
        self.buttonCam2.setObjectName("buttonCam2")
        self.option_cam.hide()

        # Bring front
        self.viewCamera.raise_()
        self.frameVienDo.raise_()
        self.frame_TKe.raise_()
        self.frame_DDanh.raise_()
        self.frame_setting.raise_()
        self.option_cam.raise_()

        # scene để hiển thị camera lên
        self.scene = QtWidgets.QGraphicsScene()
        self.viewCamera.setScene(self.scene)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButtonThongKe.clicked.connect(self.open_static_file)
        self.pushButton_KetThuc.hide()
        self.pushButton_KetThuc.clicked.connect(self.frame_TKe.show)  # type: ignore
        self.pushButton_KetThuc.clicked.connect(self.frame_DDanh.show)  # type: ignore
        self.pushButton_KetThuc.clicked.connect(self.pushButton_KetThuc.hide)  # type: ignore
        self.pushButtonDiemDanh.clicked.connect(self.pushButton_KetThuc.show)  # type: ignore
        self.pushButtonDiemDanh.clicked.connect(self.frame_DDanh.hide)  # type: ignore
        self.pushButtonDiemDanh.clicked.connect(self.frame_TKe.hide)  # type: ignore
        self.pushButton_KetThuc.clicked.connect(self.viewCamera.hide)  # hiển thị graphicView
        self.pushButtonDiemDanh.clicked.connect(self.viewCamera.show)  # đóng graphicView
        self.pushButtonDiemDanh.clicked.connect(self.deleteContent)  # xóa nội dung trong file DiemDanh
        self.pushButtonDiemDanh.clicked.connect(self.openCamera)  # bật camera
        self.pushButton_KetThuc.clicked.connect(self.closeCamera)  # đóng camera

        self.buttonCam1.clicked.connect(self.option_cam.hide)  # type: ignore
        self.buttonCam2.clicked.connect(self.option_cam.hide)  # type: ignore
        self.buttonCam1.clicked.connect(self.choose_camera_0)  # type: ignore
        self.buttonCam2.clicked.connect(self.choose_camera_1)  # type: ignore
        self.pushButtonSetting.clicked.connect(self.frame_DDanh.hide)  # type: ignore
        self.pushButtonSetting.clicked.connect(self.frame_TKe.close)  # type: ignore
        self.pushButtonSetting.clicked.connect(self.option_cam.show)  # type: ignore
        self.buttonCam1.clicked.connect(self.frame_TKe.show)  # type: ignore
        self.buttonCam1.clicked.connect(self.frame_DDanh.show)  # type: ignore
        self.buttonCam1.clicked.connect(self.frame_setting.show)  # type: ignore
        self.buttonCam2.clicked.connect(self.frame_TKe.show)  # type: ignore
        self.buttonCam2.clicked.connect(self.frame_DDanh.show)  # type: ignore
        self.buttonCam2.clicked.connect(self.frame_setting.show)  # type: ignore
        self.pushButtonSetting.clicked.connect(self.frame_setting.hide)  # type: ignore
        self.pushButtonDiemDanh.clicked.connect(self.frame_setting.hide)  # type: ignore
        self.pushButton_KetThuc.clicked.connect(self.frame_setting.show)  # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def choose_camera_0(self):
        global camera_num
        camera_num = 0
        self.buttonCam1.setStyleSheet("""
            QPushButton {
                background-color: #33CC33;                        
                border-radius: 30px;
            }
            QPushButton:pressed {
                background-color: #33CC33; 
            }
        """)

        self.buttonCam2.setStyleSheet("""
            QPushButton {
                background-color: white;
                border-radius: 30px;
            }
            QPushButton:pressed {
                background-color: #33CC33;
            }
        """)

    def choose_camera_1(self):
        global camera_num
        camera_num = 1
        self.buttonCam2.setStyleSheet("""
            QPushButton {
                background-color: #33CC33;
                border-radius: 30px;
            }
            QPushButton:pressed {
                background-color: #33CC33; 
            }
        """)

        self.buttonCam1.setStyleSheet("""
            QPushButton {
                background-color: white;
                border-radius: 30px;
            }
            QPushButton:pressed {
                background-color: #33CC33; 
            }
        """)

    def open_static_file(self):
        file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'Backend', 'DiemDanh.csv')
        os.startfile(file_path)

    # Mở camera dùng opencv
    def openCamera(self):

        self.cap = cv2.VideoCapture(camera_num)
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(0)

    # delete nội dung trong file DiemDanh
    def deleteContent(self):
        with open("../Backend/DiemDanh.csv", "w") as f:
            f.writelines("HoVaTen, MaSinhVien, ThoiGianDiemDanh")

    # them vào file điểm danh
    def diemdanh(self, id):
        global r1, g1, b1, r2, g2, b2
        with open("../Backend/DiemDanh.csv", "r+") as f:
            name, msv = map(str, id.split("-"))
            myDD = f.readlines()
            list_msv = []
            for i in myDD:
                t = i.split(", ")
                list_msv.append(t[1])
            if msv not in list_msv:
                now = datetime.today()
                _time = now.strftime("%H:%M:%S-%d/%m/%Y")
                f.writelines(f"\n{name}, {msv}, {_time}")
                mp[msv] = 1
                r1, g1, b1 = 0, 255, 0
                r2, g2, b2 = 255, 255, 255
            else:
                mp[msv] += 1
            if (mp[msv] > 3):
                r1, g1, b1 = 0, 0, 255
                r2, g2, b2 = 255, 255, 255

    # Update khung hình dùng opencv

    def update_frame(self):
        ret, frame = self.cap.read()

        if True:
            # Chuyển đổi frame từ BGR (OpenCV) sang RGB (Qt)

            imgS = cv2.resize(frame, (0, 0), None, 0.25, 0.25)
            imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

            faceFrame = face_recognition.face_locations(imgS)
            encodeFrame = face_recognition.face_encodings(imgS, faceFrame)

            for e, f in zip(encodeFrame, faceFrame):
                mat = face_recognition.compare_faces(encode, e)
                faceDis = face_recognition.face_distance(encode, e)
                matIdx = np.argmin(faceDis)  # chỉ số của thằng ảnh nhỏ nhất
                if mat[matIdx]:
                    y1, x2, y2, x1 = f
                    y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                    name, msv = map(str, stdIds[matIdx].split("-"))
                    name = f"Ten: {name}"
                    msv = f"MSV: {msv}"
                    self.diemdanh(str(stdIds[matIdx]))
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (r1, g1, b1), 1)
                    # cv2.rectangle(frame,(x1,y2-30),(x2,y2),(0,225,0),cv2.FILLED)

                    # làm đẹp 1 tý
                    color = (r1, g1, b1)
                    alpha = 0.35
                    overlay = frame.copy()
                    cv2.rectangle(overlay, (x1, y2 + 30), (x2, y2), color, cv2.FILLED)
                    # Kết hợp overlay với frame bằng alpha blending
                    cv2.addWeighted(overlay, alpha, frame, 1 - alpha, 0, frame)
                    cv2.putText(frame, name, (x1 + 6, y2 - 15 + 30), cv2.FONT_ITALIC, 0.35, (r2, g2, b2), 1)
                    cv2.putText(frame, msv, (x1 + 6, y2 - 2 + 30), cv2.FONT_ITALIC, 0.35, (r2, g2, b2), 1)

            height, width, _ = frame.shape
            qimg = QtGui.QImage(frame.data, width, height, 3 * width, QtGui.QImage.Format_RGB888).rgbSwapped()
            pixmap = QtGui.QPixmap.fromImage(qimg)

            # Điều chỉnh pixmap cho vừa khít với QGraphicsView
            self.scene.clear()  # Xóa scene trước khi hiển thị frame mới
            self.scene.addPixmap(pixmap)
            # self.viewCamera.fitInView(self.scene.sceneRect(), QtCore.Qt.KeepAspectRatio)

            # Fit scene vào QGraphicsView, chấp nhận việc hình ảnh bị cắt
            self.viewCamera.fitInView(self.scene.sceneRect(), QtCore.Qt.KeepAspectRatioByExpanding)

    # Đóng camera dùng opencv
    def closeCamera(self):
        self.timer.stop()  # Dừng timer
        self.cap.release()  # Giải phóng camera
        self.cap = None

    # Đóng với trường hợp tắt app
    def closeEvent(self, event):
        # Đóng camera khi thoát ứng dụng
        self.cap.release()
        event.accept()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Hệ thống điểm danh"))
        self.label_HTDD.setText(_translate("MainWindow", "Hệ thống điểm danh"))
        self.pushButton_KetThuc.setText(_translate("MainWindow", "Kết thúc"))
        self.label_ThongKe.setText(_translate("MainWindow", "Thống kê"))
        self.label_Ddanh.setText(_translate("MainWindow", "Điểm danh"))
        self.label_Setting.setText(_translate("MainWindow", "Thiết lập"))
        self.buttonCam1.setText(_translate("MainWindow", "Cam 1"))
        self.buttonCam2.setText(_translate("MainWindow", "Cam 2"))


if __name__ == "__main__":
    # import sys
    #
    # app = QtWidgets.QApplication(sys.argv)
    # MainWindow = QtWidgets.QMainWindow()
    # ui = Ui_MainWindow()
    # ui.setupUi(MainWindow)
    # MainWindow.show()
    layout_adjuster.process()
    # sys.exit(app.exec_())
