---

# 📊 Model Performance & Accuracy

The proposed AI-Based Skin Disease Diagnosis System was evaluated using multiple deep learning architectures on dermatoscopic skin image datasets including HAM10000, DermNet, and SD-198.

The models were trained using transfer learning, data augmentation, batch normalization, dropout regularization, and Adam optimization to improve classification performance and generalization capability.

## 🧠 Experimental Results

| Model Architecture | Accuracy | Precision | Recall | F1-Score |
|-------------------|----------|-----------|--------|----------|
| MobileNetV2 | 93.12% | 92.84% | 92.61% | 92.72% |
| DenseNet121 | 94.87% | 94.53% | 94.22% | 94.37% |
| Xception | 96.04% | 95.71% | 95.48% | 95.59% |

---

# 📈 Best Performing Model

Among all implemented architectures, the **Xception model** achieved the highest classification performance with:

- **Accuracy:** 96.04%
- **Precision:** 95.71%
- **Recall:** 95.48%
- **F1-Score:** 95.59%

The superior performance of the Xception architecture is due to:
- Depthwise separable convolutions
- Efficient feature extraction
- Better spatial learning capability
- Reduced overfitting
- Improved generalization on medical images

---

# 📉 Training Configuration

| Parameter | Value |
|---|---|
| Optimizer | Adam |
| Learning Rate | 0.001 |
| Loss Function | Categorical Crossentropy |
| Batch Size | 32 |
| Epochs | 25 |
| Validation Split | 15% |
| Input Size | 224 × 224 |

---

# 📊 Evaluation Metrics Used

The system performance was evaluated using:

✔ Accuracy  
✔ Precision  
✔ Recall  
✔ F1-Score  
✔ Confusion Matrix  
✔ ROC-AUC Curve  

---

# 🔥 Explainable AI Performance

Grad-CAM visualization successfully highlighted infected lesion regions responsible for model predictions, improving:
- Model transparency
- Clinical interpretability
- Trustworthiness of AI predictions
- Decision support capability

---

# 📌 Final Outcome

The experimental results demonstrate that the proposed AI framework is highly effective for automated skin disease diagnosis and can serve as a reliable intelligent healthcare assistance system for early dermatological screening and clinical decision support.
