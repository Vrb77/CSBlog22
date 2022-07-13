"""csBlog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django import views
from django.contrib import admin
from django.urls import path
from blog import views
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.indexView,name="index"),
    path('home/',views.homeView,name="home"),
    path('Insert/<id>',views.Insert,name='Insert'),
    path('Feedback/',views.Feedback,name='Feedback'),
    path('chatbot/',views.chatbot,name='chatbot'),
    path('myblog/<id>',views.myblog,name="myblog"),
    path('show/<bid>',views.show,name='show'),
    path('search/',views.search,name="search"),
    #path('show/<bid>/update/<bid>',views.update,name='update'),
    path('update/<bid>',views.update,name='update'),
    path('delete/<bid>/<id>',views.delete,name="delete"),
    path('about/',views.aboutView,name="about"),
    path('login/',LoginView.as_view(),name="login_url"),
    path('register/',views.registerView,name="register_url"),
    path('logout/',LogoutView.as_view(next_page='index'),name="logout"),
    #path('',(r'^myblog/(?P<id>\d+)/', views.myblog)),
]
