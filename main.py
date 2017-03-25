from PIL import Image
import cv2
import time
from PIL import Image
format = 'bw'
name = raw_input('Please enter your name:')
print('Smile!')
time.sleep(2)
cam = cv2.VideoCapture(0)
s, im = cam.read() # captures image
# cv2.imshow("test image", im) # displays captured image
print('now lets make a caricature off of that!!')
cv2.imwrite("D:\IDF\MAHANET\images\%s.jpg" % name, im)
col = Image.open("D:\IDF\MAHANET\images\%s.jpg" % name)
gray = col.convert('L')
bw = gray.point(lambda x: 0 if x<128 else 255, '1')
bw.save("D:\IDF\MAHANET\images\%s%s.JPEG" % (name, format))