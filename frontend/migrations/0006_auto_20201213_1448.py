# Generated by Django 3.1.4 on 2020-12-13 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0005_auto_20201213_1444'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.TextField(max_length=1500),
        ),
        migrations.AlterField(
            model_name='project',
            name='description2',
            field=models.TextField(blank=True, max_length=1500, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='description3',
            field=models.TextField(blank=True, max_length=1500, null=True),
        ),
    ]
