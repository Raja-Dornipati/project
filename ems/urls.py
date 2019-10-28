"""ems URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
# from employee.views import user_login, user_logout, success, register, change_password, employee_details
from employee.views import *
from django.contrib.auth import views as auth_views
from django.conf.urls import url
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('polls/', include('poll.urls')),
    path('employee/', include('employee.urls')),
    path('signup/', register, name="user_signup"),
    path('login/', user_login, name="user_login"),
    path('details/<int:id>/', employee_details, name="employee_details"),
    path('community/',community, name="community"),
    path('post_form/',post_form, name="post_form"),
    path('post_details/<int:id>/',Post_details, name="Post_details"),
    path('logout/', user_logout, name="user_logout"),
    # path('accounts/', include('django.contrib.auth.urls')),
    re_path(r'^password-reset/$', auth_views.PasswordResetView.as_view(template_name="password_reset_form.html"), name='password_reset'),
    re_path(r'^password-reset/done/$', auth_views.PasswordResetDoneView.as_view(template_name="password_reset_done.html"), name='password_reset_done'),
    re_path(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
            auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_confirm.html"), name='password_reset_confirm'),
    re_path(r'^password-reset/complete/$', auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_complete.html"), name='password_reset_complete'),
    path('change-password/', change_password, name="change_password"),





]
