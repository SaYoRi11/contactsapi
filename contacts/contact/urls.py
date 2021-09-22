from rest_framework.routers import DefaultRouter
from .views import ContactViewSet, EmailViewSet, PhoneViewSet
from django.urls import path, include

router = DefaultRouter()
router.register('contact', ContactViewSet)
router.register('emails', EmailViewSet)
router.register('phone_nos', PhoneViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]