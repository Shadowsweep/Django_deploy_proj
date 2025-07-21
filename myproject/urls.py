from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),               # New: Home page URL
    path('add/', views.add_entry, name='add_entry'), # URL for adding new entries
    path('list/', views.entry_list, name='entry_list')
]