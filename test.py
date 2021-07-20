import requests
import numpy as np
import cv2
url = 'http://127.0.0.1:5001/image'
files = {'images': open('test.jpg', 'rb')}
res= requests.post(url, files=files)
nparr = np.frombuffer(res.content, np.uint8)
img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

cv2.imwrite("detections.png", img)
print(img.shape)