from django.urls import path, include
from . import views
from rest_framework import routers

# router = routers.DefaultRouter()
# router.register(r'data', views.GetClassDataView, basename="")

app_name = "classes"

urlpatterns = [
    # path('', include(router.urls)),
    path('book/<int:id>/', views.ClassBookView.as_view(), name='ClassBookView'),
    path('data/', views.GetClassDataView.as_view(), name='GetClassDataView'),
    path('book-confirm/', views.ClassBookConfirmView.as_view(), name='ClassBookConfirmView'),
    path('schedule/', views.GetClassScheduleView.as_view(), name='GetClassScheduleView'),
]
