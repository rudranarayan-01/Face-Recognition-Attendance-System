import face_recognition
import cv2
import numpy as np
import csv
from datetime import datetime

# Initialize webcam
video_capture = cv2.VideoCapture(0)

# Load images and encode faces
known_faces = {
    "Rudra": face_recognition.face_encodings(face_recognition.load_image_file("photos/rudra.png"))[0],
    "Prabin": face_recognition.face_encodings(face_recognition.load_image_file("photos/prabin.png"))[0],
    "Sekhar": face_recognition.face_encodings(face_recognition.load_image_file("photos/sekhar.jpg"))[0],
    "Panda Sir": face_recognition.face_encodings(face_recognition.load_image_file("photos/pandasir.png"))[0]
}

known_face_encodings = list(known_faces.values())
known_face_names = list(known_faces.keys())

# Copy student list
students = known_face_names.copy()

# Create attendance CSV file
current_date = datetime.now().strftime("%Y-%m-%d")
f = open(current_date + '.csv', 'w+', newline='')
lnwriter = csv.writer(f)
lnwriter.writerow(["Name", "Time"])

while True:
    _, frame = video_capture.read()
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = small_frame[:, :, ::-1]

    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

    face_names = []

    for face_encoding in face_encodings:
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
        best_match_index = np.argmin(face_distances)

        name = "Unknown"
        if matches[best_match_index]:  # Fixes incorrect face matching
            name = known_face_names[best_match_index]

        face_names.append(name)

        # Mark attendance
        if name in students:
            students.remove(name)
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            print(f"Marked {name} at {current_time}")
            lnwriter.writerow([name, current_time])

    # Display webcam feed
    cv2.imshow("Attendance System", frame)

    # Exit on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cleanup
video_capture.release()
cv2.destroyAllWindows()
f.close()
