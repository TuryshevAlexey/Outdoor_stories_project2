from django.contrib.auth.backends import ModelBackend
from django.db.models import Q

from users.models import User


class EmailUsernameBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(Q(username__iexact=username) | Q(email__iexact=username))
        except User.DoesNotExist:
            User().set_password(password)
            return
        if user.check_password(password) and self.user_can_authenticate(user):
            return user
