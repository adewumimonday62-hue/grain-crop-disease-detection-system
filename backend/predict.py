import numpy as np
import cv2
import joblib
from tensorflow.keras.models import load_model

class DiseasePredictor:
    def __init__(self, model_path, le_path):
        # Load the trained model and label encoder
        self.model = load_model(model_path)
        self.encoder = joblib.load(le_path)

    def preprocess_image(self, image_path):
        # Load and preprocess the image
        image = cv2.imread(image_path)
        image = cv2.resize(image, (224, 224))  # Resize to 224x224
        image = image.astype('float32') / 255.0  # Normalize
        return np.expand_dims(image, axis=0)  # Add batch dimension

    def predict(self, image_path):
        # Preprocess the image
        processed_image = self.preprocess_image(image_path)
        # Make predictions
        predictions = self.model.predict(processed_image)
        confidence_score = np.max(predictions)
        class_index = np.argmax(predictions)
        disease_name = self.encoder.inverse_transform([class_index])[0]
        treatment_recommendations = self.get_treatment_recommendations(disease_name)
        return disease_name, confidence_score, treatment_recommendations

    def get_treatment_recommendations(self, disease_name):
        # Placeholder for treatment recommendations based on disease
        recommendations = {
            'DiseaseA': 'Recommendation for Disease A',
            'DiseaseB': 'Recommendation for Disease B',
            # Add more diseases and recommendations as per requirement
        }
        return recommendations.get(disease_name, 'No recommendations available')
