from PyQt5.QtWidgets import QApplication
from monitor.loginframe import LoginDialog
import sys


class MonitorApp(QApplication):
    def __init__(self):
        super(MonitorApp, self).__init__(sys.argv)
        self.dialog = LoginDialog()
        self.dialog.show()
