from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
	#title, url, pub_date
	#votes_total, image, icon, body
	title = models.CharField(max_length=225)
	url = models.TextField(default="This is the url.")
	pub_date = models.DateTimeField()
	votes_total = models.IntegerField(default=1)
	image = models.ImageField(upload_to='image/')
	icon = models.ImageField(upload_to='image/')
	body = models.TextField(default="This is product is amazing")
	hunter = models.ForeignKey(User, on_delete=models.CASCADE)
	#if user is deleted, we also want to delete the product

	def __str__(self):
		return self.title

	def summary(self):
		return self.body[:200]

	def pub_date_pretty(self):
		return self.pub_date.strftime('%b %e %Y')

	#hunter

class Vote(models.Model):
	hunter = models.ForeignKey(User, on_delete=models.CASCADE)
	product = models.ForeignKey(Product, on_delete=models.CASCASE)
	