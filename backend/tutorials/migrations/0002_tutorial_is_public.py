# Generated by Django 4.1.3 on 2022-11-17 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tutorials", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="tutorial",
            name="is_public",
            field=models.BooleanField(default=False),
        ),
    ]
