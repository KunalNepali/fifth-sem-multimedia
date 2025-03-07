import cv2
import matplotlib.pyplot as plt

#load img in GrayScale
image_path = "D:\Kunaa_____l\multi-media\lenna.jpg"
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

#histograms plot

plt.hist(image.ravel(), bins = 256, range=[0,256], color='gray', alpha=0.7)

plt.title("Histogram of Lenna.jpg")

plt.xlabel("Pixel Value")

plt.ylabel("Frequency")

plt.show()