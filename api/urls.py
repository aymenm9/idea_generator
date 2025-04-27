from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

# Create a router and register our viewset with it.
router = DefaultRouter()
router.register('Category/', views.UserView, basename='user')



urlpatterns=[
    path('users/',views.UserView.as_view(),name='create user'),
]