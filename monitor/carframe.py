from PyQt5.Qt import Qt
from PyQt5.QtGui import QImage, QPixmap
from monitor.carm import Ui_Dialog
from monitor.Videofirst import Video
import logging
from PyQt5 import QtWidgets, QtGui, QtCore

logging.basicConfig(level=logging.DEBUG)

'''
显示车流量检测监控
'''
class CarMonitorDialog(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.running = True
        self.mainframe = None
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        # 设置背景图片
        self.ui.label_9.setStyleSheet("background-image: url('data/bj.jpg');")

        # 创建视频线程实例
        self.th1 = Video('data/vd1.mp4')

        # 连接信号和槽函数
        self.th1.send.connect(self.showimg)
        self.ui.pushButton.clicked.connect(self.fanhui2)

        try:
            # 启动视频线程
            self.th1.start()
        except Exception as e:
            logging.error(f"Error starting video thread: {e}")

    def showimg(self, h, w, c, b, th_id, car_count, truck_count, bus_count, motorbike_count, tricycle_count, dev):
        try:
            # 创建QImage对象
            image = QImage(b, w, h, w * c, QImage.Format_BGR888)
            pix = QPixmap.fromImage(image)
            self.dev=dev
            if th_id == 1:
                # 获取标签的宽度和高度
                width = self.ui.label_3.width()
                height = self.ui.label_3.height()

                # 缩放图片以保持宽高比
                scale_pix = pix.scaled(width, height, Qt.KeepAspectRatio)
                self.ui.label_3.setPixmap(scale_pix)

                # 更新车辆统计标签
                total_count = car_count + truck_count + bus_count + motorbike_count + tricycle_count
                self.ui.label_2.setText(f"车流量总数：{total_count}")
                self.ui.label_4.setText(f"小汽车：{car_count}")
                self.ui.label_5.setText(f"卡车：{truck_count}")
                self.ui.label_6.setText(f"巴士：{bus_count}")
                self.ui.label_7.setText(f"摩托车：{motorbike_count}")
                self.ui.label_8.setText(f"三轮车：{tricycle_count}")
        except Exception as e:
            logging.error(f"Error in showimg: {e}")

    def closeEvent(self, event):

        # 停止视频线程
        self.th1.stop()

    def fanhui2(self):
        # 停止视频线程并等待其结束
        self.th1.stop()
        # 导入并显示主界面
        from monitor.mainframe import MainDialog
        self.mainframe = MainDialog()
        self.mainframe.show()
        self.close()
