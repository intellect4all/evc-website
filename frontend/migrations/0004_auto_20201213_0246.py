# Generated by Django 3.1.4 on 2020-12-13 01:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0003_contact_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contact',
            options={'ordering': ['-date']},
        ),
    ]
