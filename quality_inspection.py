import cv2
import numpy as np
from pathlib import Path
import json
from datetime import datetime

class DefectDetector:
    def __init__(self):
        self.defect_types = {
            'scratch': {'color': (0, 0, 255), 'severity_threshold': 0.3},
            'discoloration': {'color': (255, 0, 0), 'severity_threshold': 0.4},
            'missing_component': {'color': (0, 255, 0), 'severity_threshold': 0.5}
        }
    
    def preprocess_image(self, image):
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)
        return gray, blurred
    
    def detect_scratches(self, image):
        edges = cv2.Canny(image, 50, 150)
        kernel = np.ones((3, 1), np.uint8)
        dilated = cv2.dilate(edges, kernel, iterations=2)
        contours, _ = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        scratches = []
        for contour in contours:
            area = cv2.contourArea(contour)
            if area > 50 and area < 5000:
                x, y, w, h = cv2.boundingRect(contour)
                if h > w * 2:
                    M = cv2.moments(contour)
                    if M["m00"] != 0:
                        cx = int(M["m10"] / M["m00"])
                        cy = int(M["m01"] / M["m00"])
                        confidence = min(0.95, area / 1000)
                        severity = self.calculate_severity(area, 'scratch')
                        scratches.append({
                            'type': 'scratch',
                            'bbox': (x, y, w, h),
                            'center': (cx, cy),
                            'confidence': confidence,
                            'severity': severity,
                            'area': area
                        })
        return scratches
    
    def detect_discoloration(self, image, original):
        lab = cv2.cvtColor(original, cv2.COLOR_BGR2LAB)
        l, a, b = cv2.split(lab)
        
        clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
        l = clahe.apply(l)
        
        _, thresh = cv2.threshold(l, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        kernel = np.ones((5,5), np.uint8)
        thresh = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
        
        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        discolorations = []
        mean_brightness = np.mean(l)
        
        for contour in contours:
            area = cv2.contourArea(contour)
            if area > 200 and area < 10000:
                x, y, w, h = cv2.boundingRect(contour)
                roi = l[y:y+h, x:x+w]
                roi_mean = np.mean(roi)
                
                if abs(roi_mean - mean_brightness) > 30:
                    M = cv2.moments(contour)
                    if M["m00"] != 0:
                        cx = int(M["m10"] / M["m00"])
                        cy = int(M["m01"] / M["m00"])
                        confidence = min(0.90, abs(roi_mean - mean_brightness) / 100)
                        severity = self.calculate_severity(area, 'discoloration')
                        discolorations.append({
                            'type': 'discoloration',
                            'bbox': (x, y, w, h),
                            'center': (cx, cy),
                            'confidence': confidence,
                            'severity': severity,
                            'area': area
                        })
        return discolorations
    
    def detect_missing_components(self, image, template_path=None):
        _, binary = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY_INV)
        kernel = np.ones((5,5), np.uint8)
        binary = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel)
        
        contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        missing_components = []
        for contour in contours:
            area = cv2.contourArea(contour)
            if area > 500 and area < 8000:
                x, y, w, h = cv2.boundingRect(contour)
                aspect_ratio = float(w)/h if h != 0 else 0
                
                if 0.5 < aspect_ratio < 2.0:
                    M = cv2.moments(contour)
                    if M["m00"] != 0:
                        cx = int(M["m10"] / M["m00"])
                        cy = int(M["m01"] / M["m00"])
                        confidence = min(0.88, area / 2000)
                        severity = self.calculate_severity(area, 'missing_component')
                        missing_components.append({
                            'type': 'missing_component',
                            'bbox': (x, y, w, h),
                            'center': (cx, cy),
                            'confidence': confidence,
                            'severity': severity,
                            'area': area
                        })
        return missing_components
    
    def calculate_severity(self, area, defect_type):
        threshold = self.defect_types[defect_type]['severity_threshold']
        normalized_area = area / 10000.0
        
        if normalized_area < threshold:
            return 'low'
        elif normalized_area < threshold * 2:
            return 'medium'
        else:
            return 'high'
    
    def analyze_image(self, image_path):
        image = cv2.imread(str(image_path))
        if image is None:
            raise ValueError(f"Could not load image: {image_path}")
        
        gray, blurred = self.preprocess_image(image)
        
        all_defects = []
        all_defects.extend(self.detect_scratches(blurred))
        all_defects.extend(self.detect_discoloration(blurred, image))
        all_defects.extend(self.detect_missing_components(blurred))
        
        annotated_image = image.copy()
        for defect in all_defects:
            x, y, w, h = defect['bbox']
            cx, cy = defect['center']
            color = self.defect_types[defect['type']]['color']
            
            cv2.rectangle(annotated_image, (x, y), (x+w, y+h), color, 2)
            cv2.circle(annotated_image, (cx, cy), 5, color, -1)
            
            label = f"{defect['type']}: {defect['confidence']:.2f}"
            cv2.putText(annotated_image, label, (x, y-10), 
                       cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
        
        results = {
            'image_path': str(image_path),
            'timestamp': datetime.now().isoformat(),
            'total_defects': len(all_defects),
            'defects': all_defects,
            'quality_status': 'PASS' if len(all_defects) == 0 else 'FAIL'
        }
        
        return results, annotated_image

def main():
    detector = DefectDetector()
    
    input_dir = Path('sample_images')
    output_dir = Path('output')
    output_dir.mkdir(exist_ok=True)
    
    if not input_dir.exists():
        print(f"Creating {input_dir} directory. Please add your sample images there.")
        input_dir.mkdir(exist_ok=True)
        return
    
    image_files = list(input_dir.glob('*.jpg')) + list(input_dir.glob('*.png'))
    
    if not image_files:
        print("No images found in sample_images directory")
        return
    
    all_results = []
    
    for img_path in image_files:
        print(f"\nAnalyzing: {img_path.name}")
        
        try:
            results, annotated = detector.analyze_image(img_path)
            
            output_path = output_dir / f"annotated_{img_path.name}"
            cv2.imwrite(str(output_path), annotated)
            
            print(f"Quality Status: {results['quality_status']}")
            print(f"Total Defects Found: {results['total_defects']}")
            
            for i, defect in enumerate(results['defects'], 1):
                print(f"\nDefect {i}:")
                print(f"  Type: {defect['type']}")
                print(f"  Center coordinates: ({defect['center'][0]}, {defect['center'][1]})")
                print(f"  Confidence: {defect['confidence']:.2f}")
                print(f"  Severity: {defect['severity']}")
            
            all_results.append(results)
            
        except Exception as e:
            print(f"Error processing {img_path.name}: {str(e)}")
    
    json_path = output_dir / 'inspection_results.json'
    with open(json_path, 'w') as f:
        json.dump(all_results, f, indent=2)
    
    print(f"\n\nResults saved to {json_path}")
    print(f"Annotated images saved to {output_dir}")

if __name__ == "__main__":
    main()
