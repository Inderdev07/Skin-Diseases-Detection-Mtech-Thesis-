"""
========================================================================
AI-BASED SKIN DISEASE DIAGNOSIS SYSTEM
Model Training Module
========================================================================

Comprehensive deep learning model training with transfer learning,
data augmentation, regularization, and advanced optimization techniques
for skin disease classification.

Features:
- Transfer Learning (MobileNetV2, DenseNet121, Xception)
- Data Augmentation (rotation, flip, zoom, brightness)
- Early Stopping & Learning Rate Scheduling
- Batch Normalization & Dropout
- Model Checkpointing
- Performance Visualization
- Multi-GPU Support

Author: AI Diagnosis Team
Version: 1.0
========================================================================
"""

import os
import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers, models
from tensorflow.keras.applications import MobileNetV2, DenseNet121, Xception
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.callbacks import (
    EarlyStopping, ReduceLROnPlateau, ModelCheckpoint, TensorBoard
)
from tensorflow.keras.optimizers import Adam
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
import logging
from typing import Tuple, List, Dict, Optional
from sklearn.metrics import (
    classification_report, confusion_matrix, accuracy_score,
    precision_score, recall_score, f1_score
)

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class SkinDiseaseModel:
    """
    Comprehensive model for skin disease classification using transfer learning.
    """
    
    # Disease classes
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
    
    # Model configurations
    MODEL_CONFIGS = {
        'mobilenetv2': {
            'base_model': MobileNetV2,
            'input_shape': (224, 224, 3),
            'preprocessing': 'mobilenet'
        },
        'densenet121': {
            'base_model': DenseNet121,
            'input_shape': (224, 224, 3),
            'preprocessing': 'densenet'
        },
        'xception': {
            'base_model': Xception,
            'input_shape': (299, 299, 3),
            'preprocessing': 'xception'
        }
    }
    
    def __init__(self, 
                 model_name: str = 'mobilenetv2',
                 num_classes: int = 10,
                 freeze_base: bool = True):
        """
        Initialize the model.
        
        Args:
            model_name (str): 'mobilenetv2', 'densenet121', or 'xception'
            num_classes (int): Number of disease classes
            freeze_base (bool): Whether to freeze base model weights
        """
        self.model_name = model_name
        self.num_classes = num_classes
        self.freeze_base = freeze_base
        self.history = None
        self.model = None
        self.input_shape = self.MODEL_CONFIGS[model_name]['input_shape']
        
        logger.info(f"Initializing {model_name} model with {num_classes} classes")
    
    def build_model(self) -> keras.Model:
        """
        Build transfer learning model with custom top layers.
        
        Returns:
            keras.Model: Compiled model
        """
        config = self.MODEL_CONFIGS[self.model_name]
        
        # Load pre-trained base model
        base_model = config['base_model'](
            input_shape=self.input_shape,
            include_top=False,
            weights='imagenet'
        )
        
        # Freeze base model weights if specified
        if self.freeze_base:
            base_model.trainable = False
            logger.info(f"Froze {self.model_name} base model")
        
        # Build custom top layers
        model = models.Sequential([
            # Input layer with preprocessing
            layers.Input(shape=self.input_shape),
            layers.Rescaling(1./255),
            
            # Data augmentation
            layers.RandomRotation(0.2),
            layers.RandomFlip('horizontal'),
            layers.RandomZoom(0.2),
            layers.RandomBrightness(0.2),
            
            # Base model
            base_model,
            
            # Global Average Pooling
            layers.GlobalAveragePooling2D(),
            
            # Dropout for regularization
            layers.Dropout(0.5),
            
            # Dense layers
            layers.Dense(256, activation='relu',
                        kernel_regularizer=keras.regularizers.l2(0.001)),
            layers.BatchNormalization(),
            layers.Dropout(0.4),
            
            layers.Dense(128, activation='relu',
                        kernel_regularizer=keras.regularizers.l2(0.001)),
            layers.BatchNormalization(),
            layers.Dropout(0.3),
            
            layers.Dense(64, activation='relu',
                        kernel_regularizer=keras.regularizers.l2(0.001)),
            layers.BatchNormalization(),
            layers.Dropout(0.2),
            
            # Output layer
            layers.Dense(self.num_classes, activation='softmax')
        ])
        
        # Compile model
        model.compile(
            optimizer=Adam(learning_rate=0.001),
            loss='categorical_crossentropy',
            metrics=['accuracy', keras.metrics.Precision(), keras.metrics.Recall()]
        )
        
        self.model = model
        logger.info("Model built and compiled successfully")
        logger.info(f"Total parameters: {model.count_params():,}")
        
        return model
    
    def prepare_data(self,
                     train_dir: str,
                     val_dir: str,
                     batch_size: int = 32,
                     augment: bool = True) -> Tuple[object, object]:
        """
        Prepare training and validation data generators.
        
        Args:
            train_dir (str): Path to training directory
            val_dir (str): Path to validation directory
            batch_size (int): Batch size for training
            augment (bool): Whether to apply augmentation
            
        Returns:
            Tuple of (train_generator, val_generator)
        """
        
        if augment:
            train_datagen = ImageDataGenerator(
                rescale=1./255,
                rotation_range=25,
                width_shift_range=0.2,
                height_shift_range=0.2,
                shear_range=0.2,
                zoom_range=0.3,
                horizontal_flip=True,
                vertical_flip=False,
                brightness_range=[0.8, 1.2],
                fill_mode='nearest'
            )
        else:
            train_datagen = ImageDataGenerator(rescale=1./255)
        
        val_datagen = ImageDataGenerator(rescale=1./255)
        
        train_generator = train_datagen.flow_from_directory(
            train_dir,
            target_size=self.input_shape[:2],
            batch_size=batch_size,
            class_mode='categorical',
            shuffle=True
        )
        
        val_generator = val_datagen.flow_from_directory(
            val_dir,
            target_size=self.input_shape[:2],
            batch_size=batch_size,
            class_mode='categorical',
            shuffle=False
        )
        
        logger.info(f"Data generators created with batch size {batch_size}")
        
        return train_generator, val_generator
    
    def train(self,
              train_generator: object,
              val_generator: object,
              epochs: int = 30,
              steps_per_epoch: Optional[int] = None,
              validation_steps: Optional[int] = None,
              model_save_path: str = './model/skin_model.h5') -> Dict:
        """
        Train the model.
        
        Args:
            train_generator: Training data generator
            val_generator: Validation data generator
            epochs (int): Number of epochs to train
            steps_per_epoch (int, optional): Steps per epoch
            validation_steps (int, optional): Validation steps
            model_save_path (str): Path to save the best model
            
        Returns:
            dict: Training history
        """
        
        # Create model save directory
        Path(model_save_path).parent.mkdir(parents=True, exist_ok=True)
        
        # Define callbacks
        callbacks = [
            EarlyStopping(
                monitor='val_loss',
                patience=10,
                restore_best_weights=True,
                verbose=1
            ),
            ReduceLROnPlateau(
                monitor='val_loss',
                factor=0.5,
                patience=5,
                min_lr=1e-7,
                verbose=1
            ),
            ModelCheckpoint(
                model_save_path,
                monitor='val_accuracy',
                mode='max',
                save_best_only=True,
                verbose=1
            ),
            TensorBoard(
                log_dir='./logs',
                histogram_freq=1,
                write_graph=True
            )
        ]
        
        logger.info(f"Starting training for {epochs} epochs...")
        
        history = self.model.fit(
            train_generator,
            epochs=epochs,
            steps_per_epoch=steps_per_epoch,
            validation_data=val_generator,
            validation_steps=validation_steps,
            callbacks=callbacks,
            verbose=1
        )
        
        self.history = history
        logger.info("Training completed!")
        
        return history.history
    
    def unfreeze_and_finetune(self,
                             train_generator: object,
                             val_generator: object,
                             num_layers_unfreeze: int = 50,
                             learning_rate: float = 1e-4,
                             epochs: int = 10):
        """
        Unfreeze base model layers and perform fine-tuning.
        
        Args:
            train_generator: Training data
            val_generator: Validation data
            num_layers_unfreeze (int): Number of top layers to unfreeze
            learning_rate (float): Learning rate for fine-tuning
            epochs (int): Number of fine-tuning epochs
        """
        logger.info(f"Unfreezing top {num_layers_unfreeze} layers for fine-tuning...")
        
        # Get base model
        base_model = self.model.layers[4]  # Index of base model in architecture
        
        # Unfreeze top layers
        for layer in base_model.layers[-num_layers_unfreeze:]:
            layer.trainable = True
        
        # Recompile with lower learning rate
        self.model.compile(
            optimizer=Adam(learning_rate=learning_rate),
            loss='categorical_crossentropy',
            metrics=['accuracy', keras.metrics.Precision(), keras.metrics.Recall()]
        )
        
        logger.info(f"Fine-tuning with learning rate: {learning_rate}")
        
        callbacks = [
            EarlyStopping(
                monitor='val_loss',
                patience=5,
                restore_best_weights=True
            ),
            ReduceLROnPlateau(
                monitor='val_loss',
                factor=0.5,
                patience=3,
                min_lr=1e-7
            )
        ]
        
        history = self.model.fit(
            train_generator,
            epochs=epochs,
            validation_data=val_generator,
            callbacks=callbacks,
            verbose=1
        )
        
        return history
    
    def evaluate(self, test_generator: object) -> Dict:
        """
        Evaluate model on test data.
        
        Args:
            test_generator: Test data generator
            
        Returns:
            dict: Evaluation metrics
        """
        logger.info("Evaluating model on test data...")
        
        predictions = self.model.predict(test_generator)
        true_labels = test_generator.classes
        pred_labels = np.argmax(predictions, axis=1)
        
        metrics = {
            'accuracy': accuracy_score(true_labels, pred_labels),
            'precision': precision_score(true_labels, pred_labels, average='weighted'),
            'recall': recall_score(true_labels, pred_labels, average='weighted'),
            'f1_score': f1_score(true_labels, pred_labels, average='weighted')
        }
        
        logger.info(f"Accuracy: {metrics['accuracy']:.4f}")
        logger.info(f"Precision: {metrics['precision']:.4f}")
        logger.info(f"Recall: {metrics['recall']:.4f}")
        logger.info(f"F1-Score: {metrics['f1_score']:.4f}")
        
        return metrics
    
    def plot_training_history(self, save_path: Optional[str] = None):
        """
        Plot training and validation metrics.
        
        Args:
            save_path (str, optional): Path to save plot
        """
        if self.history is None:
            logger.warning("No training history available")
            return
        
        fig, axes = plt.subplots(2, 2, figsize=(15, 10))
        
        # Accuracy
        axes[0, 0].plot(self.history.history['accuracy'], label='Train')
        axes[0, 0].plot(self.history.history['val_accuracy'], label='Val')
        axes[0, 0].set_title('Accuracy', fontsize=14, fontweight='bold')
        axes[0, 0].set_xlabel('Epoch')
        axes[0, 0].legend()
        axes[0, 0].grid(True, alpha=0.3)
        
        # Loss
        axes[0, 1].plot(self.history.history['loss'], label='Train')
        axes[0, 1].plot(self.history.history['val_loss'], label='Val')
        axes[0, 1].set_title('Loss', fontsize=14, fontweight='bold')
        axes[0, 1].set_xlabel('Epoch')
        axes[0, 1].legend()
        axes[0, 1].grid(True, alpha=0.3)
        
        # Precision
        axes[1, 0].plot(self.history.history['precision'], label='Train')
        axes[1, 0].plot(self.history.history['val_precision'], label='Val')
        axes[1, 0].set_title('Precision', fontsize=14, fontweight='bold')
        axes[1, 0].set_xlabel('Epoch')
        axes[1, 0].legend()
        axes[1, 0].grid(True, alpha=0.3)
        
        # Recall
        axes[1, 1].plot(self.history.history['recall'], label='Train')
        axes[1, 1].plot(self.history.history['val_recall'], label='Val')
        axes[1, 1].set_title('Recall', fontsize=14, fontweight='bold')
        axes[1, 1].set_xlabel('Epoch')
        axes[1, 1].legend()
        axes[1, 1].grid(True, alpha=0.3)
        
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=150, bbox_inches='tight')
            logger.info(f"Training history plot saved to {save_path}")
        
        plt.show()
    
    def save_model(self, path: str):
        """Save model to file."""
        self.model.save(path)
        logger.info(f"Model saved to {path}")
    
    @staticmethod
    def load_model(path: str) -> keras.Model:
        """Load model from file."""
        model = keras.models.load_model(path)
        logger.info(f"Model loaded from {path}")
        return model


def main():
    """Main training script."""
    import argparse
    
    parser = argparse.ArgumentParser(
        description='Train skin disease classification model'
    )
    parser.add_argument(
        '--model',
        type=str,
        default='mobilenetv2',
        choices=['mobilenetv2', 'densenet121', 'xception'],
        help='Base model architecture'
    )
    parser.add_argument(
        '--train-dir',
        type=str,
        default='./dataset/train',
        help='Training data directory'
    )
    parser.add_argument(
        '--val-dir',
        type=str,
        default='./dataset/val',
        help='Validation data directory'
    )
    parser.add_argument(
        '--batch-size',
        type=int,
        default=32,
        help='Batch size'
    )
    parser.add_argument(
        '--epochs',
        type=int,
        default=30,
        help='Number of training epochs'
    )
    parser.add_argument(
        '--finetune',
        action='store_true',
        help='Enable fine-tuning after initial training'
    )
    
    args = parser.parse_args()
    
    # Initialize model
    model_trainer = SkinDiseaseModel(
        model_name=args.model,
        num_classes=len(SkinDiseaseModel.DISEASE_CLASSES)
    )
    
    # Build model
    model_trainer.build_model()
    model_trainer.model.summary()
    
    # Prepare data
    train_gen, val_gen = model_trainer.prepare_data(
        args.train_dir,
        args.val_dir,
        batch_size=args.batch_size
    )
    
    # Train model
    history = model_trainer.train(
        train_gen,
        val_gen,
        epochs=args.epochs,
        model_save_path='./model/skin_model.h5'
    )
    
    # Fine-tune if specified
    if args.finetune:
        model_trainer.unfreeze_and_finetune(
            train_gen,
            val_gen,
            num_layers_unfreeze=50,
            learning_rate=1e-4,
            epochs=10
        )
    
    # Plot results
    model_trainer.plot_training_history('./training_history.png')


if __name__ == '__main__':
    main()

