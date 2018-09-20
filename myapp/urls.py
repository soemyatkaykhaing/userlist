from django.urls import path
from . import views
from .views import WelcomeView

app_name = 'myapp'

urlpatterns = [
    path('', views.WelcomeView.as_view(), name='welcome'),
    path('list/', views.UserListView.as_view(), name='list'),
    path('add/', views.CreateUserView.as_view(), name='adduser'),
]