from django.db import models

# Create your models here.
class Contact(models.Model):
	name=models.CharField(max_length=100)
	mobile=models.CharField(max_length=100)
	email=models.CharField(max_length=100)
	message=models.TextField()

	def __str__(self):
		return self.name

class User(models.Model):
	fname=models.CharField(max_length=100)
	lname=models.CharField(max_length=100)
	mobile=models.CharField(max_length=100)
	email=models.CharField(max_length=100)
	password=models.CharField(max_length=100)
	cpassword=models.CharField(max_length=100)
	address=models.TextField()
	image=models.ImageField(upload_to="user_image/",default="",blank=True,null=True)
	usertype=models.CharField(max_length=100,default="user")

	def __str__(self):
		return self.fname+" - "+self.lname

class Product(models.Model):
	CHOICE=(
			('mobiles','mobiles'),
			('tablets','tablets'),
			('laptops','laptops'),
		)
	seller=models.ForeignKey(User,on_delete=models.CASCADE)
	product_category=models.CharField(max_length=100,choices=CHOICE)
	product_brand=models.CharField(max_length=100)
	product_price=models.IntegerField()
	product_color=models.CharField(max_length=100)
	product_description=models.TextField()
	product_image=models.ImageField(upload_to="productImages/")

	def __str__(self):
		return self.seller.fname+" - "+self.product_category