from django.urls import path

from apps.users import views

app_name = 'users'

urlpatterns = [
    # registration
    path('', views.UserRegisterAPIView.as_view()),
]
