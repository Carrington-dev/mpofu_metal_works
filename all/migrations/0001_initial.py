# Generated by Django 4.0.6 on 2022-07-08 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=300)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=300)),
                ('message', models.TextField()),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Contact',
                'verbose_name_plural': 'Contacts',
            },
        ),
    ]
