from django.urls import path
from tws import views

urlpatterns = [
    path('', views.hello, name='hello'),
    path('ProductList/', views.ProductListView.as_view(), name = 'ProductListView'),
    path('GiftList/', views.GiftListView.as_view(), name = 'GiftListView'),
    path('Report/', views.ReportView.as_view(), name = 'Report'),
    #path('Inventory/<Id>', views.InvView.as_view(), name = 'InvView'),
]
