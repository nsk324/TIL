# Generated by Django 2.2.6 on 2019-10-17 03:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ('-pk',)},
        ),
    ]
