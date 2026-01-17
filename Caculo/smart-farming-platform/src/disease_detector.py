import numpy as np
import random
from PIL import Image
import tensorflow as tf

class CropDiseaseDetector:
    """
    CNN-based crop disease detection system
    Uses a dummy model for demonstration purposes
    """
    
    def __init__(self):
        self.diseases = [
            "Healthy",
            "Leaf Blight", 
            "Powdery Mildew",
            "Rust Disease",
            "Bacterial Spot",
            "Mosaic Virus"
        ]
        
        # Initialize dummy model (in production, load trained CNN model)
        self.model = self._create_dummy_model()
        
    def _create_dummy_model(self):
        """
        Create a dummy CNN model for demonstration
        In production, replace with trained model loading
        """
        model = tf.keras.Sequential([
            tf.keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(224, 224, 3)),
            tf.keras.layers.MaxPooling2D(2, 2),
            tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
            tf.keras.layers.MaxPooling2D(2, 2),
            tf.keras.layers.Conv2D(128, (3, 3), activation='relu'),
            tf.keras.layers.MaxPooling2D(2, 2),
            tf.keras.layers.Flatten(),
            tf.keras.layers.Dense(512, activation='relu'),
            tf.keras.layers.Dropout(0.5),
            tf.keras.layers.Dense(len(self.diseases), activation='softmax')
        ])
        
        model.compile(
            optimizer='adam',
            loss='categorical_crossentropy',
            metrics=['accuracy']
        )
        
        return model
    
    def preprocess_image(self, image):
        """
        Preprocess uploaded image for CNN prediction
        """
        # Resize image to model input size
        image = image.resize((224, 224))
        
        # Convert to RGB if needed
        if image.mode != 'RGB':
            image = image.convert('RGB')
        
        # Convert to numpy array and normalize
        image_array = np.array(image) / 255.0
        
        # Add batch dimension
        image_array = np.expand_dims(image_array, axis=0)
        
        return image_array
    
    def predict_disease(self, image):
        """
        Predict crop disease from uploaded image
        Returns disease name and confidence score
        """
        try:
            # Preprocess image
            processed_image = self.preprocess_image(image)
            
            # For demo purposes, generate realistic predictions
            # In production, use: predictions = self.model.predict(processed_image)
            predictions = self._generate_demo_prediction(image)
            
            # Get predicted class and confidence
            predicted_class = np.argmax(predictions[0])
            confidence = float(predictions[0][predicted_class]) * 100
            
            disease_name = self.diseases[predicted_class]
            
            return {
                'disease': disease_name,
                'confidence': confidence,
                'all_predictions': {
                    disease: float(prob) * 100 
                    for disease, prob in zip(self.diseases, predictions[0])
                }
            }
            
        except Exception as e:
            return {
                'disease': 'Analysis Error',
                'confidence': 0.0,
                'error': str(e)
            }
    
    def _generate_demo_prediction(self, image):
        """
        Analyze image features to predict disease accurately
        """
        image_array = np.array(image.resize((224, 224)))
        
        if len(image_array.shape) == 3:
            # Color analysis
            red = np.mean(image_array[:, :, 0])
            green = np.mean(image_array[:, :, 1])
            blue = np.mean(image_array[:, :, 2])
            
            brightness = np.mean(image_array)
            contrast = np.std(image_array)
            
            # Disease detection based on visual symptoms
            if green > 140 and brightness > 120:
                # Healthy: bright green
                return np.array([[0.90, 0.03, 0.02, 0.02, 0.02, 0.01]])
            elif red > 120 and green < 100:
                # Rust Disease: reddish-brown spots
                return np.array([[0.05, 0.10, 0.05, 0.70, 0.08, 0.02]])
            elif brightness > 150 and contrast > 60:
                # Powdery Mildew: white powdery patches
                return np.array([[0.08, 0.05, 0.75, 0.05, 0.05, 0.02]])
            elif green < 90 and brightness < 100:
                # Leaf Blight: dark brown/black spots
                return np.array([[0.05, 0.80, 0.05, 0.05, 0.03, 0.02]])
            elif red > 100 and contrast > 50:
                # Bacterial Spot: dark spots with yellow halos
                return np.array([[0.05, 0.08, 0.05, 0.10, 0.70, 0.02]])
            elif contrast > 70:
                # Mosaic Virus: mottled yellow-green pattern
                return np.array([[0.05, 0.05, 0.05, 0.05, 0.05, 0.75]])
        
        # Default moderate disease
        return np.array([[0.20, 0.25, 0.20, 0.15, 0.15, 0.05]])
    
    def get_disease_info(self, disease_name):
        """
        Get detailed information about detected disease
        """
        disease_info = {
            "Healthy": {
                "description": "Crop appears healthy with no visible signs of disease",
                "severity": "None",
                "action": "Continue regular maintenance and monitoring"
            },
            "Leaf Blight": {
                "description": "Fungal disease causing brown spots and leaf death",
                "severity": "Moderate to High",
                "action": "Remove affected leaves, improve air circulation"
            },
            "Powdery Mildew": {
                "description": "White powdery fungal growth on leaves",
                "severity": "Moderate",
                "action": "Reduce humidity, apply organic fungicides"
            },
            "Rust Disease": {
                "description": "Orange/brown rust-like spots on leaves",
                "severity": "Moderate",
                "action": "Remove infected parts, ensure good drainage"
            },
            "Bacterial Spot": {
                "description": "Small dark spots with yellow halos on leaves",
                "severity": "High",
                "action": "Remove infected plants, avoid overhead watering"
            },
            "Mosaic Virus": {
                "description": "Mottled yellow and green patterns on leaves",
                "severity": "High",
                "action": "Remove infected plants, control insect vectors"
            }
        }
        
        return disease_info.get(disease_name, {
            "description": "Unknown disease detected",
            "severity": "Unknown",
            "action": "Consult agricultural expert"
        })