from django.conf.urls import url, include
from . import views

from boke02.uploads import upload_image
urlpatterns = [
    url(r'^upload/(?P<dir_name>[^/]+)$', upload_image, name='upload_image'),
]