
from django.urls import path
from cop import views
urlpatterns = [
    path('dash',views.home,name='ho'),
    path('cust<str:pk>',views.customer1,name='cu'),
    path('pro',views.product1,name='pr'),
    path('ccf',views.createcustomer,name='cc'),
    path('co',views.createorders,name='cof'),
    path('u<str:pk>',views.updateorder,name='uo'),
    path('del<str:pk>',views.deleteorder,name='del'),
]
