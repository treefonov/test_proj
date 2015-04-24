from django.conf.urls import url
import test_app.views as views

urlpatterns = [
    # Examples:
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.home, name='home'),
    url(r'^ajax/time$', views.get_time, name='time'),
]
