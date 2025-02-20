from django.contrib.auth.mixins import UserPassesTestMixin


class GerentePermission(UserPassesTestMixin):
    """ "Mixin that checks if the user is a Gerente"""

    def test_func(self):
        return self.request.user.groups.filter(name="Gerente").exists()


