from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class Landlord(models.Model):
    user = models.OneToOneField(User, verbose_name=_('user'), on_delete=models.CASCADE, blank=False, null=False)
    phone_number = models.CharField(_('phone_number'), unique=True, max_length=20, blank=False, null=False)
    email = models.EmailField(_('email'), unique=True)
    name = models.CharField(_('name'), max_length=200, blank=False, null=False)

    class Meta(object):
        db_table = 'landlord'
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def __str__(self):
        return self.user.username
