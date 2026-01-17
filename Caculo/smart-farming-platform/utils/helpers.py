import os
import base64
from PIL import Image
import io
from datetime import datetime

def validate_image(uploaded_file):
    """
    Validate uploaded image file
    Returns True if valid, False otherwise
    """
    try:
        # Check file size (max 10MB)
        if uploaded_file.size > 10 * 1024 * 1024:
            return False, "File size too large (max 10MB)"
        
        # Check file type
        allowed_types = ['png', 'jpg', 'jpeg', 'gif', 'bmp']
        file_extension = uploaded_file.name.split('.')[-1].lower()
        
        if file_extension not in allowed_types:
            return False, f"Unsupported file type. Allowed: {', '.join(allowed_types)}"
        
        # Try to open image
        image = Image.open(uploaded_file)
        image.verify()
        
        return True, "Valid image"
        
    except Exception as e:
        return False, f"Invalid image file: {str(e)}"

def resize_image(image, max_size=(800, 600)):
    """
    Resize image while maintaining aspect ratio
    """
    try:
        # Calculate new size maintaining aspect ratio
        image.thumbnail(max_size, Image.Resampling.LANCZOS)
        return image
    except Exception as e:
        print(f"Error resizing image: {e}")
        return image

def image_to_base64(image):
    """
    Convert PIL image to base64 string for storage/transmission
    """
    try:
        buffer = io.BytesIO()
        image.save(buffer, format='PNG')
        img_str = base64.b64encode(buffer.getvalue()).decode()
        return img_str
    except Exception as e:
        print(f"Error converting image to base64: {e}")
        return None

def base64_to_image(base64_string):
    """
    Convert base64 string back to PIL image
    """
    try:
        img_data = base64.b64decode(base64_string)
        image = Image.open(io.BytesIO(img_data))
        return image
    except Exception as e:
        print(f"Error converting base64 to image: {e}")
        return None

def format_confidence(confidence):
    """
    Format confidence score for display
    """
    if confidence >= 90:
        return f"{confidence:.1f}% (Very High)"
    elif confidence >= 75:
        return f"{confidence:.1f}% (High)"
    elif confidence >= 60:
        return f"{confidence:.1f}% (Moderate)"
    elif confidence >= 40:
        return f"{confidence:.1f}% (Low)"
    else:
        return f"{confidence:.1f}% (Very Low)"

def get_severity_color(confidence):
    """
    Get color code based on confidence/severity
    """
    if confidence >= 80:
        return "#FF4444"  # Red - High severity
    elif confidence >= 60:
        return "#FF8800"  # Orange - Medium severity
    elif confidence >= 40:
        return "#FFBB00"  # Yellow - Low severity
    else:
        return "#44AA44"  # Green - Very low/healthy

def format_eco_rating(rating):
    """
    Format eco-friendliness rating with visual indicators
    """
    stars = "🌱" * rating + "⚪" * (5 - rating)
    descriptions = {
        5: "Completely Eco-Friendly",
        4: "Very Eco-Friendly", 
        3: "Moderately Eco-Friendly",
        2: "Somewhat Eco-Friendly",
        1: "Minimally Eco-Friendly"
    }
    
    return f"{stars} {descriptions.get(rating, 'Unknown')} ({rating}/5)"

def calculate_environmental_impact(treatments):
    """
    Calculate overall environmental impact score
    """
    if not treatments:
        return 0, "No treatments selected"
    
    total_rating = sum(treatment.get('eco_rating', 0) for treatment in treatments)
    avg_rating = total_rating / len(treatments)
    
    impact_levels = {
        (4.5, 5.0): ("Excellent", "Minimal environmental impact", "#00AA00"),
        (3.5, 4.5): ("Good", "Low environmental impact", "#88AA00"),
        (2.5, 3.5): ("Fair", "Moderate environmental impact", "#AAAA00"),
        (1.5, 2.5): ("Poor", "High environmental impact", "#AA8800"),
        (0.0, 1.5): ("Very Poor", "Very high environmental impact", "#AA0000")
    }
    
    for (min_val, max_val), (level, description, color) in impact_levels.items():
        if min_val <= avg_rating <= max_val:
            return avg_rating, level, description, color
    
    return avg_rating, "Unknown", "Impact assessment unavailable", "#888888"

def generate_report_summary(disease, confidence, treatments, weather_data=None):
    """
    Generate a comprehensive report summary
    """
    summary = {
        "analysis_date": "2024-01-15",  # In production, use actual date
        "crop_health": {
            "status": disease,
            "confidence": confidence,
            "severity": "High" if confidence > 80 else "Moderate" if confidence > 60 else "Low"
        },
        "treatment_plan": {
            "total_options": len(treatments),
            "eco_rating": sum(t.get('eco_rating', 0) for t in treatments) / len(treatments) if treatments else 0,
            "estimated_cost": "Variable based on selected treatments"
        },
        "recommendations": {
            "immediate_action": "Apply most eco-friendly treatment within 24 hours" if disease != "Healthy" else "Continue preventive care",
            "monitoring": "Check plant health every 2-3 days",
            "prevention": "Implement suggested prevention measures"
        }
    }
    
    if weather_data:
        summary["environmental_factors"] = {
            "temperature": f"{weather_data['temperature']}°C",
            "humidity": f"{weather_data['humidity']}%",
            "disease_risk": weather_data.get('disease_risk', 'Unknown'),
            "irrigation_need": weather_data.get('irrigation_need', 'Unknown')
        }
    
    return summary

def create_project_structure():
    """
    Create necessary project directories if they don't exist
    """
    directories = [
        'data',
        'models', 
        'utils',
        'assets',
        'logs'
    ]
    
    for directory in directories:
        if not os.path.exists(directory):
            os.makedirs(directory)
            print(f"Created directory: {directory}")

def log_analysis(disease, confidence, treatments_count):
    """
    Log analysis for tracking and improvement
    """
    try:
        log_entry = f"Analysis: {disease} (Confidence: {confidence:.1f}%) - {treatments_count} treatments suggested\n"
        
        # Create logs directory if it doesn't exist
        if not os.path.exists('logs'):
            os.makedirs('logs')
        
        # Append to log file
        with open('logs/analysis_log.txt', 'a') as f:
            f.write(f"[{datetime.now()}] {log_entry}")
            
    except Exception as e:
        print(f"Logging error: {e}")

# Constants for the application
SUPPORTED_IMAGE_FORMATS = ['PNG', 'JPG', 'JPEG', 'GIF', 'BMP']
MAX_IMAGE_SIZE = 10 * 1024 * 1024  # 10MB
DEFAULT_IMAGE_SIZE = (800, 600)

# Disease severity thresholds
SEVERITY_THRESHOLDS = {
    'HIGH': 80,
    'MODERATE': 60,
    'LOW': 40
}

# Eco-rating descriptions
ECO_RATINGS = {
    5: "Completely natural and environmentally safe",
    4: "Mostly natural with minimal environmental impact", 
    3: "Balanced approach with moderate environmental consideration",
    2: "Some environmental concerns but still acceptable",
    1: "High environmental impact - use only when necessary"
}