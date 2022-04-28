from django.urls import include
from django.urls import path

from . import (
    users as users_urls,
    products as products_urls,
    orders as orders_urls,
)
from . import views

app_name = 'api'

urlpatterns = [
    path('users/', include(users_urls.urlpatterns)),
    path('products/', include(products_urls.urlpatterns)),
    path('orders/', include(orders_urls.urlpatterns)),
    path('health-check/', views.HealthCheck.as_view()),
]
