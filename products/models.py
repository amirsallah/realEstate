from django.db import models
from django.utils.translation import gettext_lazy as _

from users.models import Landlord


class Estate(models.Model):
    title = models.CharField(verbose_name=_('title'), max_length=40)
    description = models.TextField(verbose_name=_('description'), blank=True)
    price = models.DecimalField(verbose_name=_('price'), max_digits=10, decimal_places=2)
    address = models.TextField(verbose_name=_('address'), max_length=200)
    city = models.CharField(_('city'), max_length=40)
    landlord = models.ForeignKey(Landlord, verbose_name=_('landlord'), on_delete=models.CASCADE,
                                 related_name='landlord')
    meterage = models.DecimalField(verbose_name=_('meterage'), max_digits=20, decimal_places=2)
    parking = models.BooleanField(verbose_name=_('parking'))
    storeroom = models.BooleanField(verbose_name=_('storeroom'))
    is_active = models.BooleanField(verbose_name=_('active'), default=True)
    created_time = models.DateTimeField(verbose_name=_('created at'), auto_now_add=True)
    updated_time = models.DateTimeField(verbose_name=_('updated at'), auto_now=True)

    class Meta:
        db_table = 'estate'
        verbose_name = _('estate')
        verbose_name_plural = _('estates')

    def __str__(self):
        return self.title


class File(models.Model):
    Estate = models.ForeignKey(Estate, verbose_name=_('Estate'), related_name='files', on_delete=models.CASCADE)
    title = models.CharField(verbose_name=_('title'), max_length=50)
    file = models.FileField(verbose_name=_('file'), upload_to='files/%Y/%m/%d/')
    order = models.IntegerField(verbose_name=_('order'), default=0)
    is_active = models.BooleanField(verbose_name=_('active'), default=True)
    created_time = models.DateTimeField(verbose_name=_('created at'), auto_now_add=True)

    class Meta:
        db_table = 'files'
        verbose_name = _('file')
        verbose_name_plural = _('files')

    def __str__(self):
        return self.title
