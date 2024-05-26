# Generated by Django 4.2 on 2024-05-26 19:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40, verbose_name='title')),
                ('description', models.TextField(blank=True, verbose_name='description')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='price')),
                ('address', models.TextField(max_length=200, verbose_name='address')),
                ('city', models.CharField(max_length=40, verbose_name='city')),
                ('is_active', models.BooleanField(default=True, verbose_name='active')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_time', models.DateTimeField(auto_now=True, verbose_name='updated at')),
                ('landlord', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='landlord', to='users.landlord', verbose_name='landlord')),
            ],
            options={
                'verbose_name': 'estate',
                'verbose_name_plural': 'estates',
                'db_table': 'estate',
            },
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='title')),
                ('file', models.FileField(upload_to='files/%Y/%m/%d/', verbose_name='file')),
                ('order', models.IntegerField(default=0, verbose_name='order')),
                ('is_active', models.BooleanField(default=True, verbose_name='active')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('Estate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='files', to='products.estate', verbose_name='Estate')),
            ],
            options={
                'verbose_name': 'file',
                'verbose_name_plural': 'files',
                'db_table': 'files',
            },
        ),
    ]
