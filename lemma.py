#lab 2 question number 1
import os
from PIL import Image

# Open the image
img = Image.open('lenna.jpg')

# Save in different formats
img.save('lenna.png', 'PNG')  # Corrected PNG format
img.save('lenna.tiff', 'TIFF')  # Corrected TIFF format

# Get file sizes
jpg_size = os.path.getsize('lenna.jpg')
png_size = os.path.getsize('lenna.png')
tiff_size = os.path.getsize('lenna.tiff')

# Print file sizes
print("JPG size: {} bytes".format(jpg_size))
print("PNG size: {} bytes".format(png_size))
print("TIFF size: {} bytes".format(tiff_size))

# Read actual file size
with open('lenna.jpg', 'rb') as f:
    data = f.read()
    jpg_actual_size = len(data)

print("Actual JPG size: {} bytes".format(jpg_actual_size))
