"""
URL configuration for gym project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, include
from gym.apps.clients import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('clients/', include('gym.apps.clients.urls'), name='clients'),
    path('', views.ClientList.as_view(), name='client_list'),
    path('<int:id>/', views.ClientDetail.as_view(), name='client_detail'),
    path('create/', views.ClientCreate.as_view(), name='client_create'),
    path('<int:id>/update/', views.ClientUpdate.as_view(), name='client_update'),
    path('<int:id>/delete/', views.ClientDelete.as_view(), name='client_delete'),
]
