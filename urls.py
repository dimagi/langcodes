from __future__ import absolute_import
from __future__ import unicode_literals
from django.conf.urls import re_path as url

from langcodes.views import search, validate

urlpatterns = [
    url(r'^langs.json', search, name='search'),
    url(r'^validate.json', validate, name='validate'),
]
