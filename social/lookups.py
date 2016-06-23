'''from ajax_select import register, LookupChannel
from .models import *
from django.db.models import Q

@register('player')
class PlayerLookup(LookupChannel):

    model = Player
    min_length = 2
    
    def get_query(self, q, request):
        return self.model.objects.filter(Q(user_profile__user__first_name__icontains=q)| Q(user_profile__user__last_name__icontains=q)) 

    def format_item_display(self, item):
        return u"<span class='tag'>%s %s</span>" % (item.user_profile.user.first_name, item.user_profile.user.last_name)

    def get_result(self,obj):
    	return obj.user_profile.user.first_name

    def form_match(self,obj):
    	return self.format_item_display(obj)'''