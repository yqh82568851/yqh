from collections import deque
import cv2 as cv
import base64
import requests
import numpy as np
import logging
'''
对输入的图像进行人流量检测，并返回检测到的图像和数量信息
'''

# 使用 KCF 跟踪器对输入图像中的多个目标进行跟踪，并通过平滑处理减少跟踪结果的抖动
class Tracker:
    def __init__(self):
        self.trackers = []
        self.prev_positions = deque(maxlen=5)  # 用于存储前几帧的位置，用于平滑处理

    def update(self, img, person_info):
        # 初始化跟踪器
        if not self.trackers:
            self.trackers = [cv.TrackerKCF_create() for _ in person_info]
            for tracker, item in zip(self.trackers, person_info):
                bbox = (item['location']['left'], item['location']['top'], item['location']['width'], item['location']['height'])
                tracker.init(img, bbox)
        else:
            for tracker in self.trackers:
                success, bbox = tracker.update(img)
                if success:
                    p1 = (int(bbox[0]), int(bbox[1]))
                    p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
                    cv.rectangle(img, p1, p2, (0, 255, 0), 2, 1)
                    # 更新位置
                    self.prev_positions.append(p1)

                    # 计算平滑后的位置
                    if len(self.prev_positions) > 1:
                        avg_p1 = np.mean(self.prev_positions, axis=0).astype(int)
                        p1 = tuple(avg_p1)
                        p2 = (avg_p1[0] + int(bbox[2]), avg_p1[1] + int(bbox[3]))
                        cv.rectangle(img, p1, p2, (0, 0, 255), 2, 1)
                    else:
                        cv.rectangle(img, p1, p2, (0, 0, 255), 2, 1)

# 检测人流量
def people_detect(img, case_id, case_init=True, tracker=None):
    try:
        # 设置请求URL
        request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/body_tracking"

        # 将图像编码为JPEG格式
        _, encoded_image = cv.imencode('.jpg', img)

        # 将编码的图像转换为Base64格式
        base64_image = base64.b64encode(encoded_image.tobytes()).decode('utf-8')

        # 设置请求参数
        params = {
            "dynamic": "true",          # 是否动态检测
            "case_id": 2,               # 案例ID
            "case_init": "false",       # 是否初始化案例
            "image": base64_image,      # 图像数据
            "area": "1,1,340,1,340,340,1,340",  # 检测区域

            "show": "false"             # 是否显示检测结果
        }

        # 设置访问令牌
        access_token = '24.e415472d6a905d66d4e958488aadccd5.2592000.1722756994.282335-90985059'
        request_url = request_url + "?access_token=" + access_token

        # 设置请求头
        headers = {'content-type': 'application/x-www-form-urlencoded'}

        # 发送POST请求
        response = requests.post(request_url, data=params, headers=headers)

        # 初始化人流量统计字典
        people_counts = {
            'person_num': 0,  # 人数
            'in': 0,          # 进入人数
            'out': 0          # 离开人数
        }

        if response:
            # 将响应转换为JSON格式
            data = response.json()

            # 更新人流量统计
            people_counts['person_num'] = data.get('person_num', 0)
            person_count = data.get('person_count', {})
            people_counts['in'] = person_count.get('in', 0)
            people_counts['out'] = person_count.get('out', 0)

            # 获取person_info信息
            person_info = data.get('person_info', [])
            if len(person_info) != people_counts['person_num']:
                logging.warning("Number of persons in person_info does not match person_num")

            if tracker is not None:
                tracker.update(img, person_info)
            else:
                for item in person_info:
                    location = item['location']
                    x1 = location['left']
                    y1 = location['top']
                    x2 = x1 + location['width']
                    y2 = y1 + location['height']
                    cv.rectangle(img, (x1, y1), (x2, y2), (0, 0, 255), 2)  # 绘制矩形框
                    text = item.get('type', 'Person')
                    position = (x1, y1 - 2)
                    font = cv.FONT_HERSHEY_SIMPLEX
                    font_scale = 1
                    color = (0, 0, 255)
                    thickness = 1
                    img = cv.putText(img, text, position, font, font_scale, color, thickness, cv.LINE_AA)  # 绘制标签

        return img, people_counts  # 返回处理后的图像和人流量统计
    except Exception as e:
        logging.error(f"Error in people_detect: {e}")
        return img, {}  # 如果出现异常，返回原始图像和空的人流量统计




