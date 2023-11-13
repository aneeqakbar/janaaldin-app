from django.urls import path
from . import views


app_name = "cms"

urlpatterns = [
    path('', views.Dashboard, name='DashboardView'),
    path('profile/', views.ProfileView.as_view() , name='ProfileView'),
    path('profile/update/<int:pk>/', views.ProfileEditView.as_view() , name='ProfileEditView'),

    path('staff/', views.StaffMemberListView.as_view(), name='StaffMemberListView'),
    path('staff/new/', views.StaffMemberCreateView.as_view(), name='StaffMemberCreateView'),
    path('staff/<int:pk>/edit/', views.StaffMemberUpdateView.as_view(), name='StaffMemberUpdateView'),
    path('staff/<int:pk>/delete/', views.StaffMemberDeleteView.as_view(), name='StaffMemberDeleteView'),

    path('class/', views.ClassListView.as_view(), name='ClassListView'),
    path('class/new/', views.ClassCreateView.as_view(), name='ClassCreateView'),
    path('class/<int:pk>/edit/', views.ClassUpdateView.as_view(), name='ClassUpdateView'),
    path('class/<int:pk>/delete/', views.ClassDeleteView.as_view(), name='ClassDeleteView'),
]