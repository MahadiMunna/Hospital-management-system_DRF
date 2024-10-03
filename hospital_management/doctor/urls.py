from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()

router.register('list', DoctorViewSet)
router.register('specialization', SpecializationViewSet)
router.register('designation', DesignationViewSet)
router.register('available_time', AvailableTimeViewSet)
router.register('reviews', ReviewViewSet)

urlpatterns = [
    path('', include(router.urls))
]