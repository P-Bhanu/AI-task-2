# Automated Quality Inspection System

This project is a simple computer vision based quality inspection system.
It detects common surface defects in manufactured products using image
processing techniques instead of manual inspection.

This was created as Task 2 of a computer vision assignment.

---

## What the project does

Given an image of a product surface, the system:

- Detects scratches
- Detects discoloration
- Detects missing or empty regions
- Draws bounding boxes around detected defects
- Calculates pixel coordinates of each defect
- Assigns confidence and severity levels
- Saves the results as annotated images and a JSON file

The system works on still images and does not require a GPU.

---

## Defect types handled

1. Scratches  
   Detected using edge detection and contour analysis.

2. Discoloration  
   Detected by identifying brightness and color inconsistencies.

3. Missing components  
   Detected by finding empty or dark regions where material is expected.

---

## Requirements

- Python 3.8 or higher
- OpenCV
- NumPy
- Pillow

Works on:
- Linux
- Windows
- macOS
- ARM devices (Raspberry Pi)

---

## Project structure

quality-inspection-system/
├── quality_inspection.py
├── generate_samples.py
├── requirements.txt
├── setup.sh
├── sample_images/
├── output/
└── Documentation/

---

## How to run

Setup the environment:

chmod +x setup.sh
./setup.sh

Run the inspection:

python quality_inspection.py

All images inside the `sample_images/` folder will be processed.
Results will be saved in the `output/` folder.

---

## Output

For each image, the system generates:

- An annotated image showing detected defects
- A JSON report containing:
  - Defect type
  - Bounding box
  - Center pixel coordinates
  - Confidence score
  - Severity level

---

## Performance

Average processing time is about 150–200 ms per image on a normal laptop.
Performance depends on image resolution.

---

## Notes

- Sample images are synthetically generated
- Threshold values may need adjustment for real production data
- This project uses traditional computer vision methods, not deep learning

