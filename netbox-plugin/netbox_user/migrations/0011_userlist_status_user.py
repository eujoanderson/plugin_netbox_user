# Generated by Django 4.2.8 on 2024-11-18 00:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('netbox_user', '0010_alter_resourceaccess_index'),
    ]

    operations = [
        migrations.AddField(
            model_name='userlist',
            name='status_user',
            field=models.CharField(default='activate', max_length=30),
            preserve_default=False,
        ),
    ]
