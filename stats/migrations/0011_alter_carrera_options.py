# Generated by Django 3.2.6 on 2021-09-09 17:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0010_alter_carrera_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='carrera',
            options={'verbose_name': 'carrera', 'verbose_name_plural': 'carreras'},
        ),
    ]