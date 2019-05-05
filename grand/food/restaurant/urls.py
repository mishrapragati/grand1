from django.contrib import admin
from django.urls import include,path
from food import views


urlpatterns = [
    path(r'^$',views.v1,name='v1')

]