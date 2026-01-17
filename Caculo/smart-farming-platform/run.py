#!/usr/bin/env python3
"""
Smart Farming Platform Launcher
Run this script to start the Streamlit application
"""

import subprocess
import sys
import os

def check_requirements():
    """Check if required packages are installed"""
    try:
        import streamlit
        import tensorflow
        import PIL
        import requests
        import pandas
        import numpy
        print("✅ All required packages are installed")
        return True
    except ImportError as e:
        print(f"❌ Missing package: {e}")
        print("Please install requirements: pip install -r requirements.txt")
        return False

def main():
    print("🌱 Smart Farming Platform")
    print("=" * 50)
    
    # Check if we're in the right directory
    if not os.path.exists("src/app.py"):
        print("❌ Error: Please run this script from the smart-farming-platform directory")
        sys.exit(1)
    
    # Check requirements
    if not check_requirements():
        sys.exit(1)
    
    print("🚀 Starting Streamlit application...")
    print("📱 The app will open in your default web browser")
    print("🔗 URL: http://localhost:8501")
    print("⏹️  Press Ctrl+C to stop the application")
    print("-" * 50)
    
    try:
        # Start Streamlit app
        subprocess.run([sys.executable, "-m", "streamlit", "run", "src/app.py"])
    except KeyboardInterrupt:
        print("\n👋 Application stopped by user")
    except Exception as e:
        print(f"❌ Error starting application: {e}")

if __name__ == "__main__":
    main()