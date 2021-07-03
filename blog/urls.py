from django.urls import path
from .views import BListView,BDetailView,BCreateView,BUpdateView,BDeleteView,First

urlpatterns = [
    path('post/<int:pk>',BDetailView.as_view(),name='post_detail'),
    path('',BListView.as_view(),name='home'),
    path('post/new',BCreateView.as_view(),name='post_new'),
    path('post/<int:pk>/edit/',BUpdateView.as_view(),name='post_edit'),
    path('post/<int:pk>/delete/',BDeleteView.as_view(),name='post_delete'),
    path('first/',First.as_view(),name='first')
    

]