from django import forms
from .models import *
from django.contrib.admin.widgets import AdminDateWidget
from django.forms import extras
from .models import *

class  SignUpForm(forms.Form):
	PLAYER = 'PL'
	OWNER = 'OW'
	PROFILE_TYPE_CHOICES = (
		(PLAYER, 'Player'),
		(OWNER, 'Owner'),
	)
	first_name = forms.CharField(max_length=20,min_length=1)
	last_name = forms.CharField(max_length=20,min_length=1)
	username = forms.CharField(max_length=20,min_length=4)
	password = forms.CharField(widget=forms.PasswordInput,min_length=3)
	email = forms.EmailField()
	profile_type = forms.ChoiceField(widget=forms.Select(),label="Are you a", initial="", choices=PROFILE_TYPE_CHOICES)

	def clean_username(self):
		data = self.cleaned_data['username']
		for existing_users in User.objects.all():
			if data == existing_users.username:
				raise forms.ValidationError("This username is already registered")
		return data			

	def clean_email(self):
		data = self.cleaned_data['email']
		for existing_users in User.objects.all():
			if data == existing_users.email:
				raise forms.ValidationError("This email is already registered")
		return data	

class SignInForm(forms.Form):
	username = forms.CharField(max_length=20,min_length=4)
	password = forms.CharField(widget=forms.PasswordInput,min_length=3)


class UpdateForm(forms.Form):
	image = forms.ImageField()

class UpdatePlayer(forms.Form):
	PUNE = 'PUN'
	MUMBAI = 'BOM'
	DELHI = 'DEL'
	BANGALORE = 'BAN'
	CHENNAI = 'CHE'
	PLACE_CHOICES = (
		(PUNE,'Pune'),
		(MUMBAI,'Mumbai'),
		(DELHI,'Delhi'),
		(BANGALORE,'Bangalore'),
		(CHENNAI,'Chennai'),
	)

	DOY = ('1970', '1971', '1972', '1973', '1974', '1975', '1976', '1977',
       '1978', '1979','1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987',
       '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995',
       '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003',
       '2004', '2005', '2006', '2007', '2008', '2009', '2010',)
	birthday = forms.DateField(widget=extras.SelectDateWidget(years = DOY))
	place = forms.ChoiceField(widget=forms.Select(),label="Where do you live", initial="", choices=PLACE_CHOICES)
	game = forms.ModelChoiceField(queryset=Game.objects.all())


class AddGround(forms.Form):
	PUNE = 'PUN'
	MUMBAI = 'BOM'
	DELHI = 'DEL'
	BANGALORE = 'BAN'
	CHENNAI = 'CHE'
	PLACE_CHOICES = (
		(PUNE,'Pune'),
		(MUMBAI,'Mumbai'),
		(DELHI,'Delhi'),
		(BANGALORE,'Bangalore'),
		(CHENNAI,'Chennai'),
	)
	name = forms.CharField(max_length=50)
	city = forms.ChoiceField(widget=forms.Select(), initial="", choices=PLACE_CHOICES)
	address = forms.CharField(max_length=50)
	game = forms.ModelChoiceField(queryset=Game.objects.all())
	image = forms.ImageField(required=False)


class UpdateOwner(forms.Form):
	phone_no = forms.IntegerField(max_value=9999999999, min_value=1000000000)

class PlayerGame(forms.Form):
	game = forms.ModelChoiceField(queryset=Game.objects.all())
	position = forms.CharField(max_length=20)
	skills = forms.CharField(max_length=50)

