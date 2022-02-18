# Generated by Django 3.2.6 on 2021-11-15 16:42

import baserow.contrib.database.webhooks.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("database", "0042_add_other_trashed_indexes"),
    ]

    operations = [
        migrations.CreateModel(
            name="TableWebhook",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_on", models.DateTimeField(auto_now_add=True)),
                ("updated_on", models.DateTimeField(auto_now=True)),
                (
                    "active",
                    models.BooleanField(
                        default=True,
                        help_text="Indicates whether the web hook is active. When a "
                        "webhook has failed multiple times, it will "
                        "automatically be deactivated.",
                    ),
                ),
                (
                    "use_user_field_names",
                    models.BooleanField(
                        default=True,
                        help_text="Indicates whether the field names must be used as "
                        "payload key instead of the id.",
                    ),
                ),
                (
                    "url",
                    models.URLField(
                        help_text="The URL that must call when the webhook is "
                        "triggered."
                    ),
                ),
                (
                    "request_method",
                    models.CharField(
                        choices=[
                            ("POST", "Post"),
                            ("GET", "Get"),
                            ("PUT", "Put"),
                            ("PATCH", "Patch"),
                            ("DELETE", "Delete"),
                        ],
                        default="POST",
                        help_text="The request method that be used when the event "
                        "occurs.",
                        max_length=10,
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text="An internal name of the webhook.", max_length=255
                    ),
                ),
                (
                    "include_all_events",
                    models.BooleanField(
                        default=True,
                        help_text="Indicates whether this webhook should listen to all "
                        "events.",
                    ),
                ),
                (
                    "failed_triggers",
                    models.IntegerField(
                        default=0, help_text="The amount of failed webhook calls."
                    ),
                ),
                (
                    "table",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="database.table"
                    ),
                ),
            ],
            options={
                "ordering": ("id",),
            },
        ),
        migrations.CreateModel(
            name="TableWebhookHeader",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.TextField(
                        validators=[
                            (
                                baserow.contrib.database.webhooks.validators.header_name_validator
                            )
                        ]
                    ),
                ),
                (
                    "value",
                    models.TextField(
                        validators=[
                            (
                                baserow.contrib.database.webhooks.validators.header_value_validator
                            )
                        ]
                    ),
                ),
                (
                    "webhook",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="headers",
                        to="database.tablewebhook",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="TableWebhookEvent",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_on", models.DateTimeField(auto_now_add=True)),
                ("updated_on", models.DateTimeField(auto_now=True)),
                ("event_type", models.CharField(max_length=50)),
                (
                    "webhook",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="events",
                        to="database.tablewebhook",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="TableWebhookCall",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("event_type", models.CharField(max_length=50)),
                ("called_time", models.DateTimeField(null=True)),
                ("called_url", models.URLField()),
                (
                    "request",
                    models.TextField(
                        help_text="A text copy of the request headers and body.",
                        null=True,
                    ),
                ),
                (
                    "response",
                    models.TextField(
                        help_text="A text copy of the response headers and body.",
                        null=True,
                    ),
                ),
                (
                    "response_status",
                    models.IntegerField(
                        help_text="The HTTP response status code.", null=True
                    ),
                ),
                (
                    "error",
                    models.TextField(
                        help_text="An internal error reflecting what went wrong.",
                        null=True,
                    ),
                ),
                (
                    "webhook",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="calls",
                        to="database.tablewebhook",
                    ),
                ),
            ],
            options={
                "ordering": ("-called_time",),
            },
        ),
    ]
