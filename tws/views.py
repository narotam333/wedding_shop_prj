from django.shortcuts import render 
from .serializers import ProductListSerializer,GiftListSerializer
from .models import ProductList, GiftList
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter

# Create your views here.

from django.shortcuts import render
def hello(request):
   return render(request,'hello.html',{})


class ProductListView(generics.ListAPIView):
    parser_classes = (MultiPartParser, FormParser)
    queryset = ProductList.objects.all()
    serializer_class = ProductListSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter,)
    ordering=('id',)
    ordering_fields=('id', 'name', 'price',)
    filter_fields=('id', 'name', 'price',)

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        filter_backends = self.filter_queryset(queryset)
        serializer = ProductListSerializer(filter_backends, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        ProductList_serializer = ProductListSerializer(data=request.data)
        if ProductList_serializer.is_valid():
            ProductList_serializer.save()
            return Response(ProductList_serializer.data, status=status.HTTP_201_CREATED)
        else:
            print('error', ProductList_serializer.errors)
            return Response(ProductList_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, *args, **kwargs):
        PK = ProductList.objects.get(name=request.data['name'])
        ProductList_serializer = ProductListSerializer(PK, data=request.data)
        if ProductList_serializer.is_valid():
            ProductList_serializer.save()
            return Response(ProductList_serializer.data)
        else:
            print('error', ProductList_serializer.errors)
            return Response(ProductList_serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class GiftListView(generics.ListAPIView):
    parser_classes = (MultiPartParser, FormParser)
    queryset = GiftList.objects.all()
    serializer_class = GiftListSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter,)
    ordering=('id',)
    ordering_fields=('id', 'name', 'price',)
    filter_fields=('id', 'name', 'price',)

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        filter_backends = self.filter_queryset(queryset)
        serializer = GiftListSerializer(filter_backends, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        GiftList_serializer = GiftListSerializer(data=request.data)
        if GiftList_serializer.is_valid():
            GiftList_serializer.save()
            return Response(GiftList_serializer.data, status=status.HTTP_201_CREATED)
        else:
            print('error', GiftList_serializer.errors)
            return Response(GiftList_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, *args, **kwargs):
        PK = GiftList.objects.get(id=request.data['id'])
        GiftList_serializer = GiftListSerializer(PK, data=request.data)
        if GiftList_serializer.is_valid():
            GiftList_serializer.save()
            return Response(GiftList_serializer.data)
        else:
            print('error', GiftList_serializer.errors)
            return Response(GiftList_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        List = GiftList.objects.filter(id=request.data['id'])
        List.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ReportView(generics.ListAPIView):
    parser_classes = (MultiPartParser, FormParser)
    queryset = GiftList.objects.all()
    serializer_class = GiftListSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter,)
    ordering=('purchased_quantity',)
    #ordering_fields=('id', 'name', 'price',)
    filter_fields=('purchased_quantity',)

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        filter_backends = self.filter_queryset(queryset)
        serializer = GiftListSerializer(filter_backends, many=True)
        return Response(serializer.data)
