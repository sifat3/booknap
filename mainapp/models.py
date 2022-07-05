from django.db import models
from datetime import datetime

class Book(models.Model):
	name = models.CharField(max_length=200)
	short_desc = models.TextField()
	desc = models.TextField()
	image = models.ImageField(upload_to='pics')
	writer = models.CharField(max_length=200)
	year = models.IntegerField()
	owner = models.CharField(max_length=200)
	borrowed = models.BooleanField(default=False)
	borrowed_from = models.CharField(max_length=200)
	borrowing_date = models.DateField(default=datetime.now(), blank=True)
	borrowing_return_date = models.DateField(default=datetime.now(), blank=True)
	lent = models.BooleanField(default=False)
	lending_date = models.DateField(default=datetime.now(), blank=True)
	lending_return_date = models.DateField(default=datetime.now(), blank=True)
	lent_by = models.CharField(max_length=200)
	gift = models.BooleanField(default=False)
	gift_by = models.CharField(max_length=200)
	gift_date = models.DateField(default=datetime.now(), blank=True)