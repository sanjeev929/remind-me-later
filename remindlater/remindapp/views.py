from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Reminder
from .serializers import ReminderSerializer

@api_view(['POST'])
def create_reminder(request):
    serializer = ReminderSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_all_reminders(request):
    print("==========")
    reminders = Reminder.objects.all()
    serializer = ReminderSerializer(reminders, many=True)
    return Response(serializer.data)