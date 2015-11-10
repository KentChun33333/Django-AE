# Basic Import 
from django.shortcuts import render
from django.http import HttpResponseRedirect 
from django.http import HttpResponse

# ORM models
from django.db import models

# part of data slice and dice data with algorithm result
import numpy as np
import pandas as pd
import psycopg2
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

def login_user(request):
    state = "Login Page"
    username = password = ''
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                state = "Successfully logged in!"
                return HttpResponseRedirect('/version1/main_page',RequestContext(request))
                #return render_to_response('rango/index.html',{'state':state, 'username': username}, RequestContext(request))
                #
            else:
                state = "Your account is not active, please contact the site admin."
        else:
            state = "Your username and/or password were incorrect."
            
    return render_to_response('version1/auth_v2.html',{'state':state, 'username': username}, RequestContext(request)) # 
	
def main_page(request):
	context_dict={}
	return render(request, 'version1/main_page.html', context_dict)
	
def form_maker(request):
	context_dict={}
	return render(request, 'version1/form_v1.html', context_dict)

def echart_v1(request):
    context_dict={}
    return render(request, 'version1/echart_v1.html', context_dict)

