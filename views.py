from django.shortcuts import render
from django.views.generic import TemplateView
import json
import datetime
import time
# Create your views here.
class HomePageView(TemplateView):
    template_name="index.html"
class AboutPageView(TemplateView):
    template_name="about.html"


def filt(request):
    data=''
    day=''
    year=''
    count=0
    loca=''
    list_location= ['']
    if request.method == 'GET' and 'filter' in request.GET:
        data=request.GET['filter']
        #checks if the request is made for day filter
        if 'day' in request.GET and request.GET['day']!='':
            day=request.GET['day']
            with open('data.json') as json_file: 
                data_main = json.load(json_file)
                for x in range(len(data_main["log_details"])):
                    daii=data_main["log_details"][x]["date"]
                    if(daii==day):
                        count=count+1
                        
        #checks if the request is made for week filter
        if 'week' in request.GET and request.GET['week']!='':
            weekstr=request.GET['week']
            weekint=int(weekstr[-2:])-1
            weekyear=int(weekstr[0:4])
            startdate=time.asctime(time.strptime('%d %d 1' %(weekyear,weekint),'%Y %W %w'))
            startdate=datetime.datetime.strptime(startdate,'%a %b %d %H:%M:%S %Y')
            dates=[startdate.strftime('%Y-%m-%d')]
            for i in range(1,7):
                day=startdate+datetime.timedelta(days=i)
                dates.append(day.strftime(('%Y-%m-%d')))
            with open('data.json') as json_file: 
                data_main = json.load(json_file)
                for x in range(len(data_main["log_details"])):
                    daii=data_main["log_details"][x]["date"]
                    for i in range(1,7):
                        if(dates[i]==daii):
                            count=count+1
                            break
        
        #checks if the request is made for year filter
        if 'year' in request.GET and request.GET['year']!='':
            year=request.GET['year']
            with open('data.json') as json_file: 
                data_main = json.load(json_file)
                for x in range(len(data_main["log_details"])):
                    years=str(data_main["log_details"][x]["date"])[0:4]
                    if(years==year):
                        count=count+1
                        
          #checks if user wants list of location out of total location the website has been access from              
        if data=='loc':
            with open('data.json') as json_file: 
                data_main = json.load(json_file)
                
                for x in range(len(data_main["log_details"])):
                    temp=(data_main["log_details"][x]["location"])
                    if(temp not in list_location):
                        list_location.append(temp)
         
        #checks if user wants to check clicks from a particular location
    if 'loc' in request.GET and request.GET['loc']!='':
            loca=request.GET['loc']
            with open('data.json') as json_file: 
                data_main = json.load(json_file)
                for x in range(len(data_main["log_details"])):
                    locat=(data_main["log_details"][x]["location"])
                    if(loca==locat):
                        count=count+1    
    return render(request, 'vis.html',{'data':data,'day':day,'count':count,'list_location':list_location})
    
    
    
