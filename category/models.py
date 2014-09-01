#coding=utf-8
from django.db import models

# Create your models here.
class Category(models.Model):
	""" docting for Categorys """

	class Meta:
		verbose_name = u'类别'
		verbose_name_plural = verbose_name

	category_name = models.CharField( max_length = 30, verbose_name = u'类别名')
	parent_category = models.IntegerField( null = True, verbose_name = u'父类别')
	id = models.AutoField( primary_key = True)

	def __unicode__(self):
		return self.category_name