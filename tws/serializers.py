from rest_framework import serializers
from .models import ProductList, GiftList

class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductList
        fields = '__all__'

class GiftListSerializer(serializers.ModelSerializer):
    class Meta:
        model = GiftList
        fields = ['id', 'name', 'purchased_quantity']

    def to_representation(self, obj):
        serialized_data = super(GiftListSerializer, self).to_representation(obj) # original serialized data
        product_name = serialized_data.get('name') # get job category id from original serialized data
        product_row = ProductList.objects.get(name=product_name) # get the object from db
        serialized_data['brand'] = product_row.brand # replace id with category name
        serialized_data['price'] = product_row.price
        if product_row.in_stock_quantity > 0:
            serialized_data['available_quantity'] = product_row.in_stock_quantity - serialized_data.get('purchased_quantity')
            if serialized_data.get('purchased_quantity'):
                serialized_data['purchased_quantity'] = serialized_data.get('purchased_quantity')
            else:
                serialized_data['purchased_quantity'] = 0
        else: 
            serialized_data['available_quantity'] = 0
            if serialized_data.get('purchased_quantity'): 
                serialized_data['purchased_quantity'] = serialized_data.get('purchased_quantity')
            else:
                serialized_data['purchased_quantity'] = 0 
        return serialized_data # return modified serialized data


