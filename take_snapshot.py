import cv2

def take_snapshot():
    #initialising cv2
    videoCaptureObject=cv2.VideoCapture(0)
    result= True
    while(result):
        #read the frame when camera is on
        ret,frame=videoCaptureObject.read()
        #cv2.inwrite() method is used to save an image to any storage device
        cv2.inwrite("NewPicture1.jpg",image)
        result= False

    #release the camera
    videoCaptureObject.release()
    cv2.destroyAllWindows()
take_snapshot()