# Generated by Django 4.2.4 on 2023-09-05 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0005_alter_post_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='comment_image',
            field=models.ImageField(blank=True, null=True, upload_to='comment_image/'),
        ),
    ]