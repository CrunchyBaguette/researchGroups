# Generated by Django 4.1.4 on 2022-12-15 06:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("tutorials", "0002_tutorial_is_public"),
        ("research_groups", "0014_alter_researchgroupdisk_name_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="researchgroupguide",
            name="guide",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="research_group_guide",
                to="tutorials.tutorial",
            ),
        ),
    ]
