# Generated by Django 4.1.3 on 2022-12-13 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("projects", "0008_alter_project_funds"),
    ]

    operations = [
        migrations.AddField(
            model_name="project",
            name="contact",
            field=models.TextField(blank=True),
        ),
    ]
