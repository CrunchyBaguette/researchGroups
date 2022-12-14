# Generated by Django 4.1.3 on 2022-11-26 17:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("research_groups", "0004_rename_test_researchgrouppostcomment_text"),
    ]

    operations = [
        migrations.AddField(
            model_name="researchgroup",
            name="group_owner",
            field=models.ForeignKey(
                default=None,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="group_owner",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="researchgroup",
            name="members",
            field=models.ManyToManyField(
                related_name="members",
                through="research_groups.ResearchGroupUser",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
