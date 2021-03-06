from __future__ import unicode_literals

from django.db import models

from django.utils import timezone

# Create your models here.

class Post(models.Model):
	author = models.ForeignKey('auth.User')
	title = models.CharField(max_length=150)
	text = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)

	def publish(self):
		self.published_date = timezone.now()
		delf.safe()

	def __str__(self):
		return self.title


class Category(models.Model):
	admin = models.TextField(max_length=50)
	quest = models.TextField(max_length=50)