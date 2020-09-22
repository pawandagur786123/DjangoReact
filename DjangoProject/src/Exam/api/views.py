from rest_framework import generics
from Exam.models import Exam
from .serializers import ExamSerializer
from rest_framework.decorators import list_route

class ExamListView(generics.ListAPIView):
	queryset = Exam.objects.all()
	serializer_class = ExamSerializer
	
