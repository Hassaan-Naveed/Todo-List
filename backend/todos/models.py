from django.db import models

class Todo(models.Model):
	title = models.CharField(max_length=500)
	body = models.CharField(max_length=1000)
	date_created = models.DateTimeField()
	date_due = models.DateField()
	is_completed = models.BooleanField()
	defunct = models.BooleanField()

	def __str__(self):
		return self.title