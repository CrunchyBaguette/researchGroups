# Generated by Django 4.1.4 on 2022-12-18 21:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("tutorials", "0003_alter_tutorial_type"),
    ]

    operations = [
        migrations.RenameField(
            model_name="tutorial",
            old_name="type",
            new_name="category",
        ),
    ]