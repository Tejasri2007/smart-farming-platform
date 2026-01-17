import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import numpy as np
import os

# CRITICAL: Class labels MUST match training folder order exactly
CLASS_LABELS = [
    'Bacterial Spot',
    'Healthy', 
    'Leaf Blight',
    'Mosaic Virus',
    'Powdery Mildew',
    'Rust Disease'
]

def create_model(num_classes=6):
    """Create CNN model for crop disease classification"""
    model = models.Sequential([
        layers.Conv2D(32, (3, 3), activation='relu', input_shape=(224, 224, 3)),
        layers.BatchNormalization(),
        layers.MaxPooling2D(2, 2),
        layers.Dropout(0.25),
        
        layers.Conv2D(64, (3, 3), activation='relu'),
        layers.BatchNormalization(),
        layers.MaxPooling2D(2, 2),
        layers.Dropout(0.25),
        
        layers.Conv2D(128, (3, 3), activation='relu'),
        layers.BatchNormalization(),
        layers.MaxPooling2D(2, 2),
        layers.Dropout(0.25),
        
        layers.Flatten(),
        layers.Dense(512, activation='relu'),
        layers.Dropout(0.5),
        layers.Dense(num_classes, activation='softmax')
    ])
    
    model.compile(
        optimizer='adam',
        loss='categorical_crossentropy',
        metrics=['accuracy']
    )
    
    return model

def preprocess_data():
    """Create data generators with proper preprocessing"""
    # CRITICAL: Same preprocessing as inference
    train_datagen = ImageDataGenerator(
        rescale=1./255,  # Normalize to [0,1]
        rotation_range=20,
        width_shift_range=0.2,
        height_shift_range=0.2,
        horizontal_flip=True,
        zoom_range=0.2,
        validation_split=0.2
    )
    
    return train_datagen

def train_model():
    """Train the crop disease classification model"""
    print("Creating model...")
    model = create_model(len(CLASS_LABELS))
    
    # Create dummy training data for demo
    # In production: replace with real PlantVillage dataset
    print("Generating training data...")
    x_train = np.random.random((600, 224, 224, 3))
    y_train = tf.keras.utils.to_categorical(
        np.random.randint(0, len(CLASS_LABELS), 600), 
        num_classes=len(CLASS_LABELS)
    )
    
    x_val = np.random.random((150, 224, 224, 3))
    y_val = tf.keras.utils.to_categorical(
        np.random.randint(0, len(CLASS_LABELS), 150),
        num_classes=len(CLASS_LABELS)
    )
    
    print("Training model...")
    history = model.fit(
        x_train, y_train,
        batch_size=32,
        epochs=5,  # Demo-friendly
        validation_data=(x_val, y_val),
        verbose=1
    )
    
    # Save model
    model.save('models/crop_disease_model.h5')
    print("Model saved to models/crop_disease_model.h5")
    
    # Save class labels
    with open('models/class_labels.txt', 'w') as f:
        for label in CLASS_LABELS:
            f.write(f"{label}\n")
    
    return model, history

if __name__ == "__main__":
    # Create models directory
    os.makedirs('models', exist_ok=True)
    
    # Train model
    model, history = train_model()
    
    print(f"Training completed!")
    print(f"Classes: {CLASS_LABELS}")
    print("Model ready for inference!")