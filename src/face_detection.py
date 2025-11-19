"""
Face detection and image capture module for attendance system.

This module handles capturing face images for training the recognition model.
"""

import cv2
import os
import csv
from typing import Tuple, Optional
from config.config import (
    HAARCASCADE_PATH, TRAINING_IMAGE_DIR, STUDENT_DETAILS_CSV,
    STUDENT_DETAILS_COLUMNS, SCALE_FACTOR, MIN_NEIGHBORS,
    NUM_TRAINING_IMAGES, CAMERA_INDEX
)
from src.utils import assure_path_exists, get_next_serial_number


class FaceCapture:
    """Class for capturing face images for training."""
    
    def __init__(self):
        """Initialize the face capture system."""
        self.detector = None
        self._load_cascade()
    
    def _load_cascade(self) -> None:
        """Load the Haar Cascade classifier for face detection."""
        if not os.path.isfile(str(HAARCASCADE_PATH)):
            raise FileNotFoundError(
                f"Haarcascade file not found at {HAARCASCADE_PATH}. "
                "Please ensure the file exists."
            )
        self.detector = cv2.CascadeClassifier(str(HAARCASCADE_PATH))
    
    def capture_images(self, student_id: str, student_name: str) -> Tuple[bool, str]:
        """
        Capture face images for a student.
        
        Args:
            student_id: Unique ID for the student
            student_name: Name of the student
            
        Returns:
            Tuple of (success: bool, message: str)
        """
        # Ensure directories exist
        assure_path_exists(str(TRAINING_IMAGE_DIR))
        assure_path_exists(str(STUDENT_DETAILS_CSV.parent))
        
        # Get serial number
        serial = get_next_serial_number(str(STUDENT_DETAILS_CSV))
        
        # Initialize camera
        cam = cv2.VideoCapture(CAMERA_INDEX)
        if not cam.isOpened():
            return False, "Error: Could not access camera"
        
        sample_num = 0
        
        try:
            while True:
                ret, img = cam.read()
                if not ret:
                    return False, "Error: Could not read from camera"
                
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                faces = self.detector.detectMultiScale(
                    gray, SCALE_FACTOR, MIN_NEIGHBORS
                )
                
                for (x, y, w, h) in faces:
                    # Draw rectangle around face
                    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
                    
                    # Increment sample number
                    sample_num += 1
                    
                    # Save the captured face
                    file_name = f" {student_name}.{serial}.{student_id}.{sample_num}.jpg"
                    file_path = TRAINING_IMAGE_DIR / file_name
                    cv2.imwrite(str(file_path), gray[y:y + h, x:x + w])
                    
                    # Display the frame
                    cv2.imshow('Taking Images', img)
                
                # Wait for key press or max samples reached
                if cv2.waitKey(100) & 0xFF == ord('q'):
                    break
                elif sample_num >= NUM_TRAINING_IMAGES:
                    break
        
        finally:
            cam.release()
            cv2.destroyAllWindows()
        
        # Save student details
        if sample_num > 0:
            self._save_student_details(serial, student_id, student_name)
            return True, f"Images captured successfully for ID: {student_id}"
        else:
            return False, "No face detected. Please try again."
    
    def _save_student_details(self, serial: int, student_id: str, 
                            student_name: str) -> None:
        """
        Save student details to CSV file.
        
        Args:
            serial: Serial number
            student_id: Student ID
            student_name: Student name
        """
        file_exists = os.path.isfile(str(STUDENT_DETAILS_CSV))
        
        with open(str(STUDENT_DETAILS_CSV), 'a+', newline='') as csvFile:
            writer = csv.writer(csvFile)
            
            # Write header if file is new
            if not file_exists:
                writer.writerow(STUDENT_DETAILS_COLUMNS)
            
            # Write student data
            row = [serial, '', student_id, '', student_name]
            writer.writerow(row)


def check_haarcascade_file() -> bool:
    """
    Check if the Haarcascade file exists.
    
    Returns:
        True if file exists, False otherwise
    """
    return os.path.isfile(str(HAARCASCADE_PATH))
