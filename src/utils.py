"""
Utility functions for the Face Recognition Attendance System.

This module contains helper functions used across different modules.
"""

import os
import time
import datetime
from pathlib import Path
from typing import Tuple


def assure_path_exists(path: str) -> None:
    """
    Ensure that a directory exists, creating it if necessary.
    
    Args:
        path: Path to the directory
    """
    directory = os.path.dirname(path)
    if not os.path.exists(directory):
        os.makedirs(directory)


def get_current_timestamp() -> float:
    """
    Get the current timestamp.
    
    Returns:
        Current timestamp as a float
    """
    return time.time()


def format_date(timestamp: float, date_format: str = '%d-%m-%Y') -> str:
    """
    Format a timestamp as a date string.
    
    Args:
        timestamp: Unix timestamp
        date_format: Date format string
        
    Returns:
        Formatted date string
    """
    return datetime.datetime.fromtimestamp(timestamp).strftime(date_format)


def format_time(timestamp: float, time_format: str = '%H:%M:%S') -> str:
    """
    Format a timestamp as a time string.
    
    Args:
        timestamp: Unix timestamp
        time_format: Time format string
        
    Returns:
        Formatted time string
    """
    return datetime.datetime.fromtimestamp(timestamp).strftime(time_format)


def parse_date(date_string: str) -> Tuple[str, str, str]:
    """
    Parse a date string in DD-MM-YYYY format.
    
    Args:
        date_string: Date string in DD-MM-YYYY format
        
    Returns:
        Tuple of (day, month, year)
    """
    parts = date_string.split('-')
    if len(parts) == 3:
        return parts[0], parts[1], parts[2]
    return '', '', ''


def get_month_name(month_number: str, month_dict: dict) -> str:
    """
    Get the full name of a month from its number.
    
    Args:
        month_number: Month number as string (01-12)
        month_dict: Dictionary mapping month numbers to names
        
    Returns:
        Full month name
    """
    return month_dict.get(month_number, '')


def validate_name(name: str) -> bool:
    """
    Validate that a name contains only alphabetic characters and spaces.
    
    Args:
        name: Name string to validate
        
    Returns:
        True if name is valid, False otherwise
    """
    return name.isalpha() or (' ' in name and all(c.isalpha() or c.isspace() for c in name))


def validate_id(id_string: str) -> bool:
    """
    Validate that an ID is numeric.
    
    Args:
        id_string: ID string to validate
        
    Returns:
        True if ID is valid, False otherwise
    """
    return id_string.isdigit()


def count_csv_entries(file_path: str) -> int:
    """
    Count the number of data entries in a CSV file (excluding header).
    
    Args:
        file_path: Path to the CSV file
        
    Returns:
        Number of entries
    """
    if not os.path.isfile(file_path):
        return 0
    
    with open(file_path, 'r') as f:
        lines = f.readlines()
        # Subtract header rows and account for empty row format
        return (len(lines) // 2) - 1 if len(lines) > 1 else 0


def get_next_serial_number(file_path: str) -> int:
    """
    Get the next serial number for a new entry.
    
    Args:
        file_path: Path to the student details CSV
        
    Returns:
        Next available serial number
    """
    if not os.path.isfile(file_path):
        return 1
    
    import csv
    serial = 0
    with open(file_path, 'r') as csvFile:
        reader = csv.reader(csvFile)
        for line in reader:
            serial += 1
    return (serial // 2) if serial > 0 else 1
