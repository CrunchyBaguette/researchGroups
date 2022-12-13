# Generated by Django 4.1.3 on 2022-12-08 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("announcements", "0005_remove_announcement_date_announcement_added_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="announcement",
            name="added",
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name="announcement",
            name="edited",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
