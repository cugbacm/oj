from django.db import models

# Create your models here.
class User(models.Model):
	userID = models.CharField(max_length = 200, unique = True)
	password = models.CharField(max_length = 20)
	session = models.CharField(max_length = 20)
	specialty = models.CharField(max_length = 100)
	tel = models.CharField(max_length = 100)
	email = models.EmailField(max_length = 100)
	nickname = models.CharField(max_length = 100)
	accepted = models.IntegerField(default = 0)
	total = models.IntegerField(default = 0)
	def __unicode__(self):
		return self.userID

class Submit(models.Model):
	runID = models.IntegerField()
	userID = models.CharField(max_length = 100)
	problemID = models.IntegerField()
	status = models.CharField(max_length = 100)
	memory = models.IntegerField()
	runTime = models.IntegerField()
	language = models.CharField(max_length = 100)
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
	ac = models.IntegerField(default = 0);
	wa = models.IntegerField(default = 0);
	tle = models.IntegerField(default = 0);
	mle = models.IntegerField(default = 0);
	pe = models.IntegerField(default = 0);
	ce = models.IntegerField(default = 0);
	se = models.IntegerField(default = 0);
	totalSubmission = models.IntegerField(default = 0);
	description = models.TextField();
	input = models.TextField();
	output = models.TextField();
	sampleInput = models.TextField();
	sampleOutput = models.TextField();
	hint = models.TextField(default = "");
	visible = models.BooleanField(default = True)
	author = models.CharField(max_length = 100)

	def __unicode__(self):
		return self.title
class ContestSubmit(Submit):
	"""docstring for ContestSubmit"""
	contestID = models.IntegerField()
	def __init__(self):
		super(ContestSubmit, self).__init__()
		
class Contest(models.Model):
	"""docstring for Contest"""
	title = models.CharField(max_length = 100)
	startTime = models.DateField()
	startTimestamp = models.TimeField()
	endTime = models.DateField()
	endTimestamp = models.TimeField()
	author = models.CharField(max_length = 100)
	problemList = models.CommaSeparatedIntegerField(max_length = 10000)
	userList = models.CommaSeparatedIntegerField(max_length = 10000)

	def __unicode__(self):
		return self.title		