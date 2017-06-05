from django.db import models

class MyUser(models.Model):
	username = models.CharField(
		max_length=32
	)
	password = models.CharField(
		max_length=32
	)
	address = models.TextField()


class Type(models.Model):
	Bread = models.CharField(
		max_length = 32
	)
	Price = models.IntegerField()


class Order(models.Model):
	username = models.ForeignKey(
		'MyUser',
		on_delete = models.CASCADE,
	)
	menu = models.CharField(
		max_length=32
	)
	bread = models.ForeignKey(
		'Type'
	)
