from django.db import models

class Product(models.Model):
	title = models.CharField(max_length=200)
	image = models.ImageField(upload_to='image/')
	content = models.TextField(max_length=1000)