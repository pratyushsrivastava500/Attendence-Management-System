"""
Face recognition model training module.

This module handles training the LBPH face recognizer with captured images.
"""

import cv2
import os
import numpy as np
from PIL import Image
from typing import Tuple, List
from config.config import (
    HAARCASCADE_PATH, TRAINING_IMAGE_DIR, TRAINER_FILE,
    TRAINING_LABEL_DIR
)
from src.utils import assure_path_exists


class FaceTrainer:
    """Class for training the face recognition model."""
    
    def __init__(self):
        """Initialize the face trainer."""
        self.recognizer = cv2.face.LBPHFaceRecognizer_create()
        self.detector = None
        self._load_cascade()
    
    def _load_cascade(self) -> None:
        """Load the Haar Cascade classifier."""
        if not os.path.isfile(str(HAARCASCADE_PATH)):
            raise FileNotFoundError(
                f"Haarcascade file not found at {HAARCASCADE_PATH}"
            )
        self.detector = cv2.CascadeClassifier(str(HAARCASCADE_PATH))
    
    def train_model(self) -> Tuple[bool, str, int]:
        """
        Train the face recognition model with captured images.
        
        Returns:
            Tuple of (success: bool, message: str, num_registrations: int)
        """
        # Ensure directory exists
        assure_path_exists(str(TRAINING_LABEL_DIR))
        
        # Get images and labels
        faces, ids = self._get_images_and_labels(str(TRAINING_IMAGE_DIR))
        
        if len(faces) == 0:
            return False, "No training images found. Please register first!", 0
        
        try:
            # Train the recognizer
            self.recognizer.train(faces, np.array(ids))
            
            # Save the trained model
            self.recognizer.save(str(TRAINER_FILE))
            
            num_registrations = ids[0] if ids else 0
            return True, "Profile saved successfully!", num_registrations
        
        except Exception as e:
            return False, f"Training failed: {str(e)}", 0
    
    def _get_images_and_labels(self, path: str) -> Tuple[List, List]:
        """
        Extract faces and IDs from training images.
        
        Args:
            path: Path to training images directory
            
        Returns:
            Tuple of (faces list, IDs list)
        """
        if not os.path.exists(path):
            return [], []
        
        # Get all image paths
        image_paths = [
            os.path.join(path, f) 
            for f in os.listdir(path) 
            if f.endswith(('.jpg', '.jpeg', '.png'))
        ]
        
        faces = []
        ids = []
        
        for image_path in image_paths:
            try:
                # Load image and convert to grayscale
                pil_image = Image.open(image_path).convert('L')
                
                # Convert to numpy array
                image_np = np.array(pil_image, 'uint8')
                
                # Extract ID from filename
                # Format: name.serial.id.sample.jpg
                filename = os.path.split(image_path)[-1]
                parts = filename.split('.')
                
                if len(parts) >= 3:
                    try:
                        student_id = int(parts[2])
                        faces.append(image_np)
                        ids.append(student_id)
                    except ValueError:
                        # Skip files with invalid ID format
                        continue
            
            except Exception as e:
                print(f"Error processing {image_path}: {str(e)}")
                continue
        
        return faces, ids


def check_trained_model_exists() -> bool:
    """
    Check if a trained model file exists.
    
    Returns:
        True if trained model exists, False otherwise
    """
    return os.path.isfile(str(TRAINER_FILE))
