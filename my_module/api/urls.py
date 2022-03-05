from django.urls import include,path
from rest_framework.routers import DefaultRouter

from my_module.api.views import TestThisAPIView
router = DefaultRouter()
        
urlpatterns = [
        path('test-api/', TestThisAPIView.as_view(), name="test-api"),
    ]