# Generated by Django 4.2.8 on 2024-11-14 17:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('netbox_user', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='resourceaccess',
            options={'ordering': ('user', 'index')},
        ),
        migrations.RenameField(
            model_name='resourceaccess',
            old_name='user_list',
            new_name='user',
        ),
        migrations.AlterUniqueTogether(
            name='resourceaccess',
            unique_together={('user', 'index')},
        ),
    ]
