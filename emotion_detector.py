from deepface import DeepFace
import cv2

def detect_emotion():
    cap = cv2.VideoCapture(0)
    print("Capturing your emotion. Look at the camera...")
    ret, frame = cap.read()
    if not ret:
        print("Failed to capture image.")
        return None
    cv2.imwrite("temp.jpg", frame)
    cap.release()
    cv2.destroyAllWindows()

    result = DeepFace.analyze(img_path="temp.jpg", actions=["emotion"], enforce_detection=False)
    dominant_emotion = result[0]['dominant_emotion']
    print(f"Detected emotion: {dominant_emotion}")
    return dominant_emotion
