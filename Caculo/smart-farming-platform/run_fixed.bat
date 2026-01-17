@echo off
echo 🌱 Smart Farming Platform - Fixed Version
echo ==========================================

echo Step 1: Training CNN model...
python setup.py

if %errorlevel% neq 0 (
    echo ❌ Model training failed
    pause
    exit /b 1
)

echo Step 2: Starting application...
streamlit run src/app.py

pause