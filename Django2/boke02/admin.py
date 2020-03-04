from django.contrib import admin

# Register your models here.
from .models import Text
admin.site.register(Text)   # 在站点中注册