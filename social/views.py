from django.shortcuts import render, HttpResponse, get_object_or_404, HttpResponseRedirect
from .models import *
from .forms import *
import random
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail
from django.contrib.auth.models import User
import operator
from django.db.models import Q
from django.contrib.auth.decorators import login_required

# Create your views here.


def index(request):
	if request.method == 'POST':
		data=request.POST
		form1 = SignUpForm(request.POST)
		form2 = SignInForm()
		form3 = SearchForm()
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
		if request.session.get('user_id', None) is None:	
			form1 = SignUpForm()
			form2 = SignInForm() 
			form3 = SearchForm()
			return render(request,"social/index.html", {'form1': form1,'form2':form2, 'form3':form3})
		else:
			form3 = SearchForm()
			user_id = request.session.get('user_id')	
			user = User.objects.get(id=user_id)
			user_profile = user.user_profile
			return render(request,"social/index.html", {'form3':form3, 'user_profile':user_profile})
		
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
			form3 = SearchForm()
			return render(request, 'social/index.html', {'message':"You have been registered. Sign in to continue",'form1': form1,'form2':form2, 'form3':form3})  
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
				request.session['user_id']=user.id
				user_profile = user.user_profile
				form = UpdateForm()
				return render(request, 'social/home.html', {'user_profile' : user_profile, 'current_user' : user_profile, 'form': form})  
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
			return render(request, 'social/home.html', {'user_profile' : user_profile, 'current_user' : user_profile, 'message':"Your profile has been updated!"})
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
			return render(request, 'social/home.html', {'user_profile' : user_profile, 'current_user' : user_profile, 'message':"Your profile has been updated!"})
		else:
			form1 = UpdatePlayer()
			form2 = UpdateForm()
			return render(request, 'social/addteam.html', {'form1':form1 , 'form2':form2, 'message':"Please enter valid details!"})
	else:
		form1 = UpdatePlayer()
		form2 = UpdateForm()
		return render(request, 'social/playerupdate.html', {'form1':form1, 'form2':form2})

def add_ground(request):
	if request.method =='POST':
		data = request.POST
		form = AddGround(request.POST, request.FILES)
		if form.is_valid():
			user = request.user
			user_profile = user.user_profile
			owner = user_profile.owner
			owner.ground_set.create(name=data['name'],dp=form.cleaned_data.get('dp'), place=form.cleaned_data.get('place'), address=data['address'], game=form.cleaned_data.get('game'))
			return render(request, 'social/home.html', {'user_profile' : user_profile, 'current_user' : user_profile, 'message':"New Ground has been added!"})
		else:
			form1 = AddGround()
			return render(request, 'social/addground.html', {'form1':form1 , 'message':"Please enter valid details!"})

	else:
		form1 = AddGround()
		return render(request, 'social/addground.html', {'form1':form1})

def owner_profile(request):
	if request.method =='POST':
		data = request.POST
		form = UpdateOwner(request.POST)
		if form.is_valid():
			user = request.user
			user_profile = user.user_profile
			owner = user_profile.owner
			owner.phone_no = form.cleaned_data.get('phone_no')
			owner.save()
			return render(request, 'social/home.html', {'user_profile' : user_profile, 'current_user' : user_profile, 'message':"Your profile has been updated!"})
		else:
			form1 = UpdateOwner()
			return render(request, 'social/ownerupdate.html', {'form1':form1 , 'message':"Please enter valid details!"})

	else:
		form1 = UpdateOwner()
		return render(request, 'social/ownerupdate.html', {'form1':form1})

def player_game(request):
	if request.method =='POST':
		data = request.POST
		form = PlayerGame(request.POST)
		if form.is_valid():
			user = request.user
			user_profile = user.user_profile
			player = user_profile.player
			player.playergameprofile_set.create(game=form.cleaned_data.get('game'), position=data['position'], skills=data['skills'])
			return render(request, 'social/home.html', {'user_profile' : user_profile, 'current_user' : user_profile, 'message':"A Game has been added to your profile!"})
		else:
			form1 = PlayerGame()
			return render(request, 'social/playergame.html', {'form1':form1 , 'message':"Please enter valid details!"})

	else:
		form1 = PlayerGame()
		return render(request, 'social/playergame.html', {'form1':form1})

def ground_detail(request, ground_id):
    ground = get_object_or_404(Ground, pk=ground_id)
    return render(request, 'social/ground_detail.html', {'ground': ground})

def search_view(request):
 	if request.method == 'GET': 
 		search_for = request.GET['searchfor']
		search_query = request.GET['searchfield']
		if(search_for=='P'):
			results = Player.objects.search(search_query)
		if(search_for=='O'):
			results = Owner.objects.search(search_query)
		if(search_for=='G'):
			results = Ground.objects.search(search_query)
		form = SearchForm()
		return render(request, 'social/searchresults.html', {'results': results, 'search_for': search_for, 'form':form})


def home_redirect(request, result_id):
	user_profile = get_object_or_404(User_profile, pk=result_id)
	current = request.user
	if current.is_authenticated():
		current_user = current.user_profile
	else:
		current_user = None
	return render(request, 'social/home.html', {'user_profile' : user_profile, 'current_user' : current_user})

def build_team(request):
	if request.method =='POST':
		data = request.POST
		form = TeamForm(request.POST)
		if form.is_valid():
			user = request.user
			user_profile = user.user_profile
			player1 = user_profile.player
			p = player1.team_set.create(game=form.cleaned_data.get('game'), name=form.cleaned_data.get('name'), expertise=form.cleaned_data.get('expertise'), home_ground=form.cleaned_data.get('home_ground'))
			p.save()
			for player in form.cleaned_data.get('player'):
				p.player.add(player)
			p.save()
			return render(request, 'social/home.html', {'user_profile' : user_profile, 'current_user' : user_profile, 'message':"You have created a new team!"})
		else:
			form1 = TeamForm()
			return render(request, 'social/addteam.html', {'form1':form1 , 'message':"Please enter valid details!"})

	else:
		form1 = TeamForm()
		return render(request, 'social/addteam.html', {'form1':form1})

def team_detail(request, team_id):
	team = get_object_or_404(Team, pk=team_id)
	return render(request, 'social/team_detail.html', {'team': team})