# Generated by Django 3.2.3 on 2021-05-27 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_auto_20210525_2117'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='github_url',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='project',
            name='project_url',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]