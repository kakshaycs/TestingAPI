from django.shortcuts import render

from rest_framework import viewsets
from .models import User, Question, Answer, Reply, Tag
from .Serializers import UserSerializer,TagSerializer, QuestionSerializer,AnswerSerializer, ReplySerializer

class UserView(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer

class QuestionView(viewsets.ModelViewSet):
	queryset = Question.objects.all()
	serializer_class = QuestionSerializer

class AnswerView(viewsets.ModelViewSet):
	queryset = Answer.objects.all()
	serializer_class = AnswerSerializer

class ReplyView(viewsets.ModelViewSet):
	queryset = Reply.objects.all()
	serializer_class = ReplySerializer

class TagView(viewsets.ModelViewSet):
	queryset = Tag.objects.all()
	serializer_class = TagSerializer







