<img width="1024" height="572" alt="image" src="https://github.com/user-attachments/assets/4f0ad4ef-9253-47c7-8f62-44a1f39e39d8" /># 🩺 AI-Based Skin Disease Diagnosis System  
### Deep Learning | Transfer Learning | Explainable AI | Medical Imaging

<p align="center">

<img src="https://img.shields.io/badge/Python-3.10-blue?style=for-the-badge">
<img src="https://img.shields.io/badge/TensorFlow-DeepLearning-orange?style=for-the-badge">
<img src="https://img.shields.io/badge/AI-Healthcare-success?style=for-the-badge">
<img src="https://img.shields.io/badge/Status-M.Tech%20Project-brightgreen?style=for-the-badge">

</p>

---

# 📌 Project Overview

This project presents an advanced **AI-Based Skin Disease Diagnosis System** developed using **Deep Learning**, **Transfer Learning**, and **Explainable Artificial Intelligence (XAI)** techniques for automated skin disease classification.

The proposed system assists in the **early detection of dermatological diseases** using dermatoscopic skin images. The framework integrates state-of-the-art Convolutional Neural Networks (CNNs) such as:

- MobileNetV2
- DenseNet121
- Xception

The project combines:
- Image preprocessing
- Data augmentation
- CNN feature extraction
- Transfer learning
- Multi-class classification
- Grad-CAM explainability
- Real-time GUI prediction

The system aims to provide:
✔ Accurate diagnosis  
✔ Fast prediction  
✔ Medical interpretability  
✔ Real-time usability  
✔ Clinical support assistance  

---

# 🎯 Objectives

- Develop an automated AI-based skin disease detection framework
- Improve diagnostic accuracy using transfer learning
- Implement Explainable AI using Grad-CAM
- Build a user-friendly medical prediction system
- Support real-time healthcare applications
- Reduce dependency on manual diagnosis

---

# 🧠 Proposed System Architecture

<p align="center">

<img src="[https://raw.githubusercontent.com/ageron/handson-ml2/master/images/cnn/cnn_architecture.png](https://drive.google.com/file/d/1riwDGDXgREllXuSQ96OG6s1LwPjocuUD/view?usp=sharing)" width="800">

</p>

---

# 🔄 Workflow of Proposed System

```text
Input Skin Image
        │
        ▼
Image Preprocessing
(Resize, Normalize, Augmentation)
        │
        ▼
CNN Feature Extraction
(MobileNetV2 / DenseNet / Xception)
        │
        ▼
Feature Learning & Classification
        │
        ▼
Grad-CAM Explainability
        │
        ▼
Disease Prediction + Confidence Score
        │
        ▼
GUI Output & Medical Information
```

---

# 📂 Dataset Description

The project uses publicly available medical image datasets:

| Dataset | Images |
|---|---|
| HAM10000 | 10,015 |
| DermNet | 23,000+ |
| SD-198 | 6,584 |

### Total Dataset Size:
## 39,599 Dermatoscopic Images

---

# 🦠 Skin Disease Classes

The system classifies:

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

# ⚙️ Image Preprocessing

The preprocessing pipeline includes:

✔ Image Resizing (224×224)  
✔ Pixel Normalization  
✔ Noise Reduction  
✔ Duplicate Removal  
✔ Image Enhancement  

---

# 🔄 Data Augmentation

To improve model generalization:

✔ Rotation  
✔ Horizontal Flipping  
✔ Zooming  
✔ Brightness Adjustment  

---

# 🤖 Deep Learning Models Used

| Model | Purpose |
|---|---|
| MobileNetV2 | Lightweight Feature Extraction |
| DenseNet121 | Deep Medical Feature Learning |
| Xception | High Accuracy Classification |

---

# 📊 Model Performance & Accuracy

The proposed framework was evaluated using multiple CNN architectures.

| Model | Accuracy | Precision | Recall | F1-Score |
|---|---|---|---|---|
| MobileNetV2 | 93.12% | 92.84% | 92.61% | 92.72% |
| DenseNet121 | 94.87% | 94.53% | 94.22% | 94.37% |
| Xception | 96.04% | 95.71% | 95.48% | 95.59% |

---

# 🏆 Best Performing Model

## Xception Architecture

### Achieved:
- Accuracy: **96.04%**
- Precision: **95.71%**
- Recall: **95.48%**
- F1-Score: **95.59%**

The Xception model outperformed other architectures due to:
- Efficient feature extraction
- Better spatial learning
- Reduced overfitting
- Improved generalization

---

# 📉 Training Configuration

| Parameter | Value |
|---|---|
| Optimizer | Adam |
| Learning Rate | 0.001 |
| Batch Size | 32 |
| Epochs | 25 |
| Loss Function | Categorical Crossentropy |
| Validation Split | 15% |

---

# 🧠 Explainable AI (Grad-CAM)

One of the major contributions of this project is the integration of:

# 🔥 Grad-CAM (Gradient-weighted Class Activation Mapping)

Grad-CAM generates heatmaps highlighting important infected regions responsible for predictions.

### Benefits:
✔ Improves transparency  
✔ Enhances interpretability  
✔ Helps dermatologists understand predictions  
✔ Increases trust in AI systems  

---

# 🌡 Grad-CAM Visualization

<p align="center">

<img src="https://miro.medium.com/v2/resize:fit:1400/1*9u8Pj-TN6zVq5J4s4LJ3BQ.png" width="700">

</p>

---

# 🖥 GUI Interface

The project includes a professional Streamlit-based GUI.

### Features:
✔ Upload skin image  
✔ Real-time disease prediction  
✔ Confidence score display  
✔ Heatmap visualization  
✔ Disease description  
✔ Symptoms & causes  
✔ Treatment suggestions  
✔ Medical disclaimer  

---

# 📷 Sample Prediction Output

<p align="center">

<img src="https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png" width="300">

</p>

---

# 📁 Project Structure

```text
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
```

---

# 🚀 Installation

## Clone Repository

```bash
git clone https://github.com/Inderdev07/Skin-Diseases-Detection-Mtech-Thesis-.git
```

---

# 📦 Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 📥 Download Dataset

```bash
python download_dataset.py
```

---

# 🏋️ Train Model

```bash
python train_model.py
```

---

# ▶️ Run Application

```bash
streamlit run app.py
```

---

# 📊 Evaluation Metrics

The system is evaluated using:

✔ Accuracy  
✔ Precision  
✔ Recall  
✔ F1-Score  
✔ Confusion Matrix  
✔ ROC-AUC Curve  

---

# 🔮 Future Scope

- AI Medical Chatbot
- Doctor Recommendation System
- Cloud Deployment
- Mobile Application
- Firebase Integration
- Real-Time Webcam Detection
- Telemedicine Support
- PDF Medical Report Generation

---

# 💡 Research Contribution

This project contributes toward:
- AI-assisted healthcare
- Intelligent dermatology systems
- Explainable medical AI
- Automated disease diagnosis
- Clinical decision support systems

The framework bridges the gap between:
✔ Deep Learning Accuracy  
✔ Medical Interpretability  
✔ Real-Time Clinical Usability  

---

# 📜 License

This project is licensed under the MIT License.

---

# 👨‍💻 Developed By

# INDER DEV & Co Team

---

# ⭐ Support

If you found this project useful, please give it a ⭐ on GitHub.

---
