# Generated by Django 4.1 on 2023-12-16 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voting', '0012_merge_0011_merge_20231215_1206_0011_voting_mixnet_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='questionoptionmultichoice',
            name='selected',
            field=models.BooleanField(default=False),
        ),
    ]
