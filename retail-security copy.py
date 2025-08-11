import cv2
import requests
from twilio.rest import Client

# ===== Custom Vision Setup =====
PREDICTION_KEY = ""
PREDICTION_ENDPOINT = ""
THRESHOLD = 0.15

# ===== Twilio Setup =====
TWILIO_SID = ""
TWILIO_AUTH = ""
FROM_NUMBER = ""  # Twilio number
TO_NUMBER = ""    # Your mobile

twilio_client = Client(TWILIO_SID, TWILIO_AUTH)

# ===== Video Processing =====
video_path = "test_vid.mp4"
cap = cv2.VideoCapture(video_path)

ret, frame = cap.read()
if ret:
    # Save frame as image
    frame_path = "frame.jpg"
    cv2.imwrite(frame_path, frame)

    # Send image to Custom Vision Prediction API
    headers = {
        "Prediction-Key": PREDICTION_KEY,
        "Content-Type": "application/octet-stream"
    }

    with open(frame_path, "rb") as image_data:
        response = requests.post(PREDICTION_ENDPOINT, headers=headers, data=image_data)
    
    results = response.json()

    # Extract detected objects
    detected_items = []
    for prediction in results["predictions"]:
        if prediction["probability"] >= THRESHOLD:
            detected_items.append(prediction["tagName"])

    print("Detected objects:", detected_items)

    # If knife detected, send SMS
    if "knife" in [item.lower() for item in detected_items]:
        sms_body = f"ALERT: Knife detected in video frame! Objects: {', '.join(detected_items)}"
        twilio_client.messages.create(body=sms_body, from_=FROM_NUMBER, to=TO_NUMBER)
        print("SMS Sent!")

cap.release()
