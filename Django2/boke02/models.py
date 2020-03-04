from django.db import models

# Create your models here.
# 引入富文本
from tinymce.models import HTMLField  # HTMLField 对大文本的封装


class Text(models.Model):
    str = HTMLField()
