# Generated by Django 3.2.5 on 2021-12-02 07:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofileinfo',
            old_name='portifolio_site',
            new_name='portfolio_site',
        ),
    ]