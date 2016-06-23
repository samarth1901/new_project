from django import forms
from .models import *
from django.contrib.admin.widgets import AdminDateWidget
from django.forms import extras
from .models import *
from .choices import *
from django.forms import ModelForm

class  SignUpForm(forms.Form):
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
	birthday = forms.DateField(widget=extras.SelectDateWidget(years = DOY))
	place = forms.ChoiceField(widget=forms.Select(),label="Where do you live", initial="", choices=PLACE_CHOICES)
	game = forms.ModelChoiceField(queryset=Game.objects.all())

class AddGround(ModelForm):
	class Meta:
		model = Ground
		fields = ['name', 'place', 'address', 'game', 'dp']

class UpdateOwner(forms.Form):
	phone_no = forms.IntegerField(max_value=9999999999, min_value=1000000000)

class PlayerGame(ModelForm):
	class Meta:
		model = Playergameprofile
		fields = ['game', 'position', 'skills']

class SearchForm(forms.Form):
	searchfor = forms.ChoiceField(widget=forms.Select(),label="Search For", initial="", choices=SEARCH_CHOICES)
	searchfield = forms.TimeField(initial="Search",label="")

class TeamForm(ModelForm):
    class Meta:
        model = Team
        fields = '__all__'

	#player = AutoCompleteSelectMultipleField('player')
	#player = make_ajax_field(Team, 'player', 'player',show_help_text=False)