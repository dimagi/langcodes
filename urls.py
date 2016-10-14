from django.conf.urls import patterns, url

from views import search, validate

urlpatterns = patterns('langcodes.views',
    url(r'^langs.json', search, name='search'),
    url(r'^validate.json', validate, name='validate'),
)
