# Generated by Django 3.2.3 on 2021-05-26 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_post_last_edited_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='thumbnail',
            field=models.ImageField(default='../demo_media/blog/images/default_thumbnail.png', upload_to='../demo_media/blog/images/'),
        ),
    ]