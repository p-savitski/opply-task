from django.test import RequestFactory, TestCase
from rest_framework_simplejwt.views import TokenObtainPairView

from apps.products.views import ProductListAPIView
from apps.users.models import User
from apps.users.tests import USER_DB_DATA, USER_RAW_DATA


class ProductListAPIViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create(**USER_DB_DATA)

    def test_details(self):
        request = self.factory.get('/api/products/')
        response = ProductListAPIView.as_view()(request)
        self.assertEqual(response.status_code, 401)

        access_token_request = self.factory.post('/api/users/token/',
                                                 data=USER_RAW_DATA,
                                                 content_type='application/json')
        response = TokenObtainPairView.as_view()(access_token_request)
        token = response.data['access']

        request = self.factory.get('/api/products/', HTTP_AUTHORIZATION=f'Bearer {token}')
        products_response = ProductListAPIView.as_view()(request)
        self.assertEqual(products_response.status_code, 200)
