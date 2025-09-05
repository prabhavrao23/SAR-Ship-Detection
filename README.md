# SAR Ship Detection

This project shows how to augment and exploit Synthetic Aperture Radar (SAR) sensor data products for maritime surveillance.  
The pipeline processes Sentinel-1 SAR imagery, applies preprocessing steps, and detects ships by identifying bright radar returns on a dark water background.

## Features
- Preprocess SAR imagery with calibration, speckle noise filtering, and georeferencing
- Detect ships using threshold-based segmentation and filtering
- Visualize detections overlaid on SAR imagery
- Export results as CSV with bounding box coordinates

## File Structure
SAR-Ship-Detection/
│── README.md                # Project overview
│── requirements.txt         # Dependencies
│── notebooks/
│   └── sar_ship_detection.ipynb   # Jupyter notebook walkthrough
│── src/
│   ├── preprocess.py        # SAR preprocessing functions
│   ├── detect_ships.py      # Ship detection pipeline
│   └── visualize.py         # Visualization functions
│── data/
│   └── instructions.txt     # Notes on downloading Sentinel-1 data
│── .gitignore
