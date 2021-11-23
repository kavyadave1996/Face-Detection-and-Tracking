import cv2


cascade_classifier = cv2.CascadeClassifier('C:/Python27/haarcascades/haarcascade_frontalface_default.xml')
my_cap = cv2.VideoCapture(0)
while True:
	ret , frame = my_cap.read()
	gray = cv2.cvtColor(frame,0)
	detections = cascade_classifier.detectMultiScale(gray,1.3,5)
	
    if(len(detections)>0):
    	(x,y,w,h) = detections[0]
    	frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):b
		break
    
my_cap.release()
cv2.destroyAllWindows()