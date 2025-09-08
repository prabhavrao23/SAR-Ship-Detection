"""
preprocess.py
Author: [Your Name]
Date: 2025-09-08

Purpose:
This script handles preprocessing of Sentinel-1 SAR imagery.
Steps include calibration, speckle noise reduction, and normalization.
"""

import numpy as np
import rasterio
from skimage.restoration import denoise_bilateral

def load_sar_image(path):
    """Load a SAR GeoTIFF file into a numpy array."""
    with rasterio.open(path) as src:
        image = src.read(1)
        profile = src.profile
    return image, profile

def normalize(image):
    """Normalize SAR image to range [0, 1]."""
    return (image - image.min()) / (image.max() - image.min())

def reduce_speckle(image):
    """Apply speckle noise filtering using bilateral filter."""
    return denoise_bilateral(image, sigma_color=0.05, sigma_spatial=15)

def preprocess(path):
    """Complete preprocessing pipeline."""
    image, profile = load_sar_image(path)
    norm_img = normalize(image)
    filtered_img = reduce_speckle(norm_img)
    return filtered_img, profile
