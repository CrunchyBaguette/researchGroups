# Generated by Django 4.1.3 on 2022-11-20 22:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("projects", "0002_projectpost_projectpostcomment_projectlink_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="projectpostcomment",
            old_name="test",
            new_name="text",
        ),
    ]
