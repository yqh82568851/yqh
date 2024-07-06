import requests
import base64
import cv2 as cv
import logging
'''
对输入的图像进行车流量检测，并返回检测到的图像和数量信息
'''
def vehicle_detect(img):
    try:
        # 设置请求URL
        request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/vehicle_detect"

        # 将图像编码为JPEG格式
        _, encoded_image = cv.imencode('.jpg', img)

        # 将编码的图像转换为Base64格式
        base64_image = base64.b64encode(encoded_image.tobytes()).decode('utf-8')

        # 设置请求参数
        params = {"image": base64_image}

        # 设置访问令牌
        access_token = '24.42eb571f74a6fabadc5e5cafae7c5563.2592000.1722496296.282335-89994499'
        request_url = request_url + "?access_token=" + access_token

        # 设置请求头
        headers = {'content-type': 'application/x-www-form-urlencoded'}

        # 发送POST请求
        response = requests.post(request_url, data=params, headers=headers)

        # 初始化车辆计数字典
        vehicle_counts = {
            'motorbike': 0,
            'tricycle': 0,
            'car': 0,
            'truck': 0,
            'bus': 0
        }

        if response:
            # 将响应转换为JSON格式
            data = response.json()
            #print("Full response data:", data)  # 打印完整响应数据以调试

            # 获取车辆数量信息
            vehicle_num_data = data.get('vehicle_num', {})
            vehicle_counts['car'] = vehicle_num_data.get('car', 0)
            vehicle_counts['truck'] = vehicle_num_data.get('truck', 0)
            vehicle_counts['bus'] = vehicle_num_data.get('bus', 0)
            vehicle_counts['motorbike'] = vehicle_num_data.get('motorbike', 0)
            vehicle_counts['tricycle'] = vehicle_num_data.get('tricycle', 0)

            # 遍历车辆信息并绘制矩形框和标签
            for item in data.get('vehicle_info', []):
                location = item['location']
                x1 = location['left']
                y1 = location['top']
                x2 = x1 + location['width']
                y2 = y1 + location['height']
                cv.rectangle(img, (x1, y1), (x2, y2), (0, 0, 255), 2)  # 绘制矩形框
                text = item['type']
                position = (x1, y1 - 2)
                font = cv.FONT_HERSHEY_SIMPLEX
                font_scale = 1
                color = (0, 0, 255)
                thickness = 1
                img = cv.putText(img, text, position, font, font_scale, color, thickness, cv.LINE_AA)  # 绘制标签

        return img, vehicle_counts  # 返回处理后的图像和车辆计数
    except Exception as e:
        logging.error(f"Error in vehicle_detect: {e}")
        return img, {}  # 如果出现异常，返回原始图像和空的车辆计数


