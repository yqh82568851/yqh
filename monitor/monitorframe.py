from PyQt5.QtWidgets import QDialog, QMainWindow
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import Qt
from monitor.monitorf import Ui_Dialog
from monitor.Video import Video
'''
显示监控画面
'''
class MonitorDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        # 设置背景图片
        self.set_background_image()

        # 创建视频线程实例
        self.th1 = Video('data/vd1.mp4')

        # 连接信号和槽函数
        self.th1.send.connect(self.showimg)

        # 启动视频线程
        self.th1.start()

        # 连接按钮点击信号到 fanhui 方法
        self.ui.pushButton.clicked.connect(self.fanhui)

    def resizeEvent(self, event):
        # 调用父类的 resizeEvent
        super().resizeEvent(event)
        # 窗口大小改变时重新设置背景图片
        self.set_background_image()

    def set_background_image(self):
        # 设置 QLabel 的背景图片，并使其适应标签大小
        pixmap = QPixmap("data/bj.jpg")
        self.ui.label_3.setPixmap(pixmap.scaled(self.ui.label_3.size(), Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation))

    def showimg(self, h, w, c, b, th_id, num):
        # 创建 QImage 对象
        image = QImage(b, w, h, w * c, QImage.Format_BGR888)
        pix = QPixmap.fromImage(image)

        if th_id == 1:
            # 获取标签的宽度和高度
            width = self.ui.label_2.width()
            height = self.ui.label_2.height()

            # 缩放图片以保持宽高比
            scale_pix = pix.scaled(width, height, Qt.KeepAspectRatio)
            self.ui.label_2.setPixmap(scale_pix)

    def fanhui(self):
        # 延迟导入并显示主界面
        from monitor.mainframe import MainDialog
        self.mainframe = MainDialog()
        self.mainframe.show()

        # 关闭当前窗口
        self.close()
