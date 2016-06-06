from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(User_profile)
admin.site.register(Player)
admin.site.register(Owner)
admin.site.register(Ground)
admin.site.register(Team)
admin.site.register(Game)
admin.site.register(PlayerGameProfile)



