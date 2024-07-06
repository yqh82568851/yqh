import logging
logging.basicConfig(level=logging.DEBUG)
from PyQt5.QtCore import QThread, pyqtSignal
import cv2 as cv
import logging
from ai.people import people_detect
'''
从视频文件中读取帧，并对每个帧进行人流检测，然后通过信号将处理后的帧和检测结果发送到主线程进行显示和处理
'''
class Video(QThread):
    # 定义信号，传递视频帧数据以及人流检测结果
    send = pyqtSignal(int, int, int, bytes, int, int, int, int)

    def __init__(self, video_id, case_id):
        super().__init__()
        self.th_id = 0
        self.running = True
        self.case_id = case_id
        self.case_init = True
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
                # 对帧进行人流检测
                frame, nums = people_detect(frame, self.case_id, self.case_init)
                # 初始化后设为False，避免重复初始化
                self.case_init = False
                # 获取帧的高度、宽度和通道数
                h, w, c = frame.shape
                # 将帧转换为字节格式
                img_bytes = frame.tobytes()
                # 获取检测到的人数和进出人数统计
                person_num = nums.get('person_num', 0)
                in_count = nums.get('in', 0)
                out_count = nums.get('out', 0)
                print
                # 发射信号，传递帧数据和人流检测结果
                self.send.emit(h, w, c, img_bytes, self.th_id, person_num, in_count, out_count)
                # 休眠 10000 微秒 (10 毫秒)
                QThread.usleep(1000000)
            except Exception as e:
                logging.error(f"Error in Video thread: {e}")
                break

    def stop(self):
        # 停止视频线程
        self.running = False
        self.wait()
