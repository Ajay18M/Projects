# Generated by Django 4.0.7 on 2022-12-20 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_deligator', '0006_materials_aluminium'),
    ]

    operations = [
        migrations.AddField(
            model_name='materials',
            name='aluminium_predict',
            field=models.BooleanField(default=False),
        ),
    ]
