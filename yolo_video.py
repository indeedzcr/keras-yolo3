
from yolo import YOLO
from yolo import detect_video



if __name__ == '__main__':
    # video_path='path2your-video'
    # video_path='FD000020-000140.mp4'
    video_path='TW000500-000530.mp4'
    detect_video(YOLO(), video_path)
