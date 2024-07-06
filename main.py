import sys
from monitor.monitorapp import MonitorApp
'''
运行后登录时默认
用户名为：123
密码为：123
否则会登录失败
'''
if __name__ == '__main__':
    app = MonitorApp()
    sys.exit(app.exec())
