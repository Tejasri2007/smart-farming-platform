#!/usr/bin/env python3
"""
Setup script for Smart Farming Platform
Trains the CNN model before first use
"""

import os
import sys

def setup_project():
    """Setup the project by training the model"""
    print("🌱 Smart Farming Platform Setup")
    print("=" * 50)
    
    # Check if model exists
    if os.path.exists('models/crop_disease_model.h5'):
        print("✅ Model already exists")
        return True
    
    print("🔧 Training CNN model for disease detection...")
    print("This may take a few minutes...")
    
    try:
        # Import and run training
        from train_model import train_model
        model, history = train_model()
        
        print("✅ Model training completed!")
        print("✅ Setup successful!")
        return True
        
    except Exception as e:
        print(f"❌ Setup failed: {e}")
        return False

if __name__ == "__main__":
    success = setup_project()
    if success:
        print("\n🚀 Ready to run: streamlit run src/app.py")
    else:
        print("\n❌ Setup failed. Please check error messages above.")
        sys.exit(1)