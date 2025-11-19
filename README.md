# 👤 Face Recognition Based Attendance System

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![OpenCV](https://img.shields.io/badge/OpenCV-4.8%2B-green)
![License](https://img.shields.io/badge/License-MIT-yellow)
![Status](https://img.shields.io/badge/Status-Active-success)

> An automated attendance management system using facial recognition technology with Local Binary Patterns Histograms (LBPH) algorithm. Built with clean architecture and modular design for production deployment.

**📄 Research Publication:** This project is based on research published in IEEE  
**Paper:** [Face Recognition Based Attendance System](https://ieeexplore.ieee.org/document/9725755/)  
**Conference:** 2022 International Conference on Advances in Computing, Communication and Materials (ICACCM)  
**Author:** Pratyush Srivastava

**Table of Contents**
- [Overview](#overview)
- [Features](#features)
- [Quick Start](#quick-start)
- [Installation](#installation)
- [Usage Guide](#usage-guide)
- [Project Structure](#project-structure)
- [Technology Stack](#technology-stack)
- [Algorithm & Implementation](#algorithm--implementation)
- [Configuration](#configuration)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## 📋 Overview

The Face Recognition Attendance System enables educational institutions and organizations to:

- **Automate Attendance** tracking using facial recognition
- **Eliminate Manual Processes** and reduce proxy attendance
- **Real-time Recognition** with instant attendance marking  
- **Secure Access** with password-protected training
- **Historical Records** with date-wise CSV logs
- **User-Friendly Interface** built with Tkinter GUI

### Key Highlights

✅ **LBPH Algorithm** - Fast and accurate face recognition  
✅ **Real-time Processing** - 30+ FPS camera feed  
✅ **Easy Setup** - Just 3 steps to get started  
✅ **Cross-Platform** - Works on Windows, macOS, Linux  
✅ **CSV Export** - Easy data management and analysis  
✅ **Modular Design** - Clean, maintainable codebase  
✅ **IEEE Published** - Based on peer-reviewed research  

---

## ✨ Features

### 🎯 Face Recognition Technology

- **LBPH Algorithm** for accurate face recognition (~95% accuracy)
- **Haar Cascade** for real-time face detection
- **Confidence Threshold** filtering for reliable identification
- **Multi-face Detection** in single frame
- **Robust Performance** in varying lighting conditions

### 🏗️ Architecture

- **Modular Design** with separation of concerns
- **Type Hints** and comprehensive docstrings
- **Centralized Configuration** in `config/config.py`
- **Error Handling** throughout the application
- **Cross-platform Paths** using pathlib

### 💻 User Experience

- **Intuitive GUI** with dual-panel interface
- **Registration Module** for new students (right panel)
- **Attendance Tracking** with live feed (left panel)
- **Password Protection** for model training
- **CSV Export** for attendance records
- **Real-time Clock** and date display

### 🔒 Security

- **Password Protection** for training operations
- **Password Management** (create/change functionality)
- **Input Validation** on all user entries
- **Secure Data Storage** with organized file structure

---

## 📦 Installation

### System Requirements

**Minimum:**
- Python 3.8 or higher
- 4 GB RAM
- Webcam (720p or better)
- 500 MB disk space

**Recommended:**
- Python 3.10+
- 8 GB RAM
- Webcam (1080p)
- 2 GB disk space

### Step-by-Step Installation

#### Step 1: Install Python

**Windows:**
1. Download from [python.org](https://www.python.org/downloads/)
2. Run installer
3. ✅ **Check "Add Python to PATH"**
4. Click "Install Now"
5. Verify: `python --version`

**macOS:**
```bash
brew install python3
```

**Linux (Ubuntu/Debian):**
```bash
sudo apt update
sudo apt install python3 python3-pip python3-tk
```

#### Step 2: Clone/Download Project

```bash
# Using Git
git clone https://github.com/pratyushsrivastava500/Attendence-Management-System.git
cd Attendence-Management-System

# Or download ZIP from GitHub and extract
```

#### Step 3: Install Dependencies

```bash
# Install all requirements
pip install -r requirements.txt

# Or install individually if needed
pip install opencv-contrib-python==4.8.0
pip install numpy==1.24.0
pip install pandas==2.0.0
pip install pillow==10.0.0
```

#### Step 4: Verify Installation

```bash
# Test imports
python -c "import cv2; print('OpenCV:', cv2.__version__)"
python -c "import numpy; print('NumPy:', numpy.__version__)"
python -c "import pandas; print('Pandas:', pandas.__version__)"

# Test camera
python -c "import cv2; cap = cv2.VideoCapture(0); print('Camera: OK' if cap.isOpened() else 'Camera: Error'); cap.release()"
```

#### Step 5: Configure Camera Access

**Windows:**
- Settings → Privacy → Camera → Enable

**macOS:**  
- System Preferences → Security & Privacy → Camera → Grant permission

**Linux:**
```bash
# Check camera
ls -l /dev/video0

# Add user to video group if needed
sudo usermod -a -G video $USER
# Then logout and login
```

---

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- Webcam/Camera device
- pip package manager
- Windows/Linux/macOS

### Installation & Setup

1. **Clone or Download the repository**

```bash
git clone https://github.com/pratyushsrivastava500/Attendence-Management-System.git
cd Attendence-Management-System
```

2. **Install dependencies**

```bash
pip install -r requirements.txt
```

If you encounter issues:
```bash
pip install opencv-contrib-python==4.8.0 numpy==1.24.0 pandas==2.0.0 pillow==10.0.0
```

3. **Verify Haar Cascade file**

Ensure `haarcascade_frontalface_default.xml` is present in the root directory. If missing, download it:

```bash
# Windows PowerShell
Invoke-WebRequest -Uri "https://raw.githubusercontent.com/opencv/opencv/master/data/haarcascades/haarcascade_frontalface_default.xml" -OutFile "haarcascade_frontalface_default.xml"

# Linux/macOS
wget https://raw.githubusercontent.com/opencv/opencv/master/data/haarcascades/haarcascade_frontalface_default.xml
```

4. **Run the application**

```bash
python app.py
```

### First Time Usage (3 Steps)

**Step 1: Register a Student**
- Enter Student ID and Name in the registration panel (right side)
- Click "Take Images" button
- Face the camera until 100 images are captured (~30 seconds)

**Step 2: Train the Model**
- Click "Save Profile" button
- Set a password (first time) or enter existing password
- Wait for training to complete (3-5 seconds)

**Step 3: Mark Attendance**
- Click "Take Attendance" button (left panel)
- Face the camera - your name will appear
- Press 'Q' to stop
- Check `Attendance/Attendance_DD-MM-YYYY.csv` for records

---

## 🏗️ Architecture

```
┌─────────────────────────────────────┐
│      Tkinter GUI Interface          │
│  • Registration panel               │
│  • Attendance tracking panel        │
│  • Real-time display                │
└──────────────┬──────────────────────┘
               │
┌──────────────▼──────────────────────┐
│        Controller Layer             │
│  • Event handlers                   │
│  • User input validation            │
│  • UI updates                       │
└──────────────┬──────────────────────┘
               │
┌──────────────▼──────────────────────┐
│        Business Logic Layer         │
│  • Face detection module            │
│  • Training module                  │
│  • Attendance tracking module       │
│  • Password management              │
└──────────────┬──────────────────────┘
               │
┌──────────────▼──────────────────────┐
│    Data Processing Layer            │
│  • Image preprocessing              │
│  • Feature extraction (LBPH)        │
│  • CSV data management              │
└──────────────┬──────────────────────┘
               │
┌──────────────▼──────────────────────┐
│      Configuration Layer            │
│  • Paths & parameters               │
│  • UI settings                      │
│  • Recognition thresholds           │
└─────────────────────────────────────┘
```

---

## 🛠️ Technology Stack

| Component | Technology |
|-----------|-----------|
| Language | Python 3.8+ |
| GUI Framework | Tkinter |
| Computer Vision | OpenCV 4.8+ |
| Face Recognition | LBPH (Local Binary Patterns Histograms) |
| Face Detection | Haar Cascade Classifier |
| Data Processing | Pandas, NumPy |
| Image Processing | PIL/Pillow |
| Data Storage | CSV Files |

---

## 📁 Project Structure

```
Attendence-Management-System/
├── app.py                          # Main application entry point
├── main.py                         # Legacy monolithic code (deprecated)
├── requirements.txt                # Python dependencies
├── haarcascade_frontalface_default.xml  # Face detection classifier
├── config/
│   └── config.py                   # Configuration settings
├── src/
│   ├── gui.py                      # Tkinter GUI components
│   ├── face_detection.py           # Face capture module
│   ├── training.py                 # Model training module
│   ├── attendance.py               # Attendance tracking module
│   ├── password_manager.py         # Password management
│   └── utils.py                    # Utility functions
├── StudentDetails/
│   └── StudentDetails.csv          # Student registration data
├── TrainingImage/                  # Captured face images
├── TrainingImageLabel/
│   ├── Trainner.yml               # Trained LBPH model
│   └── psd.txt                    # Password storage
├── Attendance/
│   └── Attendance_DD-MM-YYYY.csv  # Daily attendance records
├── docs/                           # Documentation
└── tests/                          # Unit tests (future)
```

---

## 📖 Usage Guide

### 1. Student Registration

**Steps:**
1. Launch the application: `python app.py`
2. Navigate to "For New Registrations" panel (right side)
3. Enter Student **ID** (numeric, e.g., 1001)
4. Enter Student **Name** (alphabetic, e.g., John Doe)
5. Click **"Take Images"**
6. Face the camera - keep face centered
7. System captures 100 images automatically
8. Press 'Q' to finish early if needed

**Tips for Best Results:**
- Ensure good lighting (natural or diffused light)
- Look directly at the camera
- Vary facial expressions slightly
- Move head slightly for different angles
- Distance: 2-3 feet from camera

### 2. Training the Model

**Steps:**
1. After registering one or more students, click **"Save Profile"**
2. **First time**: Enter and remember a new password
3. **Subsequent times**: Enter your existing password
4. Wait 3-5 seconds for training to complete
5. Success message shows total registrations

**Important Notes:**
- Training is required after each new registration
- Password protects the training function
- Training takes only a few seconds
- Model file saved as `TrainingImageLabel/Trainner.yml`

### 3. Taking Attendance

**Steps:**
1. Navigate to "For Already Registered" panel (left side)
2. Click **"Take Attendance"**
3. Students face the camera one by one
4. System recognizes faces and displays names
5. Attendance is marked automatically
6. Green rectangle appears around recognized faces
7. Press **'Q'** to stop tracking
8. Attendance saved to CSV file

**Output Location:**
- File: `Attendance/Attendance_DD-MM-YYYY.csv`
- Format: ID, Name, Date, Time
- Opens in Excel/Google Sheets

### 4. Managing Passwords

**Change Password:**
1. Menu bar → **Help** → **Change Password**
2. Enter old password
3. Enter new password
4. Confirm new password
5. Click Save

### 5. Viewing Attendance Records

**CSV Files:**
- Location: `Attendance/` folder
- One file per day: `Attendance_19-11-2025.csv`
- Columns: Id, Name, Date, Time
- Compatible with Excel, Google Sheets, or any CSV reader

**Student Details:**
- Location: `StudentDetails/StudentDetails.csv`
- Contains: Serial No., ID, Name
- Used for looking up student information

---

## 📊 Algorithm & Implementation

### LBPH Face Recognition

**Local Binary Patterns Histograms (LBPH)** is chosen for its:
- **Robustness** to lighting variations
- **Computational efficiency**
- **Low memory footprint**
- **Real-time performance**

**How it Works:**
1. **Training Phase:**
   - Capture 100+ images per person
   - Convert to grayscale
   - Extract LBP features
   - Create histograms
   - Train LBPH recognizer

2. **Recognition Phase:**
   - Detect face using Haar Cascade
   - Extract LBP features
   - Compare with trained model
   - Calculate confidence score
   - Match if confidence < threshold (50)

### Face Detection

**Haar Cascade Classifier:**
- Pre-trained on frontal face patterns
- Fast detection (real-time capable)
- Scale invariant
- Parameters: `scaleFactor=1.3`, `minNeighbors=5`

---

## 🤖 Model Performance

| Metric | Value |
|--------|-------|
| Recognition Algorithm | LBPH |
| Detection Method | Haar Cascade |
| Confidence Threshold | < 50 |
| Training Images/Person | 100 |
| Recognition Speed | Real-time (30+ FPS) |
| Accuracy | ~95% (controlled lighting) |
| False Positive Rate | < 5% |

**Factors Affecting Performance:**
- Lighting conditions (optimal: diffused lighting)
- Camera quality (recommended: 720p+)
- Training image diversity
- Face angle variations

---

## 📚 Research & Publications

This system is based on research presented at:

**Conference:** 2022 International Conference on Advances in Computing, Communication and Materials (ICACCM)

**Paper Title:** Face Recognition Based Attendance System

**DOI:** [10.1109/ICACCM56405.2022.9725755](https://ieeexplore.ieee.org/document/9725755/)

**Abstract:** The research presents an automated attendance system using facial recognition technology to eliminate manual attendance processes, reduce proxy attendance, and improve accuracy in educational institutions.

**Key Contributions:**
- Comparative analysis of face recognition algorithms
- Implementation of LBPH for attendance systems
- Performance evaluation under various conditions
- Practical deployment in educational settings

**Citation (IEEE Format):**
```
P. Srivastava et al., "Face Recognition Based Attendance System," 
2022 International Conference on Advances in Computing, Communication 
and Materials (ICACCM), Dehradun, India, 2022, pp. 1-6, 
doi: 10.1109/ICACCM56405.2022.9725755.
```

---

## 🔮 Future Enhancements

- [ ] Add Deep Learning models (FaceNet, ArcFace)
- [ ] Implement anti-spoofing (liveness detection)
- [ ] Add database backend (SQLite/PostgreSQL)
- [ ] Create REST API for mobile integration
- [ ] Add face mask detection
- [ ] Implement multi-camera support
- [ ] Add analytics dashboard
- [ ] Email/SMS notifications
- [ ] Cloud deployment (AWS/Azure)
- [ ] Mobile app (Flutter/React Native)
- [ ] Export to Excel with formatting
- [ ] Biometric fusion (face + fingerprint)

---

## 🔧 Troubleshooting

### Common Issues and Solutions

#### Issue: Camera not accessible

**Symptoms:** "Error: Could not access camera" message

**Solutions:**
- Check if camera is connected and working
- Close other applications using camera (Zoom, Skype, Teams)
- **Windows:** Settings → Privacy → Camera → Allow apps to access camera
- **macOS:** System Preferences → Security & Privacy → Camera → Grant permission
- **Linux:** Check camera permissions: `ls -l /dev/video0`
- Restart the application

#### Issue: Module not found / Import errors

**Symptoms:** `ModuleNotFoundError: No module named 'cv2'` or similar

**Solutions:**
```bash
# Uninstall and reinstall OpenCV
pip uninstall opencv-python opencv-contrib-python
pip install opencv-contrib-python==4.8.0

# Install all dependencies
pip install -r requirements.txt

# Or install individually
pip install opencv-contrib-python numpy pandas pillow
```

#### Issue: Haarcascade file not found

**Symptoms:** "Haarcascade file missing" message

**Solutions:**
- Download the file manually:
```bash
# Windows PowerShell
Invoke-WebRequest -Uri "https://raw.githubusercontent.com/opencv/opencv/master/data/haarcascades/haarcascade_frontalface_default.xml" -OutFile "haarcascade_frontalface_default.xml"

# Linux/macOS
wget https://raw.githubusercontent.com/opencv/opencv/master/data/haarcascades/haarcascade_frontalface_default.xml
```
- Place the file in the project root directory

#### Issue: Face not detected during registration

**Symptoms:** No face rectangle appears, 0 images captured

**Solutions:**
- **Improve lighting** - avoid backlighting, use front or diffused light
- **Remove obstructions** - glasses, hat, mask (temporarily)
- **Move closer** to camera (2-3 feet optimal)
- **Ensure face is visible** and not blurred
- **Check camera angle** - position at eye level
- Restart application and try again

#### Issue: Low recognition accuracy / Not recognizing faces

**Symptoms:** "Unknown" appears instead of name, wrong person recognized

**Solutions:**
1. **Capture more training images**:
   - Delete old images: `TrainingImage/`
   - Re-register with better lighting
   - Capture images from multiple angles

2. **Adjust confidence threshold**:
   - Edit `config/config.py`
   - Increase `CONFIDENCE_THRESHOLD` from 50 to 60-70
   - Retrain the model

3. **Improve environment**:
   - Better lighting conditions
   - Consistent background
   - Same camera used for training and recognition

4. **Retrain model**:
   - Click "Save Profile" again
   - Ensure password is correct

#### Issue: GUI not displaying properly / Tkinter errors

**Symptoms:** Window doesn't open, blank screen, Tkinter import error

**Solutions:**
```bash
# Linux - Install Tkinter
sudo apt-get install python3-tk

# macOS - Reinstall Python with Tk support
brew install python-tk

# Windows - Reinstall Python ensuring Tk is selected
```

#### Issue: Permission denied errors

**Symptoms:** Cannot write to files, permission errors

**Solutions:**
```bash
# Windows - Run as Administrator
# Right-click PowerShell → Run as Administrator

# Linux/macOS - Fix permissions
chmod -R 755 .
sudo chown -R $USER:$USER .
```

#### Issue: Attendance not saving to CSV

**Symptoms:** No CSV file created in Attendance/ folder

**Solutions:**
- Check if `Attendance/` folder exists
- Verify write permissions on folder
- Ensure faces are being recognized (confidence < 50)
- Check for error messages in terminal
- Manually create `Attendance/` folder if missing

#### Issue: Password forgotten

**Symptoms:** Cannot train model, wrong password error

**Solutions:**
1. Delete password file:
   ```bash
   # Navigate to project folder
   Remove-Item TrainingImageLabel\psd.txt
   ```
2. Restart application
3. Set new password when training

#### Issue: Python version compatibility

**Symptoms:** Syntax errors, module incompatibility

**Solutions:**
- Ensure Python 3.8+ is installed:
  ```bash
  python --version
  ```
- Upgrade Python if needed
- Use virtual environment for isolation

### Platform-Specific Notes

**Windows:**
- Use PowerShell or Command Prompt
- Ensure Python is in PATH
- May need Visual C++ Redistributable
- Antivirus might block camera - add exception

**macOS:**
- Grant camera permissions in System Preferences
- May need Xcode Command Line Tools: `xcode-select --install`
- Use `python3` instead of `python` if needed

**Linux (Ubuntu/Debian):**
- Install system dependencies:
  ```bash
  sudo apt-get update
  sudo apt-get install python3-tk libgl1-mesa-glx libglib2.0-0
  ```
- Add user to video group: `sudo usermod -a -G video $USER`
- Logout and login again

### Getting More Help

If issues persist:

1. **Check existing issues:** [GitHub Issues](https://github.com/pratyushsrivastava500/Attendence-Management-System/issues)
2. **Open a new issue** with:
   - Operating System and version
   - Python version (`python --version`)
   - Error message (full text)
   - Steps to reproduce
3. **Email support:** pratyushsrivastava500@gmail.com

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

### How to Contribute

1. **Fork** the repository
2. **Create** a feature branch: `git checkout -b feature/AmazingFeature`
3. **Commit** your changes: `git commit -m 'Add AmazingFeature'`
4. **Push** to the branch: `git push origin feature/AmazingFeature`
5. **Open** a Pull Request

### Coding Standards

- Follow **PEP 8** style guide
- Add **type hints** to functions
- Write **docstrings** (Google style)
- Include **unit tests** for new features
- Update **documentation** as needed

### Areas for Contribution

**High Priority:**
- Unit tests for all modules
- Deep learning models (FaceNet, ArcFace)
- Anti-spoofing/liveness detection
- Database backend (SQLite/PostgreSQL)

**Medium Priority:**
- REST API development
- Mobile app integration
- Email/SMS notifications
- Analytics dashboard

**Good First Issues:**
- Improve error messages
- Add input validation
- Enhance UI/UX
- Fix bugs
- Update documentation

### Reporting Bugs

Open an issue with:
- Clear description of the problem
- Steps to reproduce
- Expected vs actual behavior
- Environment details (OS, Python version)
- Error messages/screenshots

### Suggesting Features

Open an issue describing:
- The feature and its benefits
- Use cases
- Implementation ideas (optional)

---

## 📝 License

This project is licensed under the **MIT License** - see below for details:

```
MIT License

Copyright (c) 2025 Pratyush Srivastava

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

## 🙏 Acknowledgments

- **OpenCV Community** for computer vision libraries
- **Python Software Foundation** for the Python language
- **IEEE** for publishing the research paper
- **Contributors** to the Haar Cascade classifiers
- **Students and Faculty** who tested the system

---

## 📧 Contact

**Author:** Pratyush Srivastava

**Email:** pratyushsrivastava500@gmail.com

**GitHub:** [@pratyushsrivastava500](https://github.com/pratyushsrivastava500)

**LinkedIn:** [Pratyush Srivastava](https://www.linkedin.com/in/pratyushsrivastava500)

For questions, issues, or collaboration opportunities, please open an issue on GitHub or contact via email.

---

## 🌟 Star History

If you find this project helpful, please consider giving it a star ⭐

---

## ⚠️ Disclaimer

This system is designed for educational and organizational use. Users should:
- Comply with data privacy regulations (GDPR, etc.)
- Obtain consent for facial data collection
- Secure stored biometric data appropriately
- Follow local laws regarding biometric systems

The system should complement, not replace, existing attendance verification methods.

---

## 📈 Project Status

- ✅ **Active Development**
- ✅ **Production Ready**
- ✅ **Well Documented**
- ✅ **Peer Reviewed** (IEEE Published)
- 🔄 **Accepting Contributions**

---

## 🎯 Use Cases

- **Educational Institutions:** Schools, colleges, universities
- **Corporate Offices:** Employee attendance tracking
- **Training Centers:** Workshop/seminar attendance
- **Events:** Conference and seminar check-ins
- **Security:** Access control systems
- **Research:** Facial recognition studies

---

**Made with ❤️ and Python | © 2025 Pratyush Srivastava**

---

**Keywords:** Face Recognition, Attendance System, LBPH, OpenCV, Computer Vision, Python, Tkinter, Automated Attendance, Biometric System, IEEE Published Research
