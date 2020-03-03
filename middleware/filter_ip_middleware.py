from django.core.exceptions import PermissionDenied
from django.utils.deprecation import MiddlewareMixin
from django.urls import resolve
from datetime import datetime
import json

#custom middleware used to check request and filter it according to our needs

class FilterIPMiddleware(MiddlewareMixin):
    def process_request(self, request):
         current_url = resolve(request.path_info).url_name
         #checks if the request is made to home page
         if 'home' in current_url:
                ip=request.META.get('REMOTE_ADDR')
                #if user is not logged in then they are by default logged as anonymous 
                username = "anonymous"
                #checking of user authentication
                if request.user.is_authenticated:
                    username = request.user.username
                path_info= request.path
                browser_info=request.META['HTTP_USER_AGENT']
                method_type=request.method
                if method_type == 'POST':
                    data_method = request.POST.copy()
                if method_type == 'GET':
                    data_method = request.GET.copy()
                timestamp=datetime.now().date()
                #all required data is collected in a dictionary
                data={"path_info":path_info, "browser_info":browser_info, "request_data":data_method, "method":method_type, "visited_by":username, "location":"mumbai", "ip_address":ip,"date":timestamp} 
                
                #previous data from json file is loaded in order to append new data
                with open('data.json') as json_file: 
                    data_main = json.load(json_file) 
                    data_main["log_details"].append(data)
                
                #data is appended in previous file with new data
                with open('data.json','w') as f: 
                    json.dump(data_main, f, indent=4, sort_keys=True, default=str)

         return None

