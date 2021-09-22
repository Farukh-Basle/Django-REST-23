from django.urls import path,include
from App1.api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('emps',views.EmpViewSet),
router.register('users',views.user_registration_view),

urlpatterns = [
    path('',include(router.urls)),
]