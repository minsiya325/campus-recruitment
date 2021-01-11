"""CampusReq URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib.admin.templatetags import admin_urls
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from django.conf.urls.static import static
from CampusReq import settings

from django.contrib.auth import views as auth_views

from campus.views import StudRegister, IndexView, Register, LoginView

from campus import admin_urls,student_urls,company_urls

urlpatterns = [
   path('', IndexView.as_view()),
    path('stud_register', StudRegister.as_view()),
    path('register', Register.as_view()),
    path('login', LoginView.as_view()),
    path('admin/', admin_urls.urls()),
    path('student/', student_urls.urls()),
    path('company/', company_urls.urls()),


]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
