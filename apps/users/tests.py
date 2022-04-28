from django.contrib.auth.hashers import make_password
from django.test import RequestFactory, TestCase

from apps.users.models import User
from apps.users.views import UserRegisterAPIView

USER_RAW_DATA = dict(username=f'test_user_unique_test_name', password='secretpass')
USER_DB_DATA = dict(username=f'test_user_unique_test_name', password=make_password('secretpass'))


class ViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        if user := User.objects.filter(username=USER_RAW_DATA['username']).first():
            user.delete()

    def test_token(self):
        # Create an instance of a GET request.
        create_user_request = self.factory.post('/api/users/signup/', USER_RAW_DATA)
        response = UserRegisterAPIView.as_view()(create_user_request)
        self.assertEqual(response.status_code, 201)
