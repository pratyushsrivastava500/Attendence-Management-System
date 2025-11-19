"""
Configuration settings for the Face Recognition Attendance System.

This module centralizes all configuration parameters including paths,
UI settings, and face recognition parameters.
"""

import os
from pathlib import Path

# Base Directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Directory Paths
TRAINING_IMAGE_DIR = BASE_DIR / "TrainingImage"
TRAINING_LABEL_DIR = BASE_DIR / "TrainingImageLabel"
STUDENT_DETAILS_DIR = BASE_DIR / "StudentDetails"
ATTENDANCE_DIR = BASE_DIR / "Attendance"
HAARCASCADE_PATH = BASE_DIR / "haarcascade_frontalface_default.xml"

# File Paths
PASSWORD_FILE = TRAINING_LABEL_DIR / "psd.txt"
TRAINER_FILE = TRAINING_LABEL_DIR / "Trainner.yml"
STUDENT_DETAILS_CSV = STUDENT_DETAILS_DIR / "StudentDetails.csv"

# Face Detection Parameters
SCALE_FACTOR = 1.3
MIN_NEIGHBORS = 5
CONFIDENCE_THRESHOLD = 50
NUM_TRAINING_IMAGES = 100
CAMERA_INDEX = 0

# UI Configuration
WINDOW_TITLE = "Face Recognition Attendance System"
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
WINDOW_BG_COLOR = "#262523"
FRAME_BG_COLOR = "#00aeff"
BUTTON_BG_COLOR = "blue"
BUTTON_FG_COLOR = "white"
HEADER_BG_COLOR = "#3ece48"

# Font Styles
FONT_LARGE = ('times', 29, 'bold')
FONT_MEDIUM = ('times', 17, 'bold')
FONT_SMALL = ('times', 15, 'bold')
FONT_BUTTON = ('times', 11, 'bold')

# Date Format
DATE_FORMAT = '%d-%m-%Y'
TIME_FORMAT = '%H:%M:%S'

# Contact Information
CONTACT_EMAIL = "pratyushsrivastava500@gmail.com"

# Month Names
MONTH_NAMES = {
    '01': 'January',
    '02': 'February',
    '03': 'March',
    '04': 'April',
    '05': 'May',
    '06': 'June',
    '07': 'July',
    '08': 'August',
    '09': 'September',
    '10': 'October',
    '11': 'November',
    '12': 'December'
}

# CSV Column Names
STUDENT_DETAILS_COLUMNS = ['SERIAL NO.', '', 'ID', '', 'NAME']
ATTENDANCE_COLUMNS = ['Id', '', 'Name', '', 'Date', '', 'Time']

# Ensure all directories exist
def ensure_directories():
    """Create all necessary directories if they don't exist."""
    directories = [
        TRAINING_IMAGE_DIR,
        TRAINING_LABEL_DIR,
        STUDENT_DETAILS_DIR,
        ATTENDANCE_DIR
    ]
    for directory in directories:
        directory.mkdir(parents=True, exist_ok=True)
