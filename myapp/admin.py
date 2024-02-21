from django.contrib import admin
from .models import User,Blogs,Contact
# Register your models here.

admin.site.register(User)
admin.site.register(Blogs)
admin.site.register(Contact)

