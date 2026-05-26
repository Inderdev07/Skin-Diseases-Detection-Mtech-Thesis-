"""
========================================================================
AI-BASED SKIN DISEASE DIAGNOSIS SYSTEM
Grad-CAM Explainability Module
========================================================================

This module implements Grad-CAM (Gradient-weighted Class Activation Mapping)
for visualizing which regions of the skin image the neural network focuses on
when making predictions. This improves model interpretability and trust in
the diagnosis system.

Key Features:
- Gradient computation from final predictions
- Class Activation Mapping visualization
- Heatmap overlay on original images
- Interpretability for medical professionals

Author: AI Diagnosis Team
Version: 1.0
========================================================================
"""

import tensorflow as tf
import numpy as np
import cv2
from typing import Tuple, List, Optional
import matplotlib.pyplot as plt


class GradCAM:
    """
    Grad-CAM implementation for CNN visualization.
    
    Grad-CAM generates class activation maps by computing gradients of the
    class score with respect to feature maps in the final convolutional layer.
    This shows which regions of the image contribute most to the prediction.
    """
    
    def __init__(self, model: tf.keras.Model, layer_name: str):
        """
        Initialize Grad-CAM.
        
        Args:
            model (tf.keras.Model): Trained CNN model
            layer_name (str): Name of the layer to visualize (usually last conv layer)
        """
        self.model = model
        self.layer_name = layer_name
        self.grad_model = None
        self._build_grad_model()
    
    def _build_grad_model(self):
        """Build model that outputs both predictions and gradients."""
        try:
            # Get the output layer
            last_conv_layer = self.model.get_layer(self.layer_name)
            
            # Create model that outputs predictions and feature maps
            self.grad_model = tf.keras.models.Model(
                inputs=self.model.input,
                outputs=[self.model.output, last_conv_layer.output]
            )
        except Exception as e:
            print(f"Error building Grad-CAM model: {e}")
            print(f"Available layers: {[layer.name for layer in self.model.layers]}")
    
    def generate_heatmap(self, 
                        image: np.ndarray, 
                        class_idx: int,
                        cam_path: Optional[str] = None) -> np.ndarray:
        """
        Generate Grad-CAM heatmap for an image.
        
        Args:
            image (np.ndarray): Input image (preprocessed, shape: (1, 224, 224, 3))
            class_idx (int): Target class index for which to generate CAM
            cam_path (str, optional): Path to save the heatmap
            
        Returns:
            np.ndarray: Grad-CAM heatmap (224, 224)
        """
        # Convert image to tensor
        image_tensor = tf.convert_to_tensor(image, dtype=tf.float32)
        
        with tf.GradientTape() as tape:
            # Forward pass
            predictions, conv_outputs = self.grad_model(image_tensor)
            
            # Get class activation
            class_output = predictions[:, class_idx]
        
        # Compute gradients
        grads = tape.gradient(class_output, conv_outputs)
        
        # Get pooled gradients
        pooled_grads = tf.reduce_mean(grads, axis=(0, 1, 2))
        
        # Generate heatmap
        conv_outputs = conv_outputs[0]
        heatmap = conv_outputs @ pooled_grads[..., tf.newaxis]
        heatmap = tf.squeeze(heatmap, axis=-1)
        
        # Normalize heatmap
        heatmap = tf.maximum(heatmap, 0) / tf.math.reduce_max(heatmap)
        heatmap = heatmap.numpy()
        
        # Upscale heatmap
        heatmap = cv2.resize(heatmap, (224, 224))
        heatmap = (heatmap * 255).astype(np.uint8)
        
        if cam_path:
            cv2.imwrite(cam_path, heatmap)
        
        return heatmap
    
    def overlay_heatmap(self, 
                       image: np.ndarray, 
                       heatmap: np.ndarray,
                       alpha: float = 0.4,
                       colormap: int = cv2.COLORMAP_JET) -> np.ndarray:
        """
        Overlay heatmap on original image.
        
        Args:
            image (np.ndarray): Original image (224, 224, 3) in RGB
            heatmap (np.ndarray): Grad-CAM heatmap
            alpha (float): Blending factor (0-1)
            colormap (int): OpenCV colormap
            
        Returns:
            np.ndarray: Overlaid image
        """
        # Ensure image is in correct format
        if image.shape[0] == 1:
            image = image[0]
        
        # Denormalize image if needed (assuming 0-1 or 0-255)
        if image.max() <= 1.0:
            image = (image * 255).astype(np.uint8)
        else:
            image = image.astype(np.uint8)
        
        # Convert RGB to BGR for OpenCV
        if len(image.shape) == 3 and image.shape[2] == 3:
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        
        # Apply colormap to heatmap
        heatmap_colored = cv2.applyColorMap(heatmap, colormap)
        
        # Blend images
        overlaid = cv2.addWeighted(image, 1 - alpha, heatmap_colored, alpha, 0)
        
        return overlaid
    
    def visualize(self, 
                 image: np.ndarray, 
                 heatmap: np.ndarray,
                 original_image: Optional[np.ndarray] = None,
                 class_name: str = "Disease",
                 save_path: Optional[str] = None):
        """
        Create visualization with original image, heatmap, and overlay.
        
        Args:
            image (np.ndarray): Processed image
            heatmap (np.ndarray): Grad-CAM heatmap
            original_image (np.ndarray, optional): Original unprocessed image
            class_name (str): Name of predicted class
            save_path (str, optional): Path to save visualization
        """
        fig, axes = plt.subplots(1, 3, figsize=(15, 5))
        
        # Original image
        if original_image is not None:
            axes[0].imshow(original_image)
            axes[0].set_title('Original Image')
        else:
            if image.shape[0] == 1:
                axes[0].imshow(image[0].astype(np.uint8))
            else:
                axes[0].imshow(image.astype(np.uint8))
            axes[0].set_title('Processed Image')
        axes[0].axis('off')
        
        # Heatmap
        axes[1].imshow(heatmap, cmap='hot')
        axes[1].set_title(f'Grad-CAM Heatmap\n({class_name})')
        axes[1].axis('off')
        
        # Overlay
        overlay = self.overlay_heatmap(image, heatmap)
        axes[2].imshow(cv2.cvtColor(overlay, cv2.COLOR_BGR2RGB))
        axes[2].set_title('Heatmap Overlay')
        axes[2].axis('off')
        
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=150, bbox_inches='tight')
        
        return fig


def create_grad_cam_visualization(model: tf.keras.Model,
                                  image: np.ndarray,
                                  class_idx: int,
                                  layer_name: str = 'conv5_block16_add',
                                  class_name: str = "Disease") -> Tuple[np.ndarray, np.ndarray]:
    """
    Convenience function to generate Grad-CAM visualization.
    
    Args:
        model: Trained model
        image: Input image
        class_idx: Class index
        layer_name: Convolutional layer to visualize
        class_name: Name of predicted class
        
    Returns:
        Tuple of (heatmap, overlay) arrays
    """
    gradcam = GradCAM(model, layer_name)
    heatmap = gradcam.generate_heatmap(image, class_idx)
    overlay = gradcam.overlay_heatmap(image, heatmap)
    
    return heatmap, overlay

