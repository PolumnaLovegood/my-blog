from django.urls import path
from .views import contact_list, contact_detail, contact_new, contact_edit

urlpatterns = [
    path('', contact_list, name='contact_list'),
    path('contact/<int:pk>/', contact_detail, name='contact_detail'),
    path('contact/new/', contact_new, name='contact_new'),
    path('post/<int:pk>/edit/', contact_edit, name='contact_edit'),
]