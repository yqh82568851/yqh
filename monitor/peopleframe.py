from PyQt5.Qt import Qt
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QDialog
from monitor.peoplem import Ui_Dialog
from monitor.Videosecond import Video
import logging

'''
显示人流量检测监控
'''


class PeopleMonitorDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        # 设置背景图像
        self.ui.label_6.setStyleSheet("background-image: url('data/bj.jpg');")

        # 初始化视频处理线程
        self.th1 = Video('data/vd1.mp4', case_id=1)
        self.th1.send.connect(self.showimg)
        self.th1.start()

        # 连接返回按钮点击信号到 fanhui 方法
        self.ui.pushButton.clicked.connect(self.fanhui3)

    def resizeEvent(self, event):
        # 在窗口大小改变时调整图片大小
        if hasattr(self, 'pixmap'):
            self.update_image_display()

    def showimg(self, h, w, c, b, th_id, person_num, in_count, out_count):
        # 将视频帧转换为 QImage 并显示在界面上
        image = QImage(b, w, h, w * c, QImage.Format_BGR888)
        pix = QPixmap.fromImage(image)

        if th_id == 1:
            width = self.ui.label_2.width()
            height = self.ui.label_2.height()
            scale_pix = pix.scaled(width, height, Qt.KeepAspectRatio)
            self.ui.label_2.setPixmap(scale_pix)

            # 显示人数信息
            self.ui.label_3.setText(f"当前画面总人数：{person_num}")
            self.ui.label_4.setText(f"进入画面累计人数：{in_count}")
            self.ui.label_5.setText(f"离开画面累计人数：{out_count}")

    # 返回上一级
    def fanhui3(self):

        # 停止视频线程
        self.th1.stop()
        self.th1.running = False
        self.th1.wait()

        # 显示上一级界面
        from monitor.mainframe import MainDialog
        self.mainframe = MainDialog()
        self.mainframe.show()
        self.close()
