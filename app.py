"""
Face Recognition Based Attendance System

A desktop application for automated attendance tracking using facial recognition.
This is the main entry point for the application.

Author: Pratyush Srivastava
Email: pratyushsrivastava500@gmail.com
"""

import sys
from pathlib import Path

# Add project root to Python path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

from src.gui import AttendanceSystemGUI
from config.config import ensure_directories


def main():
    """Main entry point for the application."""
    # Ensure all necessary directories exist
    ensure_directories()
    
    # Create and run the GUI
    app = AttendanceSystemGUI()
    app.run()


if __name__ == "__main__":
    main()
