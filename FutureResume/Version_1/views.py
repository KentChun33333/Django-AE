# Basic Import 


from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect

from django import forms
from models import Owners

# ORM models
from django.db import models


# part of data slice and dice data with algorithm result
import numpy as np
import pandas as pd
import psycopg2, os, sys
from sqlalchemy import create_engine
import pandas.io.sql as psql

# Time
from datetime import datetime
import json

# Method = Post and CSRF
from django.template import RequestContext # 
from django.template.context_processors import csrf # For Post Usage
from django.shortcuts import render_to_response # 

# Authentication
from django.contrib.auth import authenticate, login # 
import django.contrib.auth as auth


# File Upload 
from django.core.urlresolvers import reverse
from forms import UploadFileForm, UploadDocForm, UploadFileForm_2, Job_2Form, NotusemodelForm
from models  import UploadFile, Job_2


def login_user(request):
    state = "Welcome to Night Garden "
    username = password = ''
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                state = "Successfully logged in!"
                #HAVE username write in to browser's cookie,duration = 3600
                #response = HttpResponseRedirect('/index/')
                #response.set_cookie('username',username,3600)
                response = HttpResponseRedirect('/main_page',RequestContext(request))
                #response.set_cookie('username',username,3600)
                return response
                #return render_to_response('rango/index.html',{'state':state, 'username': username}, RequestContext(request))
                #
            else:
                state = "Your account is not active, please contact the site admin."
        else:
            state = "Your username and/or password were incorrect."
    return render_to_response('version1/auth_v2.html',{'state':state, 'username': username}, RequestContext(request)) # 
	
def main_page(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/',RequestContext(request))
    else:
        context_dict={}
        return render(request, 'version1/main_page.html', context_dict)
	
def form_maker(request, question_id):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/',RequestContext(request))
    context_dict={}
    return render(request, 'version1/form_v1.html', context_dict)

def echart_v1(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/',RequestContext(request))
    context_dict={}
    return render(request, 'version1/echart_v1.html', context_dict)

def inventory_scm_v1(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/',RequestContext(request))
    input_data = []
    context_dict={}
    return render(request, 'version1/inventory_scm_v1.html', context_dict)

###
# #
###

def FR_main_page(request):

    context_dict={
    'a': 'What is your habit ?',
    #'json':{'app':[1111,21111,31111]}

    'ABC_script': ''' <script>  $('#ID01').click(function(){ alert( 'What is your habit ?') }); </script>''',
    }
    return render(request, 'version1/FR_main_page.html', context_dict)


def FR_main_page_2(request):

    context_dict={
    }
    return render(request, 'version1/FR_main_page_2.html', context_dict)


def FR_main_page_2_login(request):

    context_dict={
    }
    return render(request, 'version1/FR_main_page_2_login.html', context_dict)


#######################
# File Upload Related #
#######################


def fileupload(request):
    if request.method == 'POST':
        form_1 = UploadFileForm(request.POST, request.FILES)
        if form_1.is_valid():
            new_file = UploadFile(file=request.FILES['file'])
            new_file.save()
            #handle_uploaded_file(request.FILES['file'])
            #return HttpResponseRedirect(reverse('version_1':fileupload))
            return HttpResponse('post file and form is_valid')
        else :
            return HttpResponseRedirect(reverse('nightgarden'))
    else :
        form_1 = UploadFileForm()
    data = { 'form':form_1 }
    # change main to version 1
    return render_to_response( 'version1/fileupload.html' , data , context_instance=RequestContext(request) )


def nightgarden(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/',RequestContext(request))
    path = '/Users/kentchiu/Django-AE/FutureResume/media/files'
    file_list = list(os.listdir(path))

    form_1 = UploadFileForm()
    form_2 = UploadDocForm()
    form_3 = Job_2Form()

    if request.method == 'POST':
        form_1 = UploadFileForm(request.POST, request.FILES)
        

        #print request.POST
        
        upload_time = datetime.now()
        form_2 = UploadDocForm(request.POST, request.FILES )

        #   print form_2
        if form_3.is_valid():
            print 'Form_3 is_valid'
            print form_3
        else:
            print 'Form_3 is not is_valid, user is ' + str(request.user)

#######################
#
# QueryDict: {
# u'job_close_time': [u'dfdf'], 
# u'job_project': [u'fdf'], 
# u'job_open_time': [u'dfdf'],
# u'job_function_item': [u'ddf'],
# u'job_owner': [u''],
# u'csrfmiddlewaretoken': [u't0unGn90DwNYbyPYyQGk01mmeWJq6fLs'],
# u'job_goal_time': [u'dfdf'], 
# u'job_description': [u'dfdf']}
#
#######################

        print 'job_owner :'+ request.POST['job_owner']
        print 'job_project :' + request.POST['job_project']
        print 'job_open_time :'+ request.POST['job_open_time']
        print 'job_description :' + request.POST['job_description']

        if request.POST['job_owner'] is not None:
            print 'form_3 job_owner is not None'
            AAA = Job_2(job_owner = request.user, job_close_time = None, job_function_item = request.POST['job_function_item'], job_goal_time = str(datetime.now()), job_description = request.POST['job_description'], job_open_time = str(datetime.now()) )
            AAA.save()
            print 'Successfully Create Form_3 Objects'
        else :
            pass



        

        #print form_2
        


        #class Document(models.Model):
        #    user = models.ForeignKey(User)
        #    docfile = models.FileField(upload_to='documents')
        #    upload_time = models.DateTimeField()
        if form_2.is_valid():
            new_file = Document(docfile=request.FILES['file'], user='',upload_time=str(datetime.now()))
            print new_file
            new_file.save()  ###save()  method can only be used with ModelForm.
            filename = request.FILES['file'].name
            #handle_uploaded_file(request.FILES['file'])
            data = {'name':filename}

            return HttpResponse('Form_2 post file and form is_valid')
            #return HttpResponseRedirect(reverse('main:home'))
        if form_1.is_valid():
            new_file = UploadFile(file=request.FILES['file'])
            new_file.save()
            filename = request.FILES['file'].name
            #handle_uploaded_file(request.FILES['file'])
            data = {'name':filename}
            return HttpResponse('Form_1 post file and form is_valid')        
    else:
        form_1 = UploadFileForm()
        form_2 = UploadDocForm()
        form_3 = Job_2Form()

    data = {'form_1': form_1, 'file_list':file_list , 'form_2':form_2, 'form_3':form_3}
    return render_to_response('version1/nightgarden.html', data, context_instance=RequestContext(request))


def handle_uploaded_file(f):
    filename = str(f.name)
    with open('media/'+filename, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)



    #context_dict={}
    #return render(request, 'version1/nightgarden.html', context_dict)

def test_url(request, question_id):
    context_dict={}
    return render(request, 'version1/nightgarden.html', context_dict)









class UserForm(forms.Form): 
    name = forms.CharField(label='username',max_length=100)
    password = forms.CharField(label='password',widget=forms.PasswordInput())



def regist(req):
    if req.method == 'POST':
        uf = UserForm(req.POST)
        if uf.is_valid():
            #get form data
            username = uf.cleaned_data['name']
            password = uf.cleaned_data['password']
            #add into ORM database
            Owners.objects.create(name= username,password=password)
            return HttpResponse('regist success!!')
    else:
        uf = UserForm()
    return render_to_response('version1/regist.html',{'uf':uf}, context_instance=RequestContext(req))


def login_2(req):
    if req.method == 'POST':
        uf = UserForm(req.POST)
        if uf.is_valid():
            #get form password
            username = uf.cleaned_data['name']
            password = uf.cleaned_data['password']
            #mapping to ORM to verify
            user = Owners.objects.filter(name__exact = username,password__exact = password)
            if user:
                #if mapping ok -> turn index
                response = HttpResponseRedirect('/index/')
                #HAVE username write in to browser's cookie,duration = 3600
                response.set_cookie('username',username,3600)
                return response
            else:
                # mapping fail -> re login page
                return HttpResponseRedirect('/login/')
    else:
        uf = UserForm()
    return render_to_response('version1/login.html',{'uf':uf},context_instance=RequestContext(req))

#success login 
def index(req):
    username = req.COOKIES.get('username','')
    return render_to_response('version1/index.html' ,{'username':username})


def logout(req):
    response = HttpResponse('logout !!')
    #clean cookie's username
    response.delete_cookie('username')
    response.delete_cookie('sessionid')    
    return response
#$('#a_b_c').click(function(){window.location = '/echart_v1';});


 


# Create your views here.
class UserForm(forms.Form):
    username = forms.CharField()
    headImg = forms.FileField()

def register(request):
    if request.method == "POST":
        uf = UserForm(request.POST,request.FILES)
        if uf.is_valid():
            #Aquire Information
            username = uf.cleaned_data['username']
            headImg = uf.cleaned_data['headImg']
            #Write into database
            user = User()
            user.username = username
            user.headImg = headImg
            user.save()
            return HttpResponse('upload ok!')
    else:
        uf = UserForm()
    return render_to_response('register.html',{'uf':uf},context_instance=RequestContext(req))



#class NotusemodelForm(forms.Form):
#    title = forms.CharField(max_length=50)
#    name = forms.CharField(max_length=50)
#    file = forms.FileField()


def NotusemodelView(request):
    form = NotusemodelForm()
    print request.POST
    print form 
    if form.is_valid:
        #print form
        #print request.POST
        print form

    context_dict = {
     'form': form,
    }
    return render(request, "version1/forms.html", context_dict)







