from django.urls import path

from apps.orders import views

urlpatterns = [
    path('', views.OrderCreateAPIView.as_view()),
    path('history/', views.OrderListAPIView.as_view()),
]
