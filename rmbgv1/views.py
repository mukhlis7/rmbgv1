from django.shortcuts import render, redirect
from django.http import HttpResponse

import os
import os.path

from .forms import *

from requests_toolbelt.multipart.encoder import MultipartEncoder
import requests
import json

from rembg import remove
import transfer

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


  
# Create your views here.
def proc_image_view(request):
  
    if request.method == 'POST':
        form = ImgProcForm(request.POST, request.FILES)
  
        if form.is_valid():

            img_obj = form.instance
            img_file_path = os.getcwd() + "\\media\\images\\" + str(img_obj.Image_To_Process)
            
            print("img_filename : " + str(img_obj.Image_To_Process))

            if os.path.isfile(img_file_path):

                print(img_file_path)
                form.save()
                print("Current Dir = "+ os.getcwd())

                #print("Last File Name : " + str(img_obj.Image_To_Process).split("/")[-1])

                img_file_rmd_path =  os.getcwd() + "\\media\\images\\bg_removed\\" +str(img_obj.Image_To_Process).split("/")[-1]
                img_file_rmd_path_final = img_file_rmd_path.replace(img_file_rmd_path[len(img_file_rmd_path) - 3:], "png")
                print("Image remomve path: " + img_file_rmd_path_final)

                img_removed_path = removeBG(str(img_file_path), img_file_rmd_path_final)
                print(img_file_rmd_path_final)

                img_url = "https://transfer.sh/" + str(img_obj.Image_To_Process).split("/")[-1]

                response = requests.put(img_url , data=open(img_file_rmd_path_final,'rb').read()) 
                
                up_file_link = response.content.decode("utf-8")
                request.session['up_file_link'] = up_file_link

                return redirect('success')

            else:
                form = ImgProcForm()
                return render(request, 'uploadImg.html', {'form' : form})
    else:
        form = ImgProcForm()
    return render(request, 'uploadImg.html', {'form' : form})
  
  
def success(request):
    if 'up_file_link' in request.session:
        up_file_link = request.session['up_file_link']
        return HttpResponse('successfully uploaded <br> <a href="'+ up_file_link + '">Download Now</a>')
    else:
        form = ImgProcForm()
        return render(request, 'uploadImg.html', {'form' : form})        



def removeBG(input_path, output_path):
    with open(input_path, 'rb') as i:
        with open(output_path, 'wb') as o:
            input = i.read()
            output = remove(input)
            o.write(output)
            return output



def uploadToGofile(file_path):
    mp_encoder = MultipartEncoder(
        fields={
            'filesUploaded': (file_path, open(file_path, 'rb'))
        }
    )
    r = requests.post(
        'https://store1.gofile.io/upload',
        data=mp_encoder,
        headers={'Content-Type': mp_encoder.content_type}
    )
    scrap = r.json()
    print(r)
    # send "Token file" 123Abc
    Token = scrap['data']['code']