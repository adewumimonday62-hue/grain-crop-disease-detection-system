# Grain Crop Disease Detection System

## Project Documentation

This document provides the complete documentation of the Grain Crop Disease Detection System.

### Features
- Detects various types of crop diseases using machine learning algorithms.
- User-friendly interface for easy interaction.
- Real-time disease detection and prediction.
- Supports various crop types.

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/adewumimonday62-hue/grain-crop-disease-detection-system.git
   ```
2. Navigate to the project directory:
   ```bash
   cd grain-crop-disease-detection-system
   ```
3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

### Dataset Setup
- Download the dataset from the provided link.
- Place the dataset in the ```data/``` directory of the project.

### Training
- To train the model, run:
   ```bash
   python train.py
   ```
- The model will be saved in the ```models/``` directory after training.

### API Usage
- Start the API by running:
   ```bash
   python app.py
   ```
- Make GET requests to the API for disease prediction:
   ```bash
   GET /predict?image=<image_path>
   ```
- Replace `<image_path>` with the path to the image you want to analyze.

### License
This project is licensed under the MIT License. See the LICENSE file for more details.