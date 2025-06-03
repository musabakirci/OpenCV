import cv2
import numpy as np
import matplotlib.pyplot as plt

# resmi içe aktarma
img = cv2.imread(r"C:\Users\MUSA\Desktop\OpenCV\Histogram\foto1.png")
img_vis = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.figure()
plt.imshow(img_vis)

print(img.shape)

img_hist = cv2.calcHist([img], channels = [0], mask = None, histSize = [256], ranges = [0,256])
print(img_hist.shape)
plt.figure()
plt.plot(img_hist)

color = ("b","g","r")
plt.figure()
for i, c in enumerate(color):
    hist = cv2.calcHist([img], channels=[i], mask = None, histSize = [256], ranges = [0,256])
    plt.plot(hist, color = c)

#
golden_gate = cv2.imread(r"C:\Users\MUSA\Desktop\OpenCV\Histogram\goldengate.jpeg")    
golden_gate_vis = cv2.cvtColor(golden_gate, cv2.COLOR_BGR2RGB)
plt.figure()
plt.imshow(golden_gate_vis)

print(golden_gate.shape)

mask = np.zeros(golden_gate.shape[:2], np.uint8)
plt.figure()
plt.imshow(mask, cmap="gray")

mask[250:350, 100:200] = 255
plt.figure()
plt.imshow(mask, cmap="gray")

masked_img_vis = cv2.bitwise_and(golden_gate_vis, golden_gate_vis, mask=mask)
plt.figure()
plt.imshow(masked_img_vis, cmap = "gray")

masked_img_vis = cv2.bitwise_and(golden_gate_vis, golden_gate_vis, mask=mask)
masked_img_hist = cv2.calcHist([golden_gate], channels = [1], mask = mask, histSize=[256], ranges=[0,256])
plt.figure()
plt.plot(masked_img_hist)

# histogram eşitleme
# karşıtlık arttırma
img2 = cv2.imread(r"C:\Users\MUSA\Desktop\OpenCV\Histogram\hist.jpg", 0)
plt.figure()
plt.imshow(img2, cmap="gray")

img2_hist = cv2.calcHist([img2], channels = [0], mask = None, histSize=[256], ranges=[0,256])
plt.figure()
plt.plot(img2_hist)

eq_hist = cv2.equalizeHist(img2)
plt.figure()
plt.imshow(eq_hist, cmap="gray")

plt.show( )