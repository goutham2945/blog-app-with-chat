# Django imports
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from django.views.generic import TemplateView

# user imports
from app import views as app_views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^accounts/login/$', app_views.login_user, name="login_user"),
    url(r'^accounts/register/$', app_views.register, name="register"),
    url(r'^accounts/logout/$', app_views.logout_user, name='logout_user'),

    url(r'^oauth/', include('social_django.urls', namespace='social')), # social login
    url(r'^closePopUp/$', TemplateView.as_view(template_name='closePopUp.html')), # This will close the pop up after successfull login, implemented only for gmail 

    url(r'^', include('app.urls')), 
]
