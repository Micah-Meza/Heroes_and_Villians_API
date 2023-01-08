from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import SuperSerializer
from .models import Super
from rest_framework.views import APIView

# Create your views here.
























# class SuperList(APIView):
#     def get(sefl, request):
#         supers = Super.objects.all()
#         serializer = SuperSerializer(supers, many = True)
#         return Response(serializer.data, status = status.HTTP_200_OK)






@api_view(['GET', 'POST'])
def super_list(request):
    if request.method == 'GET':
        super = Super.objects.all()
        supers_filtered_heroes = super.filter(super_type = 1)
        supers_filtered_villians = super.filter(super_type = 2)
        supers_heroes_serialized = SuperSerializer(supers_filtered_heroes, many = True)
        supers_villians_serialized = SuperSerializer(supers_filtered_villians, many = True)
        custom_dictionary = {"Heroes" : supers_heroes_serialized.data,
                            "Villians" : supers_villians_serialized.data,}
        return Response(custom_dictionary,status = status.HTTP_200_OK)

    elif request.method == 'POST':

        print(request.data)
        serializer = SuperSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)


@api_view(['GET', 'PUT'])
def super_detail(request, pk):

    super = get_object_or_404(Super, pk = pk)
    # try:
    #     super = Super.objects.get(pk = pk)
    #     serializer = SuperSerializer(super)
    #     return Response(serializer.data, status = status.HTTP_200_OK)

    # except Super.DoesNotExist:
    #     return Response(status = status.HTTP_204_NO_CONTENT)


    if request.method == 'GET':
        serializer = SuperSerializer(super)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = SuperSerializer(super, data = request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response(serializer.data)



















# class SuperList(APIView):
#     def get(self, request):
#         supers = Super.objects.all()
#         serializer = SuperSerializer(supers, many = True)
#         return Response(serializer.data, status = status.HTTP_208_ALREADY_REPORTED)

#     def post(self, request):
#         serializer = SuperSerializer(data = request.data)
#         serializer.is_valid(raise_exception = True)
#         serializer.save()
#         return Response(serializer.data, status = status. HTTP_201_CREATED)

