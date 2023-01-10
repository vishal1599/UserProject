from django.contrib import admin
from . import models
from useractivity.models import User
# Register your models here.


admin.site.register(User)