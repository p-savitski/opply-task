from django.urls import path

from apps.products import views

app_name = 'users'

urlpatterns = [
    path('', views.ProductListAPIView.as_view()),
]
