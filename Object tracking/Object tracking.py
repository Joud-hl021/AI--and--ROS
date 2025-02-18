# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 19:42:17 2025

@author: Judea
"""

import cv2
import sys

# Load the video (Make sure the path is correct)
video_path = r"C:\Users\Judea\Desktop\mnmnmn.mp4"
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Error: Video file not found!")
    sys.exit()

# Select tracking type (CSRT is accurate, KCF is faster)
tracker = cv2.legacy.TrackerCSRT_create()

# Read the first frame from the video
ret, frame = cap.read()
if not ret:
    print("Error: Unable to load video!")
    sys.exit()

# Select the object manually with the mouse
print("Select the object with the mouse...")
bbox = cv2.selectROI("Select Object for Tracking", frame, False)
tracker.init(frame, bbox)

while True:
    ret, frame = cap.read()
    if not ret:
        break  # Video ended

    # Update object position
    success, bbox = tracker.update(frame)

    if success:
        x, y, w, h = [int(i) for i in bbox]
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)  # Draw tracking box
        cv2.putText(frame, "Tracking...", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
    else:
        cv2.putText(frame, "Tracking Failed!", (50, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

    cv2.imshow("Object Tracking", frame)

    if cv2.waitKey(30) & 0xFF == ord('q'):  # Press "q" to exit
        break

cap.release()
cv2.destroyAllWindows()

