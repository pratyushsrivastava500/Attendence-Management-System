"""
Password management module for the attendance system.

This module handles password creation, verification, and modification.
"""

import os
from typing import Tuple, Optional
from config.config import PASSWORD_FILE, TRAINING_LABEL_DIR
from src.utils import assure_path_exists


class PasswordManager:
    """Class for managing system password."""
    
    def __init__(self):
        """Initialize the password manager."""
        assure_path_exists(str(TRAINING_LABEL_DIR))
    
    def password_exists(self) -> bool:
        """
        Check if a password has been set.
        
        Returns:
            True if password file exists, False otherwise
        """
        return os.path.isfile(str(PASSWORD_FILE))
    
    def get_password(self) -> Optional[str]:
        """
        Get the stored password.
        
        Returns:
            Password string if exists, None otherwise
        """
        if not self.password_exists():
            return None
        
        with open(str(PASSWORD_FILE), 'r') as f:
            return f.read().strip()
    
    def set_password(self, password: str) -> bool:
        """
        Set a new password.
        
        Args:
            password: New password string
            
        Returns:
            True if successful, False otherwise
        """
        try:
            with open(str(PASSWORD_FILE), 'w') as f:
                f.write(password)
            return True
        except Exception as e:
            print(f"Error setting password: {str(e)}")
            return False
    
    def verify_password(self, password: str) -> bool:
        """
        Verify if the provided password matches the stored password.
        
        Args:
            password: Password to verify
            
        Returns:
            True if password matches, False otherwise
        """
        stored_password = self.get_password()
        if stored_password is None:
            return False
        return password == stored_password
    
    def change_password(self, old_password: str, new_password: str, 
                       confirm_password: str) -> Tuple[bool, str]:
        """
        Change the password.
        
        Args:
            old_password: Current password
            new_password: New password
            confirm_password: Confirmation of new password
            
        Returns:
            Tuple of (success: bool, message: str)
        """
        # Verify old password
        if not self.verify_password(old_password):
            return False, "Incorrect old password"
        
        # Check if new passwords match
        if new_password != confirm_password:
            return False, "New passwords do not match"
        
        # Set new password
        if self.set_password(new_password):
            return True, "Password changed successfully"
        else:
            return False, "Error changing password"
    
    def initialize_password(self, password: str) -> Tuple[bool, str]:
        """
        Initialize password for first-time setup.
        
        Args:
            password: Password to set
            
        Returns:
            Tuple of (success: bool, message: str)
        """
        if password is None or password == "":
            return False, "Password cannot be empty"
        
        if self.set_password(password):
            return True, "Password registered successfully"
        else:
            return False, "Error registering password"
