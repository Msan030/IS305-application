#-----------------------------------------------------------------------#
#   predict.py将单张图片预测、摄像头检测、FPS测试和目录遍历检测等功能
#   整合到了一个py文件中，通过指定mode进行模式的修改。
#-----------------------------------------------------------------------#
import time

import cv2
import numpy as np
from PIL import Image

from yolo import YOLO

class YoloDetect:
    # Accept the input of the file path
    # crop: whether to crop the object
    # count: whether to show the count of the objects
    # Return the image with the detected object
    # Return -1 when an error has occurred
    @staticmethod
    def imageDetect(path,crop=False,count=False):
        yolo = YOLO()
        try:
            image = Image.open(path)
        except:
            print('Open Error! Try again!')
        else:
            r_image = yolo.detect_image(image, crop = crop, count=count)
            r_image.show()
            return r_image
        return -1

    # Accept the input path of video, and the save path of the video
    # video_fps: the fps of the output video
    # Return 1 when everything works properly
    @staticmethod
    def videoDetect(video_path,video_save_path,video_fps=-1):
        yolo = YOLO()
        capture = cv2.VideoCapture(video_path)
        if video_fps==-1:
            video_fps=capture.get(cv2.CAP_PROP_FPS)
        if video_save_path != "":
            fourcc = cv2.VideoWriter_fourcc(*'XVID')
            size = (int(capture.get(cv2.CAP_PROP_FRAME_WIDTH)), int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT)))
            out = cv2.VideoWriter(video_save_path, fourcc, video_fps, size)

        ref, frame = capture.read()
        if not ref:
            raise ValueError("未能正确读取摄像头（视频），请注意是否正确安装摄像头（是否正确填写视频路径）。")
            return -1

        fps = 0.0
        while (True):
            t1 = time.time()
            # 读取某一帧
            ref, frame = capture.read()
            if not ref:
                break
            # 格式转变，BGRtoRGB
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            # 转变成Image
            frame = Image.fromarray(np.uint8(frame))
            # 进行检测
            frame = np.array(yolo.detect_image(frame))
            # RGBtoBGR满足opencv显示格式
            frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

            fps = (fps + (1. / (time.time() - t1))) / 2
            print("fps= %.2f" % (fps))
            #frame = cv2.putText(frame, "fps= %.2f" % (fps), (0, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

            cv2.imshow("video", frame)
            c = cv2.waitKey(1) & 0xff
            if video_save_path != "":
                out.write(frame)

            if c == 27:
                capture.release()
                break

        print("Video Detection Done!")
        capture.release()
        if video_save_path != "":
            print("Save processed video to the path :" + video_save_path)
            out.release()
        cv2.destroyAllWindows()
        return 1

if __name__ == "__main__":
    YoloDetect.imageDetect('img/box.jpg')
    YoloDetect.videoDetect('test1.mp4','output.mp4')