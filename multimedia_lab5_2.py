import numpy as np
import cv2

# Generate random image (400x400) with values in range [0, 256)
random_image = np.random.randint(0, 256, (400, 400), dtype=np.uint8)

# Save the image
output_path = "D:\\Kunaa_____l\\multi-media\\random_image.jpg"

cv2.imwrite(output_path, random_image)

print(f"Random image saved at {output_path}")
