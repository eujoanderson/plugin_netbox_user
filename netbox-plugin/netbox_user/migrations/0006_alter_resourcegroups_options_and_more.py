# Generated by Django 4.2.8 on 2024-11-25 22:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('netbox_user', '0005_alter_approver_aprovador_alter_environment_ambiente_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='resourcegroups',
            options={'ordering': ('groupslist',)},
        ),
        migrations.RemoveField(
            model_name='resourcegroups',
            name='index',
        ),
    ]