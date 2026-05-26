<<<<<<< HEAD
# AI-Based Skin Disease Diagnosis System

## 🏥 Professional Healthcare Application with Deep Learning & Explainable AI

A comprehensive intelligent healthcare system for automated skin disease diagnosis using advanced deep learning techniques, transfer learning, and explainable AI (Grad-CAM visualization).

**M.Tech Thesis Project | Research-Grade Implementation**

---

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Model Architecture](#model-architecture)
- [Dataset](#dataset)
- [Training](#training)
- [Results](#results)
- [Deployment](#deployment)
- [Medical Disclaimer](#medical-disclaimer)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## 🎯 Overview

This project implements a production-ready AI system for diagnosing skin diseases using:

- **Deep Learning:** Convolutional Neural Networks (CNNs)
- **Transfer Learning:** MobileNetV2, DenseNet121, Xception
- **Explainable AI:** Grad-CAM for visualization and interpretability
- **Web Framework:** Streamlit for interactive user interface
- **Advanced Optimization:** Learning rate scheduling, early stopping, batch normalization

### Key Capabilities

✅ **Real-time Disease Prediction** - Instant diagnosis from uploaded images  
✅ **Confidence Scoring** - Probability-based reliability metrics  
✅ **Explainability Heatmaps** - Visualize which regions influence predictions  
✅ **Medical Information** - Comprehensive disease details and treatment options  
✅ **Professional UI** - Modern, responsive Streamlit interface  
✅ **Production-Ready Code** - Clean, modular, well-documented architecture  

---

## ✨ Features

### 1. **Image Input & Preprocessing**
- Upload disease images (JPG, JPEG, PNG, BMP)
- Camera capture support (when running on compatible devices)
- Automatic image resizing to 224×224 pixels
- Normalization and augmentation

### 2. **Deep Learning Models**
- **MobileNetV2**: Lightweight, fast inference (ideal for mobile)
- **DenseNet121**: High accuracy, efficient parameter usage
- **Xception**: Advanced architecture with depthwise separable convolutions

### 3. **Disease Classification**
Detects and classifies 10 types of skin diseases:

1. **Melanoma** - Most serious skin cancer (CRITICAL)
2. **Nevus** - Common benign mole (LOW)
3. **Basal Cell Carcinoma** - Most common skin cancer (HIGH)
4. **Actinic Keratosis** - Precancerous lesion (MEDIUM)
5. **Benign Keratosis** - Non-cancerous growth (LOW)
6. **Dermatofibroma** - Benign nodule (LOW)
7. **Vascular Lesions** - Blood vessel abnormalities (LOW)
8. **Squamous Cell Carcinoma** - Second most common cancer (HIGH)
9. **Psoriasis** - Chronic autoimmune condition (MEDIUM)
10. **Eczema** - Inflammatory skin condition (MEDIUM)

### 4. **Explainable AI (Grad-CAM)**
- Generates attention heatmaps highlighting important regions
- Overlays heatmaps on original images
- Improves model interpretability and trust
- Essential for medical applications

### 5. **Comprehensive Medical Information**
For each disease:
- Detailed description and overview
- Symptoms and visual characteristics
- Causes and risk factors
- Prevention strategies
- Treatment options (multiple approaches)
- Prognosis and severity assessment

### 6. **User Interface**
- **Tab 1 - Diagnosis:** Upload/capture images, view predictions
- **Tab 2 - Analytics:** Prediction statistics and distribution
- **Tab 3 - Disease Info:** Detailed medical reference database
- **Tab 4 - About:** System overview and information

### 7. **Advanced Features**
- Dark mode support
- Responsive design for all devices
- PDF report generation (optional)
- Prediction history tracking
- Medical disclaimer integration
- Professional styling and accessibility

---

## 📁 Project Structure

```
Skin-Diseases-Detection-Mtech-Thesis/
│
├── app.py                          # Main Streamlit GUI application
├── train_model.py                  # Model training with transfer learning
├── gradcam.py                      # Grad-CAM explainability module
├── download_dataset.py             # Dataset download automation
├── requirements.txt                # Python dependencies
├── README.md                       # This file
├── LICENSE                         # MIT License
├── .gitignore                      # Git ignore rules
│
├── model/
│   └── skin_model.h5              # Trained model weights
│
├── dataset/
│   ├── train/                     # Training images
│   ├── val/                       # Validation images
│   ├── test/                      # Test images
│   └── sample_images/             # Sample images for testing
│
├── utils/
│   └── disease_info.py            # Disease database and utilities
│
├── static/                         # CSS, JavaScript, assets
├── templates/                      # HTML templates (if needed)
└── assets/                         # Additional resources
=======
# 🩺 AI-Based Skin Disease Diagnosis System  
### Deep Learning | Transfer Learning | Explainable AI | Multi-Modal Healthcare Framework

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10-blue?style=for-the-badge">
  <img src="https://img.shields.io/badge/TensorFlow-DeepLearning-orange?style=for-the-badge">
  <img src="https://img.shields.io/badge/AI-Healthcare-success?style=for-the-badge">
  <img src="https://img.shields.io/badge/Status-Completed-brightgreen?style=for-the-badge">
</p>

---

# 📌 Project Overview

This project presents an advanced **AI-Based Skin Disease Diagnosis System** developed using **Deep Learning**, **Transfer Learning**, and **Explainable Artificial Intelligence (XAI)** techniques for automated dermatological disease classification.

The proposed system is designed to assist in the **early detection and diagnosis of skin diseases** using dermatoscopic images. The framework utilizes state-of-the-art **Convolutional Neural Networks (CNNs)** such as:

- MobileNetV2
- DenseNet121
- Xception

The project integrates:
- Automated image preprocessing
- Deep feature extraction
- Multi-class classification
- Explainable AI (Grad-CAM)
- Multi-modal architecture
- Real-time prediction GUI

The objective is to build an **accurate, interpretable, scalable, and clinically reliable AI healthcare system** capable of supporting dermatologists and improving medical diagnosis.

---

# 🎯 Objectives of the Project

✔ Study and analyze AI-based skin disease diagnosis techniques  
✔ Develop CNN-based disease classification models  
✔ Improve diagnostic accuracy using transfer learning  
✔ Implement Explainable AI for prediction transparency  
✔ Create a user-friendly GUI for real-time disease prediction  
✔ Perform comparative analysis of deep learning architectures  
✔ Support future multi-modal healthcare integration  

---

# 🧠 Proposed System Architecture

```text
                ┌─────────────────────┐
                │  Skin Image Upload  │
                └──────────┬──────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │  Image Preprocessing│
                │ Resize • Normalize  │
                │ Noise Reduction     │
                └──────────┬──────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │ Data Augmentation   │
                │ Flip • Rotate • Zoom│
                └──────────┬──────────┘
                           │
                           ▼
          ┌────────────────────────────────┐
          │ CNN Feature Extraction Models  │
          │ MobileNetV2 • DenseNet • Xception │
          └────────────────┬───────────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │ Feature Fusion Layer│
                └──────────┬──────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │ Disease Classification │
                └──────────┬──────────┘
                           │
                           ▼
         ┌────────────────────────────────┐
         │ Grad-CAM Explainability Module │
         └────────────────┬───────────────┘
                           │
                           ▼
               ┌──────────────────────┐
               │ GUI Prediction Output │
               │ Disease + Confidence  │
               │ Heatmap Visualization │
               └──────────────────────┘
```

---

# 🧬 Multi-Modal Neural Network Framework

The proposed architecture follows a **multi-modal learning approach** consisting of two major pathways:

## 1️⃣ Image Processing Pathway
Uses CNN-based deep learning architectures to:
- Extract visual lesion patterns
- Learn hierarchical spatial features
- Detect texture and pigmentation abnormalities

### CNN Models Used
- MobileNetV2
- DenseNet121
- Xception

---

## 2️⃣ Clinical Processing Pathway

Processes non-visual patient information such as:
- Age
- Gender
- Symptoms
- Lesion Location
- Medical History

This pathway improves:
- Diagnostic reliability
- Context understanding
- Real-world clinical applicability

---

## 3️⃣ Feature Fusion Layer

Both image features and clinical features are combined using:

✔ Feature-Level Fusion

This enables the system to:
- Learn correlated medical patterns
- Improve classification accuracy
- Enhance model robustness

---

# 📂 Dataset Description

The model is trained using multiple publicly available dermatological datasets:

| Dataset | Total Images |
|---|---|
| DermNet | 23,000 |
| SD-198 | 6,584 |
| HAM10000 | 10,015 |
| **Total** | **39,599** |

---

# 🦠 Skin Disease Classes

The system classifies the following diseases:

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

---

# ⚙️ Image Preprocessing Pipeline

The preprocessing module ensures image consistency and improved model performance.

## Implemented Techniques

✔ Image Resizing (224×224)  
✔ Image Normalization  
✔ Noise Reduction  
✔ Duplicate Removal  
✔ Data Cleaning  

---

# 🔄 Data Augmentation Techniques

To improve generalization and reduce overfitting:

✔ Rotation  
✔ Horizontal Flipping  
✔ Zooming  
✔ Brightness Adjustment  

---

# 🤖 Deep Learning Training Strategy

| Parameter | Value |
|---|---|
| Optimizer | Adam |
| Learning Rate | 0.001 |
| Loss Function | Categorical Crossentropy |
| Batch Size | 32 |
| Epochs | 20–30 |
| Validation Split | 15% |

---

# 🧠 Explainable AI (XAI) using Grad-CAM

One of the major contributions of this project is the integration of **Grad-CAM (Gradient-weighted Class Activation Mapping)**.

## Features of Grad-CAM
✔ Generates visual heatmaps  
✔ Highlights infected skin regions  
✔ Explains model predictions  
✔ Improves interpretability  
✔ Increases clinician trust  

---

# 🖥 GUI Features

The project includes a modern user-friendly interface developed using **Streamlit / Flask**.

## GUI Functionalities

✔ Upload skin image  
✔ Camera image capture  
✔ Real-time disease prediction  
✔ Confidence score display  
✔ Grad-CAM visualization  
✔ Disease information  
✔ Symptoms & treatment suggestions  
✔ Medical disclaimer  

---

# 📊 Evaluation Metrics

The proposed system is evaluated using:

✔ Accuracy  
✔ Precision  
✔ Recall  
✔ F1-Score  
✔ Confusion Matrix  
✔ ROC-AUC Curve  

---

# 📈 Expected Performance

| Model | Expected Accuracy |
|---|---|
| MobileNetV2 | 91–94% |
| DenseNet121 | 93–95% |
| Xception | 94–96% |

---

# 🛠 Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core Development |
| TensorFlow | Deep Learning |
| Keras | Neural Networks |
| OpenCV | Image Processing |
| NumPy | Numerical Computation |
| Streamlit | GUI Development |
| Matplotlib | Visualization |
| Scikit-learn | Evaluation Metrics |

---

# 📁 Project Structure

```text
Skin-Diseases-Detection-Mtech-Thesis/
│
├── app.py
├── train_model.py
├── gradcam.py
├── requirements.txt
│
├── dataset/
│   ├── train/
│   ├── validation/
│   └── test/
│
├── model/
│   └── skin_model.h5
│
├── utils/
│   └── disease_info.py
│
├── templates/
├── static/
└── README.md
>>>>>>> fdd16063cc884960a14d94cef85ca7d01b622cd0
```

---

<<<<<<< HEAD
## 📦 Requirements

### System Requirements
- **Python:** 3.8+
- **RAM:** 8GB minimum (16GB recommended)
- **GPU:** NVIDIA GPU with CUDA support (optional, for faster training)
- **Disk Space:** 5GB minimum

### Python Dependencies

Core libraries:
- `tensorflow>=2.13.0` - Deep learning framework
- `keras>=2.13.0` - Neural network API
- `opencv-python>=4.8.0` - Image processing
- `streamlit>=1.28.0` - Web interface
- `numpy>=1.24.0` - Numerical computing
- `scikit-learn>=1.3.0` - Machine learning utilities
- `pandas>=2.0.0` - Data manipulation
- `matplotlib>=3.7.0` - Plotting
- `pillow>=10.0.0` - Image handling
- `kagglehub>=0.1.0` - Dataset downloads

---

## 🚀 Installation

### Step 1: Clone Repository
```bash
git clone https://github.com/yourusername/skin-disease-diagnosis.git
cd Skin-Diseases-Detection-Mtech-Thesis
```

### Step 2: Create Virtual Environment (Recommended)
```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

### Step 3: Install Dependencies
=======
# 🚀 Future Enhancements

✔ Doctor Recommendation System  
✔ AI Medical Chatbot  
✔ Firebase Integration  
✔ Cloud Deployment  
✔ PDF Report Generation  
✔ Patient History Management  
✔ Real-Time Webcam Detection  
✔ Mobile Application Development  
✔ Telemedicine Integration  

---

# 💡 Research Contribution

This project contributes toward:
- Intelligent healthcare systems
- AI-assisted dermatology
- Explainable medical AI
- Automated disease diagnosis
- Real-time healthcare applications

The proposed framework bridges the gap between:
✔ Research and Clinical Practice  
✔ AI Accuracy and Explainability  
✔ Automation and Medical Reliability  

---

# ▶️ Installation & Execution

## Clone Repository

```bash
git clone https://github.com/yourusername/Skin-Diseases-Detection-Mtech-Thesis.git
```

## Install Dependencies

>>>>>>> fdd16063cc884960a14d94cef85ca7d01b622cd0
```bash
pip install -r requirements.txt
```

<<<<<<< HEAD
### Step 4: Download Datasets (Optional)
```bash
python download_dataset.py --dataset ham10000
python download_dataset.py --dataset dermnet
```

---

## 💻 Usage

### Running the Application

#### Option 1: Streamlit GUI (Recommended)
=======
## Train Model

```bash
python train_model.py
```

## Run GUI Application

>>>>>>> fdd16063cc884960a14d94cef85ca7d01b622cd0
```bash
streamlit run app.py
```

<<<<<<< HEAD
Then open your browser to:
```
http://localhost:8501
```

#### Option 2: Command Line
```bash
# Make a prediction
python predict.py --image path/to/image.jpg

# Train model
python train_model.py --model mobilenetv2 --epochs 30

# Download datasets
python download_dataset.py --list
```

---

## 🧠 Model Architecture

### Transfer Learning Approach

```
Input Image (224×224×3)
      ↓
Data Augmentation
      ↓
Pre-trained Base Model
(MobileNetV2/DenseNet121/Xception)
      ↓
Global Average Pooling
      ↓
Dense(256) + BatchNorm + Dropout(0.5)
      ↓
Dense(128) + BatchNorm + Dropout(0.4)
      ↓
Dense(64) + BatchNorm + Dropout(0.3)
      ↓
Dense(10, softmax) - Disease Classes
      ↓
Output: Class Probabilities
```

### Training Configuration

| Parameter | Value |
|-----------|-------|
| **Optimizer** | Adam (lr=0.001) |
| **Loss Function** | Categorical Crossentropy |
| **Batch Size** | 32 |
| **Epochs** | 30 |
| **Early Stopping** | Patience=10 |
| **Learning Rate Scheduler** | ReduceLROnPlateau |
| **Regularization** | L2 + Dropout + Batch Norm |

---

## 📊 Dataset

### Supported Datasets

1. **HAM10000** (3.2 GB)
   - 10,015 multi-source dermatoscopic images
   - 7 disease classes
   - Balanced dataset
   - Source: Kaggle

2. **DermNet** (2.3 GB)
   - Diverse skin disease images
   - 23 disease categories
   - High-quality dermatological images
   - Source: Kaggle

### Data Augmentation

Applied during training:
- Rotation: ±25°
- Horizontal flip: 50%
- Zoom: 0-30%
- Brightness: 0.8-1.2×
- Width/Height shift: ±20%

---

## 🎓 Training

### Basic Training
```bash
python train_model.py \
    --model mobilenetv2 \
    --train-dir ./dataset/train \
    --val-dir ./dataset/val \
    --batch-size 32 \
    --epochs 30
```

### Advanced Training with Fine-tuning
```bash
python train_model.py \
    --model densenet121 \
    --train-dir ./dataset/train \
    --val-dir ./dataset/val \
    --batch-size 16 \
    --epochs 50 \
    --finetune
```

### Expected Training Time
- **MobileNetV2:** ~1-2 hours per epoch (GPU)
- **DenseNet121:** ~2-3 hours per epoch (GPU)
- **Xception:** ~3-4 hours per epoch (GPU)

---

## 📈 Results

### Expected Performance Metrics

| Model | Accuracy | Precision | Recall | F1-Score |
|-------|----------|-----------|--------|----------|
| **MobileNetV2** | 92-95% | 91-94% | 91-93% | 92-94% |
| **DenseNet121** | 94-97% | 93-96% | 93-95% | 94-96% |
| **Xception** | 95-97% | 94-96% | 94-96% | 95-97% |

*Note: Performance varies based on dataset quality and training configuration.*

---

## 🌐 Deployment

### Local Deployment

1. **Start the application:**
   ```bash
   streamlit run app.py
   ```

2. **Access via browser:**
   ```
   http://localhost:8501
   ```

### Streamlit Cloud Deployment

1. **Create account on Streamlit Cloud**
   - Visit: https://streamlit.io/cloud

2. **Push to GitHub**
   ```bash
   git push origin main
   ```

3. **Deploy**
   - Connect GitHub repository
   - Select `app.py` as main file
   - Click "Deploy"

### Docker Deployment

```dockerfile
FROM python:3.10
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["streamlit", "run", "app.py"]
```

Build and run:
```bash
docker build -t skin-disease-diagnosis .
docker run -p 8501:8501 skin-disease-diagnosis
```

---

## ⚕️ Medical Disclaimer

**IMPORTANT: This system is designed for EDUCATIONAL and RESEARCH purposes ONLY.**

### ⚠️ Critical Points

❌ **NOT** intended for self-diagnosis  
❌ **NOT** a replacement for professional medical consultation  
❌ Results are AI predictions with probabilistic uncertainty  
❌ Should only be used with professional medical supervision  

### Proper Usage

✅ Always consult a qualified dermatologist  
✅ Use as a **supporting tool** only  
✅ Seek professional diagnosis before any treatment  
✅ Do not delay medical consultation based on results  

### Limitations

- Model accuracy varies with image quality
- False positives and false negatives possible
- Limited by training data diversity
- Cannot detect all skin conditions
- Requires proper lighting and image quality

---

## 🤝 Contributing

Contributions welcome! Please:

1. Fork the repository
2. Create feature branch (`git checkout -b feature/improvement`)
3. Commit changes (`git commit -am 'Add improvement'`)
4. Push to branch (`git push origin feature/improvement`)
5. Create Pull Request

---

## 📄 License

This project is licensed under the MIT License - see [LICENSE](LICENSE) file for details.

```
MIT License

Copyright (c) 2024

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction...
```

---

## 📞 Contact & Support

**Project Authors:** INDER DEV & Co Team

### Resources

- **GitHub:** [Your Repository URL]
- **Documentation:** [Full documentation site]
- **Issues:** [GitHub Issues]
- **Discussions:** [GitHub Discussions]

### Citation

If you use this project in research, please cite:

```bibtex
@thesis{SkinDiseaseDiagnosis2024,
  author = {Dev, Inder and Co-authors},
  title = {AI-Based Skin Disease Diagnosis System using Deep Learning and Transfer Learning},
  school = {University Name},
  year = {2024}
}
```

---

## 📚 References

### Papers
- Esteva et al. "Dermatologist-level classification of skin cancer with deep neural networks" (2019)
- Selvaraju et al. "Grad-CAM: Visual Explanations from Deep Networks via Gradient-based Localization" (2016)

### Datasets
- HAM10000: Large collection of multi-source dermatoscopic images
- DermNet: Comprehensive dermatological image database

### Technologies
- TensorFlow/Keras: https://tensorflow.org/
- Streamlit: https://streamlit.io/
- OpenCV: https://opencv.org/

---

## 🎉 Acknowledgments

- M.Tech Thesis Advisor and Department
- Kaggle community for datasets
- TensorFlow and Streamlit developers
- Medical professionals consulted for disease information

---

**Last Updated:** 2024  
**Status:** Production-Ready v1.0  
**Maintenance:** Active

---

## 📋 Quick Start Checklist

- [ ] Install Python 3.8+
- [ ] Create virtual environment
- [ ] Install dependencies: `pip install -r requirements.txt`
- [ ] Download datasets (optional): `python download_dataset.py`
- [ ] Train model: `python train_model.py` or download pre-trained
- [ ] Run app: `streamlit run app.py`
- [ ] Access: Open `http://localhost:8501`

---

**Made with ❤️ for healthcare and research**

=======
---

# 📌 Conclusion

The proposed AI-based Skin Disease Diagnosis System successfully demonstrates the potential of Deep Learning and Explainable AI in automated dermatological analysis. By integrating CNN architectures, transfer learning, Grad-CAM visualization, and multi-modal learning strategies, the framework achieves high classification accuracy while maintaining interpretability and scalability.

This project serves as:
- M.Tech Thesis Implementation
- AI Healthcare Research Prototype
- Intelligent Clinical Decision Support System
- Real-Time Medical Diagnostic Framework

---

# 👨‍💻 Developed By

## INDER DEV & Co Team

---

# 📜 License

This project is licensed under the MIT License.

---

# ⭐ Support

If you found this project useful, please consider giving it a ⭐ on GitHub.
>>>>>>> fdd16063cc884960a14d94cef85ca7d01b622cd0
