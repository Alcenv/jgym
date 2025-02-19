from django.urls import path
from . import views

urlpatterns = [
    path('', views.ClientList.as_view(), name='client_list'),
    path('<int:id>/', views.ClientDetail.as_view(), name='client_detail'),
    path('create/', views.ClientCreate.as_view(), name='client_create'),
    path('<int:id>/update/', views.ClientUpdate.as_view(), name='client_update'),
    path('<int:id>/delete/', views.ClientDelete.as_view(), name='client_delete'),
]
#localhost:4500:/clients/create/