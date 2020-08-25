import cv2

cam = cv2.VideoCapture(0)

while True:
    ret, frame = cam.read()

    if ret is True:
        cv2.imshow("This is OpenCV Workshop",frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
