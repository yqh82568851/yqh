from PyQt5 import QtWidgets, QtGui, QtCore
from monitor.login import Ui_Dialog
'''
显示登录
'''
class LoginDialog(QtWidgets.QMainWindow):
    instance = None  # 静态变量，存储单例对象

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls, *args, **kwargs)
            cls.instance.initialized = False  # 标记初始化状态
        return cls.instance

    def __init__(self):
        if self.initialized:
            return  # 如果已经初始化，直接返回
        super().__init__()
        self.initialized = True  # 标记为已初始化

        # 设置背景图片
        self.label = QtWidgets.QLabel(self)
        self.setCentralWidget(self.label)
        self.pixmap = QtGui.QPixmap("data/bjt.jpg")
        self.label.resize(self.width(), self.height())  # 设置 QLabel 的尺寸
        self.label.setScaledContents(True)  # 使图片自适应标签大小
        self.label.setPixmap(self.pixmap.scaled(self.label.size(), aspectRatioMode=QtCore.Qt.KeepAspectRatio,
                                                transformMode=QtCore.Qt.SmoothTransformation))  # 设置图片

        # 监听窗口大小变化事件
        self.resizeEvent = self.on_resize

        # 设置 UI
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        # 设置密码框
        self.ui.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)

        # 连接登录按钮的点击信号到登录函数
        self.ui.pushButton.clicked.connect(self.login_)

    def on_resize(self, event):
        self.label.resize(self.width(), self.height())  # 调整 QLabel 的尺寸
        self.label.setPixmap(self.pixmap.scaled(self.label.size(), aspectRatioMode=QtCore.Qt.KeepAspectRatio,
                                                transformMode=QtCore.Qt.SmoothTransformation))  # 重新设置图片

    def login_(self):
        username = self.ui.lineEdit.text()  # 获取用户名
        password = self.ui.lineEdit_2.text()  # 获取密码

        # 验证用户名和密码
        if username == "123" and password == "123":
            try:
                from monitor.mainframe import MainDialog
                self.mainframe = MainDialog()  # 打开主界面
                self.mainframe.show()
                self.hide()
            except Exception as e:
                print(f"Error opening MainDialog: {e}")
                self.show_warning("错误", f"无法打开主界面: {e}")
        else:
            self.show_warning("登录失败", "用户名或密码错误！")  # 显示登录失败信息

    def show_warning(self, title, message):
        if hasattr(self, 'msg_box') and self.msg_box.isVisible():
            return  # 如果警告框已经显示，直接返回
        self.msg_box = QtWidgets.QMessageBox(self)
        self.msg_box.setWindowTitle(title)  # 设置警告框标题
        self.msg_box.setText(message)  # 设置警告框内容
        self.msg_box.setIcon(QtWidgets.QMessageBox.Warning)  # 设置警告图标
        self.msg_box.exec_()  # 显示警告框

