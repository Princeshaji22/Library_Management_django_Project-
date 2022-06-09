"""librarymanagement URL Configuration

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
from django.conf.urls import include
from django.urls import path
from library import views
from django.contrib.auth.views import LoginView,LogoutView



urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/',include('django.contrib.auth.urls') ),
    path('', views.home_view),

   


    path('adminsignup', views.adminsignup_view),
    path('registerview', views.registerview, name="registerview"),
    
    path('adminlogin',views.adminlogin,name="adminlogin" ),
    path('studentlogin', LoginView.as_view(template_name='library/studentlogin.html')),

    path('logout', LogoutView.as_view(template_name='library/index.html')),
    path('afterlogin', views.afterlogin_view),

    path('addbook', views.addbook_view),
    path('viewbook', views.viewbook_view,name="viewbook"),
    

    

    path('editbook/<int:id>/', views.editbook,name="editbook"),
    path('editbk/<int:id>/', views.editbk,name="editbk"),
    path('deletebook/<int:id>/', views.deletebook,name="deletebook"),
]
