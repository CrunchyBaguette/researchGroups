# Generated by Django 4.1.3 on 2022-12-05 17:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("research_groups", "0008_merge_20221128_2007"),
    ]

    operations = [
        migrations.RenameField(
            model_name="researchgroupdisk",
            old_name="project",
            new_name="research_group",
        ),
        migrations.RenameField(
            model_name="researchgrouplink",
            old_name="project",
            new_name="research_group",
        ),
    ]
