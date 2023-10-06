from django.shortcuts import render,redirect
from .models import User,Vehicle
from django.conf import settings
from django.core.mail import send_mail
import random
import razorpay

# Create your views here.
def index(request):
	vehicle=Vehicle.objects.all()
	return render(request,'index.html',{'vehicle':vehicle})

def about(request):
	return render(request,'about.html')

def client(request):
	return render(request,'client.html')

def contact(request):
	return render(request,'contact.html')

def gallery(request):
	vehicle=Vehicle.objects.all()
	return render(request,'gallery.html',{'vehicle':vehicle})

def services(request):
	return render(request,'services.html')

def signup(request):
	if request.method=="POST":
		try:
			user=User.objects.get(email=request.POST['email'])
			msg1="Email Alredy Exits..."
			return render(request,'signup.html',{'msg1':msg1})
		except:
			if request.POST['pswd']==request.POST['cpswd']:
				User.objects.create(
				usertype=request.POST['usertype'],
				name=request.POST['name'],
				email=request.POST['email'],
				pswd=request.POST['pswd']
				)
				msg="SignUp Successfull...."
				return render(request,'login.html',{'msg':msg})
			else:
				msg1="Password And Confirm Password Not matched...."
				return render(request,'signup.html',{'msg1':msg1})
	else:
		return render(request,'signup.html')

	
def login(request):
	if request.method=="POST":
		try:
			user=User.objects.get(email=request.POST['email'],pswd=request.POST['pswd'])
			request.session['name']=user.name
			request.session['email']=user.email
			request.session['usertype']=user.usertype
			if user.usertype=="customer":
				return render(request,'index.html')
			else:
				return render(request,'manager_index.html')
		except:
			msg1="Username or Password incorrect"
			return render(request,'login.html',{'msg1':msg1})
	else:
		return render(request,'login.html')



def logout(request):
	del request.session['email']
	return redirect('login')


def fpswd(request):
	if request.method=="POST":
		try:
			user=User.objects.get(email=request.POST['email'])
			print("done till here")
			subject = 'Forgot Password OTP'
			otp=random.randint(1000,9999)
			message = f'Hi {user.name}, thank you for registering in . Your OTP is :{otp}'
			email_from = settings.EMAIL_HOST_USER
			recipient_list = [user.email, ]
			send_mail( subject, message, email_from, recipient_list )
			return render(request,'verify_otp.html',{'email':user.email,'otp':str(otp)})
		except:
			msg1 ="you are not a registered user..."
			return render(request,'fpswd.html',{'msg1':msg1})
	else:
		return render(request,'fpswd.html')

def verify_otp(request):
	if request.method=="POST":
		email=request.POST['email']
		otp=request.POST['otp']
		uotp=request.POST['uotp']
		if uotp==otp:
			return render(request,'set_pswd.html',{'email':email})
		else:
			msg1="OTP not match...."
			return render(request,'verify_otp.html',{'msg1':msg1})
	else:
		return render(request,'verify_otp.html')

def set_pswd(request):
	if request.method=="POST":

		email=request.POST['email']
		npswd=request.POST['npswd']
		cnpswd=request.POST['cnpswd']

		if npswd==cnpswd:
			user=User.objects.get(email=email)
			user.pswd=npswd
			user.save()
			return redirect('login')
		else:
			msg1="New Password and Confirm New Password Doesn't Matched !!!!"
			return render(request,'set_pswd.html',{'msg1':msg1})

	else:
		return render(request,'set_pswd.html')

def manager_index(request):
	vehicle=Vehicle.objects.all()
	return render(request,'manager_index.html',{'vehicle':vehicle})


def add_vehicle(request):
	if request.method=="POST":
		user=User.objects.get(email=request.session['email'])
		Vehicle.objects.create(
			user=user,
			c_image=request.FILES['c_image'],
			c_brand=request.POST['c_brand'],
			c_name=request.POST['c_name'],
			c_model=request.POST['c_model'],
			c_fuel=request.POST['c_fuel'],
			c_price=request.POST['c_price'],
			c_mileage=request.POST['c_mileage'],
			c_transmission=request.POST['c_transmission'],
			c_seats=request.POST['c_seats'],
			c_luggage=request.POST['c_luggage'],
			c_features=request.POST['c_features'],
			c_description=request.POST['c_description'],
			)
		msg="Vehical Added Successfull...."
		return render(request,'add_vehicle.html',{'msg':msg})
	else:
		return render(request,'add_vehicle.html')

def my_gallery(request):
	manager=User.objects.get(email=request.session['email'])
	print(">>>>>>>>>>>>>>>>By GET METHOD  : ",manager)
	vehicle=Vehicle.objects.filter(user=manager)
	print(">>>>>>>>>>>>>>>>>>>>>>By FILTER METHOD : ",vehicle)
	return render(request,'my_gallery.html',{'vehicle':vehicle})

def Vehicle_details(request,pk):
	manager=User.objects.get(email=request.session['email'])
	vehicle=Vehicle.objects.get(user=manager)
	print(vehicle.c_name)
	return render(request,'Vehicle_details.html',{'vehicle':vehicle})

def update_vehicle(request,pk):
	manager=User.objects.get(email=request.session['email'])
	vehicle=Vehicle.objects.get(pk=pk,user=manager)
	if request.method=="POST":
		vehicle.user=manager
		vehicle.c_image=request.FILES['c_image']
		vehicle.c_brand=request.POST['c_brand']
		vehicle.c_name=request.POST['c_name']
		vehicle.c_model=request.POST['c_model']
		vehicle.c_fuel=request.POST['c_fuel']
		vehicle.c_price=request.POST['c_price']
		vehicle.c_mileage=request.POST['c_mileage']
		vehicle.c_transmission=request.POST['c_transmission']
		vehicle.c_seats=request.POST['c_seats']
		vehicle.c_luggage=request.POST['c_luggage']
		vehicle.c_features=request.POST['c_features']
		vehicle.c_description=request.POST['c_description']
		vehicle.save()
		return redirect('my_gallery')
	else:
		return render(request,'update_vehicle.html',{'vehicle':vehicle})


def delete_vehicle(request,pk):
	manager=User.objects.get(email=request.session['email'])
	vehicle=Vehicle.objects.get(pk=pk,user=manager)

	vehicle.delete()

	return redirect('manager_index')

def v_details(request,pk):
	vehicle=Vehicle.objects.get(pk=pk)
	total=vehicle.c_price
	client = razorpay.Client(auth = (settings.KEY_ID,settings.KEY_SECRET))
	payments=client.order.create({'amount':total*100, 'currency':'INR', 'payment_capture':1})
	print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>",payments)
	vehicle.razorpay_order_id=payments['id']
	vehicle.save()

	return render(request,'v_details.html',{'total':total,'vehicle':vehicle})

