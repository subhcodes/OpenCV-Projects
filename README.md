# OpenCV-Projects


Introduction
The Facial Recognition Attendance Monitoring System is a Python-based project that utilizes facial recognition technology to automate the attendance tracking process. This system enables the efficient and accurate recording of attendance by recognizing individuals' faces and associating them with their corresponding information.

Features
Face Detection: The system detects and locates human faces in images or real-time video streams using OpenCV.
Face Recognition: It identifies and recognizes individuals by comparing their facial features with pre-registered data using the OpenCV-contrib face recognition module.
Attendance Tracking: The system records the attendance of recognized individuals, storing the information in a CSV file along with the date and time of their presence.
User Interface: The system provides a user-friendly graphical interface using the Tkinter library, allowing users to easily interact with the application.
Installation
To run the Facial Recognition Attendance Monitoring System, ensure that you have the following libraries installed:

tk-tools: pip install tk-tools
opencv-contrib-python: pip install opencv-contrib-python
datetime: pip install datetime
pytest-shutil: pip install pytest-shutil
python-csv: pip install python-csv
numpy: pip install numpy
pillow: pip install pillow
pandas: pip install pandas
times: pip install times
Usage
Clone or download the project files from the repository.
Install the required libraries as mentioned in the Installation section.
Ensure that your system has a working webcam or a video file for face detection.
Open the terminal or command prompt and navigate to the project directory.
Run the application by executing the following command: python main.py.
The application window will open, displaying options for registration and attendance tracking.
To register a new user, click on the "Register" button, provide the necessary details, and capture their face using the webcam.
To take attendance, click on the "Take Attendance" button. The system will recognize faces and mark attendance accordingly.
The attendance records will be stored in a CSV file named "attendance_records.csv" with the date and time.
Notes
It is recommended to have sufficient lighting conditions for accurate face detection and recognition.
Ensure that the captured images for registration contain clear and unobstructed views of individuals' faces.
The system may require occasional updates to improve recognition accuracy and performance.
Conclusion
The Facial Recognition Attendance Monitoring System simplifies the attendance tracking process by automating the identification and recording of individuals. By leveraging facial recognition technology, the system offers an efficient and accurate solution for attendance management in various educational and professional environments.
