# Generated by Django 4.2.8 on 2023-12-16 20:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ex07', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='movies',
            options={'ordering': ['episode_nb']},
        ),
    ]