from django.urls import path
from . import views
# from froala_editor import views

urlpatterns = [
    path('', views.home, name='home')
]