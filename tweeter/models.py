from django.db import models

class Tweet(models.Model):
	creator = models.ForeignKey('auth.User', related_name='tweets', on_delete=models.CASCADE)
	text = models.CharField(max_length=140)
	timestamp = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ['-timestamp']
