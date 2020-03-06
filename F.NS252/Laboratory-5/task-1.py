import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('[FILENAME].png')

blur = cv2.blur(img, (20, 20))

plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(blur),plt.title('Blurred')
plt.xticks([]), plt.yticks([])
plt.show()
