from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import SuperSerializer
from .models import Super

# Create your views here.

@api_view(['GET', 'POST'])
def super_list(request):
    
    if request.method == 'GET':
        super = Super.objects.all()
        
        supers_filtered_heroes = super.filter(super_type__id = 1)
        supers_heroes_serialized = SuperSerializer(supers_filtered_heroes, many = True)

        supers_filtered_villians = super.filter(super_type__id = 2)
        supers_villains_serialized = SuperSerializer(supers_filtered_villians, many = True)
        
        custom_dictionary = {"Heroes" : supers_heroes_serialized.data,
                            "Villains" : supers_villains_serialized.data,}
            
        if request.query_params.get('type') == 'hero':
            return Response(supers_heroes_serialized.data,status = status.HTTP_200_OK)
        elif request.query_params.get('type') == 'villain':
            return Response(supers_villains_serialized.data,status = status.HTTP_200_OK)
        else:
            return Response(custom_dictionary,status = status.HTTP_200_OK)
    
    elif request.method == 'POST':

        print(request.data)
        serializer = SuperSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)
    

@api_view(['GET', 'PUT', 'DELETE'])
def super_detail(request, pk):

    super = get_object_or_404(Super, pk = pk)
    if request.method == 'GET':
        serializer = SuperSerializer(super)
        return Response(serializer.data, status = status.HTTP_200_OK)

    elif request.method == 'PUT':
        serializer = SuperSerializer(super, data = request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response(serializer.data, status = status.HTTP_200_OK)

    elif request.method == 'DELETE':
        super.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

