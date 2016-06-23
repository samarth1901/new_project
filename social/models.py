from django.db import models
from django.contrib.auth.models import User
import operator
from django.db.models import Q
from .manager import *
from .choices import *


class User_profile(models.Model):
	user = models.OneToOneField(User)
	confirmation_key = models.IntegerField(default=0)
	profile_type = models.CharField(max_length=2, default='PL')
	dp = models.ImageField(upload_to = 'profile_pics/', null = True, blank = True)
	def __str__(self):
		return self.user.username
	def user_name(self):
		return self.user.username

class Player(models.Model):
	user_profile = models.OneToOneField(User_profile)
	birthday = models.DateField(null=True, blank=True)
	place = models.CharField(max_length=3, choices=PLACE_CHOICES, default=PUNE)
	objects = PlayerManager()

	def __str__(self):
		return self.user_profile.user.username
	def user_name(self):
		return self.user_profile.user.username

class Owner(models.Model):
	user_profile = models.OneToOneField(User_profile)
	phone_no = models.IntegerField(blank=True, null=True)
	objects = OwnerManager()
	def __str__(self):
		return self.user_profile.user.username
	def user_name(self):
		return self.user_profile.user.username

class Ground(models.Model):
	owner = models.ForeignKey('Owner')
	game = models.ForeignKey('Game')
	name = models.CharField(max_length=30)
	place = models.CharField(max_length=3, default='PUN', choices=PLACE_CHOICES)
	address = models.CharField(max_length=60, null = True, blank = True)
	dp = models.ImageField(upload_to = 'ground_pics/', null = True, blank = True)
	objects = GroundManager()
	def __str__(self):
		return self.name

class Team(models.Model):
	player = models.ManyToManyField('Player')
	game = models.ForeignKey('Game')
	name = models.CharField(max_length=15)
	expertise = models.CharField(max_length=15, choices=EXPERTISE_CHOICES, default = AMETUER)
	home_ground = models.ForeignKey('Ground', null = True, blank = True)
	def __str__(self):
		return self.name

class Game(models.Model):
	name = models.CharField(max_length=15)
	def __str__(self):
		return self.name

class Playergameprofile(models.Model):
	player = models.ForeignKey('Player')
	game = models.ForeignKey('Game')
	position = models.CharField(max_length=10, null=True, blank=True)
	skills = models.CharField(max_length=50, null = True, blank = True)
	def __str__(self):
		return self.player.user_profile.user.username + "'s " + self.game.name + " profile"





