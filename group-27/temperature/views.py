from __future__ import unicode_literals
from .models import Temperature 
from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
def index(request):
	received_data=Temperature.objects.all()[len(Temperature.objects.all())-1]
	temp_data=str(received_data.tem_value)
	hum_data=str(received_data.hum_value)
	rain_data=str(received_data.rain_value)
	soil_data=str(received_data.soil_value)
	water_data=str(received_data.water_value)
	context={'tem':temp_data,'hum':hum_data,'rain':rain_data,'soil':soil_data,'water':water_data}
	return render(request,'temperature/index.html',context)
def getdata(request):
	if request.method=='GET' :
		tem_value=request.GET['temperature']
		hum_value=request.GET['humidity']
		rain_value=request.GET['rain_info_1']
		soil_value=request.GET['soil_moisture']
		water_value=request.GET['water_lev']
		
				#rain_value2=request.GET['rain_info2']
		t_obj=Temperature()
		t_obj.tem_value=tem_value
		t_obj.hum_value=hum_value
		t_obj.rain_value=rain_value
		t_obj.soil_value=soil_value
		t_obj.water_value=water_value
		t_obj.save()
		return HttpResponse("data saved in db")
	else:
		return HttpResponse("error")
