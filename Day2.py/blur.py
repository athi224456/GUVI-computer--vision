import cv2
import matplotlib.pyplot as plt
img = cv2.imread('vijay.jpeg')
blurred = cv2.GaussianBlur(img, (15, 15), 0) 
blurred_rgb = cv2.cvtColor(blurred, cv2.COLOR_BGR2RGB)
plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title('blur Image')
plt.axis('off')
plt.show()
