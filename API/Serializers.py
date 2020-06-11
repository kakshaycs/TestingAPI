from rest_framework import serializers
from .models import User,Question, Answer, Reply, Tag

class UserSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = User
		fields = ('id','url','name','email','totalQuestions','totalAnswers')

class QuestionSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = Question
		fields = ('id','url','auther','question_text','noOfAnswers','upVotes','downVotes','date')

class AnswerSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = Answer
		fields = ('id','url','auther','question','answer_text','noOfReply','upVotes','downVotes','date')

class ReplySerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = Reply
		fields = ('answer','url','comment','date')


class TagSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = Tag
		fields = ('url','question','tag')

