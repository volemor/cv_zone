import cvzone
import mediapipe
import cv2
from cvzone.FaceDetectionModule import FaceDetector
from cvzone.ClassificationModule import Classifier



cap = cv2.VideoCapture('Video1.mp4')
detector = FaceDetector(minDetectionCon=0.8)
classif = Classifier()
while True:
    success, img = cap.read()
    detector.findFaces()

