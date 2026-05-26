"""
Quick Reference Guide
======================
Command-line quick reference for AI Skin Disease Diagnosis System
"""

# ============================================================================
# INSTALLATION & SETUP
# ============================================================================

# Create virtual environment
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Activate (macOS/Linux)
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Verify installation
python setup_verify.py

# ============================================================================
# RUNNING THE APPLICATION
# ============================================================================

# Start Streamlit GUI (Main Application)
streamlit run app.py

# Run on custom port
streamlit run app.py --server.port 8502

# ============================================================================
# MODEL TRAINING
# ============================================================================

# Quick training (MobileNetV2 - 20 epochs)
python train_model.py --model mobilenetv2 --epochs 20

# Standard training (DenseNet121 - 30 epochs)
python train_model.py --model densenet121 --epochs 30

# Advanced training with fine-tuning
python train_model.py --model densenet121 --epochs 30 --finetune

# Custom batch size
python train_model.py --model mobilenetv2 --batch-size 16 --epochs 30

# ============================================================================
# DATASET MANAGEMENT
# ============================================================================

# List available datasets
python download_dataset.py --list

# Download HAM10000
python download_dataset.py --dataset ham10000

# Download DermNet
python download_dataset.py --dataset dermnet

# Download all datasets
python download_dataset.py --dataset all

# Download with custom path
python download_dataset.py --dataset ham10000 --path ./custom_data

# Download and skip extraction
python download_dataset.py --dataset ham10000 --extract false

# ============================================================================
# PYTHON SCRIPTS
# ============================================================================

# Test imports
python -c "import tensorflow; print(tensorflow.__version__)"
python -c "import streamlit; print('Streamlit OK')"
python -c "import cv2; print('OpenCV OK')"

# Load and test model
python -c "import tensorflow as tf; model = tf.keras.models.load_model('model/skin_model.h5')"

# ============================================================================
# DIRECTORY STRUCTURE CREATION
# ============================================================================

# Windows Command Prompt
mkdir model dataset\sample_images utils static templates assets

# Windows PowerShell
New-Item -Path model, dataset\sample_images, utils, static, templates, assets -ItemType Directory -Force

# macOS/Linux
mkdir -p model dataset/sample_images utils static templates assets

# ============================================================================
# DISEASE CLASSES
# ============================================================================

# Available disease classes (10 total):
# 0. melanoma
# 1. nevus
# 2. basal_cell_carcinoma
# 3. actinic_keratosis
# 4. benign_keratosis
# 5. dermatofibroma
# 6. vascular_lesions
# 7. squamous_cell_carcinoma
# 8. psoriasis
# 9. eczema

# ============================================================================
# FILE STRUCTURE
# ============================================================================

# Core files:
app.py                    # Streamlit web interface
train_model.py            # Model training
gradcam.py               # Explainable AI module
download_dataset.py      # Dataset management
config.py                # Configuration

# Documentation:
README.md                # Full documentation
SETUP_INSTRUCTIONS.md    # Setup guide
PROJECT_SUMMARY.md       # Project overview

# Configuration:
requirements.txt         # Dependencies
.gitignore              # Git ignore rules
LICENSE                 # MIT License

# Directories to create:
model/                   # Trained models
dataset/                 # Training data
utils/                   # Utilities
static/                  # CSS/JS
templates/              # HTML
assets/                 # Resources

# ============================================================================
# STREAMLIT APP NAVIGATION
# ============================================================================

# Tab 1: Diagnosis
# - Upload skin image
# - View predictions
# - Check confidence scores
# - See Grad-CAM heatmaps
# - Get disease information

# Tab 2: Analytics
# - View prediction statistics
# - See disease distribution
# - Track prediction history

# Tab 3: Disease Information
# - Select disease
# - Read comprehensive info
# - View symptoms, causes
# - Review treatments

# Tab 4: About
# - Project overview
# - Technology stack
# - Acknowledgments
# - Contact information

# ============================================================================
# COMMON ISSUES & SOLUTIONS
# ============================================================================

# Issue: Module not found
# Solution: pip install -r requirements.txt

# Issue: Out of memory
# Solution: python train_model.py --batch-size 16

# Issue: GPU not detected
# Solution: CPU mode will be used automatically (slower)

# Issue: Model not found
# Solution: Train model or download pre-trained weights

# Issue: Streamlit won't start
# Solution: streamlit run app.py --server.port 8502

# Issue: Dataset download fails
# Solution: Check internet, verify Kaggle credentials

# ============================================================================
# PERFORMANCE OPTIMIZATION
# ============================================================================

# Reduce model size for faster inference
# Use MobileNetV2 instead of DenseNet121

# Reduce image resolution
# Modify input_shape in config.py to (192, 192, 3)

# Reduce batch size during training
# python train_model.py --batch-size 8

# Enable GPU acceleration
# Requires CUDA and cuDNN installed

# ============================================================================
# TESTING & VALIDATION
# ============================================================================

# Test model prediction
python -c "
import tensorflow as tf
import numpy as np
model = tf.keras.models.load_model('model/skin_model.h5')
test_input = np.random.rand(1, 224, 224, 3)
prediction = model.predict(test_input)
print('Predictions:', prediction)
"

# Test Grad-CAM
python -c "
from gradcam import GradCAM
import tensorflow as tf
model = tf.keras.models.load_model('model/skin_model.h5')
gradcam = GradCAM(model, 'conv5_block16_add')
print('Grad-CAM module loaded successfully')
"

# ============================================================================
# DEPLOYMENT COMMANDS
# ============================================================================

# Local deployment
streamlit run app.py

# Docker deployment
docker build -t skin-diagnosis .
docker run -p 8501:8501 skin-diagnosis

# Streamlit Cloud (after pushing to GitHub)
# 1. Go to streamlit.io/cloud
# 2. Connect GitHub repo
# 3. Select app.py
# 4. Deploy

# ============================================================================
# GIT COMMANDS
# ============================================================================

# Initialize repository
git init

# Add files
git add .

# Commit changes
git commit -m "Initial commit: AI Skin Disease Diagnosis System"

# Push to GitHub
git push -u origin main

# ============================================================================
# ENVIRONMENT VARIABLES
# ============================================================================

# Kaggle API credentials (if using kagglehub)
# Windows: Set kaggle.json in %USERPROFILE%\.kaggle\
# Linux/Mac: Place kaggle.json in ~/.kaggle/

# TensorFlow GPU (optional)
# export CUDA_VISIBLE_DEVICES=0

# ============================================================================
# USEFUL LINKS
# ============================================================================

# Documentation:
# - TensorFlow: https://tensorflow.org
# - Streamlit: https://streamlit.io
# - OpenCV: https://opencv.org
# - Keras: https://keras.io

# Datasets:
# - HAM10000: https://www.kaggle.com/datasets/kmader/skin-cancer-mnist-ham10000
# - DermNet: https://www.kaggle.com/datasets/shrivastava2340/dermnet

# Cloud Deployment:
# - Streamlit Cloud: https://streamlit.io/cloud
# - Docker Hub: https://hub.docker.com

# ============================================================================
# MEMORY REQUIREMENTS
# ============================================================================

# Minimum:
# - RAM: 8GB
# - Disk: 5GB
# - Python: 3.8+

# Recommended:
# - RAM: 16GB
# - Disk: 20GB (with datasets)
# - GPU: NVIDIA with CUDA 11.0+

# ============================================================================
# EXECUTION TIME ESTIMATES
# ============================================================================

# Installation: 5-10 minutes
# Setup: 5 minutes
# Model training (MobileNetV2): 20-30 min per epoch
# Model training (DenseNet121): 40-60 min per epoch
# First prediction: <1 second
# Grad-CAM generation: 1-2 seconds

# ============================================================================
# FILE SIZES
# ============================================================================

# Trained models:
# - MobileNetV2: ~100 MB
# - DenseNet121: ~150 MB
# - Xception: ~200 MB

# Datasets:
# - HAM10000: 3.2 GB
# - DermNet: 2.3 GB

# ============================================================================
# SUPPORT & HELP
# ============================================================================

# Documentation: See README.md
# Setup Guide: See SETUP_INSTRUCTIONS.md
# Project Summary: See PROJECT_SUMMARY.md
# Code Comments: Check source files
# Issues: Check troubleshooting section

# ============================================================================
# QUICK START (3 STEPS)
# ============================================================================

# 1. Install
pip install -r requirements.txt

# 2. Run
streamlit run app.py

# 3. Open browser to http://localhost:8501

# ============================================================================
# END OF QUICK REFERENCE
# ============================================================================

# Made with ❤️ for healthcare and research
# Designed by INDER DEV & Co Team
# Version 1.0.0 | 2024
