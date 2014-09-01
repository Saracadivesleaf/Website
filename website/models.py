#coding=utf-8
from django.db import models
# Create your models here.

class Navigation(models.Model):
	""" docting for Navigations """

	class Meta:
		verbose_name = u'导航'
		verbose_name_plural = verbose_name

	title = models.CharField( max_length = 50, verbose_name = u' 导航名称 ')
	parent_navigation = models.IntegerField( null = True, verbose_name = u' 父导航 ')

	def __unicode__(self):
		return self.title
