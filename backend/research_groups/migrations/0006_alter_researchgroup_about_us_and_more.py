# Generated by Django 4.1.3 on 2022-11-27 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("research_groups", "0005_alter_researchgroup_name_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="researchgroup",
            name="about_us",
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name="researchgroup",
            name="name",
            field=models.CharField(max_length=120),
        ),
        migrations.AlterField(
            model_name="researchgrouppost",
            name="added",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name="researchgrouppost",
            name="edited",
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name="researchgrouppost",
            name="title",
            field=models.CharField(max_length=120),
        ),
    ]
