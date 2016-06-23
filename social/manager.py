from django.db import models
from django.contrib.auth.models import User
import operator
from django.db.models import Q

class PlayerManager(models.Manager):
	def search(self, search_terms):
		terms = [term.strip() for term in search_terms.split()]
		q_objects = []

		for term in terms:
			q_objects.append(Q(user_profile__user__first_name__icontains=term))
			q_objects.append(Q(user_profile__user__last_name__icontains=term))

		qs = self.get_queryset()

		return qs.filter(reduce(operator.or_, q_objects))

class OwnerManager(models.Manager):
	def search(self, search_terms):
		terms = [term.strip() for term in search_terms.split()]
		q_objects = []

		for term in terms:
			q_objects.append(Q(user_profile__user__first_name__icontains=term))
			q_objects.append(Q(user_profile__user__last_name__icontains=term))

		qs = self.get_queryset()

		return qs.filter(reduce(operator.or_, q_objects))

class GroundManager(models.Manager):
	def search(self, search_terms):
		terms = [term.strip() for term in search_terms.split()]
		q_objects = []

		for term in terms:
			q_objects.append(Q(name__icontains=term))
			q_objects.append(Q(place__icontains=term))
			q_objects.append(Q(address__icontains=term))

		qs = self.get_queryset()

		return qs.filter(reduce(operator.or_, q_objects))