Project Overview

This project trains an EfficientNet-B0 deep learning model for multi-class image classification. The dataset contains 16 classes, including "Boundary Wall," "Chimney," "Construction Worker," and more.

The model is trained using PyTorch with Weighted Loss, Data Augmentation, and Early Stopping to handle class imbalance and prevent overfitting.

Clone the Repository:
git clone https://github.com/Prashita18/Image_classification.git

Install Dependencies:
pip install -r requirements.txt

Train model and evaluate it:
run train.ipynb

Test the model:
run test.ipynb

EfficientNet-B0: Lightweight but powerful CNN model.
Handles Class Imbalance: Uses Weighted Random Sampling and Class Weights.
Preprocessing & Augmentation: Applies grayscale conversion, brightness adjustments, flipping, and cropping.
Optimized Training: Uses Mixed Precision (torch.amp), Early Stopping, and LR Scheduler.
Batch Inference: Supports processing multiple images at once.
Visualizations: Confusion Matrix, Accuracy/Loss Curves, and Image Predictions.
