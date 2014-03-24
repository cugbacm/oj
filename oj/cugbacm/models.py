from django.db import models

# Create your models here.
class User(models.Model):
	name = models.CharField(max_length = 200)
	password = models.CharField(max_length = 20)
	session = models.CharField(max_length = 20)
	specialty = models.CharField(max_length = 100)
	tel = models.CharField(max_length = 100)
	email = models.EmailField(max_length = 100)
	nickname = models.CharField(max_length = 100)
	def __unicode__(self):
		return self.name

class Submit(models.Model):
	runID = models.IntegerField()
	userName = models.CharField(max_length = 100)
	problemID = models.IntegerField()
	status = models.CharField(max_length = 100)
	memory = models.IntegerField()
	runTime = models.IntegerField()
	codeLength = models.IntegerField()
	date = models.DateField(auto_now = True)
	timestamp = models.TimeField(auto_now = True)
	code = models.TextField()
	def __unicode__(self):
		return str(self.runID)

class Problem(models.Model):
	problemID = models.IntegerField()
	title = models.CharField(max_length = 100)
	timeLimit = models.IntegerField()
	memoryLimit = models.IntegerField();
	acceptedSubmission = models.IntegerField();
	totalSubmission = models.IntegerField();
	description = models.TextField();
	input = models.TextField();
	output = models.TextField();
	sampleInput = models.TextField();
	sampleOutput = models.TextField();
	author = models.CharField(max_length = 100)
	def __unicode__(self):
		return self.title


