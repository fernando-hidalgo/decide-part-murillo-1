# Generated by Django 4.1 on 2023-11-30 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('census', '0002_census_group'),
    ]

    operations = [
        migrations.CreateModel(
            name='CensusByPreference',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('voting_id', models.PositiveIntegerField()),
                ('voter_id', models.PositiveIntegerField()),
                ('group', models.CharField(default='', max_length=50)),
            ],
            options={
                'unique_together': {('voting_id', 'voter_id')},
            },
        ),
    ]
