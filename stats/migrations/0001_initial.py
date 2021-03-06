# Generated by Django 3.2.6 on 2021-09-07 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='piloto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('foto', models.ImageField(blank=True, null=True, upload_to='stats')),
                ('created', models.DateTimeField(auto_now=True)),
                ('nacimiento', models.DateTimeField()),
                ('update', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'piloto',
                'verbose_name_plural': 'pilotos',
            },
        ),
    ]
