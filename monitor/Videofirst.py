from PyQt5.QtCore import QThread, pyqtSignal
import cv2 as cv
from ai.car import vehicle_detect
import logging
logging.basicConfig(level=logging.DEBUG)
'''
从视频文件中读取帧，并对每个帧进行车辆检测，然后通过信号将处理后的帧和检测结果发送到主线程进行显示和处理
'''
class Video(QThread):
    # 定义信号，传递视频帧数据以及车辆检测结果
    send = pyqtSignal(int, int, int, bytes, int, int, int, int, int, int, object)

    def __init__(self, video_id):
        super().__init__()
        self.th_id = 0
        self.running = True
        # 根据视频文件路径设置线程 ID
        if video_id == 'data/vd1.mp4':
            self.th_id = 1
        # 打开视频文件
        self.dev = cv.VideoCapture(video_id)
        # 检查视频文件是否成功打开
        if not self.dev.isOpened():
            logging.error(f"Error opening video file: {video_id}")

    def run(self):
        # 主线程循环
        while self.running:
            try:
                # 读取视频帧
                ret, frame = self.dev.read()
                if not ret:
                    logging.error("Failed to read frame")
                    break
                # 对帧进行车辆检测
                frame, nums = vehicle_detect(frame)
                #print(nums)
                # 获取帧的高度、宽度和通道数
                h, w, c = frame.shape
                # 将帧转换为字节格式
                img_bytes = frame.tobytes()
                # 发射信号，传递帧数据和车辆检测结果
                self.send.emit(h, w, c, img_bytes, self.th_id, nums['car'], nums['truck'], nums['bus'],
                               nums['motorbike'], nums['tricycle'],self.dev)
                # 休眠 1000 毫秒 (1 秒)
                QThread.msleep(1000)
            except Exception as e:
                logging.error(f"Error in Video thread: {e}")
                break
        # 释放视频捕捉对象
        self.dev.release()


    def stop(self):
        # 停止视频线程
        self.running = False
        # self.quit()
        self.wait()

