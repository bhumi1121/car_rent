from django.db import models

class User(models.Model):
	usertype=models.CharField(max_length=100)
	name=models.CharField(max_length=100)
	email=models.EmailField()
	pswd=models.CharField(max_length=100)

	def __str__(self):
		return self.usertype+"  "+self.name

class Vehicle(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	vehicletype=models.CharField(max_length=100)
	c_image=models.ImageField(blank=True,null=True,upload_to="images/")
	c_brand=models.CharField(max_length=100,default="mahindra")
	c_name=models.CharField(max_length=100,default="Thar")
	c_model=models.CharField(max_length=100,default="2021")
	c_fuel=models.CharField(max_length=100,default="diesel")
	c_price=models.IntegerField(default=1000)
	c_mileage=models.IntegerField(default=12)
	c_transmission=models.CharField(max_length=100,default="Automatic")
	c_seats=models.IntegerField(default=5)
	c_luggage=models.IntegerField(default=2)
	c_features=models.CharField(max_length=100,default="best car for offroad")
	c_description=models.CharField(max_length=100,default="good")

	razorpay_order_id=models.CharField(max_length=100,null=True,blank=True)
	razorpay_payment_id=models.CharField(max_length=100,null=True,blank=True)
	razorpay_payment_signature=models.CharField(max_length=100,null=True,blank=True)



	def __str__(self):
		return self.vehicletype+"  "+self.c_brand

