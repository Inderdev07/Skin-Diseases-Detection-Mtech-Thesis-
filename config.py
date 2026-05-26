"""
Configuration and Constants Module
===================================
Centralized configuration for the AI Skin Disease Diagnosis System.

Usage:
    from config import MODEL_CONFIG, DISEASE_CLASSES, PATHS
"""

from pathlib import Path

# =========================================================================
# PROJECT PATHS
# =========================================================================

PROJECT_ROOT = Path(__file__).parent
PATHS = {
    'model': PROJECT_ROOT / 'model' / 'skin_model.h5',
    'dataset': PROJECT_ROOT / 'dataset',
    'dataset_train': PROJECT_ROOT / 'dataset' / 'train',
    'dataset_val': PROJECT_ROOT / 'dataset' / 'val',
    'dataset_test': PROJECT_ROOT / 'dataset' / 'test',
    'logs': PROJECT_ROOT / 'logs',
    'static': PROJECT_ROOT / 'static',
    'templates': PROJECT_ROOT / 'templates',
}

# =========================================================================
# DISEASE CLASSES
# =========================================================================

DISEASE_CLASSES = [
    'melanoma',
    'nevus',
    'basal_cell_carcinoma',
    'actinic_keratosis',
    'benign_keratosis',
    'dermatofibroma',
    'vascular_lesions',
    'squamous_cell_carcinoma',
    'psoriasis',
    'eczema'
]

DISEASE_NAMES = [
    'Melanoma',
    'Nevus (Common Mole)',
    'Basal Cell Carcinoma',
    'Actinic Keratosis',
    'Benign Keratosis',
    'Dermatofibroma',
    'Vascular Lesions',
    'Squamous Cell Carcinoma',
    'Psoriasis',
    'Eczema'
]

NUM_CLASSES = len(DISEASE_CLASSES)

# =========================================================================
# MODEL CONFIGURATIONS
# =========================================================================

MODEL_CONFIG = {
    'mobilenetv2': {
        'input_shape': (224, 224, 3),
        'preprocessing': 'mobilenet',
        'inference_speed': 'Fast',
        'accuracy': 'High',
        'suitable_for': 'Mobile & Edge devices'
    },
    'densenet121': {
        'input_shape': (224, 224, 3),
        'preprocessing': 'densenet',
        'inference_speed': 'Medium',
        'accuracy': 'Very High',
        'suitable_for': 'High accuracy requirements'
    },
    'xception': {
        'input_shape': (299, 299, 3),
        'preprocessing': 'xception',
        'inference_speed': 'Medium',
        'accuracy': 'Very High',
        'suitable_for': 'Advanced applications'
    }
}

DEFAULT_MODEL = 'mobilenetv2'
DEFAULT_INPUT_SHAPE = (224, 224, 3)

# =========================================================================
# TRAINING CONFIGURATION
# =========================================================================

TRAINING_CONFIG = {
    'batch_size': 32,
    'epochs': 30,
    'learning_rate': 0.001,
    'early_stopping_patience': 10,
    'reduce_lr_patience': 5,
    'optimizer': 'Adam',
    'loss_function': 'categorical_crossentropy',
    'metrics': ['accuracy', 'precision', 'recall'],
    'validation_split': 0.2,
    'test_split': 0.1
}

# Data augmentation parameters
DATA_AUGMENTATION = {
    'rotation_range': 25,
    'width_shift_range': 0.2,
    'height_shift_range': 0.2,
    'shear_range': 0.2,
    'zoom_range': 0.3,
    'horizontal_flip': True,
    'vertical_flip': False,
    'brightness_range': [0.8, 1.2],
    'fill_mode': 'nearest'
}

# Regularization
REGULARIZATION = {
    'dropout_rates': [0.5, 0.4, 0.3, 0.2],
    'l2_factor': 0.001,
    'batch_norm_enabled': True
}

# =========================================================================
# INFERENCE CONFIGURATION
# =========================================================================

INFERENCE_CONFIG = {
    'confidence_threshold': 0.6,
    'top_k_predictions': 3,
    'input_shape': DEFAULT_INPUT_SHAPE,
    'normalize_input': True,
    'scale_factor': 1.0 / 255.0  # For RGB images
}

# =========================================================================
# GRAD-CAM CONFIGURATION
# =========================================================================

GRADCAM_CONFIG = {
    'layer_mobilenetv2': 'conv5_block16_add',
    'layer_densenet121': 'relu',
    'layer_xception': 'block14_sepconv2_act',
    'heatmap_alpha': 0.4,
    'colormap': 'jet',
    'generate_overlay': True,
    'visualization_size': (224, 224)
}

# =========================================================================
# STREAMLIT APP CONFIGURATION
# =========================================================================

STREAMLIT_CONFIG = {
    'page_title': 'AI Skin Disease Diagnosis System',
    'page_icon': '🏥',
    'layout': 'wide',
    'initial_sidebar_state': 'expanded',
    'max_upload_size': 200,  # MB
    'supported_formats': ['jpg', 'jpeg', 'png', 'bmp'],
    'default_tab': 'Diagnosis'
}

# =========================================================================
# UI CONFIGURATION
# =========================================================================

UI_CONFIG = {
    'primary_color': '#667eea',
    'secondary_color': '#764ba2',
    'success_color': '#27ae60',
    'warning_color': '#f39c12',
    'error_color': '#e74c3c',
    'info_color': '#3498db',
    'dark_mode_enabled': False
}

# Severity levels and colors
SEVERITY_LEVELS = {
    'CRITICAL': '#8B0000',  # Dark red
    'HIGH': '#DC143C',       # Crimson
    'MEDIUM': '#FFB6C1',     # Light pink
    'LOW': '#90EE90'         # Light green
}

# =========================================================================
# DATASET CONFIGURATION
# =========================================================================

DATASET_CONFIG = {
    'ham10000': {
        'name': 'HAM10000',
        'size_gb': 3.2,
        'num_images': 10015,
        'num_classes': 7,
        'source': 'Kaggle',
        'identifier': 'kmader/skin-cancer-mnist-ham10000'
    },
    'dermnet': {
        'name': 'DermNet',
        'size_gb': 2.3,
        'num_images': 10000,
        'num_classes': 23,
        'source': 'Kaggle',
        'identifier': 'shrivastava2340/dermnet'
    }
}

# =========================================================================
# PERFORMANCE TARGETS
# =========================================================================

PERFORMANCE_TARGETS = {
    'accuracy': 0.92,
    'precision': 0.91,
    'recall': 0.91,
    'f1_score': 0.91,
    'auc_roc': 0.95
}

# =========================================================================
# LOGGING CONFIGURATION
# =========================================================================

LOGGING_CONFIG = {
    'level': 'INFO',
    'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    'date_format': '%Y-%m-%d %H:%M:%S',
    'file': PATHS['logs'] / 'app.log' if PATHS['logs'] else None
}

# =========================================================================
# CONSTANTS
# =========================================================================

# Medical disclaimer
MEDICAL_DISCLAIMER = """
⚕️ IMPORTANT MEDICAL DISCLAIMER

This AI system is designed for EDUCATIONAL and RESEARCH purposes ONLY.
It is NOT intended for self-diagnosis or to replace professional medical advice.

❌ DO NOT:
- Use for self-diagnosis
- Delay seeking professional medical help
- Skip consultation with qualified dermatologists
- Rely solely on this system for medical decisions

✅ DO:
- Consult a qualified dermatologist
- Use as a supporting tool only
- Seek professional medical supervision
- Verify results with medical professionals

The accuracy of predictions depends on image quality and may not be 100% reliable.
Always seek professional medical advice for proper diagnosis and treatment.
"""

# Project information
PROJECT_INFO = {
    'name': 'AI-Based Skin Disease Diagnosis System',
    'version': '1.0.0',
    'author': 'INDER DEV & Co Team',
    'license': 'MIT',
    'description': 'Deep Learning system for automated skin disease diagnosis with Explainable AI',
    'keywords': ['healthcare', 'AI', 'dermatology', 'deep learning', 'transfer learning', 'grad-cam']
}

# =========================================================================
# UTILITY FUNCTIONS
# =========================================================================

def get_disease_index(disease_name: str) -> int:
    """Get index of disease in DISEASE_CLASSES"""
    try:
        return DISEASE_CLASSES.index(disease_name.lower())
    except ValueError:
        return -1

def get_disease_name(index: int) -> str:
    """Get disease name from index"""
    if 0 <= index < len(DISEASE_CLASSES):
        return DISEASE_NAMES[index]
    return "Unknown"

def get_model_config(model_name: str) -> dict:
    """Get configuration for specific model"""
    return MODEL_CONFIG.get(model_name.lower(), MODEL_CONFIG[DEFAULT_MODEL])

def ensure_paths_exist():
    """Create all required directories"""
    for path in PATHS.values():
        if isinstance(path, Path):
            path.parent.mkdir(parents=True, exist_ok=True)

# =========================================================================
# VALIDATION
# =========================================================================

def validate_config():
    """Validate configuration"""
    assert len(DISEASE_CLASSES) == NUM_CLASSES, "Disease classes mismatch"
    assert len(DISEASE_CLASSES) == len(DISEASE_NAMES), "Names count mismatch"
    assert all(isinstance(dc, str) for dc in DISEASE_CLASSES), "Invalid disease class type"
    return True

# Run validation on import
try:
    validate_config()
except AssertionError as e:
    print(f"Configuration validation error: {e}")
