# Generated by Django 4.1.3 on 2022-12-13 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("research_groups", "0009_alter_researchgroup_category"),
    ]

    operations = [
        migrations.AlterField(
            model_name="researchgroupuser",
            name="created",
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
