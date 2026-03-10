# Configuration Settings for Grain Crop Disease Detection System

model_paths = {
    'model_1': 'path/to/model1',
    'model_2': 'path/to/model2'
}

image_size = 224
batch_size = 32
api_title = 'Grain Crop Disease Detection System'
api_version = '1.0.0'
allowed_file_extensions = ['jpg', 'jpeg', 'png']
max_file_size = 5 * 1024 * 1024  # 5 MB
confidence_threshold = 0.5
cors_origins = ['*']  # Allow all origins
