Generate complete working code for an AI-Based Skin Disease Diagnosis System using Deep Learning, Transfer Learning, Explainable AI, and Multi-Modal Architecture.

Project folder structure:

Skin-Diseases-Detection-Mtech-Thesis/
│
├── app.py
├── train_model.py
├── gradcam.py
├── download_dataset.py
├── requirements.txt
├── README.md
├── LICENSE
├── .gitignore
│
├── model/
│   └── skin_model.h5
│
├── dataset/
│   └── sample_images/
│
├── utils/
│   └── disease_info.py
│
├── static/
├── templates/
└── assets/

===========================================================
PROJECT REQUIREMENTS
===========================================================

Develop a professional AI healthcare application for automated skin disease diagnosis using:

- Python
- TensorFlow
- Keras
- OpenCV
- Streamlit
- NumPy
- Matplotlib
- Scikit-learn

===========================================================
FUNCTIONAL REQUIREMENTS
===========================================================

The project must include:

1. Skin image upload
2. Image preprocessing
3. CNN-based feature extraction
4. Transfer learning
5. Multi-class disease prediction
6. Confidence score generation
7. Grad-CAM explainability
8. Heatmap visualization
9. Disease information display
10. User-friendly GUI
11. Medical disclaimer
12. Modular code architecture

===========================================================
DATASET REQUIREMENTS
===========================================================

Use:
- HAM10000
- DermNet

Automatically download datasets using KaggleHub inside download_dataset.py

===========================================================
MODEL REQUIREMENTS
===========================================================

Implement transfer learning using:
- MobileNetV2
- DenseNet121
- Xception

Training configuration:
- Optimizer: Adam
- Learning Rate: 0.001
- Loss Function: categorical_crossentropy
- Batch Size: 32
- Epochs: 20–30
- Early Stopping
- Learning Rate Scheduler
- Batch Normalization
- Dropout

===========================================================
SKIN DISEASE CLASSES
===========================================================

Classes:
1. Melanoma
2. Nevus
3. Basal Cell Carcinoma
4. Actinic Keratosis
5. Benign Keratosis
6. Dermatofibroma
7. Vascular Lesions
8. Squamous Cell Carcinoma
9. Psoriasis
10. Eczema

===========================================================
PREPROCESSING
===========================================================

Apply:
- Image resizing (224x224)
- Normalization
- Rotation
- Horizontal flip
- Zoom augmentation
- Brightness augmentation

===========================================================
EXPLAINABLE AI
===========================================================

Implement Grad-CAM:
- Generate heatmaps
- Highlight infected skin region
- Overlay on original image
- Improve interpretability

===========================================================
GUI REQUIREMENTS
===========================================================

Create modern Streamlit GUI with:
- Upload image option
- Camera capture option
- Disease prediction
- Confidence score
- Heatmap visualization
- Disease description
- Symptoms
- Causes
- Treatment suggestions
- Medical disclaimer

Add footer:
“Designed by INDER DEV & Co Team”

===========================================================
FILE REQUIREMENTS
===========================================================

Generate complete code for:

1. app.py
- Streamlit GUI
- Image upload
- Prediction interface
- Grad-CAM visualization

2. train_model.py
- Dataset loading
- Preprocessing
- Model training
- Validation
- Saving trained model

3. gradcam.py
- Heatmap generation
- Explainability implementation

4. utils/disease_info.py
- Disease descriptions
- Symptoms
- Causes
- Prevention
- Treatment

5. download_dataset.py
- Download datasets using kagglehub

6. requirements.txt
- All required libraries

===========================================================
OUTPUT REQUIREMENTS
===========================================================

The application should display:
- Predicted disease name
- Confidence percentage
- Grad-CAM heatmap
- Disease information
- Medical recommendation

===========================================================
ADVANCED FEATURES
===========================================================

Add:
- Dark mode UI
- PDF report generation
- Save prediction history
- Webcam support
- Better UI styling
- Error handling
- Responsive design

===========================================================
CODE STYLE
===========================================================

Requirements:
- Professional coding structure
- Proper comments
- Clean architecture
- Modular implementation
- Production-ready code
- Research-level implementation

===========================================================
DEPLOYMENT
===========================================================

Provide:
- Local deployment commands
- Streamlit deployment steps
- requirements.txt
- README instructions

===========================================================
FINAL OUTPUT
===========================================================

Generate complete working source code for all files with detailed explanations and comments suitable for:
- M.Tech thesis implementation
- Research publication
- Conference demonstration
- Healthcare AI prototype
- GitHub portfolio project
