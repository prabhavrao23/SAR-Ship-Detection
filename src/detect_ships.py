"""
detect_ships.py
Author: [Your Name]
Date: 2025-09-08

Purpose:
This script detects ships in preprocessed SAR imagery using thresholding and contour filtering.
"""

import cv2
import numpy as np
import pandas as pd

def detect_ships(image, threshold=0.6, min_area=20):
    """Detect ships by threshold segmentation and contour filtering."""
    binary = (image > threshold).astype(np.uint8) * 255

    contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    detections = []

    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > min_area:
            x, y, w, h = cv2.boundingRect(cnt)
            detections.append({"x": x, "y": y, "w": w, "h": h, "area": area})

    return pd.DataFrame(detections)
