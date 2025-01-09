# Generated by Django 4.2.8 on 2024-12-24 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0005_alter_user_username"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="gender",
            field=models.CharField(
                blank=True,
                choices=[("male", "남성"), ("female", "여성"), ("other", "기타")],
                max_length=10,
                verbose_name="성별",
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="introduction",
            field=models.TextField(blank=True, verbose_name="자기소개"),
        ),
    ]
