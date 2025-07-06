👤🤖 AI-Powered Face Recognition Attendance System with Humanoid Robot 


![image](https://github.com/user-attachments/assets/32bde8d9-32cd-4891-9365-29b93d617580)


This project implements an AI-driven facial recognition system integrated with a humanoid robot that greets recognized individuals and logs their attendance. It uses computer vision (OpenCV, MediaPipe, face_recognition), speech synthesis (gTTS), servo-based gestures (AiNex SDK), and real-time logging (Excel via pandas). The robot not only identifies known faces but also greets them personally and records their entry into an Excel sheet.

🚀 Features
🎯 Real-time Face Detection and Recognition
Detects and recognizes faces from a live video stream using MediaPipe and face_recognition.


![image](https://github.com/user-attachments/assets/47a51563-10ea-4826-850a-fd80045bcae4)




📊 Attendance Logging
Logs recognized names with timestamps into an Excel sheet (.xlsx format) for attendance tracking.


![excelop](https://github.com/user-attachments/assets/feec15c2-83cf-408a-9163-97dac1fe18bd)



🗣️ Personalized Voice Greetings
Uses gTTS to greet known individuals with a custom message and deletes the temporary audio file after playback.

🤖 Humanoid Gestures
Performs greeting gestures using the AiNex SDK and MotionManager for a more interactive experience.

![image](https://github.com/user-attachments/assets/4892dc32-1904-4ad9-8a9a-60b831e45cd0)


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

📁 File Structure
bash
Copy
Edit
├── main.py                      # Main script with face detection and control logic
├── venky.jpeg                   # Sample known face
├── baalu.jpeg
├── naidu.jpeg
├── suresh_sir.jpeg
├── indhira_mam.jpeg
├── face_recognition_log.xlsx    # Auto-generated attendance log
⚙️ How It Works
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
