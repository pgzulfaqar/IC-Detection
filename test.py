# import the necessary packages
from PIL import Image
import pytesseract
import argparse
import cv2
import os
import re

# load the example image and convert it to grayscale
image = cv2.imread("test_n.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# check to see if we should apply thresholding to preprocess the
# image
#Tresh
gray = cv2.threshold(gray, 0, 255,
cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
# make a check to see if median blurring should be done to remove
# noise
#blur
#gray = cv2.medianBlur(gray, 3)
# write the grayscale image to disk as a temporary file so we can
# apply OCR to it
filename = "{}.png".format(os.getpid())
cv2.imwrite(filename, gray)

# load the image as a PIL/Pillow image, apply OCR, and then delete
# the temporary file
text = pytesseract.image_to_string(Image.open(filename))
os.remove(filename)
print(text)
t2 = re.sub(r'[\n\t\ ]+', ' ', text)
print(t2)
#result = re.findall('^[0-9]*$', t2)
t3 = re.search(r'\d+[\D-]+\d+\D+\d+', t2).group(0)
result = re.sub(r'[\D-]+ ', '', t3, 1)

print("Last: {}".format(result))

# show the output images
cv2.imshow("Image", image)
cv2.imshow("Output", gray)