from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import json
# Create your views here.
def index(request):
    return HttpResponse('Welcome the Restuarant')

def assign_staff(request):
    restaurant_id = request.GET.get('restaurant_id')
    staff_id_list = request.GET.getlist('staff_id_list')
    with open('restaurant/staff_id_list.json', 'r') as f:
        temp = json.load(f)
        for i in temp['field']:
          if i['restaurant_id'] == restaurant_id:
             print(i['restaurant_id'])
             print(i['assign_staffed'])
             return HttpResponse('Already assigned')
          
        temp['field'].append({'restaurant_id':int(restaurant_id), 'assign_staffed':staff_id_list})

    with open('restaurant/staff_id_list.json', 'w') as f:
        json.dump(temp, f)
    return HttpResponse('Staff assigned')


  
def check_staff(request):
    restaurant_id = request.GET.get('restaurant_id')
    with open('restaurant/staff_id_list.json', 'r') as f:
        #load the json and get the staff_id_list from the restaurant_id
        staff_id_list = json.load(f)
        for i in staff_id_list['field']:
            print(type(i['restaurant_id']))
            if i['restaurant_id'] == int(restaurant_id):
                print(i['restaurant_id'])
                print(i['assign_staffed'])
                return JsonResponse(i['assign_staffed'], safe=False)
        
    
    return HttpResponse("not available")

    

        