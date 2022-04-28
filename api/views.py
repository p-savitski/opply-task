from django.http import JsonResponse
from rest_framework import views, permissions


class HealthCheck(views.APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, *args, **kwargs):
        return JsonResponse({'status': 'OK'})
