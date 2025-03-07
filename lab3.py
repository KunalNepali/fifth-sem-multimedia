from PIL import Image

# Open the image
img = Image.open('lenna.png')

# Convert to grayscale
grayscale_img = Image.new('L', img.size)

# Iterate over each pixel
for x in range(img.width):
    for y in range(img.height):
        r, g, b = img.getpixel((x, y))
        grayscale = int(0.299 * r + 0.587 * g + 0.114 * b)
        grayscale_img.putpixel((x, y), grayscale)

# Set threshold for binarization
threshold = 128
binary_img = Image.new('1', img.size)

# Convert to binary
for x in range(grayscale_img.width):
    for y in range(grayscale_img.height):
        intensity = grayscale_img.getpixel((x, y))
        if intensity >= threshold:
            binary_img.putpixel((x, y), 255)
        else:
            binary_img.putpixel((x, y), 0)

# Show the final binary image
binary_img.show()
