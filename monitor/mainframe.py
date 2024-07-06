from PyQt5 import QtWidgets, QtGui, QtCore
from monitor.maind import Ui_Dialog
from monitor.carframe import CarMonitorDialog
from monitor.peopleframe import PeopleMonitorDialog
from monitor.monitorframe import MonitorDialog as MonitorFrameDialog
'''
显示主页面
'''
class MainDialog(QtWidgets.QMainWindow):
    instance = None

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls, *args, **kwargs)
            cls.instance.initialized = False
        return cls.instance

    def __init__(self):
        if self.initialized:
            return
        super().__init__()
        self.initialized = True

        self.label = QtWidgets.QLabel(self)
        self.setCentralWidget(self.label)
        self.pixmap = QtGui.QPixmap("data/bjt.jpg")

        # 设置QLabel的尺寸
        self.label.resize(self.width(), self.height())
        self.label.setScaledContents(True)
        # 将背景图片设置为QLabel的内容
        self.label.setPixmap(self.pixmap.scaled(self.label.size(), aspectRatioMode=QtCore.Qt.KeepAspectRatio,
                                                transformMode=QtCore.Qt.SmoothTransformation))
        # 监听窗口大小变化事件
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        # 设置槽函数
        self.ui.pushButton.clicked.connect(self.goin)
        self.ui.pushButton_2.clicked.connect(self.goin2)
        self.ui.pushButton_3.clicked.connect(self.goin3)
        self.ui.pushButton_4.clicked.connect(self.goin4)
        self.ui.pushButton_5.clicked.connect(self.goback)

    def on_resize(self, event):
        self.label.resize(self.width(), self.height())
        self.label.setPixmap(self.pixmap.scaled(self.label.size(), aspectRatioMode=QtCore.Qt.KeepAspectRatio,
                                                transformMode=QtCore.Qt.SmoothTransformation))

    # 退出程序按钮
    def goin4(self):
        self.close()

    # 人流量检测
    def goin3(self):
        self.peopleframe = PeopleMonitorDialog()
        self.peopleframe.show()
        self.hide()

    # 车流量检测
    def goin2(self):
        self.carframe = CarMonitorDialog()
        self.carframe.show()
        self.hide()

    # 显示监控
    def goin(self):
        self.monitorframe = MonitorFrameDialog()
        self.monitorframe.show()
        self.hide()

    # 返回登录
    def goback(self):
        from monitor.loginframe import LoginDialog
        self.loginframe = LoginDialog()
        self.loginframe.show()
        self.hide()
