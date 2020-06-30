import cv2

#capture from camera
objCapture = cv2.VideoCapture(0)

#to capture from file
#objCapture = cv2.VideoCapture("name.avi")

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('media/output.mp4', fourcc, 20.0, (640, 480))

while objCapture.isOpened():
    ret, frame = objCapture.read()

    if ret == True:

        #to save it to a output file
        out.write(frame)

        #to display the image as it is
        #cv2.imshow('video', frame)

        #print(objCapture.get(cv2.CAP_PROP_FRAME_HEIGHT))
        #print(objCapture.get(cv2.CAP_PROP_FRAME_WIDTH))

        #to display the image in gray
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('gray video', gray)

        if cv2.waitKey(1) == ord('q'):
            break
    else:
        break

objCapture.release()
out.release()
cv2.destroyAllWindows()
