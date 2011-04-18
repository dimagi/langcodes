from django.conf.urls.defaults import patterns

urlpatterns = patterns('langcodes.views',
    (r'^langs.json', 'search'),
    (r'^validate.json', 'validate'),
)