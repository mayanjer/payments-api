from django.contrib import admin
from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'payers', PayerViewSet, basename = "payers")
router.register(r'payees', PayeeViewSet, basename = "payees")
router.register(r'payments', PaymentViewSet, basename = "payments")
router.register(r'users', UserViewSet, basename = "users")

urlpatterns = [
    path('admin/', admin.site.urls),
    
] + router.urls
