from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(TechnologyLabel)
admin.site.register(Question)
admin.site.register(Answers)
# admin.site.register(Meetup)
# admin.site.register(Meetup_Participants)
admin.site.register(Badges)
admin.site.register(User_Badges)
# admin.site.register(Tutorials)