# Generated by Django 4.2.8 on 2023-12-16 22:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ex09', '0002_alter_people_birth_year_alter_people_eye_color_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='people',
            name='homeworld',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='residents', to='ex09.planets'),
        ),
    ]
