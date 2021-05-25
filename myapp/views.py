from django.shortcuts import render,redirect
from .models import Contact,User,Product
from django.conf import settings
# Create your views here.
def index(request):
	return render(request,'index.html')

def about(request):
	return render(request,'about.html')

def brand(request):
	return render(request,'brand.html')

def special(request):
	return render(request,'special.html')

def contact(request):
	if request.method=="POST":
		Contact.objects.create(
				name=request.POST['name'],
				mobile=request.POST['mobile'],
				email=request.POST['email'],
				message=request.POST['message']
			)
		msg="Contact saved successfully"
		return render(request,'contact.html',{'msg':msg})
	else:
		return render(request,'contact.html')

def login(request):

	if request.method=="POST":
		try:
			user=User.objects.get(
				email=request.POST['email'],
				password=request.POST['password']
				)
			if user.usertype=="user":

				request.session['email']=user.email
				request.session['fname']=user.fname
				request.session['image']=user.image.url
				return render(request,'index.html')
			elif user.usertype=="seller":
				request.session['email']=user.email
				request.session['fname']=user.fname
				request.session['image']=user.image.url
				return render(request,'seller_index.html')

		except:
			msg="Email Or Password Is Incorrect"
			return render(request,'login.html',{'msg':msg})
	else:
		return render(request,'login.html')


def signup(request):

	if request.method=="POST":
		try:
			user=User.objects.get(email=request.POST['email'])
			msg="Email already registered"
			return render(request,'signup.html',{'msg':msg})
		except:
			if request.POST['password']==request.POST['cpassword']:
				User.objects.create(
						usertype=request.POST['usertype'],
						fname=request.POST['fname'],
						lname=request.POST['lname'],
						mobile=request.POST['mobile'],
						email=request.POST['email'],
						password=request.POST['password'],
						cpassword=request.POST['cpassword'],
						address=request.POST['address']
					)
				msg="User sign up successful"
				return render(request,'login.html',{'msg':msg})
			else:
				msg="Password and Confirm password does not match"
				return render(request,'signup.html',{'msg':msg})
	else:
		return render(request,'signup.html')

def logout(request):
	try:
		del request.session['email']
		del request.session['fname']
		return render(request,'login.html')
	except:
		return render(request,'login.html')

def seller_add_product(request):
	if request.method=="POST":
		product_seller=User.objects.get(email=request.session['email'])
		Product.objects.create(
				product_seller=product_seller,
				product_category=request.POST['product_category'],
				product_brand=request.POST['product_brand'],
				product_price=request.POST['product_price'],
				product_color=request.POST['product_color'],
				product_description=request.POST['product_description'],
				product_image=request.FILES['product_image']
			)
		msg="Product added successfully"
		return render(request,'seller_add_product.html',{'msg':msg})
	else:
		return render(request,'seller_add_product.html')

def seller_index(request):
	return render(request,'seller_index.html')