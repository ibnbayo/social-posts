from django.contrib import admin
from . models import Post #The . is cos theyre in same folder
# Register your models here.

admin.site.register(Post)
