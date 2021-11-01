from django.urls import path
from .views import *

urlpatterns = [
    path('', toolBox_view, name="toolbox_home"),
]