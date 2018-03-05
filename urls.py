from __future__ import absolute_import
from __future__ import unicode_literals
from django.conf.urls import url

from .views import search, validate

urlpatterns = [
    url(r'^langs.json', search, name='search'),
    url(r'^validate.json', validate, name='validate'),
]
