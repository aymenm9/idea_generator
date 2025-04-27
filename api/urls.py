from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter

# Create a router and register our viewset with it.
router = DefaultRouter()
router.register(r'category', views.CategoryView, basename='category')



urlpatterns=[
    path('users/',views.UserView.as_view(),name='create user'),
    path('', include(router.urls)),
]