# from store import forms
from store.forms import ProductForm
from django.shortcuts import render, redirect
from django.core.files.storage import default_storage
from django.contrib.auth.decorators import login_required
import os
import requests
import numpy as np
import cv2
import sys
import os
# Keras
from tensorflow.keras.applications.imagenet_utils import preprocess_input, decode_predictions
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# model = 'vgg-16.h5'

# def model_predict(img_path, model):
#     img = image.load_img(img_path, target_size=(224, 224))
#     x = image.img_to_array(img)
#     x = np.expand_dims(x, axis=0)
#     preds = model.predict(x)
#     return preds

def addproduct(request):
    form = ProductForm()
    msg = None
    if request.method == "POST":
        form = ProductForm(request.POST,request.FILES)
        if form.is_valid():
            f=request.FILES['image']
            response = {}
            file_name = "pic.jpg"
            file_name_2 = default_storage.save(file_name, f)
            file_url = default_storage.url(file_name_2)
            file_url = '.'+file_url
            url = 'http://127.0.0.1:5001/image'
            files = {'images': open(file_url, 'rb')}
            res= requests.post(url, files=files)
            nparr = np.frombuffer(res.content, np.uint8)
            print(nparr)
            img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
            cv2.imwrite("detections.png", img)
            print(img.shape)
            form.save()
            msg = "Product classified and added to the Database"
            context = {
            'form':form,
            'msg':msg,
            'img':res.content
            }
            return render(request,'products.html',context)
    context = {
        'form':form,
    }
    return render(request,'products.html',context)


