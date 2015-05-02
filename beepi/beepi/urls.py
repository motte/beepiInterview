from django.conf.urls import patterns, include, url
from django.contrib import admin
from main.views import IndexView, IndexTwoView, IndexThreeView

urlpatterns = patterns('',
    # Examples:
    url(r'^$', IndexThreeView.as_view(), name='home'),
    url(r'^alt1/', IndexTwoView.as_view(), name='home'),
    url(r'^alt2/', IndexThreeView.as_view(), name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
