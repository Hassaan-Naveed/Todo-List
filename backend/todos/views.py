from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from .models import Todo
from .serializers import TodoSerializer
class TodosViewSet(viewsets.ModelViewSet):
	queryset = Todo.objects.all()
	serializer_class = TodoSerializer
		