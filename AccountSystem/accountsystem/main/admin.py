from django.contrib import admin
from django.contrib.auth.models import Group, User
from .models import Profile

admin.site.unregister(Group)

class PIL(admin.StackedInline):
    model = Profile

class UA(admin.ModelAdmin):
    model = User
    fields = ["username"]
    inlines = [PIL] 


