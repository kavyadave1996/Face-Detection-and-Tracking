import cv2


cascade_classifier = cv2.CascadeClassifier('C:/Python27/haarcascades/haarcascade_frontalface_default.xml')
eye_classifier = cv2.CascadeClassifier('C:/Python27/haarcascades/haarcascade_eye.xml')
vid_cap = cv2.VideoCapture(0)

while True:
	ret , frame = vid_cap.read()
	gray = cv2.cvtColor(frame,0)
	detections = cascade_classifier.detectMultiScale(gray,1.3,5)
	
	for (x,y,w,h) in detections:
		cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
		roi_gray = gray[y:y+h, x:x+w] # this particular code will return the cropped face from the image.
		roi_color = frame[y:y+h,x:x+w] # this particular code will return the details of the image that u will receive after getting the coordinates of the image.
        eye = eye_classifier.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eye:
        	cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
        
	cv2.imshow('frame',frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
    
vid_cap.release()
cv2.destroyAllWindows()