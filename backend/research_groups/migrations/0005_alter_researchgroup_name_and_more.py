# Generated by Django 4.1.3 on 2022-11-26 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("research_groups", "0004_rename_test_researchgrouppostcomment_text"),
    ]

    operations = [
        migrations.AlterField(
            model_name="researchgroup",
            name="name",
            field=models.CharField(max_length=120, unique=True),
        ),
        migrations.AlterField(
            model_name="researchgrouppost",
            name="added",
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name="researchgrouppost",
            name="edited",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name="researchgrouppost",
            name="title",
            field=models.CharField(max_length=120, unique=True),
        ),
        migrations.AlterField(
            model_name="researchgroupuser",
            name="role",
            field=models.CharField(
                choices=[("mem", "Member"), ("mod", "Moderator"), ("cr", "Creator")],
                default="mem",
                max_length=20,
            ),
        ),
    ]
