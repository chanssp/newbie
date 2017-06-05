from django.contrib import admin
from django.contrib.sessions.models import Session


# Register your models here.
from .models import *

admin.site.register(MyUser)
admin.site.register(Type)
admin.site.register(Order)
admin.site.register(Session)
