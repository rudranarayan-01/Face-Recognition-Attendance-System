# Face Recognition Attendance System

## Overview
This project is a real-time **Face Recognition Attendance System** using OpenCV and face_recognition in Python. It captures live video from a webcam, detects and recognizes faces, and marks attendance by saving the timestamp in a CSV file.

## Features
- Detects and recognizes faces in real-time using a webcam.
- Matches recognized faces against a predefined database of known faces.
- Records the attendance of recognized individuals with a timestamp in a CSV file.
- Displays live video feed with recognized names.
- Saves attendance data in a CSV file with the current date.

## Requirements
Ensure you have Python installed along with the following dependencies:

```sh
pip install face-recognition opencv-python numpy
```

## Installation & Usage
1. Clone the repository or copy the script to your local machine.
2. Install required dependencies using the command above.
3. Place the images of known individuals in the **photos/** directory.
4. Update the image paths in the script accordingly.
5. Run the script:
   
   ```sh
   python attendance_system.py
   ```

6. The system will open a webcam feed and start recognizing faces.
7. Press **'q'** to quit the program.
8. Attendance is recorded in a CSV file named with the current date (e.g., `2025-02-04.csv`).

## File Structure
```
project_folder/
│── photos/                # Folder to store images of known individuals
│   ├── rudra.png
│   ├── prabin.png
│   ├── sekhar.jpg
│   ├── pandasir.png
│── attendance_system.py   # Main Python script
│── README.md              # Project documentation
```

## How It Works
1. Loads images of known individuals and encodes their faces.
2. Captures video from the webcam and processes frames.
3. Detects faces and matches them against the known encodings.
4. If a face is recognized, marks attendance in the CSV file with the timestamp.
5. Displays the live webcam feed with recognized names.

## Notes
- Ensure the images in the `photos/` folder are clear and well-lit for better recognition accuracy.
- If a face is not recognized, it will be labeled as **Unknown**.
- You can add more known faces by updating the `known_faces` dictionary.

## Future Improvements
- Store recognized faces in a database instead of CSV files.
- Add a GUI for better user experience.
- Implement multi-camera support.

## License
This project is open-source and available for modification and distribution.

---

Developed with ❤️ using Python & OpenCV.

