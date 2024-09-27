import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWidgets import QApplication, QMainWindow
from gui.app_ui import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # self.ratio_h = 1
        # self.ratio_w = 1
        self.new_x_button_1 = None
        self.new_x_button = None
        self.new_y_button = None
        self.new_y_button_1 = None
        self.new_x_kthuc = None
        self.new_y_kthuc = None
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self)

        # self.old_screen_w = self.geometry().width()
        # self.old_screen_h = self.geometry().height()

    def resizeEvent(self, event):
        # self.new_button_ratio()
        self.button_calculate()
        # self.font_button()

    #tính tỉ lệ
    # def new_button_ratio(self):
    #     # frame width
    #     new_screen_w = self.geometry().width()
    #     new_screen_h = self.geometry().height()
    #     self.ratio_w = round((new_screen_w / self.old_screen_w), 2)
    #     self.ratio_h = round((new_screen_h / self.old_screen_h), 2)

    #tính toán lại nút nhấn
    def button_calculate(self):
        # frame width
        new_screen_w = self.geometry().width()
        new_screen_h = self.geometry().height()

        # calculate x coordinates of center button (tke + ddanh)
        center_x_button = int(new_screen_w / 4 ) #Tke
        center_x_button_1 = int(new_screen_w * 3 / 4) #Ddanh

        #caculate y coordinates of center button (tke + ddanh)
        vdo = self.uic.frameVienDo.geometry()
        center_y_button   = int((new_screen_h - vdo.height()) / 2) #Tke
        center_y_button_1 = int((new_screen_h - vdo.height()) / 2) #Ddanh

        # calculate new x,y button base on center button
        self.new_button_pos(center_x_button, center_y_button, center_x_button_1, center_y_button_1)

    def new_button_pos(self, center_x_button, center_y_button, center_x_button_1, center_y_button_1):
        rect = self.uic.frame_TKe.geometry()
        self.new_x_button   = center_x_button   - rect.width() // 2
        self.new_x_button_1 = center_x_button_1 - rect.width() // 2

        vdo = self.uic.frameVienDo.geometry()
        self.new_y_button   = center_y_button   - rect.height() // 2 + vdo.height()
        self.new_y_button_1 = center_y_button_1 - rect.height() // 2 + vdo.height()

        #Pos button Ket thuc
        new_screen_w = self.geometry().width()
        new_screen_h = self.geometry().height()
        Kthuc = self.uic.pushButton_KetThuc.geometry()

        self.new_x_kthuc = new_screen_w - 20 - Kthuc.width()
        self.new_y_kthuc = vdo.height() // 2 - Kthuc.height() // 2

        #New pos and size for 3 button
        self.set_new_button()

    def set_new_button(self):
        Tke   = self.uic.frame_TKe.geometry()
        Dd    = self.uic.frame_DDanh.geometry()
        Kthuc = self.uic.pushButton_KetThuc.geometry()
        self.uic.frame_TKe.setGeometry(self.new_x_button, self.new_y_button, Tke.width(), Tke.height())
        self.uic.frame_DDanh.setGeometry(self.new_x_button_1, self.new_y_button_1, Dd.width(), Dd.height())
        self.uic.pushButton_KetThuc.setGeometry(self.new_x_kthuc, self.new_y_kthuc, Kthuc.width(), Kthuc.height())

        # resize graphicview
        winW = self.geometry().width()
        winH = self.geometry().height()
        self.uic.viewCamera.setGeometry(0, self.uic.frameVienDo.height(), winW, winH - self.uic.frameVienDo.height())

    # def font_button(self):
    #     # Tạo font và áp dụng cho QPushButton
    #     font = QFont("Arial", int(20*self.ratio_w), QFont.Bold)
    #     self.uic.pushButton.setFont(font)
    #     self.uic.pushButton_2.setFont(font)

def process():
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()

    sys.exit(app.exec())
