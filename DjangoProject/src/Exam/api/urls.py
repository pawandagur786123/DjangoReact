from django.conf.urls import url, include
from django.contrib import admin
from .views import ExamListView

urlpatterns = [
    url(r'', ExamListView.as_view()),
]
