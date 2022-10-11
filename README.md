# OpenCV-Color_Detection_To_SQL_DB
Utilizes OpenCV color detection and outputs results to an SQL database

Requirements:
-MySQL
-OpenCV
-PrettyTable

How to use:
-Have the three python files in the same folder and run DroneColorDetection, it should bring up a window showing the webcam feed and have overlays for the objects it sees which have the target color (or in range of based on upper and lower variables which are in HSL)

NetworkTable.py:
Connects to the SQL database and places/deletes/gets data from the database

VisionCV.py:
Is where the OpenCV color detection is processed

DroneColorDetection.py:
Processes the color detection and puts data from the color detection into the database
  - Objects seeen are labled by index starting at 0
  - Index -1 hold the count of the valid objects seen
