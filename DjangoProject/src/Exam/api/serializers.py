from rest_framework import serializers
from Exam.models import Exam

class ExamSerializer(serializers.ModelSerializer):
	class Meta:
		model = Exam
		fields = ('id','question','answer','option1','option2','option3','option4','difficulty_level','subject')
