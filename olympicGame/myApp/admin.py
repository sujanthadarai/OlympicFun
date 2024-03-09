from django.contrib import admin
from .models import signin,signup
# Register your models here.
@admin.register(signup)
class signupAdmin(admin.ModelAdmin):
    list_display=['id','name','country','phone','username','email','interest_sports','password','confirm_password']
@admin.register(signin)
class signinAdmin(admin.ModelAdmin):
    list_display=['id','username','password','confirm_password']
