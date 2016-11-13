
import datetime
from django.db import models
from django.utils import timezone

# Create your models here.

class Event(models.Model):
	location = models.CharField(max_length = 200, default = "")
	name = models.CharField(max_length = 200, default = "")
	date_time = models.DateTimeField(auto_now_add = True)
	description = models.TextField()
	event_pic = models.ImageField(upload_to='upload/upload_img/',default='upload/upload_img/1.jpg')
	attendees = models.IntegerField(default = 0)

	def __str__(self) :
		return self.name

	class Meta:
		ordering = ['-date_time']


class Food(models.Model):
	name = models.CharField(max_length = 200, default = "")
	food_type = models.CharField(max_length = 100, default = "")
	events = models.ManyToManyField(Event, related_name = "foods")

	