import cv2

cam = cv2.VideoCapture(1)
classifier = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

while True:
    status, frame = cam.read()
    gray_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = classifier.detectMultiScale(gray_image, 1.3, 5)
    for face in faces:
        x = face[0]
        y = face[1]
        w = face[2]
        h = face[3]
        cv2.rectangle(frame, (x, y), (x+w, y+h), (139, 75, 123), 2)
        cv2.putText(frame, "Face", (x, y - 20), cv2.FONT_HERSHEY_TRIPLEX, 1, (0, 255, 0), 1)

    cv2.imshow("My Faces", frame)

    if cv2.waitKey(1) == ord("q"):
        break

cv2.destroyAllWindows()
cam.release()


# image = cv2.imread("./celeb.jpeg")
# gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# classifier = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
# faces = classifier.detectMultiScale(gray_image, 1.3, 5)
# for face in faces:
#     x = face[0]
#     y = face[1]
#     w = face[2]
#     h = face[3]

#     cv2.rectangle(image, (x, y), (x+w, y+h), (139, 75, 123), 2)

# while True:
#     cv2.imshow("My Image", image)
#     # cv2.imshow("My Gray Image", gray_image)
#     if cv2.waitKey(1) == ord("q"):
#         break
# cv2.destroyAllWindows()
