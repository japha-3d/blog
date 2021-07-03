from  django.urls import  path
from .views import View
urlpatterns=[
    path('signup',View.as_view(),name='signup'),
    ]