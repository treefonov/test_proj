from django.conf.urls import include, url
from django.contrib import admin
import test_app.views as views

urlpatterns = [
    # Examples:
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.home, name='home'),
]
