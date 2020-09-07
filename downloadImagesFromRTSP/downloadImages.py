import os
BASE_DIR = os.path.dirname(os.path.realpath(__file__))

import cv2
import imutils
from imutils.video import FPS
import datetime
import time
import pandas as pd


def checkDir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)


def getCurrentTime():
    return datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d-%H-%M-%S-%f')


def getCameraList(filePath = './data/csv/Camera_Names_with_Coordinates_Updated.csv'):

    df = pd.read_csv(filePath)
    df = df.dropna(axis=0, subset=['ip_address'])
    currentTIme = '_'+datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d-%H-%M-%S')
    df['rtsp'] = df.apply(lambda x : 'rtsp://' + str(x.admin)+':'+str(x.password)+'@'+x.ip_address +'/1/h264major',axis=1)
    return df




def getImageDownload(folder_name,rtsp_link):

    try:
        stream = cv2.VideoCapture()

        fps = FPS().start()

        stream.open(rtsp_link)
        time.sleep(1)
        # Capture frame-by-frame
        # grab the frame from the threaded video file stream
        (grabbed, frame) = stream.read()


        directory = BASE_DIR + '/imageDownload_' + \
            datetime.datetime.now().strftime('%Y-%m-%d') + '/'

        checkDir(directory)

        directory = directory + str(folder_name) + '/'
        checkDir(directory)

        filePath = directory + getCurrentTime() + '.jpg'
        print(filePath)
        # frame = draw_BBox(frame, bboxes)
        # Display the resulting frame
        #cv2.imshow('Pothole',frame)
        cv2.imwrite(filePath,frame)
        #cv2.waitKey(5000)

        stream.release()
        # cv2.destroyAllWindows()

        return frame
    except Exception as e:
        print(e)
        stream.release()



if __name__ == "__main__":

    df = getCameraList('./RTSP.csv')

    for index in df.index:

        getImageDownload(df['camera_name'][index],df['rtsp'][index])
    pass
