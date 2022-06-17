from django.shortcuts import render, redirect
from django.http import HttpResponse

import os
import os.path

from .forms import *

from requests_toolbelt.multipart.encoder import MultipartEncoder
import requests
import json


# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


# Create your views here.
def proc_image_view(request):
    if request.method == 'POST':
        form = ImgProcForm(request.POST, request.FILES)

        if form.is_valid():
            img_obj = form.instance

            print(form.files['Image_To_Process'])
            rmbgv1_api = "https://rmbgv1api.herokuapp.com/upload_image2proc"
            values = {'filename': str(form.files['Image_To_Process'])}
            file = {'file1': form.files['Image_To_Process'].read()}

            req_resp = requests.post(rmbgv1_api, files=file, data=values)
            
            print(req_resp.text)
            json_data = json.loads(req_resp.text)
            print(json_data.get('message'))
            up_file_link = json_data.get('up_file_link')
            request.session['up_file_link'] = up_file_link

            return redirect('success')

        else:
            form = ImgProcForm()
            return render(request, 'uploadImg.html', {'form': form})

    else:
        form = ImgProcForm()
        return render(request, 'uploadImg.html', {'form': form})


def success(request):
    if 'up_file_link' in request.session:
        up_file_link = request.session['up_file_link']
        return HttpResponse('successfully uploaded <br> <a href="' + up_file_link + '">Download Now</a>')
    else:
        form = ImgProcForm()
        return render(request, 'uploadImg.html', {'form': form})


def removeBG(input_path, output_path):
    with open(input_path, 'rb') as i:
        with open(output_path, 'wb') as o:
            input = i.read()
            output = remove(input)
            o.write(output)
            return output
