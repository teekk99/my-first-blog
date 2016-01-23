from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
	"""
	Blog posts 
	
	Extends:
		models.Model
	
	Variables:
		author {[type]} -- [description]
		title {[type]} -- [description]
		text {[type]} -- [description]
		created_date {[type]} -- [description]
		published_date {[type]} -- [description]
	"""
	author = models.ForeignKey('auth.User')
	title = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(
		default=timezone.now)
	published_date = models.DateTimeField(
		blank=True, null=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title
