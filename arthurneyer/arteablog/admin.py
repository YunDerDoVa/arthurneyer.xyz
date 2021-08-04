from django.contrib import admin

from .models import Acticle, Category

# Register your models here.
admin.site.register(Category)
admin.site.register(Article)
