import numpy as np
from PIL import Image
import potrace

def image_to_vector_svg(image_path, svg_output_path):
    # Step 1: Open the image and convert it to grayscale
    img = Image.open(image_path).convert('L')
    
    # Step 2: Binary Thresholding (Force pixels to pure 0 or 1)
    # The Potrace engine strictly expects a boolean matrix.
    threshold = 127
    img_data = np.array(img)
    bitmap_data = (img_data < threshold).astype(int)  # 1 for black/shape, 0 for white
    
    # Step 3: Initialize the Potrace Bitmap
    bitmap = potrace.Bitmap(bitmap_data)
    
    # Step 4: Run the Potrace Tracing Algorithm
    # This executes Phase 1-4: Edge finding, polygon fitting, and bezier smoothing.
    path = bitmap.trace()
    
    # Step 5: Extract the Bezier mathematical data and write an SVG
    # We grab the dimensions of the original canvas
    width, height = img.size
    
    with open(svg_output_path, "w") as f:
        # Write standard SVG vector file headers
        f.write(f'<svg xmlns="http://w3.org" viewBox="0 0 {width} {height}" width="{width}" height="{height}">\n')
        
        # Loop through every vector path discovered by Potrace
        for curve in path:
            # Get the starting coordinate anchor point
            start_x, start_y = curve.start_point
            svg_path_data = f"M {start_x} {start_y} "
            
            # Loop through the consecutive bezier segments that map the outline
            for segment in curve.segments:
                if segment.is_corner:
                    # Straight line polygon sections
                    cx, cy = segment.c
                    x, y = segment.end_point
                    svg_path_data += f"L {cx} {cy} L {x} {y} "
                else:
                    # True Bezier curves (Cubic representation)
                    # c1 and c2 are the off-curve handles, end_point is the next anchor
                    c1x, c1y = segment.c1
                    c2x, c2y = segment.c2
                    ex, ey = segment.end_point
                    svg_path_data += f"C {c1x} {c1y}, {c2x} {c2y}, {ex} {ey} "
            
            # Close the path loop and fill it with solid color
            svg_path_data += "Z"
            f.write(f'  <path d="{svg_path_data}" fill="black" stroke="none" />\n')
            
        f.write('</svg>\n')
    
    print(f"Successfully vectorized! Saved math paths to {svg_output_path}")

# Run the pipeline
image_to_vector_svg("25645.png", "output_font_glyph.svg")
