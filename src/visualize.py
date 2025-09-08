"""
visualize.py
Author: [Your Name]
Date: 2025-09-08

Purpose:
This script provides visualization tools for overlaying ship detections on SAR imagery.
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches

def visualize_detections(image, detections):
    """Overlay detections on SAR image."""
    fig, ax = plt.subplots(figsize=(10, 10))
    ax.imshow(image, cmap="gray")

    for _, det in detections.iterrows():
        rect = patches.Rectangle((det["x"], det["y"]), det["w"], det["h"],
                                 linewidth=2, edgecolor="red", facecolor="none")
        ax.add_patch(rect)

    plt.title("SAR Ship Detections")
    plt.show()
