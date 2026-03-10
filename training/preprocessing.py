import os
import cv2
import numpy as np
from sklearn.model_selection import train_test_split
from keras.preprocessing.image import ImageDataGenerator

class DataPreprocessor:
    def __init__(self, dataset_directory):
        self.dataset_directory = dataset_directory
        self.images = []
        self.labels = []

    def load_images(self):
        for filename in os.listdir(self.dataset_directory):
            if filename.endswith('.jpg') or filename.endswith('.png'):
                img_path = os.path.join(self.dataset_directory, filename)
                image = cv2.imread(img_path)
                image = cv2.resize(image, (224, 224))
                self.images.append(image)
                # Assuming the label is derived from the filename
                label = filename.split('_')[0]
                self.labels.append(label)
        self.images = np.array(self.images)
        self.labels = np.array(self.labels)

    def normalize(self):
        self.images = self.images.astype('float32') / 255.0

    def augment_data(self):
        datagen = ImageDataGenerator(
            rotation_range=40,
            width_shift_range=0.2,
            height_shift_range=0.2,
            shear_range=0.2,
            zoom_range=0.2,
            horizontal_flip=True,
            fill_mode='nearest',
            brightness_range=[0.2, 1.0]
        )
        # Fit the generator to the images
        datagen.fit(self.images)
        return datagen

    def split_data(self, test_size=0.2, val_size=0.1):
        X_train, X_temp, y_train, y_temp = train_test_split(self.images, self.labels, test_size=test_size)
        val_size_adjusted = val_size / (1 - test_size)  # Adjust validation size to account for testing split
        X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=val_size_adjusted)
        return (X_train, y_train), (X_val, y_val), (X_test, y_test)

