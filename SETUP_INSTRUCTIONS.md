# 🚀 Setup Instructions - Skin Disease Diagnosis System

Complete setup guide for the AI-Based Skin Disease Diagnosis System.

---

## 📋 Pre-Requisites

✅ **System Requirements:**
- Python 3.8 or higher
- 8GB RAM (16GB recommended for training)
- 5GB disk space
- Internet connection (for downloading datasets and dependencies)

✅ **Optional (for faster training):**
- NVIDIA GPU with CUDA 11.0+
- cuDNN 8.0+

---

## 🛠️ Step 1: Environment Setup

### Windows

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
venv\Scripts\activate
```

### macOS/Linux

```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate
```

---

## 📦 Step 2: Install Dependencies

```bash
pip install --upgrade pip

# Install from requirements.txt
pip install -r requirements.txt
```

**Expected installation time:** 5-10 minutes

**What gets installed:**
- TensorFlow 2.13+
- Keras
- OpenCV
- Streamlit
- NumPy, Pandas, Scikit-learn
- Matplotlib, Seaborn
- kagglehub (for dataset download)

---

## 📁 Step 3: Create Directory Structure

Run these commands from the project root directory:

### Windows (Command Prompt)
```bash
mkdir model dataset\sample_images utils static templates assets
```

### Windows (PowerShell)
```powershell
New-Item -Path model, dataset\sample_images, utils, static, templates, assets -ItemType Directory -Force
```

### macOS/Linux
```bash
mkdir -p model dataset/sample_images utils static templates assets
```

---

## 📥 Step 4: Copy Disease Information Database

The disease information has been embedded in the main modules. To create a separate `utils/disease_info.py` file:

**Option A: Automatic (Recommended)**
```bash
python setup.py  # (if available)
```

**Option B: Manual**
1. Create file `utils/disease_info.py`
2. Copy the disease database code from `train_model.py`
3. Save and verify

---

## 🎯 Step 5: Download Pre-trained Model (Recommended)

If you don't want to train from scratch:

```bash
# Create model directory if not exists
mkdir model

# Download pre-trained model from repository
# (Link will be provided - approximately 100MB)
# Place skin_model.h5 in model/ directory
```

**OR Skip and train your own model** (see Step 6)

---

## 🧠 Step 6: Train Model (Optional - Only if no pre-trained model)

### Quick Start (MobileNetV2 - Fastest)
```bash
python train_model.py \
    --model mobilenetv2 \
    --train-dir ./dataset/train \
    --val-dir ./dataset/val \
    --epochs 20
```

### Standard Training (DenseNet121 - Better Accuracy)
```bash
python train_model.py \
    --model densenet121 \
    --train-dir ./dataset/train \
    --val-dir ./dataset/val \
    --batch-size 32 \
    --epochs 30 \
    --finetune
```

### With GPU Acceleration
```bash
# TensorFlow will automatically use GPU if available
python train_model.py --model mobilenetv2 --epochs 30
```

**Expected training time:**
- MobileNetV2: 20-30 minutes per epoch (GPU)
- DenseNet121: 40-60 minutes per epoch (GPU)
- CPU: 2-4 hours per epoch

---

## 📊 Step 7: Download Training Data (Optional)

### Download HAM10000 Dataset
```bash
python download_dataset.py --dataset ham10000 --path ./dataset
```

### Download DermNet Dataset
```bash
python download_dataset.py --dataset dermnet --path ./dataset
```

### List Available Datasets
```bash
python download_dataset.py --list
```

**Note:** Requires Kaggle API credentials for HAM10000. Set up:
1. Go to https://www.kaggle.com/settings/account
2. Click "Create New API Token"
3. Place `kaggle.json` in `~/.kaggle/`

---

## ✅ Step 8: Verify Installation

Test that everything is installed correctly:

```bash
python -c "import tensorflow; print('TensorFlow:', tensorflow.__version__)"
python -c "import streamlit; print('Streamlit: OK')"
python -c "import cv2; print('OpenCV: OK')"
python -c "import numpy; print('NumPy: OK')"
```

---

## 🌐 Step 9: Run the Application

### Start Streamlit GUI (Main Application)
```bash
streamlit run app.py
```

The application will open in your browser at:
```
http://localhost:8501
```

### Command Line Tools

```bash
# Make predictions on a single image
python -c "from gradcam import GradCAM; print('Grad-CAM module loaded')"

# Download datasets
python download_dataset.py --help

# Train model
python train_model.py --help
```

---

## 🔧 Step 10: Configuration (Optional)

### Customize Model Parameters

Edit `train_model.py` to adjust:
- `batch_size` - Reduce if out of memory (default: 32)
- `epochs` - Increase for better accuracy (default: 30)
- `learning_rate` - Adjust Adam optimizer learning rate (default: 0.001)
- `dropout_rate` - Increase regularization (default: 0.5)

### Adjust Web Interface

Edit `app.py` to modify:
- Disease classes (update `DISEASE_CLASSES` list)
- Model path (update `load_model()` function)
- UI colors and styling (custom CSS section)
- Confidence threshold (default: 60%)

---

## 📝 Project Files Summary

### Core Application Files

| File | Purpose | Status |
|------|---------|--------|
| `app.py` | Streamlit web interface | ✅ Ready |
| `train_model.py` | Model training with transfer learning | ✅ Ready |
| `gradcam.py` | Grad-CAM explainability module | ✅ Ready |
| `download_dataset.py` | Automated dataset download | ✅ Ready |
| `requirements.txt` | Python dependencies | ✅ Ready |
| `README.md` | Comprehensive documentation | ✅ Ready |

### Directories

| Directory | Purpose |
|-----------|---------|
| `model/` | Trained model weights (skin_model.h5) |
| `dataset/` | Training and test data |
| `utils/` | Utility modules and disease database |
| `static/` | CSS, JS, and static files |
| `templates/` | HTML templates (if needed) |
| `assets/` | Additional resources |

---

## 🚨 Troubleshooting

### Issue: "Module not found" errors

```bash
# Reinstall all dependencies
pip install --upgrade -r requirements.txt
```

### Issue: Out of Memory (OOM)

```bash
# Reduce batch size in training
python train_model.py --batch-size 16  # Default is 32
```

### Issue: GPU not detected

```bash
# Check TensorFlow GPU support
python -c "import tensorflow as tf; print(tf.config.list_physical_devices('GPU'))"

# If no GPU found, CPU training will be used (slower)
```

### Issue: Streamlit app won't start

```bash
# Check if port 8501 is in use
# Try custom port
streamlit run app.py --server.port 8502
```

### Issue: Dataset download fails

```bash
# Check internet connection
# Verify Kaggle API credentials
# Try manual download from Kaggle website
```

---

## 📚 Usage Examples

### Making Predictions

```python
import tensorflow as tf
import numpy as np
from PIL import Image

# Load model
model = tf.keras.models.load_model('model/skin_model.h5')

# Load and preprocess image
img = Image.open('sample_image.jpg')
img_array = np.array(img) / 255.0
img_array = np.expand_dims(img_array, axis=0)

# Make prediction
predictions = model.predict(img_array)
class_idx = np.argmax(predictions[0])
confidence = predictions[0][class_idx] * 100

print(f"Predicted Class: {class_idx}")
print(f"Confidence: {confidence:.2f}%")
```

### Generating Grad-CAM Heatmap

```python
from gradcam import GradCAM

# Create Grad-CAM generator
gradcam = GradCAM(model, layer_name='conv5_block16_add')

# Generate heatmap
heatmap = gradcam.generate_heatmap(img_array, class_idx)

# Overlay on image
overlay = gradcam.overlay_heatmap(img_array, heatmap)

# Visualize
gradcam.visualize(img_array, heatmap, class_name="Disease Name")
```

---

## 🎓 Next Steps

1. ✅ **Complete Setup** - Follow steps above
2. ✅ **Explore GUI** - Run `streamlit run app.py`
3. ✅ **Try Sample Images** - Use sample_images/ directory
4. ✅ **Review Results** - Check prediction accuracy
5. ✅ **Train Your Model** - Follow training instructions
6. ✅ **Deploy** - Use Streamlit Cloud or Docker
7. ✅ **Cite in Research** - See README.md for citation

---

## 📞 Support

- **Documentation:** See README.md
- **Issues:** Check troubleshooting section above
- **GitHub Issues:** Report bugs and feature requests
- **Discussions:** Ask questions in GitHub Discussions

---

## ✅ Verification Checklist

- [ ] Python 3.8+ installed
- [ ] Virtual environment activated
- [ ] Dependencies installed (`pip install -r requirements.txt`)
- [ ] Directory structure created
- [ ] Model file in place or training plan ready
- [ ] Can run `streamlit run app.py` without errors
- [ ] Web interface loads at http://localhost:8501
- [ ] Can upload test image and get predictions
- [ ] Grad-CAM heatmap generates (if enabled)

---

## 🎉 You're All Set!

Your AI-Based Skin Disease Diagnosis System is ready to use.

**Start the application:**
```bash
streamlit run app.py
```

**Enjoy exploring the system!**

---

**Designed by:** INDER DEV & Co Team  
**Version:** 1.0  
**Last Updated:** 2024
