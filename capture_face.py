import cv2


def recognize_person():
    face_cascade = cv2.CascadeClassifier('face_detection_xml/face_cascade_classifier.xml')
    video_capture = cv2.VideoCapture(0)
    while True:
        # Capture frame-by-frame
        ret, frame = video_capture.read()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            print "Face Detected!!"
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
            image = frame[y:y+h, x:x+w]
            cv2.imwrite('face.png', image)
            exit(0)
        cv2.imshow('img', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    # When everything is done, release the capture
    video_capture.release()
    cv2.destroyAllWindows()

recognize_person()