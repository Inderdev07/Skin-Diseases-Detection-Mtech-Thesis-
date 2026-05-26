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
```

---

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

```bash
pip install -r requirements.txt
```

## Train Model

```bash
python train_model.py
```

## Run GUI Application

```bash
streamlit run app.py
```

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
