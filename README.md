👤🤖 AI-Powered Face Recognition Attendance System with Humanoid Robot 

This project implements an AI-driven facial recognition system integrated with a humanoid robot that greets recognized individuals and logs their attendance. It uses computer vision (OpenCV, MediaPipe, face_recognition), speech synthesis (gTTS), servo-based gestures (AiNex SDK), and real-time logging (Excel via pandas). The robot not only identifies known faces but also greets them personally and records their entry into an Excel sheet.

🚀 Features
🎯 Real-time Face Detection and Recognition
Detects and recognizes faces from a live video stream using MediaPipe and face_recognition.

📊 Attendance Logging
Logs recognized names with timestamps into an Excel sheet (.xlsx format) for attendance tracking.

🗣️ Personalized Voice Greetings
Uses gTTS to greet known individuals with a custom message and deletes the temporary audio file after playback.

🤖 Humanoid Gestures
Performs greeting gestures using the AiNex SDK and MotionManager for a more interactive experience.

🧠 Face Memory
Prevents repeated greetings in a single session by tracking already greeted individuals.

🧩 Technologies Used
Technology	Purpose
OpenCV	Camera access, image handling, bounding boxes
MediaPipe	Efficient face detection
face_recognition	Face encoding and matching
NumPy	Array operations for face distance matching
pandas	Attendance logging in Excel files
gTTS	Text-to-Speech for audio greetings
AiNex SDK	Servo motor control for humanoid gestures
cv2.VideoCapture	Webcam video input

Face Encoding
Loads and encodes predefined images of known individuals.

Live Detection
Continuously reads frames from the webcam and detects faces.

Recognition & Matching
Compares detected faces to known encodings and identifies matches.

Greeting & Logging
If a match is found and the person hasn't been greeted yet:

Logs name and timestamp to Excel.

Plays a personalized greeting via gTTS.

Executes a humanoid gesture.


🎓 Use Cases
Smart Attendance in Educational Institutions

Office Entry Automation with Personalization

Human-Robot Interaction Demonstrations
