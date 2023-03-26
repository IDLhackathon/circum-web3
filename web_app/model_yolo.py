#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 20:07:56 2023

@author: florianlabaye
"""

from ultralytics import YOLO
import numpy as np
import cv2
from PIL import Image


def predict_img():
    
    # Load a model
    model = YOLO("yolov8n.yaml")  # build a new model from scratch
    model = YOLO("yolov8n.pt")  # load a pretrained model (recommended for training)
    
    # from PIL
    im1 = Image.open("/Users/florianlabaye/Documents/Cassini_hackaton/content/image.png")
    results = model.predict(source=im1, save=True)  # save plotted images
    return Image.open("runs/detect/predict9/image.png")

