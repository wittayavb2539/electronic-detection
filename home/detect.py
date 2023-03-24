import torch
import cv2,os
import numpy as np


def detect(path):
    #model = torch.hub.load('ultralytics/yolov5', 'best3.pt')
    model = torch.hub.load('ultralytics/yolov5', 'custom',path='home/ele03.pt', force_reload=True)
    #model = torch.hub.load('ultralytics/yolov5',  'custom', path='best.pt ',force_reload=True)
    # model = torch.hub.load('ultralytics/yolov5', 'custom', path='yolov5/runs/train/exp8/weights/best.pt',force_reload=True)
    # model.conf = 0.5
    # print(model)
    img = cv2.imread(path,1)
    results = model(img)
    results.print()
    #print(results.xyxy)


    
  
   
    #cv2.waitKey(0)
    if results.pandas().xyxy[0].name.empty:
        name = 'Empty'
        return(name)
    name = results.pandas().xyxy[0].name[0]
    cv2.imwrite(path, np.squeeze(results.render()))
    return(name)