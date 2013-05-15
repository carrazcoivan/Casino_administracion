from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'FirstWebsite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	# url()
	#	regular-expression: used to match url patterns, comparing the requested url against each regular expression
	#	view: the view requested by the url.  It calls the view function with an HttpRequest object as its first arg and any "captured" values from the regular expression.
	#	kwargs [optional]: 
	# 	name [optional]: alias for the url, it allows you to refer to it from elsewhere in Django.
	url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^admin/', include(admin.site.urls)),
)
