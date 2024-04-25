from django.urls import path
from menu.views import APIFoodList

urlpatterns = [
    path('foods/', APIFoodList.as_view(), name='food_list')
]
