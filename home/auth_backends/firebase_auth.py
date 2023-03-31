from django.contrib.auth.backends import BaseBackend
from firebase_admin import auth
from home.models import waste

class FirebaseAuthenticationBackend(BaseBackend):
    def authenticate(self, request, token=None):
        try:
            decoded_token = auth.verify_id_token(token)
            uid = decoded_token['uid']
            return self.get_user(uid)
        except:
            return None

    def get_user(self, uid):
        try:
            user = waste.objects.get(firebase_uid=uid)
            return user
        except waste.DoesNotExist:
            return None