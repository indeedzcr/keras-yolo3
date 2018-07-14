import numpy as np
import cv2
from yolo import YOLO
from yolo import detect_video
from PIL import Image, ImageFont, ImageDraw

import colorsys
import os
import random
from timeit import default_timer as timer

import numpy as np
from keras import backend as K
from keras.models import load_model
from keras.layers import Input
from PIL import Image, ImageFont, ImageDraw

from yolo3.model import yolo_eval, yolo_body, tiny_yolo_body
from yolo3.utils import letterbox_image


cap = cv2.VideoCapture(0)
cnt = 99
while True:
    cnt = cnt + 1
    ret, frame = cap.read()
    image = Image.fromarray(frame)
    if cnt == 100000000:
        image = YOLO.detect_image(YOLO(),image)
        cnt = 0
    image = np.asarray(image)
    cv2.imshow("Frame", image)
    c = cv2.waitKey(50)
    k = cv2.waitKey(30) & 0xFF
    if k == 32:
        break


