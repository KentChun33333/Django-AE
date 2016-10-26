# Basic Import


from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect

from django import forms
from models import Owners

# ORM models
from django.db import models


# part of data slice and dice data with algorithm result
import numpy as np
import pandas as pd
import os, sys
from sqlalchemy import create_engine
import pandas.io.sql as psql

# Time
from datetime import datetime
import json

# Method = Post and CSRF
# This method is depreciated by 1.10, just use render
from django.template import RequestContext
from django.template.context_processors import csrf # For Post Usage
from django.views.decorators.csrf import csrf_protect


# Authentication
from django.contrib.auth import authenticate, login #
import django.contrib.auth as auth


# File Upload
from django.core.urlresolvers import reverse
from forms import UploadFileForm, UploadDocForm, UploadFileForm_2, Job_2Form, NotusemodelForm
from models  import UploadFile, Job_2

#
from multiprocessing import Process

def main(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/',RequestContext(request))

    path = '/FutureResume/media/files'
    file_list = list(os.listdir(path))

    form_1 = UploadFileForm()
    form_2 = UploadDocForm()

    if request.method == 'POST':
        form_1 = UploadFileForm(request.POST, request.FILES)


        #print request.POST

        upload_time = datetime.now()


        #   print form_2


        if form_1.is_valid():
            new_file = UploadFile(file=request.FILES['file'])
            new_file.save()
            filename = request.FILES['file'].name
            #handle_uploaded_file(request.FILES['file'])
            data = {'name':filename}
            return HttpResponse('Form_1 post file and form is_valid')
    else:
        form_1 = UploadFileForm()


    data = {'form_1': form_1, 'file_list':file_list }
    return render(request,'vedio_parser/main.html', data)


def ajax_res(request):
    # select video & show
    pass

def codec_trans(video_file_name):
    from os import system
    try :
        # Validation ...
        # ...
        # ...
        video_file_name.split('.')[0]
        code='''ffmpeg -i {} -vcodec h264 {}aac.mp4'''.format(video_file_name, video_file_name.split('.')[0] )
        system(code)
    except:
        return ('the file format is not a standard video with avi or mp4')



def exec_codec(video_file_name):
    p = Process(target=codec_trans, args=(video_file_name,))
    p.start()
    p.join()
