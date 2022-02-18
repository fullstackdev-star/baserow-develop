# Generated by Django 3.2.6 on 2021-12-01 09:46

import baserow.contrib.database.webhooks.validators
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("database", "0048_fix_trashed_field_dependencies"),
    ]

    operations = [
        migrations.AlterField(
            model_name="tablewebhook",
            name="url",
            field=models.TextField(
                help_text="The URL that must be called when the webhook is triggered.",
                validators=[
                    django.core.validators.MaxLengthValidator(2000),
                    django.core.validators.URLValidator(),
                    baserow.contrib.database.webhooks.validators.url_validator,
                ],
            ),
        ),
        migrations.AlterField(
            model_name="tablewebhookcall",
            name="called_url",
            field=models.TextField(
                validators=[
                    django.core.validators.MaxLengthValidator(2000),
                    django.core.validators.URLValidator(),
                    baserow.contrib.database.webhooks.validators.url_validator,
                ]
            ),
        ),
    ]
