from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'blog_tutorial.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
	
	# Blog URLS
	url(r'', include('blogengine.urls')),
	
	# Flat pages
	url(r'', include('django.contrib.flatpages.urls')),
)
