import requests
import os
from rest_framework import status   
from django.shortcuts import render, redirect
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ItemVisualSerializer,EstorLogoSerializer
from . models import ItemVisual,EstorLogo
from django.contrib import messages
# Create your views here.

#import time
# time.sleep(5)  # Wait for 5 seconds before re-trying
def home(request):
    
    if request.method == 'GET':
        
        return render(request,'TheFiles/home.html')

@api_view(['POST'])
def ItemVisualCreate(request):
    #print(f"Hello from save: {request}")
    serializer = ItemVisualSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()     
    return Response(serializer.data)

@api_view(['GET'])
def VisualDetail(request, pk):
    itemVisual = ItemVisual.objects.get(ItemId=pk)

    serializer = ItemVisualSerializer(itemVisual, many=False)
    return Response(serializer.data)







@api_view(['POST'])
def EstorLogoCreate(request):
    #print(f"Hello from save: {request}")
    serializer = EstorLogoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()     
    return Response(serializer.data)

@api_view(['GET'])
def EstorLogoDetail(request, pk):
    estorLogo = EstorLogo.objects.get(EstorId=pk)

    serializer = EstorLogoSerializer(estorLogo, many=False)
    return Response(serializer.data)


























# @api_view(['GET'])
# def FederationList(request):
	
# 	federation = Federation.objects.all()
# 	serializer = FederationSerializer(federation, many=True)
# 	#taskTest = Task.objects.all(user = user)

# 	return Response(serializer.data)


# @api_view(['POST'])
# def FederationUpdate(request, pk):
# 	federation = Federation.objects.get(superID=pk)
# 	serializer = FederationSerializer(instance=federation, data=request.data)

# 	if serializer.is_valid():
# 		serializer.save()

# 	return Response(serializer.data)
#creating federation

# def createFed(request):
    
    
#     if request.method == 'GET':
        
#         return render(request, 'TheFiles/createFed.html')
    
    
#     if request.method == 'POST':
#             attempt_num = 0  # keep track of how many times we've retried
#        # while attempt_num < MAX_RETRIES:
#             url = 'http://kznsannualreport.pythonanywhere.com/FederationCreate/'
#             payload = {
#                 #FedId
#                 'SARS_Tax_Clearance':request.POST["SARS_Tax_Clearance"],
#                  'Child_Protection_Policies':request.POST["Child_Protection_Policies"],
#                     'superID':3,
#                     'FederationName':"Ethekwini Softball Association",
                    
#             }
#             p2 = {
#                 'OfficialLetterhead':request.FILES["OfficialLetterhead"],
#                     'Constitution': request.FILES["Constitution"],
#                     'last_AGM_Minutes':request.FILES["last_AGM_Minutes"],
#                     'Annual_Financial_Statement':request.FILES["Annual_Financial_Statement"],
                    
#                     'Tax_Clearance_Copy':request.FILES["Tax_Clearance_Copy"],
                   
#                     'Child_Protection_Copy':request.FILES["Child_Protection_Copy"],
#             }
#             r = requests.post(url, data = payload,files=p2)
            
#             if r.status_code == 200:
#                 data = r.json()
#                 messages.error(request, "Status: "+str(r.status_code))
#                 print(f"data: {data}")
#                 return redirect('viewFed',fedId =int(data["FedId"]))
#             else:
#                 messages.error(request,f"Request failed: "+str(r.status_code))
#                 return redirect('createFed')
#                 pass
        #return Response({"error": "Request failed"}, status=r.status_code)
    
# def viewFed(request, fedId):
#     url = 'http://kznsannualreport.pythonanywhere.com/FederationDetail/'+str(fedId)+'/'
    
#     r = requests.get(url)
#     print("Before R")
#     print(r.json())
#     federation = r.json()
#     return render(request, 'TheFiles/viewFed.html', {"federation":federation})
    
    
    
# @api_view()
# def FedList(request):
	
# 	tasks = Federation.objects.all()
# 	serializer = FederationSerializer(tasks, many=True)
# 	#taskTest = Task.objects.all(user = user)

# 	return Response(serializer.data)