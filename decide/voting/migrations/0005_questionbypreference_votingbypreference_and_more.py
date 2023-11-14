# Generated by Django 4.1 on 2023-11-14 15:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0003_auto_20180921_1119"),
        ("voting", "0004_alter_voting_postproc_alter_voting_tally"),
    ]

    operations = [
        migrations.CreateModel(
            name="QuestionByPreference",
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
                ("desc", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="VotingByPreference",
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
                ("name", models.CharField(max_length=200)),
                ("desc", models.TextField(blank=True, null=True)),
                ("start_date", models.DateTimeField(blank=True, null=True)),
                ("end_date", models.DateTimeField(blank=True, null=True)),
                ("tally", models.JSONField(blank=True, null=True)),
                ("postproc", models.JSONField(blank=True, null=True)),
                (
                    "auths",
                    models.ManyToManyField(
                        related_name="votingsbypreference", to="base.auth"
                    ),
                ),
                (
                    "pub_key",
                    models.OneToOneField(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="votingbypreference",
                        to="base.key",
                    ),
                ),
                (
                    "question",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="votingbypreference",
                        to="voting.questionbypreference",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="QuestionOptionByPreference",
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
                ("number", models.PositiveIntegerField(blank=True, null=True)),
                ("option", models.TextField()),
                ("preference", models.PositiveIntegerField(blank=True, null=True)),
                (
                    "question",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="preferences",
                        to="voting.questionbypreference",
                    ),
                ),
            ],
        ),
    ]
