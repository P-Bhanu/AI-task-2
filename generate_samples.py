import cv2
import numpy as np
from pathlib import Path

def create_sample_images():
    output_dir = Path('sample_images')
    output_dir.mkdir(exist_ok=True)
    
    img_width, img_height = 800, 600
    
    print("Generating synthetic sample images...")
    
    base_image = np.ones((img_height, img_width, 3), dtype=np.uint8) * 200
    cv2.rectangle(base_image, (100, 100), (700, 500), (180, 180, 180), -1)
    
    good_sample = base_image.copy()
    cv2.putText(good_sample, "GOOD SAMPLE", (250, 50), 
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
    cv2.imwrite(str(output_dir / 'good_sample_1.jpg'), good_sample)
    print(f"Created: good_sample_1.jpg")
    
    scratch_image = base_image.copy()
    cv2.putText(scratch_image, "DEFECT: SCRATCH", (200, 50), 
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    
    cv2.line(scratch_image, (150, 200), (180, 400), (50, 50, 50), 3)
    cv2.line(scratch_image, (400, 150), (420, 450), (40, 40, 40), 2)
    cv2.line(scratch_image, (550, 250), (560, 380), (60, 60, 60), 2)
    
    cv2.imwrite(str(output_dir / 'defect_scratch_1.jpg'), scratch_image)
    print(f"Created: defect_scratch_1.jpg")
    
    discolor_image = base_image.copy()
    cv2.putText(discolor_image, "DEFECT: DISCOLORATION", (150, 50), 
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
    
    cv2.circle(discolor_image, (300, 300), 80, (120, 120, 120), -1)
    cv2.ellipse(discolor_image, (500, 250), (60, 40), 0, 0, 360, (140, 140, 140), -1)
    cv2.rectangle(discolor_image, (200, 400), (280, 450), (160, 160, 160), -1)
    
    cv2.imwrite(str(output_dir / 'defect_discolor_1.jpg'), discolor_image)
    print(f"Created: defect_discolor_1.jpg")
    
    missing_image = base_image.copy()
    cv2.putText(missing_image, "DEFECT: MISSING COMPONENT", (100, 50), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
    
    cv2.rectangle(missing_image, (250, 200), (350, 280), (0, 0, 0), -1)
    cv2.circle(missing_image, (500, 350), 50, (0, 0, 0), -1)
    cv2.rectangle(missing_image, (400, 150), (450, 180), (0, 0, 0), -1)
    
    cv2.imwrite(str(output_dir / 'defect_missing_1.jpg'), missing_image)
    print(f"Created: defect_missing_1.jpg")
    
    multi_defect = base_image.copy()
    cv2.putText(multi_defect, "MULTIPLE DEFECTS", (200, 50), 
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 255), 2)
    
    cv2.line(multi_defect, (150, 150), (170, 300), (50, 50, 50), 2)
    cv2.circle(multi_defect, (400, 250), 60, (130, 130, 130), -1)
    cv2.rectangle(multi_defect, (550, 350), (620, 400), (0, 0, 0), -1)
    
    cv2.imwrite(str(output_dir / 'defect_multiple_1.jpg'), multi_defect)
    print(f"Created: defect_multiple_1.jpg")
    
    print(f"\nAll sample images created in '{output_dir}' directory")
    print("You can now run: python quality_inspection.py")

if __name__ == "__main__":
    create_sample_images()
