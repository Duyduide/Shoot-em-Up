#!/usr/bin/env python3
"""
SHOOT 'EM UP - Setup Script
Script để cài đặt dependencies và setup game
"""

import subprocess
import sys
import os

def install_requirements():
    """Cài đặt requirements"""
    try:
        print("Installing pygame...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pygame>=2.5.0"])
        print("✅ pygame installed successfully!")
        
        print("Installing numpy...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "numpy>=1.21.0"])
        print("✅ numpy installed successfully!")
        
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error installing packages: {e}")
        return False

def check_python_version():
    """Kiểm tra version Python"""
    if sys.version_info < (3, 8):
        print("❌ Python 3.8 or higher is required!")
        return False
    print(f"✅ Python {sys.version_info.major}.{sys.version_info.minor} detected")
    return True

def main():
    """Main setup function"""
    print("=== SHOOT 'EM UP - Game Setup ===\n")
    
    # Check Python version
    if not check_python_version():
        return 1
    
    # Install requirements
    print("\nInstalling dependencies...")
    if not install_requirements():
        return 1
    
    print("\n✅ Setup completed successfully!")
    print("\nTo run the game:")
    print("python main.py")
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
