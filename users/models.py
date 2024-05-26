from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class Landlord(models.Model):
    user = models.OneToOneField(User, verbose_name=_('user'), on_delete=models.CASCADE)
    phone_number = models.CharField(_('phone_number'), unique=True, max_length=20)
    email = models.EmailField(_('email'), unique=True)

    class Meta(object):
        db_table = 'landlord'
        verbose_name = _('user')
        verbose_name_plural = _('users')
