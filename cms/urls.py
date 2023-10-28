from django.urls import path
from . import views


app_name = "cms"

urlpatterns = [
    path('', views.Dashboard, name='DashboardView'),
    path('profile/', views.ProfileView.as_view() , name='ProfileView'),
    path('profile/update/<int:pk>/', views.ProfileEditView.as_view() , name='ProfileEditView'),
]