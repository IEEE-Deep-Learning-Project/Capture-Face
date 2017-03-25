import cv2


def model_predict():
    return "Male"


def recognize_person():
    gender = ""
    face_cascade = cv2.CascadeClassifier('face_detection_xml/face_cascade_classifier.xml')
    video_capture = cv2.VideoCapture(0)
    face_detected = False
    while True:
        # Capture frame-by-frame
        ret, frame = video_capture.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
            image = frame[y:y+h, x:x+w]
            cv2.imwrite('face.png', image)
            gender = model_predict()
            face_detected = True
        if face_detected:
            cv2.putText(image, gender, (image.shape[1]/5, image.shape[0]/5), cv2.FONT_HERSHEY_SIMPLEX, 2, 255)
            cv2.imshow("Prediction", image)
            raw_input("Enter To continue")
            face_detected = False
        cv2.imshow('img', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    # When everything is done, release the capture
    video_capture.release()
    cv2.destroyAllWindows()

recognize_person()
