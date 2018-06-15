from django.db import models
from datetime import datetime

class WebUrl(models.Model):
	url = models.URLField()
	short_url = models.CharField(max_length=30)
	date_create = models.DateTimeField(auto_now=True)
	visit_count = models.IntegerField(default=0)


