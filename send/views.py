from os import terminal_size

import json
import utils_nails
import nails
from django.shortcuts import render
from django.http import JsonResponse 
from django.views import View
import base64
from django.views.decorators.csrf import csrf_exempt
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

colors = {
    '#f25858': 'Reds',
    # '#f68cde',
    # '#c472ec',
    # '#7d5eff',
    # '#5770ef',
    # '#3142b2',
    # '#7bb6eb',
    # '#92ecff',
    # '#83f3bb',
    # '#aff696',
    # '#e4ffb5',
    # '#fce96d',
    '#ffec71': 'Purples_r',
    # '#b9a09c',
    # '#a1a1a1',
}

class SendView(View):
    def get(self, request):
        if request.method = 'GET':
            return JsonResponse({'message' : 'success'},status=200)
    @csrf_exempt
    def post(request):
        if request.method == 'POST':
            # json 형식 받기
            data = json.loads(request.body)
            #json 형식 배열로 각 변수에 저장
            color_raw = data.get("color")
            
            image_dec = base64.b64decode(data.get('image')[23:])
            image = 'userinput.jpg'
            
            with open(image, 'wb') as f:
                f.write(image_dec)
            
            fusion_image = nails.makeNail(image, colors[color_raw])[0]
            fusion_image = './results/' + fusion_image

            with open(fusion_image, 'rb') as f:
                image_enc = base64.b64encode(f.read())
            # json 형식으로 return  

            send_data = {
                "image" : 'data:image/jpeg;base64,'+image_enc.decode('utf-8')
            }
            
            return JsonResponse(send_data)


# Create your views here.
