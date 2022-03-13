import cv2
import cvzone
from cvzone.FaceMeshModule import FaceMeshDetector
from cvzone.HandTrackingModule import HandDetector

# face detecting

img1= cv2.imread('image.jpg')
img1 = cv2.resize(img1, (50,50))
h, w, _ = img1.shape
cap = cv2.VideoCapture(0)#'video1.mp4')
detector = FaceMeshDetector( maxFaces=3)
pointList = [ 10]
pointPosList =[]
fourcc = cv2.VideoWriter_fourcc(*'MPEG')
out_video = cv2.VideoWriter('video_out.avi', fourcc, 25,(640, 480) )
maxList=0
while True: #maxList < 600:
    # if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):
    #     cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
    maxList +=1
    success, img = cap.read()
    img , faces = detector.findFaceMesh(img, draw=True )

    if faces:
        face = faces[0]
        for id in pointList:
            cv2.circle(img, face[id], 15,(255,0,255) , thickness=3)
            # print(face[id])
        pointPosList.append(face[id])
        # print(pointPosList)
        for i, pionts in enumerate(pointPosList):
             cv2.circle(img, pointPosList[i], 15-i, (255, 0, 255), thickness=1)
        if len(pointPosList)> 10:
             pointPosList.pop(0)


            # img [y:y+h, x:x+w] = img1
    # img = cv2.resize(img, (330,640))
    img = cv2.resize(img, (1080,720))
    cv2.imshow("image", img)
    out_video.write(img)
    cv2.waitKey(3)

out_video.release()

