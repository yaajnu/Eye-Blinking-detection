import cv2 as cv
import dlib
import time
from scipy.spatial import distance
detector=dlib.get_frontal_face_detector()
shape_detector=dlib.shape_predictor(r'shape_predictor_68_face_landmarks.dat')
# img=cv.imread(r'D:\Work\Personal\OpenCV\test.jpg')
r_start,r_end= 36, 42
l_start,l_end=42, 48
def get_np(shape,start,end):
    res=[]
    for i in range(start,end):
        res.append((shape.part(i).x,shape.part(i).y))
    return res
def plot_eye(res,img):
    for j,i in enumerate(res):
        cv.circle(img,(i[0],i[1]),1,(0,0,255),4)
def calculate_dist(eye):
    a=distance.euclidean(eye[1],eye[5])
    b=distance.euclidean(eye[2],eye[4])
    c=distance.euclidean(eye[0],eye[3])
    ear=(a+b)/(2*c)
    return ear
def check_open(dist,count,blink):
    #Checks if eyes closed , if closed upadtes the counter
    if dist<0.2:
        count+=1
    else:
        #WHen eyes open , checks if closed for more than three frames if so update the blink counter 
        # Reset the eyes closed counter regardless 
        if count>=2:
            blink+=1
        count=0
    return count,blink
cap=cv.VideoCapture(0)
start=time.time()
if not cap.isOpened():
    print('ERROR WITH CAM')
    exit()
left_blink,left_count=0,0
right_blink,right_count=0,0
while True:
    ret,frame=cap.read()
    
    if not ret:
        print('frame not read')
        break
    dets=detector(frame,1)
    for k,d in enumerate(dets):
        cv.rectangle(frame,(d.left(),d.top()),(d.right(),d.bottom()),(0,0,255),4)
        shape=shape_detector(frame,d)
        left_eye=get_np(shape,l_start,l_end)
        right_eye=get_np(shape,r_start,r_end)
        plot_eye(left_eye,frame)
        plot_eye(right_eye,frame)
        left_ear=calculate_dist(left_eye)
        right_ear=calculate_dist(right_eye)
        left_count,left_blink=check_open(left_ear,left_count,left_blink)
        right_count,right_blink=check_open(right_ear,right_count,right_blink)
        cv.putText(frame,f'Left eye blinks={left_blink}',(50,50),cv.FONT_HERSHEY_SIMPLEX,0.5,(0,0,0),1)
        cv.putText(frame,f'Right eye blinks={right_blink}',(250,50),cv.FONT_HERSHEY_SIMPLEX,0.5,(0,0,0),1)
    cv.imshow('frame',frame)
    if cv.waitKey(1)==ord('q'):
        break
end=time.time()
print(end-start)