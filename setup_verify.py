#!/usr/bin/env python
"""
Quick Start Script for Skin Disease Diagnosis System
=====================================================
Automates initial setup and validation.

Run this after installing dependencies to verify everything is working.
"""

import sys
import os
from pathlib import Path

def check_python_version():
    """Check if Python version is 3.8+"""
    print("✓ Checking Python version...")
    if sys.version_info >= (3, 8):
        print(f"  ✅ Python {sys.version.split()[0]} (OK)")
        return True
    else:
        print(f"  ❌ Python {sys.version.split()[0]} - requires 3.8+")
        return False

def check_imports():
    """Check if all required packages are installed"""
    print("\n✓ Checking required packages...")
    required = {
        'tensorflow': 'TensorFlow',
        'keras': 'Keras',
        'cv2': 'OpenCV',
        'streamlit': 'Streamlit',
        'numpy': 'NumPy',
        'pandas': 'Pandas',
        'sklearn': 'Scikit-learn',
        'matplotlib': 'Matplotlib',
        'PIL': 'Pillow'
    }
    
    missing = []
    for module, name in required.items():
        try:
            __import__(module)
            print(f"  ✅ {name}")
        except ImportError:
            print(f"  ❌ {name} (missing)")
            missing.append(module)
    
    return len(missing) == 0

def create_directories():
    """Create required directories"""
    print("\n✓ Creating directory structure...")
    dirs = [
        'model',
        'dataset/sample_images',
        'utils',
        'static',
        'templates',
        'assets',
        'logs'
    ]
    
    for dir_path in dirs:
        Path(dir_path).mkdir(parents=True, exist_ok=True)
        print(f"  ✅ {dir_path}/")
    
    return True

def check_files():
    """Check if required files exist"""
    print("\n✓ Checking required files...")
    required_files = [
        'app.py',
        'train_model.py',
        'gradcam.py',
        'download_dataset.py',
        'requirements.txt',
        'README.md'
    ]
    
    for file_path in required_files:
        if Path(file_path).exists():
            print(f"  ✅ {file_path}")
        else:
            print(f"  ⚠️  {file_path} (not found)")
    
    return True

def test_tensorflow():
    """Test TensorFlow setup"""
    print("\n✓ Testing TensorFlow...")
    try:
        import tensorflow as tf
        gpu_available = len(tf.config.list_physical_devices('GPU')) > 0
        
        print(f"  ✅ TensorFlow {tf.__version__}")
        if gpu_available:
            print(f"  ✅ GPU support enabled")
        else:
            print(f"  ℹ️  CPU mode (GPU not detected)")
        return True
    except Exception as e:
        print(f"  ❌ TensorFlow error: {e}")
        return False

def main():
    """Run all checks"""
    print("="*60)
    print("🏥 AI Skin Disease Diagnosis System - Setup Verification")
    print("="*60)
    
    checks = [
        ("Python Version", check_python_version),
        ("Package Imports", check_imports),
        ("Directory Structure", create_directories),
        ("Required Files", check_files),
        ("TensorFlow", test_tensorflow)
    ]
    
    results = []
    for name, check_func in checks:
        try:
            result = check_func()
            results.append((name, result))
        except Exception as e:
            print(f"  ❌ Error: {e}")
            results.append((name, False))
    
    # Summary
    print("\n" + "="*60)
    print("SUMMARY")
    print("="*60)
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    for name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{status} - {name}")
    
    print(f"\n{passed}/{total} checks passed")
    
    if passed == total:
        print("\n🎉 Setup complete! You can now run:")
        print("   streamlit run app.py")
    else:
        print("\n⚠️  Some checks failed. Please review the errors above.")
        print("   See SETUP_INSTRUCTIONS.md for detailed setup guide.")
    
    return passed == total

if __name__ == '__main__':
    success = main()
    sys.exit(0 if success else 1)
