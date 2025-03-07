from PIL import image
import ast
img = Image.open('lenna.jpg')

img.save('lemma.png', 'png')

img.save('lemma.tiff', 'tiff')

jpg_size = os.path.getsize('lenna.jpg')
png_size = os.path.getsize('lenna.png')
tiff_size = os.path.getsize('lenna.tiff')

print("JPG size: {} bytes".format(jpg_size))
print("PNG size|: {} bytes".format(png_size))
print("TIF size: {} bytes".format(tiff_size))

with open('lenna.jpg', 'rb') as f:

    data = f.read()

    jpg_actual_size = len(data)

    print("Actual JPG size: {} bytes".format(jpg_actual_size))