import cv2 as cv
import numpy as np

cascade_clf=cv.CascadeClassifier()
face_clf=cv.CascadeClassifier()
face_clf.load(cv.samples.findFile(r'D:\Work\Personal\OpenCV\haarcascade_frontalface_alt.xml'))
cascade_clf.load(cv.samples.findFile(r'D:\Work\Personal\OpenCV\haarcascade_eye_tree_eyeglasses.xml'))
# img=cv.imread(r'D:\Work\Personal\OpenCV\test.jpg')
# img_gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# face_dets=face_clf.detectMultiScale(img_gray)
# for (x,y,w,h) in face_dets:
#     bot_right=(x+w,y+h)
#     top_left=(x,y)    
# cv.rectangle(img,top_left,bot_right,(0,0,255),2)
# face_ro=img_gray[y:y+h,x:x+w]
# eye_dets=cascade_clf.detectMultiScale(face_ro)
# for i,(x2,y2,w2,h2) in enumerate(eye_dets):
#     print(i)
#     x2,y2,w2,h2=eye_dets[0]
#     eye_center = (x + x2 + w2//2, y + y2 + h2//2)
#     radius = int(round((w2 + h2)*0.25))
#     cv.circle(img, eye_center, radius, (255, 0, 0 ), 4)
# cv.imshow('frame',img)
# cv.waitKey(0)

cap=cv.VideoCapture(0)
if not cap.isOpened():
    print('Camera faulty try again')
    exit()
while True:
    ret,frame=cap.read()
    if not ret:
        print('Frame isssue exists')
        break
    img_gray=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    face_det=face_clf.detectMultiScale(img_gray)
    for (x,y,w,h) in face_det:
        centre=(x+w//2,y+h//2)
        top_left=(x,y)
        bot_right=(x+w,y+h)
        cv.rectangle(frame,top_left,bot_right,(0,0,255),2)
    # Y comes first as indexed by rows
        face_roi=img_gray[y:y+h,x:x+w]
        eye_det=cascade_clf.detectMultiScale(face_roi)
        for (x2,y2,w2,h2) in eye_det:
            c=(x+x2+w2//2,y+y2+h2//2)
            r=int(round((w2 + h2)*0.25))
            cv.circle(frame,c,r,(0,0,255),4)
    cv.imshow('frame',frame)
    if cv.waitKey(1)==ord('q'):
        break