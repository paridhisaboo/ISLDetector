import cv2

import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

# Setup Model & configs
base_options = python.BaseOptions(model_asset_path='gesture_recognizer.task')
options = vision.GestureRecognizerOptions(base_options=base_options)
recognizer = vision.GestureRecognizer.create_from_options(options)

# Display variables
threshold = 0.0
categ_name = "NA"
confidence = "NA"
text = ""

vid = cv2.VideoCapture(0)
while(True):
    ret, frame = vid.read()
    height, width, _ = frame.shape
    
    # Convert the frame received from OpenCV to a MediaPipe’s Image object.
    mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=frame)
    recognition_result = recognizer.recognize(mp_image)

    # If detection made with accuracy more than threshold
    if recognition_result.gestures:
        top_gesture = recognition_result.gestures[0][0]
        if top_gesture.score > threshold and top_gesture.category_name not in (''):
            # Store category name
            categ_name = top_gesture.category_name
            confidence = round(top_gesture.score, 4)
            text += " " if categ_name == "none" else categ_name

            # Highlight detected region

    # Annotate information 
    frame = cv2.putText(frame, f"Last Symbol: {categ_name}", (width - 325, height - 75), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA, False)
    frame = cv2.putText(frame, f"Confidence: {confidence}", (width - 325, height - 25), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA, False)
    frame = cv2.rectangle(frame, (width - 350, height - 125), (width, height), (0, 255, 0), 2)
    frame = cv2.putText(frame, f"Text: {text}", (width-1250, height - 25), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA, False)
        
    cv2.imshow("Webcam", frame)

    if cv2.waitKey(1) == ord('q'):
        break