import cv2
import mediapipe as mp
import face_recognition
import numpy as np
import time
import pandas as pd
from datetime import datetime
from ainex_sdk import hiwonder_servo_controller
from ainex_kinematics.motion_manager import MotionManager
from gtts import gTTS
import os

# Function to speak and delete the speech file
def speak_and_delete(text):
    filename = "temp_speech.mp3"
    tts = gTTS(text=text, lang='en')
    tts.save(filename)

    # Play the MP3 file
    os.system(f"mpg321 {filename}")  # For Linux

    # Wait to ensure the file finishes playing before deletion
    time.sleep(2)
    os.remove(filename)
    print("Speech completed, file deleted.")

# Create or load the attendance Excel file
excel_file = "face_recognition_log.xlsx"

# Check if the file exists, if not, create it
if not os.path.exists(excel_file):
    df = pd.DataFrame(columns=["Name", "Time"])
    df.to_excel(excel_file, index=False)

# Function to log recognized face data
def log_face(name):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    new_entry = pd.DataFrame({"Name": [name], "Time": [now]})

    df = pd.read_excel(excel_file)
    df = pd.concat([df, new_entry], ignore_index=True)
    df.to_excel(excel_file, index=False)
    print(f"Logged {name} at {now}")

# Initialize motion manager and start position
motion_manager = MotionManager()
motion_manager.run_action('forward')
time.sleep(1)
motion_manager.run_action('stand')

# Mediapipe Face Detection
mp_face_detection = mp.solutions.face_detection
face_detection = mp_face_detection.FaceDetection(min_detection_confidence=0.5)

# Load known faces and their encodings
known_faces = [
    {"name": "venky", "image": "venky.jpeg"},
    {"name": "baalu", "image": "baalu.jpeg"},
    {"name": "Naidu", "image": "naidu.jpeg"},
    {"name": "Sureshsir", "image": "suresh_sir.jpeg"},
    {"name": "Indhiramam", "image": "indhira_mam.jpeg"}
]

# Encode known faces
known_encodings = []
for person in known_faces:
    image = face_recognition.load_image_file(person["image"])
    encoding = face_recognition.face_encodings(image)[0]
    known_encodings.append({"name": person["name"], "encoding": encoding})

# Keep track of greeted people
greeted_people = set()

# Webcam initialization
video_capture = cv2.VideoCapture("/dev/usb_cam")
servo_control = hiwonder_servo_controller.HiwonderServoController('/dev/ttyAMA0', 115200)

while True:
    ret, frame = video_capture.read()
    if not ret:
        break

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = face_detection.process(rgb_frame)

    if results.detections:
        for detection in results.detections:
            bboxC = detection.location_data.relative_bounding_box
            ih, iw, _ = frame.shape
            x = int(bboxC.xmin * iw)
            y = int(bboxC.ymin * ih)
            w = int(bboxC.width * iw)
            h = int(bboxC.height * ih)

            if x >= 0 and y >= 0 and w > 0 and h > 0 and x + w <= iw and y + h <= ih:
                face_image = frame[y:y+h, x:x+w]

                if face_image.size != 0:
                    face_rgb = cv2.cvtColor(face_image, cv2.COLOR_BGR2RGB)
                    face_encodings = face_recognition.face_encodings(face_rgb)

                    if face_encodings:
                        face_encoding = face_encodings[0]
                        matches = face_recognition.compare_faces([person["encoding"] for person in known_encodings], face_encoding)
                        face_distances = face_recognition.face_distance([person["encoding"] for person in known_encodings], face_encoding)
                        best_match_index = np.argmin(face_distances)

                        name = "Unknown"
                        if matches[best_match_index]:
                            name = known_encodings[best_match_index]["name"]

                            if name not in greeted_people:
                                greeted_people.add(name)
                                log_face(name)  # Log the face into Excel

                                if name == 'venky':
                                    speak_and_delete("Good morning venky sir, welcome to the IT Department")
                                    motion_manager.run_action('greet')

                                elif name == 'Naidu':
                                    speak_and_delete("Good morning Naidu, Jai Balayya")
                                    motion_manager.run_action('greet')

                                elif name == 'Sureshsir':
                                    speak_and_delete("Good morning Suresh sir, welcome to the IT Department")
                                    motion_manager.run_action('greet')

                                elif name == 'Indhiramam':
                                    speak_and_delete("Good morning Indhira mam, welcome to the IT Department")
                                    motion_manager.run_action('greet')

                                elif name == 'Venky':
                                    speak_and_delete("Good morning Venky, welcome to the IT Department")
                                    motion_manager.run_action('greet')

                        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
                        cv2.putText(frame, name, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
                else:
                    print("Warning: Empty face region detected.")
            else:
                print("Warning: Invalid bounding box coordinates detected.")

    cv2.imshow('Known Face Detector', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()