# Generated by Django 3.2.4 on 2021-06-15 14:45

import core.storage_backends
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('issue', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Category',
            new_name='Project',
        ),
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['-id', '-created_at'], 'verbose_name': 'project', 'verbose_name_plural': 'projects'},
        ),
        migrations.RenameField(
            model_name='card',
            old_name='category',
            new_name='project',
        ),
        migrations.AlterField(
            model_name='card',
            name='attachment',
            field=models.FileField(blank=True, null=True, storage=core.storage_backends.PublicMediaStorage(), upload_to=''),
        ),
    ]
