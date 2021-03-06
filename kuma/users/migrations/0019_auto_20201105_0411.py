# Generated by Django 2.2.16 on 2020-11-05 04:11

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0018_user_subscriber_number"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="mozillians_url",
        ),
        migrations.AddField(
            model_name="user",
            name="pmo_url",
            field=models.TextField(
                blank=True,
                validators=[
                    django.core.validators.RegexValidator(
                        "^https?://people\\.mozilla\\.org/",
                        "Enter a valid PMO URL.",
                        "invalid",
                    )
                ],
                verbose_name="Mozilla People Directory",
            ),
        ),
    ]
