# Smart Farming Platform - Setup Guide

## Quick Start (3 Steps)

### 1. Install Python Dependencies
```bash
pip install -r requirements.txt
```

### 2. Run the Application
**Option A - Windows:**
```bash
run.bat
```

**Option B - Cross-platform:**
```bash
python run.py
```

**Option C - Direct Streamlit:**
```bash
streamlit run src/app.py
```

### 3. Open Your Browser
- The app will automatically open at: `http://localhost:8501`
- If not, manually navigate to the URL above

## Detailed Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- 4GB+ RAM recommended
- Internet connection (for weather data)

### Step-by-Step Setup

1. **Download/Clone the Project**
   ```bash
   # If using git
   git clone <repository-url>
   cd smart-farming-platform
   
   # Or extract downloaded ZIP file
   cd smart-farming-platform
   ```

2. **Create Virtual Environment (Recommended)**
   ```bash
   # Create virtual environment
   python -m venv farming_env
   
   # Activate it
   # Windows:
   farming_env\Scripts\activate
   
   # macOS/Linux:
   source farming_env/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Verify Installation**
   ```bash
   python -c "import streamlit, tensorflow, PIL; print('All packages installed successfully!')"
   ```

5. **Run the Application**
   ```bash
   streamlit run src/app.py
   ```

## Optional: Weather API Setup

For real weather data (optional - demo mode works without this):

1. **Get Free API Key**
   - Visit: https://openweathermap.org/api
   - Sign up for free account
   - Get your API key

2. **Configure API Key**
   - Open `src/weather_service.py`
   - Replace `YOUR_API_KEY` with your actual key
   - Set `demo_mode = False`

## Troubleshooting

### Common Issues

**1. TensorFlow Installation Issues**
```bash
# If TensorFlow fails to install
pip install tensorflow-cpu  # For CPU-only version
# OR
pip install tensorflow==2.13.0  # Specific version
```

**2. Streamlit Port Already in Use**
```bash
# Use different port
streamlit run src/app.py --server.port 8502
```

**3. Module Import Errors**
```bash
# Ensure you're in the correct directory
cd smart-farming-platform
python run.py
```

**4. Memory Issues**
```bash
# If running out of memory, reduce TensorFlow usage
# Edit src/disease_detector.py and use smaller model
```

### System Requirements

**Minimum:**
- Python 3.8+
- 2GB RAM
- 1GB free disk space

**Recommended:**
- Python 3.9+
- 4GB+ RAM
- 2GB+ free disk space
- GPU (optional, for faster processing)

## Project Structure Explained

```
smart-farming-platform/
├── src/                    # Main application code
│   ├── app.py             # Streamlit web interface
│   ├── disease_detector.py # AI disease detection
│   ├── weather_service.py  # Weather API integration
│   └── treatment_advisor.py # Treatment recommendations
├── models/                 # AI model files
│   └── crop_disease_model.py # CNN model definition
├── data/                   # Data files
│   └── treatments.json     # Treatment database
├── utils/                  # Utility functions
│   └── helpers.py         # Helper functions
├── requirements.txt        # Python dependencies
├── run.py                 # Cross-platform launcher
├── run.bat               # Windows launcher
└── README.md             # Project documentation
```

## Features Overview

### 🔍 Disease Detection
- Upload crop images
- AI-powered disease identification
- Confidence scoring
- Multiple disease types supported

### 🌿 Sustainable Treatments
- Eco-friendly treatment options
- Natural ingredient recommendations
- Environmental impact ratings
- Cost-effective solutions

### 🌤️ Weather Integration
- Real-time weather data
- Climate-aware farming advice
- Irrigation recommendations
- Disease risk assessment

### 📊 Analytics
- Treatment effectiveness tracking
- Environmental impact scoring
- Comprehensive reporting
- Prevention guidance

## Usage Tips

1. **Best Image Quality**: Use clear, well-lit photos of affected plant parts
2. **Multiple Angles**: Upload different angles for better analysis
3. **Regular Monitoring**: Check plants weekly for early detection
4. **Follow Treatments**: Implement recommended eco-friendly solutions
5. **Weather Awareness**: Check weather advice before applying treatments

## Development Notes

### For Developers

**Adding New Diseases:**
1. Update `disease_detector.py` with new disease classes
2. Add treatment data to `data/treatments.json`
3. Retrain CNN model with new disease images

**Customizing Treatments:**
1. Edit `data/treatments.json` for new treatments
2. Modify `treatment_advisor.py` for custom logic
3. Update eco-rating system as needed

**Weather Integration:**
1. Replace demo weather with real API in `weather_service.py`
2. Add new weather parameters as needed
3. Customize farming advice logic

## Support

### Getting Help
- Check this setup guide first
- Review error messages carefully
- Ensure all dependencies are installed
- Verify you're in the correct directory

### Common Solutions
- Restart the application
- Clear browser cache
- Check Python version compatibility
- Reinstall dependencies if needed

## Next Steps

After successful setup:
1. 📸 Upload crop images to test disease detection
2. 🌍 Enter your location for weather insights
3. 📋 Review eco-friendly treatment recommendations
4. 🌱 Implement sustainable farming practices

---

**Ready to revolutionize your farming with AI? Start the application and begin your sustainable farming journey!** 🚀🌱