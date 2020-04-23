from django.urls import path
from . import views

app_name = 'main_app'

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_request, name='logout'),
    path('login/', views.login_request, name='login'),
    path('payment/', views.payment, name='payment'),
    path('subtype/', views.subtype, name='subtype'),
    path('stream/', views.stream, name='stream'),
    path('manage_account/', views.manage_account, name='manage_account'),
    path('confirmation/', views.confirmation, name='confirmation'),
]