from django.conf.urls import include, url
from . import views
from dimecapp import views as core_views

urlpatterns = [
    url(r'^$', views.trabajos_lista),
    url(r'^signup/$', core_views.signup, name='signup'),
]