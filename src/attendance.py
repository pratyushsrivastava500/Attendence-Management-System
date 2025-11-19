"""
Attendance tracking module using face recognition.

This module handles real-time face recognition and attendance marking.
"""

import cv2
import os
import csv
import pandas as pd
from typing import List, Tuple, Optional
from config.config import (
    HAARCASCADE_PATH, TRAINER_FILE, STUDENT_DETAILS_CSV,
    ATTENDANCE_DIR, ATTENDANCE_COLUMNS, CONFIDENCE_THRESHOLD,
    CAMERA_INDEX
)
from src.utils import (
    assure_path_exists, get_current_timestamp,
    format_date, format_time
)


class AttendanceTracker:
    """Class for tracking attendance using face recognition."""
    
    def __init__(self):
        """Initialize the attendance tracker."""
        self.recognizer = cv2.face.LBPHFaceRecognizer_create()
        self.face_cascade = None
        self.student_df = None
        self._load_models()
    
    def _load_models(self) -> None:
        """Load the trained model and student details."""
        # Load face cascade
        if not os.path.isfile(str(HAARCASCADE_PATH)):
            raise FileNotFoundError(
                f"Haarcascade file not found at {HAARCASCADE_PATH}"
            )
        self.face_cascade = cv2.CascadeClassifier(str(HAARCASCADE_PATH))
        
        # Load trained model
        if not os.path.isfile(str(TRAINER_FILE)):
            raise FileNotFoundError(
                "Trained model not found. Please train the model first!"
            )
        self.recognizer.read(str(TRAINER_FILE))
        
        # Load student details
        if not os.path.isfile(str(STUDENT_DETAILS_CSV)):
            raise FileNotFoundError(
                "Student details not found. Please register students first!"
            )
        self.student_df = pd.read_csv(str(STUDENT_DETAILS_CSV))
    
    def start_tracking(self, update_callback=None) -> Tuple[bool, str, List]:
        """
        Start real-time face recognition for attendance.
        
        Args:
            update_callback: Optional callback function to update UI with attendance data
            
        Returns:
            Tuple of (success: bool, message: str, attendance_records: List)
        """
        # Ensure attendance directory exists
        assure_path_exists(str(ATTENDANCE_DIR))
        
        # Initialize camera
        cam = cv2.VideoCapture(CAMERA_INDEX)
        if not cam.isOpened():
            return False, "Error: Could not access camera", []
        
        font = cv2.FONT_HERSHEY_SIMPLEX
        attendance_records = []
        recognized_ids = set()
        
        try:
            while True:
                ret, frame = cam.read()
                if not ret:
                    break
                
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                faces = self.face_cascade.detectMultiScale(gray, 1.2, 5)
                
                for (x, y, w, h) in faces:
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (225, 0, 0), 2)
                    
                    # Predict the face
                    serial, confidence = self.recognizer.predict(gray[y:y + h, x:x + w])
                    
                    if confidence < CONFIDENCE_THRESHOLD:
                        # Get student details
                        student_data = self.student_df.loc[
                            self.student_df['SERIAL NO.'] == serial
                        ]
                        
                        if not student_data.empty:
                            name = student_data['NAME'].values[0]
                            student_id = str(student_data['ID'].values[0])
                            
                            # Record attendance if not already recorded
                            if serial not in recognized_ids:
                                ts = get_current_timestamp()
                                date = format_date(ts)
                                time = format_time(ts)
                                
                                attendance = [student_id, '', name, '', date, '', time]
                                attendance_records.append(attendance)
                                recognized_ids.add(serial)
                                
                                # Update callback if provided
                                if update_callback:
                                    update_callback(student_id, name, date, time)
                            
                            display_name = name
                        else:
                            display_name = "Unknown"
                    else:
                        display_name = "Unknown"
                    
                    cv2.putText(frame, display_name, (x, y + h), 
                              font, 1, (255, 255, 255), 2)
                
                cv2.imshow('Taking Attendance', frame)
                
                # Break on 'q' key
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
        
        finally:
            cam.release()
            cv2.destroyAllWindows()
        
        # Save attendance to CSV
        if attendance_records:
            self._save_attendance(attendance_records)
            return True, "Attendance recorded successfully", attendance_records
        else:
            return False, "No faces recognized", []
    
    def _save_attendance(self, records: List) -> None:
        """
        Save attendance records to CSV file.
        
        Args:
            records: List of attendance records
        """
        ts = get_current_timestamp()
        date = format_date(ts)
        attendance_file = ATTENDANCE_DIR / f"Attendance_{date}.csv"
        
        file_exists = os.path.isfile(str(attendance_file))
        
        with open(str(attendance_file), 'a+', newline='') as csvFile:
            writer = csv.writer(csvFile)
            
            # Write header if new file
            if not file_exists:
                writer.writerow(ATTENDANCE_COLUMNS)
            
            # Write all records
            for record in records:
                writer.writerow(record)
    
    def get_today_attendance(self) -> List[Tuple[str, str, str, str]]:
        """
        Get attendance records for today.
        
        Returns:
            List of tuples (ID, Name, Date, Time)
        """
        ts = get_current_timestamp()
        date = format_date(ts)
        attendance_file = ATTENDANCE_DIR / f"Attendance_{date}.csv"
        
        if not os.path.isfile(str(attendance_file)):
            return []
        
        records = []
        with open(str(attendance_file), 'r') as csvFile:
            reader = csv.reader(csvFile)
            next(reader)  # Skip header
            
            for row in reader:
                if len(row) >= 7:
                    records.append((row[0], row[2], row[4], row[6]))
        
        return records
