from django.shortcuts import render, HttpResponse, get_object_or_404, HttpResponseRedirect
from .models import *
from .forms import *
import random
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail
from django.contrib.auth.models import User
# Create your views here.


def index(request):
	if request.method == 'POST':
		data=request.POST
		form1 = SignUpForm(request.POST)
		form2 = SignInForm()
		if form1.is_valid():
			#i = random.randint(1000,9999)
			i=1111
			user = User.objects.create_user(data['username'], data['email'], data['password'])
			user.first_name = data['first_name']
			user.last_name = data['last_name']
			user.is_active=False
			user.save()
			user_profile=User_profile.objects.create(user=user)
			user_profile.confirmation_key=i
			user_profile.profile_type = data['profile_type']
			user_profile.save()
			content = "Confirmation Key for your Account Registeration: " + str(i)
			request.session['user_id'] = user.id
			#send_mail('Account-Confirmation',content,'persontest42@gmail.com',[data['email']], fail_silently=False)
			return render(request,"social/key.html")
			# user_list.append(user)
		else:
			return render(request, "social/index.html", {'form1': form1,'form2':form2})

	else:	
		form1 = SignUpForm()
		form2 = SignInForm() 
		return render(request,"social/index.html", {'form1': form1,'form2':form2})

def sign_up(request):
	user_id = request.session.get('user_id')	
	user = User.objects.get(id=user_id)
	user_profile = user.user_profile

	try:	
		if int(request.POST['confirmation_key']) == user_profile.confirmation_key :
			user.is_active=True
			user.save()
			user_profile.save()
			if(user_profile.profile_type == 'PL'):
				player = Player.objects.create(user_profile=user_profile)
				player.save()
			else:
				owner = Owner.objects.create(user_profile=user_profile)
				owner.save()
			form1 = SignUpForm()
			form2 = SignInForm()
			return render(request, 'social/index.html', {'message':"You have been registered. Sign in to continue",'form1': form1,'form2':form2})  
		else :
			message='Invalid Key'	
			return render(request,"social/key.html",{'message':message})
	except ValueError:
		message='The field cannot be left blank.'	
		return render(request,"social/key.html",{'message':message})
	
def sign_in(request):
	if request.method == 'POST':	
		data = request.POST
		user = authenticate(username=data['username'], password=data['password'])
		if user is not None:
			if user.is_active==True:
				login(request, user)
				user = request.user
				user_profile = user.user_profile
				form = UpdateForm()
				return render(request, 'social/home.html', {'user_profile' : user_profile, 'form': form})  
			else :
				request.session['user_id'] = user.id
				return render(request,"social/key.html")
		else:
			form1 = SignUpForm()
			form2 = SignInForm()
			return render(request,'social/index.html',{'error':"Please enter valid login details",'form1':form1,'form2':form2})

def log_out(request):
	logout(request)
	return HttpResponseRedirect('/social/')

def update(request):
	if request.method == 'POST':
		data = request.POST
		form = UpdateForm(request.POST, request.FILES)
		if form.is_valid():
			user = request.user
			user_profile = user.user_profile
			user_profile.dp = form.cleaned_data['image']
			user_profile.save()
			return render(request, 'social/home.html', {'user_profile' : user_profile, 'message':"Your profile has been updated!"})
	return HttpResponse('allowed only via POST')

def player_profile(request):
	if request.method =='POST':
		data = request.POST
		form = UpdatePlayer(request.POST)
		if form.is_valid():
			user = request.user
			user_profile = user.user_profile
			player = user_profile.player
			player.birthday = form.cleaned_data.get('birthday')
			player.place = data['place']
			player.save()
			return render(request, 'social/home.html', {'user_profile' : user_profile, 'message':"Your profile has been updated!"})
	else:
		form1 = UpdatePlayer()
		form2 = UpdateForm()
		return render(request, 'social/playerupdate.html', {'form1':form1, 'form2':form2})