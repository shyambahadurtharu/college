# Generated by Django 4.2.4 on 2023-09-22 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0006_comment_comment_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment_image',
            field=models.ImageField(blank=True, max_length=250, null=True, upload_to='c_image/'),
        ),
    ]
