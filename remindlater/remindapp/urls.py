from django.urls import path
from .views import create_reminder,get_all_reminders

urlpatterns = [
    path('api/create/',create_reminder, name='create_reminder'),
    path('api/all/', get_all_reminders, name='get_all_reminders'),
]