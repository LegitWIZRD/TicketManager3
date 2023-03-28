from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('logout/', views.logout_user, name='logout'),
    path('admin/', views.admin, name='admin'),
    path('add/', views.add_ticket, name='add'),
    path('ticket/<int:pk>', views.ticket, name='ticket'),
    path('edit/<int:pk>', views.edit_ticket, name='edit'),
    path('delete_ticket/<int:pk>', views.delete_ticket, name='delete')

]

