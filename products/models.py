from django.db import models
from django.utils.translation import gettext_lazy as _

from users.models import Landlord


class Estate(models.Model):
    title = models.CharField(verbose_name=_('title'), max_length=40)
    description = models.TextField(verbose_name=_('description'), blank=True)
    price = models.DecimalField(verbose_name=_('price'), max_digits=10, decimal_places=2)
    address = models.TextField(verbose_name=_('address'), max_length=200)
    city = models.CharField(_('city'), max_length=40)
    state = models.CharField(_('state'), max_length=40, blank=True)
    photo_main = models.ImageField(_('photo_main'), upload_to='photos/%y/%m/%d/', blank=True)
    photo_2 = models.ImageField(_('photo_2'), upload_to='photos/%y/%m/%d/', blank=True)
    photo_3 = models.ImageField(_('photo_3'), upload_to='photos/%y/%m/%d/', blank=True)
    landlord = models.ForeignKey(Landlord, verbose_name=_('landlord'), on_delete=models.CASCADE,
                                 related_name='landlord')

    class Meta:
        db_table = _('estate')
        verbose_name = _('estate')
        verbose_name_plural = _('estates')

    def __str__(self):
        return self.title
