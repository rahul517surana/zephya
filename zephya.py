import plistlib
import subprocess
import shutil
import re
import os
from typing import Dict
from colorama import Fore, Style, init   # type: ignore

# Define constants
ANDROID_PERMISSIONS = [
    "android.permission.ACCESS_COARSE_LOCATION",
    "android.permission.ACCESS_FINE_LOCATION",
    "android.permission.CAMERA",
    "android.permission.RECORD_AUDIO",
    "android.permission.READ_CONTACTS",
    "android.permission.WRITE_CONTACTS",
    "android.permission.READ_SMS",
    "android.permission.RECEIVE_SMS",
    "android.permission.SEND_SMS",
    "android.permission.READ_CALL_LOG",
    "android.permission.WRITE_CALL_LOG",
    "android.permission.PROCESS_OUTGOING_CALLS",
    "android.permission.READ_PHONE_STATE",
    "android.permission.CALL_PHONE",
    "android.permission.READ_PHONE_NUMBERS",
    "android.permission.ANSWER_PHONE_CALLS"
]

IOS_PERMISSIONS = [
    "NSLocationAlwaysUsageDescription",
    "NSLocationWhenInUseUsageDescription",
    "NSCameraUsageDescription",
    "NSMicrophoneUsageDescription",
    "NSContactsUsageDescription",
    "NSCalendarUsageDescription",
    "NSRemindersUsageDescription",
    "NSHealthUsageDescription",
    "NSMotionUsageDescription",
    "NSHealthShareUsageDescription",
    "NSHealthUpdateUsageDescription"
]

NS_APP_TRANSPORT_SECURITY = "NSAppTransportSecurity"
NS_ALLOWS_ARBITRARY_LOADS = "NSAllowsArbitraryLoads"

def print_header():
    """Prints the Zephyr app header with an eye design"""
    color = Fore.GREEN
    print(color + """
  

███████╗███████╗██████╗░██╗░░██╗██╗░░░██╗██████╗░
╚════██║██╔════╝██╔══██╗██║░░██║╚██╗░██╔╝██╔══██╗
░░███╔═╝█████╗░░██████╔╝███████║░╚████╔╝░██████╔╝
██╔══╝░░██╔══╝░░██╔═══╝░██╔══██║░░╚██╔╝░░██╔══██╗
███████╗███████╗██║░░░░░██║░░██║░░░██║░░░██║░░██║
╚══════╝╚══════╝╚═╝░░░░░╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝

  Zephyr Mobile App Security Analyzer

  Made by Rahul Surana
  """ + Style.RESET_ALL)


def print_menu():
    """ Prints the menu options"""
    color = Fore.GREEN
    print(color + """
  1. Select File
  2. Help
  3. About
  4. Exit
  Enter your choice: """ + Style.RESET_ALL)


def select_file():
    """Prompts the user to select a file"""
    print_header()
    print("Enter the path to the mobile app file (APK or IPA):")
    file_path = input()

    try:
        with open(file_path, 'rb') as file:
            file_content = file.read()  # Read the file content
            print(f"File '{file_path}' selected successfully. Size: {len(file_content)} bytes")
            # Implement code to analyze the file here
            if file_path.lower().endswith('.apk'):
                analyze_android_app(file_path)
            elif file_path.lower().endswith('.ipa'):
                analyze_ios_app(file_path)
            else:
                print("Unsupported file type. Please select an APK or IPA file.")
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")


def print_help():
    """Prints the help message"""
    print_header()
    color = Fore.GREEN
    print(color + """
  Zephyr helps you analyze mobile applications for security vulnerabilities.

  * Select File (1): Choose the mobile app file (APK or IPA) for analysis.

  * Help (2): Displays this help message.

  * About (3): Displays information about Zephyr and its developer.

  * Exit (4): Terminates the application.
  """ + Style.RESET_ALL)
    print("1. Back")
    print("2. Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        main_menu()
    elif choice == '2':
        print("Exiting Zephyr. Goodbye!")
        exit()
    else:
        print("Invalid choice. Please try again.")
        print_help()


def print_about():
    """ Prints information about Z ephyr and its developer"""
    print_header()
    color = Fore.GREEN
    print(color + """
  Zephyr is a mobile app security analyzer developed by Rahul Surana.

  It helps you identify potential security vulnerabilities in your mobile apps.

  For more information, please visit https://github.com/rahulsurana/zephyr
  """ + Style.RESET_ALL)
    print("1. Back")
    print("2. Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        main_menu()
    elif choice == '2':
        print("Exiting Zephyr. Goodbye!")
        exit()
    else:
        print("Invalid choice. Please try again.")
        print_about()


def analyze_android_app(file_path):
    """Analyzes the Android app for security vulnerabilities"""
    print("Analyzing Android app...")
    # Implement code to analyze the Android app here
    pass


def analyze_ios_app(file_path):
    """Analyzes the iOS app for security vulnerabilities"""
    print("Analyzing iOS app...")
    # Implement code to analyze the iOS app here
    pass


def main_menu():
    """Displays the main menu"""
    print_header()
    print_menu()
    choice = input()
    if choice == '1':
        select_file()
    elif choice == '2':
        print_help()
    elif choice == '3':
        print_about()
    elif choice == '4':
        print("Exiting Zephyr. Goodbye!")
        exit()
    else:
        print("Invalid choice. Please try again.")
        main_menu()


if __name__ == "__main__":
    init()  # Initialize colorama
    main_menu()
