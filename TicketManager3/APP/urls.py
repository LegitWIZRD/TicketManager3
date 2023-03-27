from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('logout/', views.logout_user, name='logout'),
    path('admin/', views.admin, name='admin'),
    path('ticket/<int:pk>', views.ticket, name='ticket')
]

