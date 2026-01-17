import numpy as np
from PIL import Image
import os

class CropDiseasePredictor:
    """Visual analysis-based crop disease predictor for deployment"""
    
    def __init__(self):
        self.class_labels = [
            'Bacterial Spot',
            'Healthy', 
            'Leaf Blight',
            'Mosaic Virus',
            'Powdery Mildew',
            'Rust Disease'
        ]
        print("Visual analysis predictor initialized")
    
    def predict(self, image):
        """Predict disease using visual analysis"""
        try:
            image_array = np.array(image.resize((224, 224)))
            
            if len(image_array.shape) == 3:
                # Extract color statistics
                red = np.mean(image_array[:, :, 0])
                green = np.mean(image_array[:, :, 1])
                blue = np.mean(image_array[:, :, 2])
                brightness = np.mean(image_array)
                
                # Disease detection based on visual characteristics
                
                # Healthy: Dominant green, good brightness
                if green > red + 15 and green > blue + 10 and brightness > 100:
                    return "Healthy", 85.0
                
                # Powdery Mildew: High brightness (white patches)
                elif brightness > 180 or (red > 200 and green > 200 and blue > 200):
                    return "Powdery Mildew", 82.0
                
                # Rust Disease: High red, low green (orange/brown)
                elif red > green + 25 and red > 130:
                    return "Rust Disease", 80.0
                
                # Leaf Blight: Low brightness (dark spots)
                elif brightness < 80 or (red < 90 and green < 90 and blue < 90):
                    return "Leaf Blight", 78.0
                
                # Bacterial Spot: Moderate values with some contrast
                elif 90 < brightness < 150 and abs(red - green) > 10:
                    return "Bacterial Spot", 75.0
                
                # Mosaic Virus: Default for other patterns
                else:
                    return "Mosaic Virus", 72.0
                    
            else:
                # Grayscale analysis
                brightness = np.mean(image_array)
                if brightness > 180:
                    return "Powdery Mildew", 70.0
                elif brightness < 80:
                    return "Leaf Blight", 70.0
                else:
                    return "Healthy", 65.0
                    
        except Exception as e:
            print(f"Prediction error: {e}")
            return "Uncertain - Retake Image", 0.0
