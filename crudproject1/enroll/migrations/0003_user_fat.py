# Generated by Django 3.1.1 on 2020-09-18 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0002_user_calorie'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='fat',
            field=models.CharField(default=0, max_length=100),
        ),
    ]
