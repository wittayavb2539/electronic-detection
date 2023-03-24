import torch
import cv2
import numpy as np

#model = torch.hub.load('ultralytics/yolov5', 'best3.pt')
model = torch.hub.load('ultralytics/yolov5', 'custom',
                       path='ele03.pt', force_reload=True)
#model = torch.hub.load('ultralytics/yolov5',  'custom', path='best.pt ',force_reload=True)
# model = torch.hub.load('ultralytics/yolov5', 'custom', path='yolov5/runs/train/exp8/weights/best.pt',force_reload=True)
# model.conf = 0.5
# print(model)
img = cv2.imread('b4.PNG')
results = model(img)
results.print()
print(results.xyxy)
cv2.imshow('YOLO COCO', np.squeeze(results.render()))
cv2.waitKey(0)
