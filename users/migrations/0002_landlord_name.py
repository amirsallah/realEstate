# Generated by Django 4.2 on 2024-05-27 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='landlord',
            name='name',
            field=models.CharField(default='kamran', max_length=200, verbose_name='name'),
            preserve_default=False,
        ),
    ]
