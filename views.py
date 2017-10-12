# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import gspread
import json,os
from django.shortcuts import render
from django.http import HttpResponse
import sqlite3
#import sys
#print sys.path
#from oauth2client.service_account import ServiceAccountCredentials

# Create your views here.
def ff(): 
    from oauth2client.service_account import ServiceAccountCredentials
    scope = ['https://spreadsheets.google.com/feeds']
    creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
    client = gspread.authorize(creds)
    sheet = client.open("From Mrudula 918522890196").sheet1 
    list_of_hashes = sheet.get_all_records()
    n=len(list_of_hashes)
    k = list_of_hashes[n-1]["Today's temperature is:  31.00 *C"]
    return k

def result(request):
    a = ff()
    return render(request,'sensor/index.html',{'a':a})  
     
def detail(request):
    a = ff()
    return render(request,'sensor/detail.html',{'a':a})  
     
