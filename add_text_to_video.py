import cv2
import datetime

cap = cv2.VideoCapture(0)


print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

while cap.isOpened():
    ret, frame = cap.read()

    currentdt = datetime.datetime.now()
    text = str(currentdt)
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame, text, (10, 50), font, 1, (255, 255, 0), 1, cv2.LINE_AA)

    if ret == True:
        cv2.imshow("frame", frame)


        if cv2.waitKey(1) == ord('q'):
            break
    else:
        break


cap.release()
cv2.destroyAllWindows()