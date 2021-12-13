import cv2 as cv
cap=cv.VideoCapture(0)
if not cap.isOpened():
    print('Camera faulty try again')
    exit()
# frame_count=0
# h=cap.get(cv.CAP_PROP_FRAME_HEIGHT)
# w=cap.get(cv.CAP_PROP_FRAME_WIDTH)
# while True:
#     frame_count+=1
    
#     ret,frame=cap.read()
#     frame=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
#     img_blur=cv.GaussianBlur(frame,(3,3),sigmaX=0.0,sigmaY=0.0)
#     if not ret:
#         print('Cant read frame')
#         break
#     sobel=cv.Canny(img_blur,100,200)
#     cv.putText(frame,str(frame_count),(50,50),cv.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2,cv.LINE_AA)
#     cv.imshow('FRAME',frame)
#     if cv.waitKey(1)==ord('q'):
#         break
# cap.release()
# cv.destroyAllWindows()c
