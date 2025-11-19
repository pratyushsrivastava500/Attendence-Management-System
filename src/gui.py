"""
GUI module for the Face Recognition Attendance System.

This module contains all the Tkinter interface components.
"""

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mess
import tkinter.simpledialog as tsd
import time
from typing import Callable
from config.config import (
    WINDOW_TITLE, WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_BG_COLOR,
    FRAME_BG_COLOR, BUTTON_BG_COLOR, BUTTON_FG_COLOR, HEADER_BG_COLOR,
    FONT_LARGE, FONT_MEDIUM, FONT_SMALL, FONT_BUTTON, CONTACT_EMAIL,
    MONTH_NAMES
)
from src.utils import get_current_timestamp, format_date, format_time, parse_date
from src.face_detection import FaceCapture, check_haarcascade_file
from src.training import FaceTrainer
from src.attendance import AttendanceTracker
from src.password_manager import PasswordManager


class AttendanceSystemGUI:
    """Main GUI class for the attendance system."""
    
    def __init__(self):
        """Initialize the GUI."""
        self.window = tk.Tk()
        self.window.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
        self.window.resizable(True, False)
        self.window.title(WINDOW_TITLE)
        self.window.configure(background=WINDOW_BG_COLOR)
        
        # Initialize components
        self.face_capture = FaceCapture()
        self.face_trainer = FaceTrainer()
        self.password_manager = PasswordManager()
        
        # GUI elements
        self.txt = None
        self.txt2 = None
        self.message1 = None
        self.message = None
        self.clock = None
        self.tv = None
        
        self._setup_ui()
        self._start_clock()
    
    def _setup_ui(self):
        """Setup all UI components."""
        self._create_header()
        self._create_frames()
        self._create_registration_panel()
        self._create_attendance_panel()
        self._create_menubar()
        self._update_registration_count()
    
    def _create_header(self):
        """Create the header section."""
        message3 = tk.Label(
            self.window,
            text="Face Recognition Based Attendance System",
            fg="white",
            bg=WINDOW_BG_COLOR,
            width=55,
            height=1,
            font=FONT_LARGE
        )
        message3.place(x=10, y=10)
        
        # Date display
        frame4 = tk.Frame(self.window, bg="#c4c6ce")
        frame4.place(relx=0.36, rely=0.09, relwidth=0.16, relheight=0.07)
        
        ts = get_current_timestamp()
        date = format_date(ts)
        day, month, year = parse_date(date)
        month_name = MONTH_NAMES.get(month, month)
        
        datef = tk.Label(
            frame4,
            text=f"{day}-{month_name}-{year}  |  ",
            fg="orange",
            bg=WINDOW_BG_COLOR,
            width=55,
            height=1,
            font=('times', 22, 'bold')
        )
        datef.pack(fill='both', expand=1)
        
        # Clock display
        frame3 = tk.Frame(self.window, bg="#c4c6ce")
        frame3.place(relx=0.52, rely=0.09, relwidth=0.09, relheight=0.07)
        
        self.clock = tk.Label(
            frame3,
            fg="orange",
            bg=WINDOW_BG_COLOR,
            width=55,
            height=1,
            font=('times', 22, 'bold')
        )
        self.clock.pack(fill='both', expand=1)
    
    def _create_frames(self):
        """Create main frames."""
        self.frame1 = tk.Frame(self.window, bg=FRAME_BG_COLOR)
        self.frame1.place(relx=0.11, rely=0.17, relwidth=0.39, relheight=0.80)
        
        self.frame2 = tk.Frame(self.window, bg=FRAME_BG_COLOR)
        self.frame2.place(relx=0.51, rely=0.17, relwidth=0.38, relheight=0.80)
    
    def _create_registration_panel(self):
        """Create the registration panel (right side)."""
        head2 = tk.Label(
            self.frame2,
            text="For New Registrations",
            fg="black",
            bg=HEADER_BG_COLOR,
            font=FONT_MEDIUM
        )
        head2.grid(row=0, column=0)
        
        # ID input
        lbl = tk.Label(
            self.frame2,
            text="Enter ID",
            width=20,
            height=1,
            fg="black",
            bg=FRAME_BG_COLOR,
            font=FONT_MEDIUM
        )
        lbl.place(x=80, y=55)
        
        self.txt = tk.Entry(self.frame2, width=32, fg="black", font=FONT_SMALL)
        self.txt.place(x=30, y=88)
        
        clearButton = tk.Button(
            self.frame2,
            text="Clear",
            command=self._clear_id,
            fg="black",
            bg="#ea2a2a",
            width=11,
            activebackground="white",
            font=FONT_BUTTON
        )
        clearButton.place(x=335, y=86)
        
        # Name input
        lbl2 = tk.Label(
            self.frame2,
            text="Enter Name",
            width=20,
            fg="black",
            bg=FRAME_BG_COLOR,
            font=FONT_MEDIUM
        )
        lbl2.place(x=80, y=140)
        
        self.txt2 = tk.Entry(self.frame2, width=32, fg="black", font=FONT_SMALL)
        self.txt2.place(x=30, y=173)
        
        clearButton2 = tk.Button(
            self.frame2,
            text="Clear",
            command=self._clear_name,
            fg="black",
            bg="#ea2a2a",
            width=11,
            activebackground="white",
            font=FONT_BUTTON
        )
        clearButton2.place(x=335, y=172)
        
        # Messages
        self.message1 = tk.Label(
            self.frame2,
            text="1) Take Images  >>>  2) Save Profile",
            bg=FRAME_BG_COLOR,
            fg="black",
            width=39,
            height=1,
            font=FONT_SMALL
        )
        self.message1.place(x=7, y=230)
        
        self.message = tk.Label(
            self.frame2,
            text="",
            bg=FRAME_BG_COLOR,
            fg="black",
            width=39,
            height=1,
            font=('times', 16, 'bold')
        )
        self.message.place(x=7, y=450)
        
        # Buttons
        takeImg = tk.Button(
            self.frame2,
            text="Take Images",
            command=self._take_images,
            fg="white",
            bg=BUTTON_BG_COLOR,
            width=34,
            height=1,
            activebackground="white",
            font=FONT_SMALL
        )
        takeImg.place(x=30, y=300)
        
        trainImg = tk.Button(
            self.frame2,
            text="Save Profile",
            command=self._save_profile,
            fg="white",
            bg=BUTTON_BG_COLOR,
            width=34,
            height=1,
            activebackground="white",
            font=FONT_SMALL
        )
        trainImg.place(x=30, y=380)
    
    def _create_attendance_panel(self):
        """Create the attendance panel (left side)."""
        head1 = tk.Label(
            self.frame1,
            text="For Already Registered",
            fg="black",
            bg=HEADER_BG_COLOR,
            font=FONT_MEDIUM
        )
        head1.place(x=0, y=0)
        
        lbl3 = tk.Label(
            self.frame1,
            text="Attendance",
            width=20,
            fg="black",
            bg=FRAME_BG_COLOR,
            height=1,
            font=FONT_MEDIUM
        )
        lbl3.place(x=100, y=115)
        
        # Treeview for attendance
        self.tv = ttk.Treeview(
            self.frame1,
            height=13,
            columns=('name', 'date', 'time')
        )
        self.tv.column('#0', width=82)
        self.tv.column('name', width=130)
        self.tv.column('date', width=133)
        self.tv.column('time', width=133)
        self.tv.grid(row=2, column=0, padx=(0, 0), pady=(150, 0), columnspan=4)
        self.tv.heading('#0', text='ID')
        self.tv.heading('name', text='NAME')
        self.tv.heading('date', text='DATE')
        self.tv.heading('time', text='TIME')
        
        # Scrollbar
        scroll = ttk.Scrollbar(
            self.frame1,
            orient='vertical',
            command=self.tv.yview
        )
        scroll.grid(row=2, column=4, padx=(0, 100), pady=(150, 0), sticky='ns')
        self.tv.configure(yscrollcommand=scroll.set)
        
        # Buttons
        trackImg = tk.Button(
            self.frame1,
            text="Take Attendance",
            command=self._track_attendance,
            fg="black",
            bg="yellow",
            width=35,
            height=1,
            activebackground="white",
            font=FONT_SMALL
        )
        trackImg.place(x=30, y=50)
        
        quitWindow = tk.Button(
            self.frame1,
            text="Quit",
            command=self.window.destroy,
            fg="black",
            bg="red",
            width=35,
            height=1,
            activebackground="white",
            font=FONT_SMALL
        )
        quitWindow.place(x=30, y=450)
    
    def _create_menubar(self):
        """Create the menu bar."""
        menubar = tk.Menu(self.window, relief='ridge')
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label='Change Password', command=self._change_password)
        filemenu.add_command(label='Contact Us', command=self._show_contact)
        filemenu.add_command(label='Exit', command=self.window.destroy)
        menubar.add_cascade(label='Help', font=FONT_LARGE, menu=filemenu)
        self.window.configure(menu=menubar)
    
    def _start_clock(self):
        """Start the clock update loop."""
        def tick():
            time_string = time.strftime('%H:%M:%S')
            self.clock.config(text=time_string)
            self.clock.after(200, tick)
        tick()
    
    def _clear_id(self):
        """Clear the ID input field."""
        self.txt.delete(0, 'end')
        self.message1.configure(text="1) Take Images  >>>  2) Save Profile")
    
    def _clear_name(self):
        """Clear the name input field."""
        self.txt2.delete(0, 'end')
        self.message1.configure(text="1) Take Images  >>>  2) Save Profile")
    
    def _take_images(self):
        """Handle taking images for registration."""
        if not check_haarcascade_file():
            mess._show(
                title='File Missing',
                message='Haarcascade file missing. Please contact support.'
            )
            return
        
        student_id = self.txt.get().strip()
        student_name = self.txt2.get().strip()
        
        if not student_id or not student_name:
            mess._show(title='Error', message='Please enter both ID and Name')
            return
        
        if not student_name.replace(' ', '').isalpha():
            mess._show(title='Error', message='Name should contain only letters')
            return
        
        success, message = self.face_capture.capture_images(student_id, student_name)
        self.message1.configure(text=message)
        
        if success:
            self._update_registration_count()
    
    def _save_profile(self):
        """Handle saving/training the profile."""
        if not self.password_manager.password_exists():
            password = tsd.askstring(
                'Password Required',
                'Set a password for training:',
                show='*'
            )
            if password:
                success, msg = self.password_manager.initialize_password(password)
                if not success:
                    mess._show(title='Error', message=msg)
                    return
            else:
                return
        else:
            password = tsd.askstring('Password', 'Enter Password:', show='*')
            if not password:
                return
            if not self.password_manager.verify_password(password):
                mess._show(title='Wrong Password', message='Incorrect password!')
                return
        
        success, message, num_reg = self.face_trainer.train_model()
        self.message1.configure(text=message)
        
        if success:
            self.message.configure(
                text=f'Total Registrations: {num_reg}'
            )
    
    def _track_attendance(self):
        """Handle tracking attendance."""
        if not check_haarcascade_file():
            mess._show(
                title='File Missing',
                message='Haarcascade file missing. Please contact support.'
            )
            return
        
        # Clear existing treeview entries
        for item in self.tv.get_children():
            self.tv.delete(item)
        
        try:
            tracker = AttendanceTracker()
            
            def update_ui(student_id, name, date, time):
                """Callback to update treeview."""
                self.tv.insert('', 0, text=f"{student_id}   ",
                             values=(name, date, time))
            
            success, message, records = tracker.start_tracking(update_ui)
            
            if not success and "Error" in message:
                mess._show(title='Error', message=message)
        
        except FileNotFoundError as e:
            mess._show(title='Error', message=str(e))
        except Exception as e:
            mess._show(title='Error', message=f'An error occurred: {str(e)}')
    
    def _change_password(self):
        """Open change password dialog."""
        dialog = tk.Toplevel(self.window)
        dialog.geometry("400x160")
        dialog.resizable(False, False)
        dialog.title("Change Password")
        dialog.configure(background="white")
        
        # Old password
        tk.Label(
            dialog,
            text='Enter Old Password',
            bg='white',
            font=('times', 12, 'bold')
        ).place(x=10, y=10)
        
        old = tk.Entry(dialog, width=25, fg="black", show='*',
                      font=('times', 12, 'bold'), relief='solid')
        old.place(x=180, y=10)
        
        # New password
        tk.Label(
            dialog,
            text='Enter New Password',
            bg='white',
            font=('times', 12, 'bold')
        ).place(x=10, y=45)
        
        new = tk.Entry(dialog, width=25, fg="black", show='*',
                      font=('times', 12, 'bold'), relief='solid')
        new.place(x=180, y=45)
        
        # Confirm password
        tk.Label(
            dialog,
            text='Confirm New Password',
            bg='white',
            font=('times', 12, 'bold')
        ).place(x=10, y=80)
        
        confirm = tk.Entry(dialog, width=25, fg="black", show='*',
                          font=('times', 12, 'bold'), relief='solid')
        confirm.place(x=180, y=80)
        
        def save_new_password():
            success, msg = self.password_manager.change_password(
                old.get(), new.get(), confirm.get()
            )
            mess._show(
                title='Success' if success else 'Error',
                message=msg
            )
            if success:
                dialog.destroy()
        
        # Buttons
        tk.Button(
            dialog,
            text="Cancel",
            command=dialog.destroy,
            fg="black",
            bg="red",
            height=1,
            width=25,
            font=('times', 10, 'bold')
        ).place(x=200, y=120)
        
        tk.Button(
            dialog,
            text="Save",
            command=save_new_password,
            fg="black",
            bg=HEADER_BG_COLOR,
            height=1,
            width=25,
            font=('times', 10, 'bold')
        ).place(x=10, y=120)
    
    def _show_contact(self):
        """Show contact information."""
        mess._show(
            title='Contact Us',
            message=f'Please contact us at: {CONTACT_EMAIL}'
        )
    
    def _update_registration_count(self):
        """Update the registration count display."""
        from src.utils import count_csv_entries
        from config.config import STUDENT_DETAILS_CSV
        
        count = count_csv_entries(str(STUDENT_DETAILS_CSV))
        self.message.configure(text=f'Total Registrations: {count}')
    
    def run(self):
        """Run the GUI main loop."""
        self.window.mainloop()
