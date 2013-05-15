from django.db import models
from datetime import datetime, timedelta
from django.utils import timezone
#from django.db.models import Model

# Create your models here.
class Poll(models.Model):
	question = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')
	
	def was_published_recently(self):
		return self.pub_date >= timezone.now() - timedelta(days=1)
	
	def __unicode__(self):
		return self.question
	
class Choice(models.Model):
	poll = models.ForeignKey(Poll)
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)
	
	def __unicode__(self):
		return self.choice_text