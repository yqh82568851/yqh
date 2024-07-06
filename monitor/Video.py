from PyQt5.QtCore import QThread
import cv2 as cv
from PyQt5.QtCore import pyqtSignal
'''
从视频文件中读取帧，通过信号将处理后的帧发送到主线程进行显示和处理
'''
class Video(QThread):
    # 定义信号，传递视频帧数据
    send = pyqtSignal(int, int, int, bytes, int, int)

    def __init__(self, video_id):
        super().__init__()
        # 准备工作
        self.th_id = 0
        # 根据视频文件路径设置线程 ID
        if video_id == 'data/vd1.mp4':
            self.th_id = 1
        # 打开视频文件
        self.dev = cv.VideoCapture(video_id)
        self.dev.open(video_id)

    def run(self):
        # 耗时操作
        while True:
            # 读取视频帧
            ret, frame = self.dev.read()
            # 获取帧的高度、宽度和通道数
            h, w, c = frame.shape
            # 将帧转换为字节格式
            img_bytes = frame.tobytes()
            # 发射信号，传递帧数据
            self.send.emit(h, w, c, img_bytes, self.th_id, 0)
            # 休眠 10 毫秒
            QThread.usleep(10000)
