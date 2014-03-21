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
	runID = models.CharField(max_length = 200)
	userID = models.CharField(max_length = 100)
	problemID = models.CharField(max_length = 100)
	status = models.CharField(max_length = 100)
	memory = models.CharField(max_length = 100)
	time = models.CharField(max_length = 100)
	codeLength = models.CharField(max_length = 100)
	date = models.DateField()
	timestamp = models.TimeField()
	code = models.TextField()
	def __unicode__(self):
		return self.runID		
