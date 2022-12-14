# Generated by Django 4.1.3 on 2022-12-09 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("research_groups", "0008_merge_20221128_2007"),
    ]

    operations = [
        migrations.AlterField(
            model_name="researchgroup",
            name="category",
            field=models.CharField(
                choices=[("math", "Matematyka"), ("med", "Medycyna"), ("chem", "Chemia"), ("def", "Default")],
                default="def",
                max_length=20,
            ),
        ),
    ]
