# Generated by Django 4.0.1 on 2022-08-22 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Quests',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('description', models.TextField()),
                ('required_level', models.PositiveIntegerField(default=1)),
                ('start_zone', models.CharField(max_length=64)),
            ],
        ),
    ]
