# Generated by Django 4.2.4 on 2023-08-26 18:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_post_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='like',
            old_name='is_likes',
            new_name='is_liked',
        ),
    ]
