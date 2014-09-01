from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from article.views import show_article
from category.views import category_list
from website.views import nav,nav_list
from django.conf import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Website_Electionics.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # url(r'^admin/', include(' django.contrib.admin.urls ')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^article/$', show_article),
    url(r'^category/$',category_list),
    url(r'^website/homepage/$',nav),
    url(r'^website/newscenter/$',nav_list),

)

urlpatterns += patterns(
	url( r'^static/(?P<path>.*)$', 'django.views.static.serve',
                                            { 'document_root':settings.STATIC_ROOT }),
   )