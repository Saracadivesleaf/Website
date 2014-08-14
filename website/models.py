#coding=utf-8
from django.db import models
import datetime
# Create your models here.

class List(models.Model):
	#""" docting for Lists """
	title = models.CharField( max_length = 250, unique = True )
	def __self__(self):
		return self.title
class Meta(models.Model):
	""" docting for Metas """
	ordering = [ '-created_date', ' title ']

class Item(models.Model):
	""" docting for Item """
	title = models.CharField( max_length = 250 )
	created_date = models.DateTimeField( default = datetime.datetime.now )
	completed = models.BooleanField( default = False )
	website_list = models.ForeignKey( List )
	def __self__(self):
		return self_title


		

