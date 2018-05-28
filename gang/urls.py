from django.conf.urls import include, url
from django.contrib.auth import views as login_view
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^home/$', views.home, name='home'),
    url(r'^(?P<user_id>[0-9]+)/profile/$', views.profile, name='profile'),
    url(r'^(?P<user_id>[0-9]+)/edits/$', views.profile_edit, name='profile_edit'),
    url(r'^newhood/$', views.new_hood, name='newHood'),
    url(r'^Post/$', views.hood_post, name='newPost'),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^logout/$', login_view.logout, {"next_page": '/'}),
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
