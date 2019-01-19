import cv2
from timeit import default_timer as timer
from PIL import Image, ImageFont, ImageDraw
import numpy as np

video_path = 'FD000020-000140.mp4'
vid = cv2.VideoCapture(video_path)

if not vid.isOpened():
    raise IOError("Couldn't open webcam or video")
accum_time = 0
curr_fps = 0
fps = "FPS: ??"
prev_time = timer()
result_cnt = 1;

while True:
    return_value, frame = vid.read()
    image = Image.fromarray(frame)
    result = np.asarray(image)
    cv2.namedWindow("result", cv2.WINDOW_NORMAL)
    cv2.imshow("result", result)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    result_cnt_str = "%05d" % result_cnt
    # result_filename = "E:\extractpicfrommp4\" + result_cnt_str + ".jpg"

    result_filename = "E:\extractpicfrommp4\%05d.jpg" % result_cnt
    result_cnt = result_cnt + 1
    cv2.imwrite(result_filename, result)
    break