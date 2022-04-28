from django.urls import include
from django.urls import path

from . import (
    users as users_urls
)
from . import views

app_name = 'api'

urlpatterns = [
    path('users/', include(users_urls.urlpatterns)),
    path('health-check/', views.HealthCheck.as_view()),

]
