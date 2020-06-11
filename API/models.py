from django.db import models
from datetime import datetime 


class User(models.Model):
	"""docstring for Users"""
	name = models.CharField(max_length=200)
	email = models.EmailField(max_length=100)
	phone_no = models.CharField(max_length=15)
	totalQuestions = models.IntegerField(default=0)
	totalAnswers = models.IntegerField(default=0)

	def __str__(self):
		return self.name

class Question(models.Model):
	"""docstring for Questions"""
	auther = models.ForeignKey(User,on_delete=models.CASCADE)
	question_text = models.TextField()
	noOfAnswers = models.IntegerField(default=0)
	upVotes = models.IntegerField(default=0)
	downVotes = models.IntegerField(default=0)
	date = models.DateTimeField(default=datetime.now, blank=True)

	def __str__(self):
		return self.question_text[:100]


class Answer(models.Model):
	"""docstring for Answers"""
	auther = models.ForeignKey(User,on_delete=models.CASCADE)
	question = models.ForeignKey(Question,on_delete=models.CASCADE)
	answer_text = models.TextField()
	upVotes = models.IntegerField(default=0)
	downVotes = models.IntegerField(default=0)
	date = models.DateTimeField(default=datetime.now, blank=True)
	noOfReply = models.IntegerField(default=0)

	def __str__(self):
		return self.answer_text[:100]

class Reply(models.Model):
	answer = models.ForeignKey(Answer,on_delete=models.CASCADE)
	comment = models.TextField()
	date = models.DateTimeField(default=datetime.now, blank=True)

	def __str__(self):
		return self.comment
		

class Tag(models.Model):
	question = models.ForeignKey(Question,on_delete=models.CASCADE)
	tag = models.CharField(max_length=50)

	def __str__(self):
		return self.tag 

		
